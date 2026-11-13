"""Ours + timing fixes: each admitted base video with the automatic, model-free fixes of c2vlab/temporal.py applied
(Transform whose target is used later -> ReplacementTransform; prose typeset as maths keeps its spaces), rendered
into runs/<topic>/autofix/. One of the three versions of the layout side study (ours, ours + timing fixes,
Claude-fixed); never used inside F0-F5, where the same fixes are part of F2.

    python bench/autofix.py            # every NOVEL-12 topic
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from c2vlab import generate, temporal


def autofix(topic):
    run = ROOT / "runs" / generate.slug(topic)
    out = run / "autofix"
    if (out / "autofix.json").exists():
        return json.loads((out / "autofix.json").read_text())
    (out / "sections").mkdir(parents=True, exist_ok=True)
    plan = json.loads((run / "plan.json").read_text())
    secs = json.loads((run / "sections.json").read_text())
    record, clips = {"topic": topic, "sections": {}}, {}
    for s in secs:
        src, dst = run / "sections" / f"{s['id']}.py", out / "sections" / f"{s['id']}.py"
        new, applied = temporal.fix(src.read_text())
        dst.write_text(new)
        mp4, _ = generate.render(dst, s["id"].upper(), out / "media")
        if not mp4 and applied:  # a fix that breaks the render is withdrawn
            shutil.copy(src, dst)
            mp4, _ = generate.render(dst, s["id"].upper(), out / "media")
            applied = [{**a, "withdrawn": "did not render"} for a in applied]
        if mp4:
            clips[s["id"]] = mp4
        record["sections"][s["id"]] = {"applied": applied, "rendered": bool(mp4)}
    generate.join(out, plan, clips)
    (out / "autofix.json").write_text(json.dumps(record, indent=1, ensure_ascii=False))
    return record


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--questions", default=str(ROOT / "bench" / "novel" / "questions.json"))
    ap.add_argument("--topics", nargs="*")
    ap.add_argument("--workers", type=int, default=3)
    a = ap.parse_args()
    topics = a.topics or list(json.loads(Path(a.questions).read_text()))
    with cf.ThreadPoolExecutor(a.workers) as pool:
        for t, rec in zip(topics, pool.map(autofix, topics), strict=True):
            n = sum(len(v["applied"]) for v in rec["sections"].values())
            print(f"[autofix] {t}: {n} fixes, {sum(v['rendered'] for v in rec['sections'].values())} sections rendered",
                  flush=True)  # fmt: skip


if __name__ == "__main__":
    main()
