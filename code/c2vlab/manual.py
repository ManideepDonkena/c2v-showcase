"""Code2Video's TeachQuiz through a chat app (e.g. Gemini in the browser) instead of the API, to save cost.

export: a folder per topic with the videos under blind labels (V1, V2, ...: the person pasting and the chatbot
        never see which condition a video is), the three stages' prompts ready to paste, an empty reply file per
        prompt, and INSTRUCTIONS.md. The key from label to condition stays in key.json.
import: reads the pasted replies, grades each question as Code2Video does (the first standalone A-D after
        "ANSWER", else the first anywhere; NULL / INSUFFICIENT = wrong) and writes eval_manual.json.

Differences from Code2Video, to state in the paper: the questions of one stage go in ONE message (theirs: one call
per question), and the chat app's model, system prompt and temperature are the app's, not an API's.
"""

from __future__ import annotations

import json
import random
import re
import shutil
from pathlib import Path

from .c2v_eval import BASELINE, UNLEARN, UNLEARN_VIDEO

ASK = """{prefix}

{questions}
Answer EVERY question above. For each one write exactly:
Question <n>:
EVIDENCE_STATUS = (SUFFICIENT | INSUFFICIENT)
ANSWER = (A|B|C|D or NULL)
then one short sentence."""

STEPS = """# Code2Video TeachQuiz by hand: {topic}

Model used (write it here before you start, e.g. "Gemini 2.5 Pro, gemini.google.com"): ______

Rules that keep the numbers valid:
1. **A NEW chat for every prompt file.** A chat that has seen one video, or one stage's answers, remembers it.
2. Use the same model for every file of every topic. If the app changes model, note it here.
3. Paste the prompt file's text exactly as it is; attach only the video it names; change nothing.
4. Copy the chatbot's WHOLE answer into the reply file of the same name (`replies/<same name>.txt`).
5. Do not tell the chatbot which video is which; the labels V1, V2, ... are blind on purpose.

Files to do, in any order ({n} chats):
{todo}

Then run: `python run.py manual-import {folder}`
"""


def _questions(qs):
    return "\n".join(
        f"Question {i}: {q['question']}\nOptions:\n" + "\n".join(f"{k}) {q['options'][k]}" for k in "ABCD") + "\n"
        for i, q in enumerate(qs, 1)
    )


def export(run_dir, out_dir, modes=("learner", "generic", "learner_all")):
    run_dir, out_dir = Path(run_dir), Path(out_dir)
    plan = json.loads((run_dir / "plan.json").read_text())
    quiz = json.loads((run_dir / "quiz.json").read_text())
    qs, concept = quiz["test"], plan["topic"]
    videos = {"base": run_dir / "video.mp4"}
    videos.update({m: run_dir / m / "video.mp4" for m in modes if (run_dir / m / "video.mp4").exists()})
    names = list(videos)
    random.Random(concept).shuffle(names)
    key = {f"V{i}": name for i, name in enumerate(names, 1)}
    (out_dir / "prompts").mkdir(parents=True, exist_ok=True)
    (out_dir / "replies").mkdir(exist_ok=True)
    (out_dir / "videos").mkdir(exist_ok=True)
    todo = []

    def write(name, prefix, video=None):
        (out_dir / "prompts" / f"{name}.txt").write_text(ASK.format(prefix=prefix, questions=_questions(qs)))
        reply = out_dir / "replies" / f"{name}.txt"
        if not reply.exists():
            reply.write_text("")
        todo.append(f"- [ ] `prompts/{name}.txt`" + (f" + attach `videos/{video}`" if video else " (no video)"))

    write("stage1_baseline", BASELINE)
    write("stage2_unlearned", UNLEARN.format(concept=concept))
    for label, name in key.items():
        shutil.copy(videos[name], out_dir / "videos" / f"{label}.mp4")
        write(f"stage3_{label}", UNLEARN_VIDEO.format(concept=concept), f"{label}.mp4")
    (out_dir / "key.json").write_text(json.dumps({"run": str(run_dir), "topic": concept, "key": key}, indent=1))
    (out_dir / "questions.json").write_text(json.dumps(qs, indent=1, ensure_ascii=False))
    steps = STEPS.format(topic=concept, n=len(todo), todo="\n".join(todo), folder=out_dir)
    (out_dir / "INSTRUCTIONS.md").write_text(steps)
    return out_dir


def grade(reply, qs):
    """Per question: split the reply at "Question n", take ANSWER = X, else the first standalone A-D (theirs)."""
    parts = re.split(r"(?im)^\W*question\s*(\d+)\s*[:.)]", reply)
    blocks = {int(parts[i]): parts[i + 1] for i in range(1, len(parts) - 1, 2)}
    out = []
    for i, q in enumerate(qs, 1):
        text = blocks.get(i, "")
        m = re.search(r"ANSWER\s*[=:]\s*\**\s*([A-D]|NULL)\b", text, re.IGNORECASE) or re.search(r"\b([A-D])\b", text)
        choice = m.group(1).upper() if m else "MISSING"
        out.append({"id": q["id"], "choice": choice, "right": choice == q["answer"]})
    return out


def import_(out_dir):
    out_dir = Path(out_dir)
    meta = json.loads((out_dir / "key.json").read_text())
    qs = json.loads((out_dir / "questions.json").read_text())

    def score(name):
        text = (out_dir / "replies" / f"{name}.txt").read_text()
        if not text.strip():
            return None, []
        rows = grade(text, qs)
        return round(100 * sum(r["right"] for r in rows) / len(rows), 1), rows

    s1, _ = score("stage1_baseline")
    s2, _ = score("stage2_unlearned")
    result = {"protocol": "code2video-manual", "topic": meta["topic"], "pre": s1, "unlearned": s2,
              "unlearning_success": None if s1 is None or s2 is None else s2 <= s1, "videos": {}}  # fmt: skip
    for label, name in meta["key"].items():
        s3, r3 = score(f"stage3_{label}")
        missing = sum(r["choice"] == "MISSING" for r in r3)
        result["videos"][name] = {"label": label, "video": s3, "gain": None if s3 is None or s2 is None else round(s3 - s2, 1),
                                  "unparsed": missing, "answers": r3}  # fmt: skip
    (out_dir / "eval_manual.json").write_text(json.dumps(result, indent=1))
    Path(meta["run"], "eval_c2v_manual.json").write_text(json.dumps(result, indent=1))
    return result
