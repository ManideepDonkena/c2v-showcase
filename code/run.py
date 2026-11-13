"""c2v-lab command line (one topic at a time; bench/run_bench.py runs many).

python run.py topic "Pythagoras theorem" [--grade "class 8"]     video, quiz, base eval, every feedback mode
python run.py gen "Pythagoras theorem"                             only the video (plan, code, render, layout)
python run.py layout runs/<slug>                                   scene graph + MVQS + repair per section
python run.py eval runs/<slug> [--split dev|test]                  TeachQuiz (local student), evidence, controls
python run.py feedback runs/<slug> --mode learner|generic|learner_all
python run.py c2v runs/<slug>                                      Code2Video's own TeachQuiz via the Gemini API
python run.py estimate runs/<slug> [--topics 12 --runs 3]          what `c2v` would cost, before spending
python run.py manual-export runs/<slug>                            the same by hand in a chat app (free)
python run.py manual-import manual/<slug>
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from c2vlab import c2v_eval, feedback, generate, layout, manual, pipeline

ROOT = Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["topic", "gen", "layout", "eval", "feedback", "c2v", "estimate",
                                    "manual-export", "manual-import"])  # fmt: skip
    ap.add_argument("target")
    ap.add_argument("--grade", default="undergraduate students")
    ap.add_argument("--sections", type=int, default=4)
    ap.add_argument("--split", default="test")
    ap.add_argument("--mode", default="learner", choices=feedback.MODES)
    ap.add_argument("--topics", type=int, default=1)
    ap.add_argument("--runs", type=int, default=1)
    a = ap.parse_args()
    t = Path(a.target)

    if a.cmd == "topic":
        print(json.dumps(pipeline.run_topic(a.target, a.grade, ROOT / "runs" / generate.slug(a.target)), indent=1))
    elif a.cmd == "gen":
        print(pipeline.make_video(a.target, a.grade, ROOT / "runs" / generate.slug(a.target), a.sections))
    elif a.cmd == "layout":
        for p in sorted((t / "sections").glob("s*.py")):
            print(p.stem, layout.repair(p.stem, t)[0])
    elif a.cmd == "eval":
        print(json.dumps(pipeline.headline(pipeline.evaluate(t, a.split)), indent=1))
    elif a.cmd == "feedback":
        print(json.dumps(feedback.round_(t, a.mode), indent=1))
    elif a.cmd == "c2v":
        plan, quiz = json.loads((t / "plan.json").read_text()), json.loads((t / "quiz.json").read_text())
        for d in [t] + [t / m for m in feedback.MODES if (t / m / "video.mp4").exists()]:
            r = c2v_eval.evaluate(plan["topic"], quiz["test"], d / "video.mp4")
            (d / "eval_c2v.json").write_text(json.dumps(r, indent=1))
            print(d.name, {k: r[k] for k in ("pre", "unlearned", "video", "gain")})
    elif a.cmd == "estimate":
        videos = 1 + sum((t / m / "video.mp4").exists() for m in feedback.MODES)
        secs = c2v_eval.seconds(t / "video.mp4")
        for model in ("or:google/gemini-2.5-pro", "or:google/gemini-3-flash-preview", "or:google/gemini-2.5-flash"):
            print(c2v_eval.estimate(secs, videos_per_topic=videos, topics=a.topics, runs=a.runs, model=model))
    elif a.cmd == "manual-export":
        print(manual.export(t, ROOT / "manual" / t.name) / "INSTRUCTIONS.md")
    elif a.cmd == "manual-import":
        r = manual.import_(t)
        print(json.dumps({k: v for k, v in r.items() if k != "videos"}, indent=1))
        for name, v in r["videos"].items():
            print(name, v["label"], "video", v["video"], "gain", v["gain"], "unparsed", v["unparsed"])


if __name__ == "__main__":
    main()
