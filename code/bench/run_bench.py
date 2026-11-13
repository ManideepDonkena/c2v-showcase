"""Run the benchmark over MMMC topics: for each, video -> quiz (ours = DEV, MMMC's = TEST) -> base eval -> every
feedback mode -> eval. Resumable (every step is cached in runs/<slug>/). Then the other-topic control on each base.

    python bench/run_bench.py --n 12 --seed 0 [--workers 2] [--modes learner,generic,learner_all]
    python bench/run_bench.py --topics "Change of basis;The determinant"
    python bench/run_bench.py --n 12 --manual-export        # prompts and videos for the chat-app evaluation
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import random
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from c2vlab import feedback, generate, manual, pipeline, teachquiz

GRADE = "undergraduate students"


def choose(n, seed, names, questions):
    if names:
        return [t.strip() for t in names.split(";") if t.strip()]
    if n >= len(questions):
        return list(questions)
    return random.Random(seed).sample(sorted(questions), n)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=12)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--topics", default="")
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--modes", default=",".join(feedback.MODES))
    ap.add_argument("--name", default="")
    ap.add_argument("--manual-export", action="store_true")
    ap.add_argument("--questions", default=str(ROOT / "bench" / "mmmc" / "questions.json"), help="TEST per topic")
    ap.add_argument("--cards", default="", help="invented concepts: the card every writing step is given")
    a = ap.parse_args()
    questions = json.loads(Path(a.questions).read_text())
    cards = json.loads(Path(a.cards).read_text()) if a.cards else {}
    topics = choose(a.n, a.seed, a.topics, questions)
    modes = tuple(m for m in a.modes.split(",") if m)
    name = a.name or f"mmmc-n{len(topics)}-seed{a.seed}"
    out = ROOT / "bench" / "results" / name
    out.mkdir(parents=True, exist_ok=True)
    (out / "topics.json").write_text(json.dumps(topics, indent=1, ensure_ascii=False))
    dirs = {t: ROOT / "runs" / generate.slug(t) for t in topics}

    if a.manual_export:
        for t, d in dirs.items():
            if (d / "video.mp4").exists():
                print(manual.export(d, ROOT / "manual" / d.name, modes) / "INSTRUCTIONS.md")
        return

    def one(topic):
        began = time.time()
        log = lambda m: print(f"[{generate.slug(topic)[:24]}] {m}", flush=True)
        row = pipeline.run_topic(topic, GRADE, dirs[topic], modes, questions[topic], log=log, source=cards.get(topic))
        row["seconds"] = round(time.time() - began)
        return row

    rows = []
    with cf.ThreadPoolExecutor(a.workers) as pool:
        futures = {pool.submit(one, t): t for t in topics}
        for f in cf.as_completed(futures):
            try:
                rows.append(f.result())
                print(f"[bench] done {futures[f]}", flush=True)
            except Exception as exc:  # noqa: BLE001 - one topic's failure is recorded, the rest go on
                rows.append({"topic": futures[f], "error": f"{type(exc).__name__}: {exc}"})
                print(f"[bench] FAILED {futures[f]}: {exc}", flush=True)

    # other-topic control: each base video's quiz answered from the NEXT topic's base video
    done = [t for t in topics if (dirs[t] / "video.mp4").exists() and (dirs[t] / "quiz.json").exists()]
    for i, t in enumerate(done):
        other = dirs[done[(i + 1) % len(done)]]
        if len(done) < 2:
            break
        plan = json.loads((dirs[t] / "plan.json").read_text())
        quiz = json.loads((dirs[t] / "quiz.json").read_text())
        images, body = teachquiz.material(other)
        score = teachquiz.student(plan["topic"], plan["grade"], quiz["test"], images, body)["score"]
        for row in rows:
            if row.get("topic") == t and "base" in row:  # a topic that failed after its base video has no row to fill
                row["base"]["control_other_topic"] = score
    (out / "rows.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    print(f"[bench] {len(rows)} topics -> {out / 'rows.json'}; next: python bench/analyze.py {out}")


if __name__ == "__main__":
    main()
