"""Claude as the student: the NOVEL-12 forced-choice probes of D-VGAIN, asked of Claude Haiku 5.5 or Sonnet 5.5.

Same material as the gemma probes (the 12 frames per video, 3 per section, at 768 px), same questions, same unlearn
system prompt. Two differences, both forced by the API:
    - Claude returns no log-probabilities, so an answer is right (1) or wrong (0). To make that less coarse, every
      pass uses 4 cyclic option orders instead of 2 (32 answers per concept).
    - The reply is constrained by a JSON schema (one letter per question) instead of the "1: <letter>" lines.
A request served by a fallback model (another model than the one asked) does not count: its answers are dropped.

Passes per concept: blind (no material), frames (own video), other_frames (another topic's video, the ladder's
pairing), claude_frames (the Claude-fixed video), and frames again (rep1) for Claude's own repeat noise.
Cached as dv_<model>_<pass>_test.json in the same format as dvgain.probes, so bench/noise_model.py reads them.

    python bench/claude_student.py --model claude-haiku-5-5 [--workers 6]
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import subprocess
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "bench"))

from claude_fix import CLAUDE_PY, api_env

from c2vlab import dvgain, generate, teachquiz

ROTATIONS = (0, 1, 2, 3)
ASK = "Give one letter (A, B, C or D) for every question, in the JSON format required."
LOCK = threading.Lock()
SPEND = {"in": 0, "out": 0, "calls": 0, "fallback": 0}


def schema(n):
    keys = [f"q{i}" for i in range(1, n + 1)]
    return {"type": "object", "properties": {k: {"type": "string", "enum": list(dvgain.LETTERS)} for k in keys},
            "required": keys, "additionalProperties": False}  # fmt: skip


def ask(model, system, text, images, n):
    req = {"system": system, "text": text, "images": [str(p) for p in images], "schema": schema(n), "effort": "low",
           "model": model, "max_tokens": 8000}  # fmt: skip
    r = subprocess.run([str(CLAUDE_PY), str(ROOT / "bench" / "claude_call.py")], input=json.dumps(req),
                       capture_output=True, text=True, env=api_env(), timeout=900, check=False)  # fmt: skip
    if r.returncode:
        raise RuntimeError(f"claude_call failed: {r.stderr[-400:]}")
    out = json.loads(r.stdout)
    with LOCK:
        SPEND["in"] += out["usage"]["input_tokens"]
        SPEND["out"] += out["usage"]["output_tokens"]
        SPEND["calls"] += 1
    if out["model"] != model:  # served by a fallback: not this student's answer
        with LOCK:
            SPEND["fallback"] += 1
        return None, out
    try:
        parsed = json.loads(out["text"])
    except (json.JSONDecodeError, TypeError):
        return None, out
    return [parsed.get(f"q{i}") for i in range(1, n + 1)], out


def probe(model, topic, qs, images, body, rotation):
    shown = [{**q, "options": dvgain.rotate(q, rotation)} for q in qs]
    listing = "\n\n".join(
        f"{i}. {q['question']}\n" + "\n".join(f"{L}) {q['options'][L]}" for L in dvgain.LETTERS)
        for i, q in enumerate(shown, 1)
    )
    system = teachquiz.forced(teachquiz.UNLEARN.format(topic=topic))
    letters, out = None, None
    for _ in range(2):
        letters, out = ask(model, system, f"{body}\n\nQUESTIONS:\n{listing}\n\n{ASK}", images, len(qs))
        if letters is not None:
            break
    items = []
    for i, q in enumerate(qs):
        shown_letter = letters[i] if letters else None
        if shown_letter not in dvgain.LETTERS:
            items.append({"id": q["id"], "p": None, "choice": None, "right": False, "p_right": None})
            continue
        j = dvgain.LETTERS.index(shown_letter)
        choice = dvgain.LETTERS[(j - rotation) % dvgain.K]  # shown letter -> original letter
        p = {L: (1.0 if L == choice else 0.0) for L in dvgain.LETTERS}
        items.append({"id": q["id"], "p": p, "choice": choice, "right": choice == q["answer"],
                      "p_right": p[q["answer"]]})  # fmt: skip
    return {"rotation": rotation, "items": items, "served_by": out.get("model") if out else None,
            "request_id": out.get("request_id") if out else None, "usage": out.get("usage") if out else None}  # fmt: skip


def run_pass(model, topic_dir, material_dir, kind, cache_dir, tag):
    path = cache_dir / f"dv_{tag}{kind}_test.json"
    if path.exists():
        return json.loads(path.read_text())
    plan = json.loads((topic_dir / "plan.json").read_text())
    qs = json.loads((topic_dir / "quiz.json").read_text())["test"]
    images, body = dvgain.material(material_dir, kind)
    out = {"kind": kind, "student": model, "frames": len(images),
           "rotations": [probe(model, plan["topic"], qs, images, body, r) for r in ROTATIONS]}  # fmt: skip
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, choices=["claude-haiku-5-5", "claude-sonnet-5-5"])
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args()
    tag = args.model.replace("-", "_") + "_"
    topics = json.loads((ROOT / "bench" / "results" / "novel12" / "topics.json").read_text())
    dirs = {t: ROOT / "runs" / generate.slug(t) for t in topics}
    have = [t for t in topics if (dirs[t] / "video.mp4").exists()]
    other = {t: dirs[have[(i + 1) % len(have)]] for i, t in enumerate(have)}  # the ladder's pairing
    jobs = []
    for t in have:
        d = dirs[t]
        jobs += [(t, d, d, "blind", d, tag), (t, d, d, "frames", d, tag), (t, d, other[t], "frames", d, tag + "other_"),
                 (t, d, d, "frames", d, tag + "rep1_")]  # fmt: skip
        if (d / "claude_fixed" / "video.mp4").exists():
            jobs.append((t, d, d / "claude_fixed", "frames", d / "claude_fixed", tag))
    with cf.ThreadPoolExecutor(args.workers) as pool:
        futures = {pool.submit(run_pass, args.model, d, m, k, c, g): (t, m, g) for t, d, m, k, c, g in jobs}
        for f in cf.as_completed(futures):
            t, m, g = futures[f]
            try:
                r = f.result()
                s = dvgain.score(r, False, ROTATIONS)
                print(f"[claude] {args.model} {g[len(tag):] or 'own_'}{'fixed_' if 'claude_fixed' in str(m) else ''}"
                      f"{r['kind']:7s} {t[:30]:30s} right {s:.2f}  spend in {SPEND['in']} out {SPEND['out']} "
                      f"calls {SPEND['calls']} fallback {SPEND['fallback']}", flush=True)  # fmt: skip
            except Exception as exc:  # noqa: BLE001 - one failure is reported, the rest go on
                print(f"[claude] FAILED {t} {m} {g}: {type(exc).__name__}: {exc}", flush=True)
    print(f"[claude] done {args.model}: {SPEND}", flush=True)


if __name__ == "__main__":
    main()
