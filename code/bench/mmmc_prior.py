"""How much of MMMC's TEST can a student answer with no video? Forced choice, the unlearning prompt kept, two option
rotations, log-probabilities (c2vlab.dvgain.probe). If the prior is near 1, no video can show a gain on these items.

    python bench/mmmc_prior.py [--student gemma4:26b]   ->  bench/results/mmmc-prior-<student>.json
    python bench/mmmc_prior.py --questions bench/novel/questions.json --name novel [--cards bench/novel/cards.json]
    (--cards gives the student each topic's card as text: the ceiling, and a check of the answer key)
"""

from __future__ import annotations

import argparse
import json
import statistics as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from c2vlab import dvgain, llm


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--student", default=llm.STUDENT)
    ap.add_argument("--questions", default=str(ROOT / "bench" / "mmmc" / "questions.json"))
    ap.add_argument("--name", default="mmmc")
    ap.add_argument("--cards", default="")
    a = ap.parse_args()
    llm.STUDENT = a.student
    questions = json.loads(Path(a.questions).read_text())
    cards = json.loads(Path(a.cards).read_text()) if a.cards else {}
    tag = f"{a.name}-{'card' if cards else 'prior'}"
    out = ROOT / "bench" / "results" / f"{tag}-{a.student.replace(':', '_').replace('/', '_')}.json"
    done = json.loads(out.read_text()) if out.exists() else {}
    for topic, qs in questions.items():
        if topic in done:
            continue
        qs = [{**q, "id": f"t{i}"} for i, q in enumerate(qs, 1)]
        try:
            body = f"MATERIAL (a text, not a video): {cards[topic]}" if cards else "MATERIAL: none."
            done[topic] = [dvgain.probe(topic, qs, [], body, r) for r in dvgain.ROTATIONS]
        except RuntimeError as exc:
            print(f"FAILED {topic}: {exc}", flush=True)
            continue
        out.write_text(json.dumps(done, indent=1, ensure_ascii=False))
    items = [it for rots in done.values() for r in rots for it in r["items"]]
    p = [it["p_right"] for it in items if it["p_right"] is not None]
    acc = [it["right"] for it in items]
    per_topic = [st.mean(it["right"] for r in rots for it in r["items"]) for rots in done.values()]
    summary = {
        "set": tag, "student": a.student, "topics": len(done), "item_rotations": len(items),
        "accuracy": round(st.mean(acc), 3), "mean_p_right": round(st.mean(p), 3),
        "share_p_right_over_0.9": round(sum(x > 0.9 for x in p) / len(p), 3),
        "share_p_right_under_0.5": round(sum(x < 0.5 for x in p) / len(p), 3),
        "topics_all_right": sum(x == 1 for x in per_topic),
        "topics_under_0.75": sum(x < 0.75 for x in per_topic),
        "missing_letters": sum(it["p_right"] is None for it in items),
    }  # fmt: skip
    (out.with_suffix(".summary.json")).write_text(json.dumps(summary, indent=1))
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
