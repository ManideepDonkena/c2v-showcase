"""Noise model for the D-VGAIN results: is a difference larger than what measurement noise alone produces?

Three sources of noise, each measured from the cached probes (no model call unless --repeat is given):
    repeat   the same request twice (same images, prompt, seed, temperature 0) can still move P(right). Measured on
             pairs with byte-identical material: autofix folders whose 12 frames equal ours, and --repeat re-probes.
    items    a topic has 8 TEST questions (x 2 option orders). Another 8 questions would give another score.
    topics   10 concepts. A claim about videos in general must hold over topics, not only over these 10.

Two questions per comparison, both answered by resampling, never by a normal approximation:
    measurement  "for these videos, is the difference beyond measurement noise?" Item-level randomisation test: under
                 H0 the two materials are exchangeable on every question, so their answers are swapped at random per
                 question, jointly over all topics (10,000 draws). The statistic is recomputed each time, including the
                 normalisation by 1 - B_eff, so it is exact for the ratio M9.
    general      "would it hold on other topics?" Exact sign-flip test over per-topic values, and a hierarchical
                 bootstrap CI (topics, then questions within a topic).
Holm's correction runs over the primary family. MDE is the smallest effect the design detects (80% power, a = .05):
2.8 x the bootstrap standard error.

    python bench/noise_model.py                 -> bench/results/noise-model/{report.md, report.json}
    python bench/noise_model.py --repeat 2      first re-probes the NOVEL-12 base frames twice (about 40 calls)
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from c2vlab import dvgain, generate

OUT = ROOT / "bench" / "results" / "noise-model"
REPEATS = ROOT / "bench" / "results" / "noise-repeats"
RNG = np.random.default_rng(0)
DRAWS = 10_000


def load(path):
    """item id -> P(right) averaged over option orders (a missing letter counts as chance)."""
    if not path.exists():
        return None
    d = json.loads(path.read_text())
    out = {}
    for r in d["rotations"]:
        for it in r["items"]:
            out.setdefault(it["id"], []).append(dvgain.CHANCE if it["p_right"] is None else it["p_right"])
    return {k: float(np.mean(v)) for k, v in out.items()}


def topic(run, files):
    """{key: np.array over the blind file's item order}, or None when any file is missing."""
    data = {k: load(run / f) for k, f in files.items()}
    if any(v is None for v in data.values()):
        return None
    ids = list(data["blind"])
    out = {k: np.array([v[i] for i in ids]) for k, v in data.items()}
    out["room"] = 1 - max(dvgain.CHANCE, float(out["blind"].mean()))
    return out


def nvg(s, b):
    v = dvgain.nvg(float(s), float(b))
    return None if v is None else v


def dvg(v, s, b):
    x = dvgain.dvgain(float(v), float(s), float(b))
    return None if x is None else x


# ---- statistics per topic: arrays of per-question values in, a number (or None when undefined) out ----
def st_gain(a):  # M9 / NVG of material "x" over the blind prior
    return nvg(a["x"].mean(), a["blind"].mean())


def st_gain_test(a):  # the test statistic for st_gain: the same gain with the room 1 - B_eff fixed at its observed
    # value, so that swapping video and no-video answers does not also move the denominator (valid, and stable)
    return None if a["room"] < dvgain.MIN_ROOM else float((a["x"].mean() - a["blind"].mean()) / a["room"])


def st_dgain(a):  # NVG(x) - NVG(y), same prior
    gx, gy = nvg(a["x"].mean(), a["blind"].mean()), nvg(a["y"].mean(), a["blind"].mean())
    return None if gx is None or gy is None else gx - gy


def st_raw(a):  # raw P(right) difference, defined even at the ceiling
    return float(a["x"].mean() - a["y"].mean())


def st_dm7(a):  # D-VGAIN(x) - D-VGAIN(y)
    gx = dvg(a["xv"].mean(), a["xs"].mean(), a["blind"].mean())
    gy = dvg(a["yv"].mean(), a["ys"].mean(), a["blind"].mean())
    return None if gx is None or gy is None else gx - gy


def pooled(values):
    v = [x for x in values if x is not None]
    return (float(np.mean(v)), len(v)) if v else (None, 0)


def randomisation(topics, stat, swaps):
    """Item-level randomisation test of H0 "the swapped materials are exchangeable", jointly over topics.
    Returns the two-sided p of the pooled mean and, per topic, its own two-sided p."""
    obs = [stat(t) for t in topics]
    obs_mean, _ = pooled(obs)
    null_mean, per_topic_null = [], [[] for _ in topics]
    for _ in range(DRAWS):
        vals = []
        for j, t in enumerate(topics):
            n = len(t["blind"])
            flip = RNG.random(n) < 0.5
            u = dict(t)
            for a, b in swaps:
                u[a] = np.where(flip, t[b], t[a])
                u[b] = np.where(flip, t[a], t[b])
            v = stat(u)
            vals.append(v)
            if v is not None:
                per_topic_null[j].append(v)
        m, _ = pooled(vals)
        if m is not None:
            null_mean.append(m)
    p_all = (1 + sum(abs(x) >= abs(obs_mean) - 1e-12 for x in null_mean)) / (1 + len(null_mean))
    p_topic = [None if o is None or not nl else (1 + sum(abs(x) >= abs(o) - 1e-12 for x in nl)) / (1 + len(nl))
               for o, nl in zip(obs, per_topic_null)]  # fmt: skip
    return obs, obs_mean, float(p_all), p_topic


def rule_fpr(topics, stat, swaps, min_mean=0.05, min_share=0.7):
    """How often the preregistered layout rule (mean >= +5 points and >= 7 of 10 topics ahead) fires when H0 is true:
    the same item-level randomisation as above, so the noise is the measured one, not an assumed flip rate."""
    fired = total = 0
    for _ in range(DRAWS):
        vals = []
        for t in topics:
            flip = RNG.random(len(t["blind"])) < 0.5
            u = dict(t)
            for a, b in swaps:
                u[a], u[b] = np.where(flip, t[b], t[a]), np.where(flip, t[a], t[b])
            vals.append(stat(u))
        v = [x for x in vals if x is not None]
        if not v:
            continue
        total += 1
        fired += np.mean(v) >= min_mean and sum(x > 0 for x in v) >= int(np.ceil(min_share * len(v)))
    return fired / total if total else None


def sign_flip(values):
    """Exact two-sided sign-flip test over per-topic values (H0: symmetric about 0)."""
    v = np.array([x for x in values if x is not None])
    if len(v) == 0:
        return None
    obs = abs(v.mean())
    hits = sum(abs((v * np.array(s)).mean()) >= obs - 1e-12 for s in itertools.product((1, -1), repeat=len(v)))
    return hits / 2 ** len(v)


def bootstrap(topics, stat, draws=4000):
    """Hierarchical bootstrap of the pooled mean: topics with replacement, then questions within each topic.
    Also the per-topic bootstrap SD (questions only)."""
    n = len(topics)
    means, per = [], [[] for _ in topics]
    for _ in range(draws):
        idx = RNG.integers(0, n, n)
        vals = []
        for j in idx:
            t = topics[j]
            k = RNG.integers(0, len(t["blind"]), len(t["blind"]))
            v = stat({key: (arr[k] if isinstance(arr, np.ndarray) else arr) for key, arr in t.items()})
            vals.append(v)
        m, _ = pooled(vals)
        if m is not None:
            means.append(m)
    for j, t in enumerate(topics):
        for _ in range(1000):
            k = RNG.integers(0, len(t["blind"]), len(t["blind"]))
            v = stat({key: (arr[k] if isinstance(arr, np.ndarray) else arr) for key, arr in t.items()})
            if v is not None:
                per[j].append(v)
    lo, hi = np.percentile(means, [2.5, 97.5]) if means else (None, None)
    return (None if lo is None else float(lo), None if hi is None else float(hi), float(np.std(means)) if means else None,
            [float(np.std(p)) if p else None for p in per])  # fmt: skip


def holm(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i])
    adj, run = [None] * len(ps), 0.0
    for rank, i in enumerate(order):
        run = max(run, min(1.0, (len(ps) - rank) * ps[i]))
        adj[i] = run
    return adj


# ---- repeat noise ----
def frames_hash(d):
    files = sorted(p for p in (d / "frames").glob("*/s*_*.jpg") if p.stem.split("_")[1] in ("40", "70", "95"))
    return [hashlib.md5(p.read_bytes()).hexdigest() for p in files]


def repeat_pairs(novel_runs):
    """(topic, a, b) per-question P(right) pairs measured on byte-identical material."""
    pairs = []
    for name, run in novel_runs.items():
        a = run / "autofix"
        if (a / "dv_frames_test.json").exists() and frames_hash(run) and frames_hash(run) == frames_hash(a):
            pairs.append((name, "ours vs autofix (identical frames)", load(run / "dv_frames_test.json"),
                          load(a / "dv_frames_test.json")))  # fmt: skip
        reps = sorted((REPEATS / run.name).glob("r*/dv_frames_test.json"))
        base = load(run / "dv_frames_test.json")
        for r in reps:
            pairs.append((name, f"repeat {r.parent.name}", base, load(r)))
    return pairs


def run_repeats(novel_runs, k):
    for name, run in novel_runs.items():
        if not (run / "dv_frames_test.json").exists():
            continue
        for i in range(1, k + 1):
            cache = REPEATS / run.name / f"r{i}"
            cache.mkdir(parents=True, exist_ok=True)
            dvgain.probes(run, run, "frames", cache_dir=cache)
            print(f"[noise] repeat {i} {name}", flush=True)


def noise_floor(deltas, topics_b, draws=20000):
    """95% range of a version difference in M9 produced by repeat noise alone: each question's difference is drawn
    from the observed identical-input differences with a random sign, then normalised by the topic's 1 - B_eff."""
    d = np.array(deltas)
    rooms = [1 - max(dvgain.CHANCE, b) for b in topics_b]
    rooms = [r for r in rooms if r >= dvgain.MIN_ROOM]
    single, pooled_m = [], []
    for _ in range(draws):
        per = []
        for r in rooms:
            x = RNG.choice(d, 8) * RNG.choice((-1, 1), 8)
            per.append(x.mean() / r)
        single.append(per[0])
        pooled_m.append(np.mean(per))
    return (float(np.percentile(np.abs(single), 95)), float(np.percentile(np.abs(pooled_m), 95)))


# ---- the comparisons ----
def novel_runs():
    topics = json.loads((ROOT / "bench" / "results" / "novel12" / "topics.json").read_text())
    return {t: ROOT / "runs" / generate.slug(t) for t in topics}


def mmmc_runs():
    topics = json.loads((ROOT / "bench" / "results" / "mmmc-n12-seed0" / "topics.json").read_text())
    return {t: ROOT / "runs" / generate.slug(t) for t in topics}


def build(runs, files):
    out = []
    for name, run in runs.items():
        t = topic(run, files)
        if t is not None:
            out.append((name, t))
    return out


def comparisons():
    nv, mm = novel_runs(), mmmc_runs()
    q3 = "dv_qwen2_5vl_3b_"
    C = []
    # (id, family, question, topics, stat, swaps, scale label)
    C.append(
        (
            "N1",
            "primary",
            "NOVEL-12: the base video teaches (M9 > 0, 3 frames vs no video)",
            build(nv, {"blind": "dv_blind_test.json", "x": "dv_frames_test.json"}),
            st_gain,
            [("x", "blind")],
            st_gain_test,
        )
    )
    C.append(("N2", "primary", "NOVEL-12: the gain is specific (own video − another topic's video, M9)",
              build(nv, {"blind": "dv_blind_test.json", "x": "dv_frames_test.json", "y": "dv_other_frames_test.json"}),
              st_dgain, [("x", "y")]))  # fmt: skip
    C.append(
        (
            "N3",
            "secondary",
            "NOVEL-12: the dense video teaches (NVG, dense vs no video)",
            build(nv, {"blind": "dv_blind_test.json", "x": "dv_visual_test.json"}),
            st_gain,
            [("x", "blind")],
            st_gain_test,
        )
    )
    C.append(("N4", "secondary", "NOVEL-12: 3 frames teach more than the dense video (M9 − NVG dense)",
              build(nv, {"blind": "dv_blind_test.json", "x": "dv_frames_test.json", "y": "dv_visual_test.json"}),
              st_dgain, [("x", "y")]))  # fmt: skip
    C.append(("L1", "primary", "Layout study: Claude-fixed − ours (M9, preregistered)",
              build(nv, {"blind": "dv_blind_test.json", "x": "claude_fixed/dv_frames_test.json",
                         "y": "dv_frames_test.json"}), st_dgain, [("x", "y")]))  # fmt: skip
    C.append(("L2", "secondary", "Layout study: autofix − ours (M9)",
              build(nv, {"blind": "dv_blind_test.json", "x": "autofix/dv_frames_test.json", "y": "dv_frames_test.json"}),
              st_dgain, [("x", "y")]))  # fmt: skip
    C.append(("L3", "secondary", "Layout study: Claude-fixed − ours (M7, dense video + motion bonus)",
              build(nv, {"blind": "dv_blind_test.json", "xv": "claude_fixed/dv_visual_test.json",
                         "xs": "claude_fixed/dv_static_test.json", "yv": "dv_visual_test.json",
                         "ys": "dv_static_test.json"}), st_dm7, [("xv", "yv"), ("xs", "ys")]))  # fmt: skip
    C.append(("P1", "primary", "MMMC pilot, 3B student: learner − base (M9)",
              build(mm, {"blind": f"{q3}blind_test.json", "x": f"learner/{q3}frames_test.json",
                         "y": f"{q3}frames_test.json"}), st_dgain, [("x", "y")]))  # fmt: skip
    C.append(("P2", "secondary", "MMMC pilot, 3B student: own − other topic (raw P(right), R9)",
              build(mm, {"blind": f"{q3}blind_test.json", "x": f"{q3}frames_test.json",
                         "y": f"{q3}other_frames_test.json"}), st_raw, [("x", "y")]))  # fmt: skip
    C.append(("P3", "secondary", "MMMC pilot, gemma: own − other topic (raw P(right), R9; M9 undefined at the ceiling)",
              build(mm, {"blind": "dv_blind_test.json", "x": "dv_frames_test.json", "y": "dv_other_frames_test.json"}),
              st_raw, [("x", "y")]))  # fmt: skip
    C.append(("P4", "secondary", "MMMC pilot, gemma: learner − base (raw P(right), R9)",
              build(mm, {"blind": "dv_blind_test.json", "x": "learner/dv_frames_test.json", "y": "dv_frames_test.json"}),
              st_raw, [("x", "y")]))  # fmt: skip
    # frame size or frame count (bench/frames512.py): the same 3 frames per section at 512 px
    C.append(("N5", "secondary", "NOVEL-12: 3 frames at 768 px − the same frames at 512 px (M9)",
              build(nv, {"blind": "dv_blind_test.json", "x": "dv_frames_test.json", "y": "dv_f512_frames_test.json"}),
              st_dgain, [("x", "y")]))  # fmt: skip
    C.append(("N6", "secondary", "NOVEL-12: 3 frames at 512 px − the dense video at 512 px (M9 − NVG dense)",
              build(nv, {"blind": "dv_blind_test.json", "x": "dv_f512_frames_test.json", "y": "dv_visual_test.json"}),
              st_dgain, [("x", "y")]))  # fmt: skip
    # Claude as the student (bench/claude_student.py): right/wrong scores over 4 option orders
    for cid, model in (("H", "claude_haiku_5_5_"), ("S", "claude_sonnet_5_5_")):
        name = "Haiku 5.5" if cid == "H" else "Sonnet 5.5"
        C.append((f"{cid}1", "secondary", f"{name} student: the base video teaches (M9 > 0, binary)",
                  build(nv, {"blind": f"dv_{model}blind_test.json", "x": f"dv_{model}frames_test.json"}),
                  st_gain, [("x", "blind")], st_gain_test))  # fmt: skip
        C.append((f"{cid}2", "secondary", f"{name} student: own video − another topic's video (M9)",
                  build(nv, {"blind": f"dv_{model}blind_test.json", "x": f"dv_{model}frames_test.json",
                             "y": f"dv_{model}other_frames_test.json"}), st_dgain, [("x", "y")]))  # fmt: skip
        C.append((f"{cid}3", "secondary", f"{name} student: Claude-fixed − ours (M9)",
                  build(nv, {"blind": f"dv_{model}blind_test.json", "x": f"claude_fixed/dv_{model}frames_test.json",
                             "y": f"dv_{model}frames_test.json"}), st_dgain, [("x", "y")]))  # fmt: skip
    # the repair on NOVEL-12 (stage F0, the pilot loop's revisions). Appended last, so the random draws of the
    # comparisons above stay the same.
    C.append(("N7", "secondary", "NOVEL-12, stage F0: learner repair − base (M9)",
              build(nv, {"blind": "dv_blind_test.json", "x": "learner/dv_frames_test.json", "y": "dv_frames_test.json"}),
              st_dgain, [("x", "y")]))  # fmt: skip
    C.append(("N8", "secondary", "NOVEL-12, stage F0: learner repair − generic repair (M9)",
              build(nv, {"blind": "dv_blind_test.json", "x": "learner/dv_frames_test.json",
                         "y": "generic/dv_frames_test.json"}), st_dgain, [("x", "y")]))  # fmt: skip
    # stages F1-F5: the video TEST sees, i.e. the base video where the stage's gate refused the revision (as in
    # bench/stages.py), so such a topic's difference is exactly 0. Appended after N7/N8 for the same reason.
    for k, stage in enumerate(STAGES_LATER, 1):
        C.append((f"R{k}", "secondary", f"NOVEL-12, stage {stage}: learner repair − base (M9)",
                  stage_build(nv, stage, "learner", "base"), st_dgain, [("x", "y")]))
        C.append((f"R{k}g", "secondary", f"NOVEL-12, stage {stage}: learner repair − generic repair (M9)",
                  stage_build(nv, stage, "learner", "generic"), st_dgain, [("x", "y")]))
    return C, nv


STAGES_LATER = ("F1", "F2", "F3", "F4", "F5")


def stage_build(runs, stage, x, y):
    """build() over the videos a stage served: rows_<stage>.json says, per topic and mode, revision or base."""
    path = ROOT / "bench" / "results" / "novel12-stages" / f"rows_{stage}.json"
    if not path.exists():
        return []
    served = {r["topic"]: r for r in json.loads(path.read_text())}

    def frames(run, mode):
        r = served.get(run.name)
        if mode == "base" or r is None or r[mode]["served"] != "revision":
            return "dv_frames_test.json"
        return f"{mode}/dv_frames_test.json" if stage == "F1" else f"stages/{stage}/{mode}/dv_frames_test.json"

    out = []
    for name, run in runs.items():
        if run.name not in served:
            continue
        t = topic(run, {"blind": "dv_blind_test.json", "x": frames(run, x), "y": frames(run, y)})
        if t is not None:
            out.append((name, t))
    return out


def students(nv):
    """Accuracy (share right, all option orders) per student and material, as means over concepts."""
    tags = {"gemma": ("", (0, 1)), "haiku": ("claude_haiku_5_5_", (0, 1, 2, 3)),
            "sonnet": ("claude_sonnet_5_5_", (0, 1, 2, 3))}  # fmt: skip
    out = {}
    for name, (tag, rots) in tags.items():
        row = {}
        for key, sub, kind in (("blind", "", "blind"), ("frames", "", "frames"), ("other", "", "other_frames"),
                               ("fixed", "claude_fixed/", "frames")):  # fmt: skip
            vals = [dvgain.score(json.loads(p.read_text()), False, rots)
                    for p in (run / sub / f"dv_{tag}{kind}_test.json" for run in nv.values()) if p.exists()]  # fmt: skip
            row[key] = float(np.mean(vals)) if vals else None
        out[name] = row
    return out


def claude_repeat(nv):
    """Claude's own repeat noise: the frames pass asked twice (rep1), per model."""
    out = {}
    for model in ("claude_haiku_5_5_", "claude_sonnet_5_5_"):
        answers = changed = 0
        deltas, blinds = [], []
        for run in nv.values():
            a_path, b_path = run / f"dv_{model}frames_test.json", run / f"dv_{model}rep1_frames_test.json"
            if not (a_path.exists() and b_path.exists()):
                continue
            a, b = json.loads(a_path.read_text()), json.loads(b_path.read_text())
            for ra, rb in zip(a["rotations"], b["rotations"]):
                for x, y in zip(ra["items"], rb["items"]):
                    answers += 1
                    changed += x["choice"] != y["choice"]
            la, lb = load(a_path), load(b_path)
            deltas += [lb[i] - la[i] for i in la if i in lb]
            bl = load(run / f"dv_{model}blind_test.json")
            if bl:
                blinds.append(np.mean(list(bl.values())))
        if answers:
            f1, f10 = noise_floor(deltas, blinds) if deltas and blinds else (None, None)
            out[model.rstrip("_")] = {"answers": answers, "changed": changed, "floor_one_topic_M9": f1,
                                      "floor_mean_of_topics_M9": f10}  # fmt: skip
    return out


def verdict(p_meas, p_holm, p_gen, lo, hi):
    if p_meas is None:
        return "no data"
    if (p_holm if p_holm is not None else p_meas) < 0.05 and lo is not None and (lo > 0 or hi < 0):
        return "real, and holds over topics" if p_gen is not None and p_gen < 0.05 else "beyond noise for these videos"
    if p_meas < 0.05:
        return "beyond noise for these videos only (not over topics / not after correction)"
    return "within noise"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repeat", type=int, default=0, help="re-probe the NOVEL-12 base frames this many times first")
    args = ap.parse_args()
    C, nv = comparisons()
    if args.repeat:
        run_repeats(nv, args.repeat)

    pairs = repeat_pairs(nv)
    deltas = [b[i] - a[i] for _, _, a, b in pairs for i in a if i in b]
    moved = sum(abs(x) > 0.01 for x in deltas)
    blind_b = [load(r / "dv_blind_test.json") for r in nv.values() if (r / "dv_blind_test.json").exists()]
    floor1, floor10 = noise_floor(deltas, [np.mean(list(b.values())) for b in blind_b]) if deltas else (None, None)

    rows, prim = [], []
    for cid, fam, q, tops, stat, swaps, *test in C:
        names = [n for n, _ in tops]
        ts = [t for _, t in tops]
        if not ts:
            rows.append({"id": cid, "family": fam, "question": q, "n": 0})
            continue
        _, _, p_meas, p_topic = randomisation(ts, test[0] if test else stat, swaps)
        obs = [stat(t) for t in ts]
        mean, _ = pooled(obs)
        lo, hi, se, per_sd = bootstrap(ts, stat)
        p_gen = sign_flip(obs)
        n_def = sum(o is not None for o in obs)
        pos = sum(o is not None and o > 0 for o in obs)
        rows.append({"id": cid, "family": fam, "question": q, "n": n_def, "mean": mean, "ci": [lo, hi], "se": se,
                     "mde": None if se is None else 2.8 * se, "p_measurement": p_meas, "p_topics": p_gen,
                     "positive": pos, "per_topic": [{"topic": n, "value": o, "p": p, "sd_items": s}
                                                    for n, o, p, s in zip(names, obs, p_topic, per_sd)]})  # fmt: skip
        if cid == "L1":
            rows[-1]["rule_false_positive_rate"] = rule_fpr(ts, stat, swaps)
            rows[-1]["rule_fires"] = bool(mean >= 0.05 and pos >= int(np.ceil(0.7 * n_def)))
        if fam == "primary":
            prim.append(len(rows) - 1)
    adj = holm([rows[i]["p_measurement"] for i in prim])
    for i, a in zip(prim, adj):
        rows[i]["p_holm"] = a
    for r in rows:
        if r["n"]:
            r["verdict"] = verdict(r["p_measurement"], r.get("p_holm"), r["p_topics"], *r["ci"])

    OUT.mkdir(parents=True, exist_ok=True)
    rep = {"repeat_noise": {"pairs": len(pairs), "questions": len(deltas), "moved_over_0.01": moved,
                            "max_abs": max((abs(x) for x in deltas), default=None),
                            "floor_one_topic_M9": floor1, "floor_mean_of_topics_M9": floor10,
                            "sources": sorted({s for _, s, _, _ in pairs})}, "comparisons": rows,
           "claude_repeat": claude_repeat(nv), "students": students(nv)}  # fmt: skip
    (OUT / "report.json").write_text(json.dumps(rep, indent=1, ensure_ascii=False))
    (OUT / "report.md").write_text(markdown(rep))
    print(markdown(rep))


def f(x, pts=True):
    return "n/a" if x is None else (f"{100 * x:+.1f}" if pts else f"{x:.3g}")


def markdown(rep):
    rn = rep["repeat_noise"]
    out = ["# Noise model", "",
           "Points are on the 0-100 scale (M9, NVG, D-VGAIN, or raw P(right) x 100).", "",
           "## Repeat noise (same input twice)", "",
           (f"{rn['questions']} questions in {rn['pairs']} identical-input pairs ({', '.join(rn['sources']) or 'none'}): "
           f"{rn['moved_over_0.01']} moved by more than 0.01, the largest by {f(rn['max_abs'])} points of P(right)."),
           (f"Repeat noise alone puts 95% of version differences within ±{f(rn['floor_one_topic_M9'])[1:]} M9 points on "
           f"one topic and ±{f(rn['floor_mean_of_topics_M9'])[1:]} on the mean of all topics."), "",
           "## Comparisons", "",
           "| | Question | n | Mean | 95% CI (topics, questions) | MDE | p (measurement) | p Holm | p (over topics) | > 0 | Verdict |",
           "|---|---|---|---|---|---|---|---|---|---|---|"]  # fmt: skip
    for r in rep["comparisons"]:
        if not r["n"]:
            out.append(f"| {r['id']} | {r['question']} | 0 | | | | | | | | no data yet |")
            continue
        out.append(f"| {r['id']} | {r['question']} | {r['n']} | {f(r['mean'])} | [{f(r['ci'][0])}, {f(r['ci'][1])}] | "
                   f"{f(r['mde'])[1:]} | {r['p_measurement']:.4f} | {f(r.get('p_holm'), False)} | "
                   f"{f(r['p_topics'], False)} | {r['positive']}/{r['n']} | {r['verdict']} |")  # fmt: skip
    for r in rep["comparisons"]:
        if "rule_false_positive_rate" in r:
            out += [
                "",
                (
                    f"Preregistered layout rule (mean >= +5 and >= 70% of topics ahead): fires now = {r['rule_fires']}; "
                    f"it fires on noise alone in {100 * r['rule_false_positive_rate']:.1f}% of randomisations."
                ),
            ]
    for m, c in (rep.get("claude_repeat") or {}).items():
        out += ["", (f"Repeat noise, {m}: {c['changed']} of {c['answers']} answers changed when the frames pass was "
                f"asked again; 95% of M9 differences within ±{f(c['floor_one_topic_M9'])[1:]} on one topic and "
                f"±{f(c['floor_mean_of_topics_M9'])[1:]} on the mean.")]  # fmt: skip
    out += ["", "## Per topic (value, item-level p, SD from resampling the questions)", ""]
    for r in rep["comparisons"]:
        if not r["n"]:
            continue
        out.append(f"**{r['id']}** {r['question']}")
        out.append("")
        out += [f"- {t['topic'][:40]}: {f(t['value'])} (p {f(t['p'], False)}, SD {f(t['sd_items'])[1:]})"
                for t in r["per_topic"]]  # fmt: skip
        out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    main()
