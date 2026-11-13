"""Pipeline ablation: the feedback loop with features added one at a time (c2vlab/stages.py), every stage scored on
TEST with the same metric (the ladder's continuous, rotated, forced-choice probes) on the same base videos.

    python bench/stages.py bench/results/novel12 --stage F2 [--workers 3]     run one stage (cumulative features)
    python bench/stages.py bench/results/novel12 --report                      table over every stage run so far

F0 and F1 reuse the pilot loop's revisions (runs/<topic>/<mode>); F1 serves the base video when the gate failed.
Writes bench/results/<run>-stages/{rows.json, report.json, report.md}.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import os
import statistics as stats
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "bench"))

from analyze import paired

from c2vlab import dvgain, feedback, generate, stages

MODES = feedback.MODES
DENSE = os.getenv("C2V_DENSE", "1") != "0"  # 0: score on M9 only; must be the same for every version compared
PAIRS = (("learner", "base"), ("learner", "generic"), ("learner", "learner_all"), ("generic", "base"))


def score(video_dir, topic_dir):
    """The ladder's metrics for one video (M5 discrete, M7 continuous rotated) and raw S_visual. With C2V_DENSE=0 only
    M9 (3 frames per section): the dense video and start/end frames are not asked, and M7, M5 and their raw scores are
    None. The dense video is about two thirds of the student's work."""
    blind = dvgain.probes(topic_dir, topic_dir, "blind")
    if not DENSE:
        sf, sb = dvgain.score(dvgain.probes(video_dir, topic_dir, "frames"), True, (0, 1)), dvgain.score(blind, True, (0, 1))
        return {"m7": None, "m9": dvgain.nvg(sf, sb), "s_frames_p": sf, "nvg": None, "s_visual_p": None, "s_static_p": None,
                "s_blind_p": sb, "m5": None, "sections": len(json.loads((video_dir / "sections.json").read_text())),
                "mvqs": feedback.section_mvqs(video_dir)}  # fmt: skip
    p = {k: dvgain.probes(video_dir, topic_dir, k) for k in ("frames", "static", "visual")}
    both = (0, 1)
    sv, ss, sb = (dvgain.score(p["visual"], True, both), dvgain.score(p["static"], True, both),
                  dvgain.score(blind, True, both))  # fmt: skip
    sf = dvgain.score(p["frames"], True, both)
    return {"m7": dvgain.dvgain(sv, ss, sb), "m9": dvgain.nvg(sf, sb), "s_frames_p": sf, "nvg": dvgain.nvg(sv, sb),
            "s_visual_p": sv, "s_static_p": ss,
            "s_blind_p": sb, "m5": dvgain.dvgain(dvgain.score(p["visual"]), dvgain.score(p["static"]),
                                                  dvgain.score(blind)),
            "sections": len(json.loads((video_dir / "sections.json").read_text())),
            "mvqs": feedback.section_mvqs(video_dir)}  # fmt: skip


def one_topic(topic_dir, stage):
    row = {"topic": topic_dir.name, "base": score(topic_dir, topic_dir)}
    for mode in MODES:
        if stage in ("F0", "F1"):
            v = topic_dir / mode
            fb = json.loads((v / "feedback.json").read_text()) if (v / "feedback.json").exists() else {}
            changed = fb.get("changed") or []
            serve = bool(changed) and (stage == "F0" or fb.get("kept"))
            rep = {"changed": changed, "kept": fb.get("kept", False), "fixes": fb.get("fixes") or {},
                   "served": "revision" if serve else "base", "edit_size": {}}  # fmt: skip
        else:
            rep = stages.round_(topic_dir, mode, stage)
            v = topic_dir / "stages" / stage / mode
            serve = rep["served"] == "revision"
        s = score(v, topic_dir) if serve else row["base"]
        row[mode] = {**s, "served": rep["served"], "changed": len(rep["changed"]), "fixed": len(rep["fixes"]),
                     "kept": rep.get("kept"), "edit_size": rep.get("edit_size") or {}}  # fmt: skip
    return row


def run(results, stage, workers):
    topics = json.loads((results / "topics.json").read_text())
    dirs = [ROOT / "runs" / generate.slug(t) for t in topics]
    dirs = [d for d in dirs if (d / "video.mp4").exists()]
    out = results.parent / f"{results.name}-stages"
    out.mkdir(parents=True, exist_ok=True)
    path = out / f"rows_{stage}.json"
    rows = []
    with cf.ThreadPoolExecutor(workers) as pool:
        futures = {pool.submit(one_topic, d, stage): d for d in dirs}
        for f in cf.as_completed(futures):
            try:
                rows.append(f.result())
                print(f"[stages] {stage} done {futures[f].name}", flush=True)
            except Exception as exc:  # noqa: BLE001 - one topic's failure is recorded, the rest go on
                print(f"[stages] {stage} FAILED {futures[f].name}: {type(exc).__name__}: {exc}", flush=True)
    path.write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    return rows


def fmt(p):
    if not p:
        return "n/a"
    lo, hi = p["ci95"]
    w = f", p {p['wilcoxon_p']}" if p.get("wilcoxon_p") is not None else ""
    return f"{p['mean_diff']:+.3f} [{lo:+.3f}, {hi:+.3f}] {p['wins']}/{p['ties']}/{p['losses']}{w}"


def report(results):
    out = results.parent / f"{results.name}-stages"
    rep = {}
    for stage in stages.STAGES:
        path = out / f"rows_{stage}.json"
        if not path.exists():
            continue
        rows = json.loads(path.read_text())
        r = {"topics": len(rows)}
        for metric in ("m7", "m9", "s_visual_p", "s_frames_p", "m5"):
            r[metric] = {f"{a} - {b}": paired([x[a][metric] for x in rows], [x[b][metric] for x in rows])
                         for a, b in PAIRS}  # fmt: skip
        r["means"] = {c: {m: (round(stats.mean(v), 3) if (v := [x[c][m] for x in rows if x[c][m] is not None]) else None)
                          for m in ("m7", "m9", "s_visual_p", "s_frames_p", "sections", "mvqs")} for c in ("base", *MODES)}  # fmt: skip
        r["process"] = {
            mode: {"sections_fixed": sum(x[mode]["fixed"] for x in rows),
                   "sections_changed": sum(x[mode]["changed"] for x in rows),
                   "served_revision": sum(x[mode]["served"] == "revision" for x in rows),
                   "mean_edit_size": round(stats.mean(e), 3) if (e := [v for x in rows for v in x[mode]["edit_size"].values()]) else None}
            for mode in MODES}  # fmt: skip
        rep[stage] = r
    (out / "report.json").write_text(json.dumps(rep, indent=1))
    lines = [f"# Pipeline ablation: {results.name}"]
    for metric, name in (("m9", "M9 (gain on 3 frames per section, continuous, two option orders)"),
                         ("m7", "M7 (D-VGAIN on the dense video, continuous, two option orders)")):  # fmt: skip
        lines += ["", f"Metric: {name}.", "",
                  "| Stage | Features | learner − base | learner − generic | learner − learner_all | generic − base |",
                  "|---|---|---|---|---|---|"]  # fmt: skip
        for stage, r in rep.items():
            feats = ", ".join(sorted(stages.FEATURES[stage])) or "pilot loop"
            lines.append(f"| {stage} | {feats} | " + " | ".join(fmt(p) for p in r[metric].values()) + " |")
    head = ("| Stage | sections asked (learner) | rewritten and rendered | served revisions (of topics) | mean edit size"
            " | MVQS learner | sections learner |")
    lines += ["", head, "|---|---|---|---|---|---|---|"]
    for stage, r in rep.items():
        p, m = r["process"]["learner"], r["means"]["learner"]
        lines.append(f"| {stage} | {p['sections_fixed']} | {p['sections_changed']} | {p['served_revision']}/{r['topics']} "
                     f"| {p['mean_edit_size']} | {m['mvqs']} | {m['sections']} |")  # fmt: skip
    (out / "report.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("results")
    ap.add_argument("--stage", choices=stages.STAGES)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    results = Path(a.results)
    if a.stage:
        run(results, a.stage, a.workers)
    report(results)


if __name__ == "__main__":
    main()
