"""Metric ladder: TeachQuiz improved one change at a time, every rung judged by the same four tests on the same videos.

Rungs (each adds one change to the one before):
    M0  TeachQuiz as the pilot scored it (S2 - S1, NULL allowed, answers matched by id only)
    M1  + answers matched by order when the student copies the template's ids
    M2  + forced choice (no NULL): S_frames - S_blind, discrete, one option order
    M3  + normalised gain: NVG(S_frames) with B_eff = max(1/4, S_blind)
    M4  + dense silent video: NVG(S_visual) at up to 4 frames a second
    M5  + motion control: D-VGAIN = NVG(S_visual) + 0.5 max(0, S_visual - S_static)
    M6  + continuous scoring: P(right letter) from log-probabilities instead of 0/1
    M7  + option rotation: the mean of two cyclic option orders
    M8  + prior filter: only items the blind student does not already know (P_blind(right) < 0.5), pooled per video
    M9  M7 without the dense video: NVG of the 3-frames-per-section material, continuous, two option orders (added
        after the first NOVEL-12 video taught far more through 3 sharp frames per section than through hundreds of
        small ones)

Tests (a teaching metric must pass all four):
    defined      share of videos with a score (NVG is undefined when the student knows everything without the video)
    separation   own video vs another topic's video, base videos, paired over topics: must be clearly > 0
    reliability  agreement of two measurements over videos (seeds for M0-M1, option orders for M2-M6)
    resolution   ties among learner - base differences (a tie carries no information)
and then the paper's comparisons (learner vs base, generic, learner_all) under every rung.

    python bench/metric_ladder.py bench/results/mmmc-n12-seed0 [--workers 2] [--analyse-only]
Writes bench/results/<run>-ladder/{rows.json, report.json, report.md}.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import re
import statistics as stats
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "bench"))

from analyze import paired

from c2vlab import dvgain, feedback, generate, llm, teachquiz

CONDITIONS = ("base", *feedback.MODES)
PAIRS = (("learner", "base"), ("learner", "generic"), ("learner", "learner_all"), ("generic", "base"))
RUNGS = ("M0", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "R7", "R9")
NAMES = {
    "M0": "TeachQuiz, as in the pilot", "M1": "+ answers matched by order", "M2": "+ forced choice",
    "M3": "+ normalised gain (NVG)", "M4": "+ dense silent video", "M5": "+ motion control (D-VGAIN)",
    "M6": "+ continuous scoring", "M7": "+ option rotation", "M8": "+ prior filter (unknown items only)",
    "M9": "M7 on 3 frames per section (no dense video)",
    # not rungs: the raw continuous difference, defined even with no room, to show what normalisation hides
    "R7": "raw: dense video P(right) minus no-video P(right)",
    "R9": "raw: 3 frames/section P(right) minus no-video P(right)",
}  # fmt: skip


TAG = ""  # set by --student: every cached measurement of another student carries its name


def tq2(video_dir, other=None):
    path = video_dir / f"eval_test.{TAG}tq2.json"
    if path.exists():
        return json.loads(path.read_text())
    r = teachquiz.evaluate(video_dir, "test", other=other)
    path.write_text(json.dumps(r, indent=1, ensure_ascii=False))
    return r


PASSES = (*dvgain.PASSES, "tq")  # --passes narrows this, e.g. to frames only for a student with a small context


def measure(topic_dir, video_dir, other):
    """Every raw measurement one video needs; all cached in the video's folder. A pass not run is None."""
    raw = {"tq2": None}
    if "tq" in PASSES:
        try:
            raw["tq2"] = tq2(video_dir, other)
        except RuntimeError as exc:  # the student gave no readable TeachQuiz reply: only the TeachQuiz rows go missing
            print(f"[ladder] no TeachQuiz for {video_dir}: {exc}", flush=True)
    for kind in dvgain.PASSES:
        raw[kind] = dvgain.probes(video_dir, topic_dir, kind, tag=TAG) if kind in PASSES else None
    if other is not None:
        for kind in dvgain.PASSES:
            raw[f"other_{kind}"] = (dvgain.probes(other, topic_dir, kind, cache_dir=video_dir, tag=f"{TAG}other_")
                                    if kind in PASSES else None)  # fmt: skip
    return raw


def _none(f):
    """f, but None when any argument is None (a pass that was not run)."""
    return lambda *a: None if any(x is None for x in a) else f(*a)


def rungs(raw, blind, pilot):
    """The score of every rung for one video's measurements (and its other-topic control when measured)."""
    s = lambda p, cont=False, rots=(0,), keep=None: None if p is None else dvgain.score(p, cont, rots, keep)
    nvg, dvg, sub = _none(dvgain.nvg), _none(dvgain.dvgain), _none(lambda a, b: a - b)
    p_blind = {}
    for r in blind["rotations"]:
        for it in r["items"]:
            p_blind.setdefault(it["id"], []).append(dvgain.CHANCE if it["p_right"] is None else it["p_right"])
    unknown = {i for i, ps in p_blind.items() if stats.mean(ps) < 0.5}

    def ladder(fr, st, vi, rot=(0,)):
        b0, b1 = s(blind, False, rot), s(blind, True, rot)
        both = (0, 1)
        bp = s(blind, True, both)
        out = {
            "M2": sub(s(fr, False, rot), b0),
            "M3": nvg(s(fr, False, rot), b0),
            "M4": nvg(s(vi, False, rot), b0),
            "M5": dvg(s(vi, False, rot), s(st, False, rot), b0),
            "M6": dvg(s(vi, True, rot), s(st, True, rot), b1),
            "M7": dvg(s(vi, True, both), s(st, True, both), bp),
            "M8": (dvg(s(vi, True, both, unknown), s(st, True, both, unknown), s(blind, True, both, unknown))
                   if unknown else None),
            "M9": nvg(s(fr, True, both), bp),
            "R7": sub(s(vi, True, both), bp),
            "R9": sub(s(fr, True, both), bp),
        }  # fmt: skip
        return out

    t = raw["tq2"]
    own = {"M0": None if pilot is None else pilot["teachquiz"] / 100, "M1": None if t is None else t["teachquiz"] / 100,
           **ladder(raw["frames"], raw["static"], raw["visual"])}  # fmt: skip
    rot1 = ladder(raw["frames"], raw["static"], raw["visual"], rot=(1,))
    seeds = [] if t is None else [r["score"] / 100 for r in t["runs"]["full"]]
    out = {"own": own, "rot1": {k: rot1[k] for k in ("M2", "M3", "M4", "M5", "M6")}, "tq2_seeds": seeds,
           "unknown_items": len(unknown), "s_blind": s(blind), "s_blind_p": s(blind, True, (0, 1)),
           "s_frames": s(raw["frames"]), "s_static": s(raw["static"]), "s_visual": s(raw["visual"]),
           "s_visual_p": s(raw["visual"], True, (0, 1)), "abstained": None if t is None else t.get("abstained"),
           "s_frames_p": s(raw["frames"], True, (0, 1)), "s_static_p": s(raw["static"], True, (0, 1)),
           "split": {"R7": [sub(s(raw["visual"], True, (r,)), s(blind, True, (r,))) for r in (0, 1)],
                     "R9": [sub(s(raw["frames"], True, (r,)), s(blind, True, (r,))) for r in (0, 1)]}}  # fmt: skip
    if "other_frames" in raw:
        ctl = ladder(raw["other_frames"], raw["other_static"], raw["other_visual"])
        co = None if t is None else t.get("control_other_topic")
        ctl["M0"] = None if pilot is None or pilot.get("control_other_topic") is None else (
            pilot["control_other_topic"] - pilot["none"]) / 100  # fmt: skip
        ctl["M1"] = None if co is None else (co - t["none"]) / 100
        out["other"] = ctl
    return out


def collect(run, workers):
    topics = json.loads((run / "topics.json").read_text())
    dirs = {t: ROOT / "runs" / generate.slug(t) for t in topics}
    have = [t for t in topics if (dirs[t] / "video.mp4").exists()]
    other = {t: dirs[have[(i + 1) % len(have)]] for i, t in enumerate(have)}
    for t in have:
        b = dvgain.probes(dirs[t], dirs[t], "blind", tag=TAG)
        print(f"[ladder] blind {dvgain.score(b):.2f} P {dvgain.score(b, True, (0, 1)):.3f} {t[:50]}", flush=True)
    pilot_rows = {}  # M0 is the pilot's own student; it means nothing for another student
    if (run / "rows.json").exists() and not TAG:
        pilot_rows = {r["topic"]: r for r in json.loads((run / "rows.json").read_text())}
    jobs = [(t, c, dirs[t] if c == "base" else dirs[t] / c) for t in have for c in CONDITIONS]
    jobs = [j for j in jobs if (j[2] / "video.mp4").exists() and (j[2] / "sections.json").exists()]

    def one(t, c, v):
        return measure(dirs[t], v, other[t] if c == "base" else None)

    raws = {}
    with cf.ThreadPoolExecutor(workers) as pool:
        futures = {pool.submit(one, *j): j for j in jobs}
        for f in cf.as_completed(futures):
            t, c, _ = futures[f]
            try:
                raws[(t, c)] = f.result()
                print(f"[ladder] measured {c:11} {t[:50]}", flush=True)
            except Exception as exc:  # noqa: BLE001 - one failure is recorded, the rest go on
                print(f"[ladder] FAILED {c} {t}: {type(exc).__name__}: {exc}", flush=True)
    rows = []
    for t in have:
        blind = dvgain.probes(dirs[t], dirs[t], "blind", tag=TAG)
        row = {"topic": t}
        for c in CONDITIONS:
            v = dirs[t] if c == "base" else dirs[t] / c
            if (t, c) in raws:
                pilot = json.loads((v / "eval_test.json").read_text()) if (v / "eval_test.json").exists() else None
                if pilot is not None and c == "base":
                    pilot["control_other_topic"] = ((pilot_rows.get(t) or {}).get("base") or {}).get("control_other_topic")
                row[c] = rungs(raws[(t, c)], blind, pilot)
            elif c != "base" and "base" in row and not (v / "video.mp4").exists():
                row[c] = {**row["base"], "same_as_base": True}  # no revision was made: the base video is what it serves
            # a video that exists but could not be measured is left out, so it drops from its pairs instead of tying
        rows.append(row)
    return rows


def spearman(a, b):
    pairs = [(x, y) for x, y in zip(a, b, strict=True) if x is not None and y is not None]
    if len(pairs) < 4 or len({p[0] for p in pairs}) < 2 or len({p[1] for p in pairs}) < 2:
        return None
    from scipy.stats import spearmanr

    return round(float(spearmanr([p[0] for p in pairs], [p[1] for p in pairs]).statistic), 3)


def reliability(m, vids):
    """Agreement of two measurements of the same videos, for one rung."""
    seeded = [v for v in vids if len(v["tq2_seeds"]) > 1]  # a video whose TeachQuiz failed has no seeds
    if m == "M1" and seeded:
        return spearman([v["tq2_seeds"][0] for v in seeded], [stats.mean(v["tq2_seeds"][1:]) for v in seeded]), \
            "seed 1 vs seeds 2-3"  # fmt: skip
    if m in ("M2", "M3", "M4", "M5", "M6"):
        return spearman([v["own"][m] for v in vids], [v["rot1"][m] for v in vids]), "option order 0 vs 1"
    if m in ("R7", "R9"):
        return spearman([v["split"][m][0] for v in vids], [v["split"][m][1] for v in vids]), "option order 0 vs 1"
    return None, "n/a"


def analyse(rows):
    """Whether a rung measures teaching (scored, distinct values, agreement, separation, the prior) is judged on the
    base videos: one per topic. A topic's repairs are near-copies of its base video, so pooling them would count each
    topic up to four times. The pooled values are kept as *_all, for reference. The repair columns pair by topic."""
    vids = [r[c] for r in rows for c in CONDITIONS if c in r and not r[c].get("same_as_base")]
    base = [r["base"] for r in rows if "base" in r]
    rep = {"topics": len(rows), "videos": len(vids), "rungs": {}}
    for m in RUNGS:
        defined = [x for x in (v["own"][m] for v in base) if x is not None]
        defined_all = [x for x in (v["own"][m] for v in vids) if x is not None]
        rel, rel_kind = reliability(m, base)
        sep = paired([b["own"][m] for b in base], [(b.get("other") or {}).get(m) for b in base])
        both = [r for r in rows if "learner" in r and "base" in r]  # pair by topic; paired() drops undefined pairs
        lb = paired([r["learner"]["own"][m] for r in both], [r["base"]["own"][m] for r in both])
        rep["rungs"][m] = {
            "name": NAMES[m], "defined": f"{len(defined)}/{len(base)}",
            "mean": round(stats.mean(defined), 3) if defined else None,
            "distinct_values": len({round(x, 4) for x in defined}),
            "separation_own_minus_other": sep, "reliability": rel, "reliability_kind": rel_kind,
            "defined_all": f"{len(defined_all)}/{len(vids)}", "distinct_values_all": len({round(x, 4) for x in defined_all}),
            "reliability_all": reliability(m, vids)[0],
            "learner_base_ties": None if not lb else lb["ties"],
            "conditions": {f"{a} - {b}": paired([r[a]["own"][m] for r in rows if a in r and b in r],
                                                [r[b]["own"][m] for r in rows if a in r and b in r]) for a, b in PAIRS},
        }  # fmt: skip
    avg = lambda xs: round(stats.mean(x), 3) if (x := [v for v in xs if v is not None]) else None
    rep["prior"] = {
        "s_blind_mean": avg(b["s_blind"] for b in base),
        "s_blind_p_mean": avg(b["s_blind_p"] for b in base),
        "topics_blind_all_right": sum(b["s_blind"] >= 1 for b in base),
        "unknown_items_per_topic": [b["unknown_items"] for b in base],
    }
    for k in ("s_visual", "s_static", "s_frames", "s_visual_p", "s_frames_p", "s_static_p"):
        rep["prior"][f"{k}_mean"] = avg(v[k] for v in base)
        rep["prior"][f"{k}_mean_all"] = avg(v[k] for v in vids)
    rep["prior"]["tq_abstained_mean"] = avg(v["abstained"] for v in base)
    rep["prior"]["tq_abstained_mean_all"] = avg(v["abstained"] for v in vids)
    return rep


def fmt(p):
    if not p:
        return "n/a"
    lo, hi = p["ci95"]
    w = f", p {p['wilcoxon_p']}" if p.get("wilcoxon_p") is not None else ""
    return f"{p['mean_diff']:+.3f} [{lo:+.3f}, {hi:+.3f}] {p['wins']}/{p['ties']}/{p['losses']}{w}"


def markdown(rep, name):
    out = [f"# Metric ladder: {name}", "", (f"{rep['topics']} topics, {rep['videos']} distinct videos. Defined, distinct "
           "values, reliability and separation: base videos (one per topic); in brackets, over all videos."), "",
           "| Rung | Change | Defined | Distinct values | Own − other topic (base) | Reliability | learner−base ties |",
           "|---|---|---|---|---|---|---|"]  # fmt: skip
    for m, r in rep["rungs"].items():
        rel = "n/a" if r["reliability"] is None else f"{r['reliability']} [{r['reliability_all']}] ({r['reliability_kind']})"
        out.append(f"| {m} | {r['name']} | {r['defined']} [{r['defined_all']}] | {r['distinct_values']} "
                   f"[{r['distinct_values_all']}] | {fmt(r['separation_own_minus_other'])} | {rel} | "
                   f"{r['learner_base_ties']} |")  # fmt: skip
    out += ["", "## Paired condition differences per rung", "", "mean [bootstrap 95% CI] wins/ties/losses, Wilcoxon p",
            "", "| Rung | learner − base | learner − generic | learner − learner_all | generic − base |",
            "|---|---|---|---|---|"]  # fmt: skip
    for m, r in rep["rungs"].items():
        out.append(f"| {m} | " + " | ".join(fmt(p) for p in r["conditions"].values()) + " |")
    out += ["", "## What the student knows without the video", "", "```", json.dumps(rep["prior"], indent=1), "```"]
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run")
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--analyse-only", action="store_true")
    ap.add_argument("--student", default="", help="another student model; its results go to <run>-ladder-<student>")
    ap.add_argument("--passes", default="", help="comma list of frames,static,visual,tq (default: all)")
    ap.add_argument("--base-only", action="store_true", help="measure only each topic's base video (no repairs)")
    ap.add_argument("--out", default="", help="results folder name (default <run>-ladder)")
    a = ap.parse_args()
    global TAG, PASSES, CONDITIONS
    if a.base_only:
        CONDITIONS = ("base",)
    if a.passes:
        PASSES = tuple(x.strip() for x in a.passes.split(","))
    run = Path(a.run)
    out = run.parent / f"{run.name}-ladder"
    if a.student:
        llm.STUDENT = a.student
        TAG = re.sub(r"[^a-z0-9]+", "_", a.student.lower()) + "_"
        out = run.parent / f"{run.name}-ladder-{TAG[:-1]}"
    if a.out:
        out = run.parent / a.out
    out.mkdir(parents=True, exist_ok=True)
    rows = json.loads((out / "rows.json").read_text()) if a.analyse_only else collect(run, a.workers)
    (out / "rows.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    rep = analyse(rows)
    (out / "report.json").write_text(json.dumps(rep, indent=1))
    (out / "report.md").write_text(markdown(rep, run.name))
    print(markdown(rep, run.name))


if __name__ == "__main__":
    main()
