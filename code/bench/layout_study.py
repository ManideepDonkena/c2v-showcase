"""Layout side study on the NOVEL-12 base videos: ours, ours + timing fixes (no model), Claude-fixed.

For every topic and version: sections complete, layout (SGA MVQS per section, measured again now so every version
uses the same tracker), lasting conflicts, timing faults (c2vlab/temporal.py), and what the student learns: confidence
on the right answer with no video, 3 frames per section and the dense silent video, the gain on 3 frames (M9) and
D-VGAIN on the dense video (M7). The no-video probe is shared by the three versions of a topic.

    python bench/layout_study.py            -> bench/results/layout-study/{rows.json, report.md}
"""

from __future__ import annotations

import argparse
import collections
import json
import statistics as st
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from c2vlab import attach, dvgain, generate, layout, mvqs, temporal

VERSIONS = {"ours": "", "autofix": "autofix", "claude": "claude_fixed"}
OUT = ROOT / "bench" / "results" / "layout-study"


def layout_of(vdir, plan):
    secs = json.loads((vdir / "sections.json").read_text()) if (vdir / "sections.json").exists() else []
    scores, conflicts, timing, attached = [], 0, 0, 0
    with tempfile.TemporaryDirectory() as tmp:
        for s in secs:
            path = vdir / "sections" / f"{s['id']}.py"
            g, m, _ = layout.measure(path, s["id"].upper(), Path(tmp) / f"{s['id']}.json")
            scores.append(m)
            conflicts += len(mvqs.persistent_conflicts(g["states"])) if g.get("states") else 0
            timing += len(temporal.check(path.read_text()))
            attached += len(attach.broken(path.read_text(), g))
    return {"sections": len(secs), "planned": len(plan["sections"]), "mvqs_mean": round(st.mean(scores), 1) if scores else None,
            "mvqs_min": round(min(scores), 1) if scores else None, "conflicts": conflicts, "timing": timing,
            "broken_attachments": attached}  # fmt: skip


def teaching(vdir, run):
    s = lambda p: dvgain.score(p, True, (0, 1))
    blind = dvgain.probes(run, run, "blind")
    p = {k: dvgain.probes(vdir, run, k) for k in ("frames", "static", "visual")}
    sb, sf, ss, sv = s(blind), s(p["frames"]), s(p["static"]), s(p["visual"])
    return {"blind": round(sb, 3), "frames": round(sf, 3), "static": round(ss, 3), "visual": round(sv, 3),
            "M9": dvgain.nvg(sf, sb), "M7": dvgain.dvgain(sv, ss, sb)}  # fmt: skip


def collect(topics):
    rows = []
    for t in topics:
        run = ROOT / "runs" / generate.slug(t)
        plan = json.loads((run / "plan.json").read_text())
        row = {"topic": t, "admission": json.loads((run / "admission.json").read_text()) if (run / "admission.json").exists() else None}
        for v, sub in VERSIONS.items():
            vdir = run / sub if sub else run
            if not (vdir / "video.mp4").exists():
                continue
            row[v] = {"layout": layout_of(vdir, plan), "teaching": teaching(vdir, run)}
            print(f"[study] {t[:30]:30s} {v:8s} {row[v]['layout']} M9 {row[v]['teaching']['M9']}", flush=True)
        fx = run / "claude_fixed" / "fixes.json"
        if fx.exists():
            f = json.loads(fx.read_text())
            row["claude_issues"] = collections.Counter(i["kind"] for s in f["sections"] for i in s["issues"])
            row["claude_tokens"] = {"in": f["input_tokens"], "out": f["output_tokens"]}
            row["claude_kept"] = f"{sum(s['kept'] for s in f['sections'])}/{len(f['sections'])}"
        rows.append(row)
    return rows


def report(rows):
    lines = ["# Layout side study: ours, ours + timing fixes, Claude-fixed", "",
             "| Topic | Version | Sections | MVQS mean | MVQS min | Conflicts | Timing faults | Broken attachments | No video | 3 frames | Dense | M9 | M7 |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]  # fmt: skip
    f = lambda x: "--" if x is None else f"{x:.2f}"
    for r in rows:
        for v in VERSIONS:
            if v not in r:
                continue
            lay, te = r[v]["layout"], r[v]["teaching"]
            lines.append(f"| {r['topic']} | {v} | {lay['sections']}/{lay['planned']} | {lay['mvqs_mean']} | {lay['mvqs_min']} | "
                         f"{lay['conflicts']} | {lay['timing']} | {lay.get('broken_attachments', '--')} | {f(te['blind'])} | {f(te['frames'])} | {f(te['visual'])} | "
                         f"{f(te['M9'])} | {f(te['M7'])} |")  # fmt: skip
    kinds = collections.Counter()
    for r in rows:
        kinds.update(r.get("claude_issues") or {})
    lines += ["", f"Faults Claude fixed, by kind: {dict(kinds)}"]
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--questions", default=str(ROOT / "bench" / "novel" / "questions.json"))
    ap.add_argument("--topics", nargs="*")
    a = ap.parse_args()
    topics = a.topics or list(json.loads(Path(a.questions).read_text()))
    OUT.mkdir(parents=True, exist_ok=True)
    rows = collect(topics)
    (OUT / "rows.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False, default=dict))
    (OUT / "report.md").write_text(report(rows))
    print(report(rows))


if __name__ == "__main__":
    main()
