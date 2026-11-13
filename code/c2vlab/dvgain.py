"""D-VGAIN (Dynamic Video-Grounded Gain) and the probe every rung of the metric ladder is computed from.

TeachQuiz asks a prompted-to-forget student to answer NULL when the video does not show the answer. Without a video it
abstains on everything (S1 = 0 because it refuses, not because it does not know). D-VGAIN removes NULL and measures the
prior instead of trying to erase it:

    S_blind   question and options only (once per topic)
    S_frames  TeachQuiz's material: 3 frames per section (at 40, 70, 95% of it)
    S_static  the first and last frame of every section: start and end states, no animation
    S_visual  the silent video densely sampled (FPS frames a second)

    c = 1/K,  B_eff = max(c, S_blind),  NVG = (S - B_eff) / (1 - B_eff),  DML = S_visual - S_static,
    D-VGAIN = NVG(S_visual) + LAMBDA * max(0, DML)

One probe = one call per (material, option rotation): the student answers every question as "<n>: <letter>" lines at
temperature 0, and the log-probabilities at each letter's position give P(A..D). The top letter is the forced-choice
answer (discrete scoring); P(right letter) is the continuous score. Asking for one letter per call does not work with
gemma4: its first token is often not a letter, and one call per question with 400 frames costs 90 s.

Rotation r shows the options shifted cyclically (the text under A moves to B, ...); probabilities are mapped back to the
original letters, so averaging rotations cancels a preference for a letter.

Choices made where the proposal is open, and why:
- The student keeps Code2Video's unlearning prompt with NULL removed (`teachquiz.forced`), so the change from TeachQuiz
  is one thing at a time.
- S_static uses each section's first and last frame (at 2% and 98%), the stronger control for animation.
- A local model cannot take an mp4: S_visual gets frames at FPS a second, 512 px wide, capped so the prompt fits the
  context (about 70 tokens a frame; Ollama silently truncates a prompt that does not fit).
- NVG is None when B_eff = 1 (everything right without the video), never 0.
- Counterfactual relabelling (the proposal's step 1.2) is not applied: it rewrites MMMC's TEST per video and breaks the
  paired design. S_blind measures what it would hide.
"""

from __future__ import annotations

import json
import math
import subprocess

from . import llm, teachquiz

K = 4
LETTERS = "ABCD"
CHANCE = 1 / K
LAMBDA = 0.5
MIN_ROOM = 0.05  # NVG needs at least this much room above the prior (see nvg)
FPS = 4
TOKENS_PER_FRAME = 70
CTX = 32768
MAX_FRAMES = (CTX - 4000) // TOKENS_PER_FRAME
ROTATIONS = (0, 1)
PASSES = ("frames", "static", "visual")

FORMAT = """Answer every question. Reply with exactly one line per question, in order, and nothing else:
1: <letter>
2: <letter>
...
Each <letter> is one of A, B, C, D."""
STRICT = "Write no explanation. If the material does not settle a question, still write your best letter for it."


def _frames(run_dir, kind):
    """Frames for one pass, cached per version of the video (as teachquiz does)."""
    if kind == "frames":
        return teachquiz.material(run_dir)[0]
    folder = teachquiz.frames_dir(run_dir) / f"dv_{kind}"
    if folder.exists() and any(folder.glob("*.jpg")):
        return sorted(folder.glob("*.jpg"))
    folder.mkdir(parents=True, exist_ok=True)
    video = run_dir / "video.mp4"
    sections = json.loads((run_dir / "sections.json").read_text())
    if kind == "static":
        for s in sections:
            for share in (0.02, 0.98):
                t = s["start"] + share * (s["end"] - s["start"])
                teachquiz.grab(video, t, folder / f"{s['id']}_{int(share * 100):02}.jpg")
    else:
        fps = min(FPS, MAX_FRAMES / max(sections[-1]["end"], 1))
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(video), "-an", "-vf",
                        f"fps={fps:.4f},scale=512:-2", "-q:v", "5", str(folder / "f%04d.jpg")], check=True)  # fmt: skip
    return sorted(folder.glob("*.jpg"))


def material(run_dir, kind):
    if kind == "blind":
        return [], "MATERIAL: none."
    images = _frames(run_dir, kind)
    if kind == "frames":
        return images, teachquiz.material(run_dir)[1]
    if kind == "static":
        return images, f"FRAMES: the first and last frame of each section, {len(images)} frames (start, end, ...)."
    end = json.loads((run_dir / "sections.json").read_text())[-1]["end"]
    return images, f"FRAMES: the silent video sampled evenly, {len(images)} frames in order over {teachquiz.stamp(end)}."


def rotate(q, r):
    """Shown letter L holds the text of original letter LETTERS[(i - r) % K]."""
    return {L: q["options"][LETTERS[(i - r) % K]] for i, L in enumerate(LETTERS)}


def _letter_probs(entry):
    lp = {L: -1e9 for L in LETTERS}
    for t in entry.get("top_logprobs") or []:
        tok = t["token"].strip()
        if tok in lp:
            lp[tok] = max(lp[tok], t["logprob"])
    top = max(lp.values())
    if top <= -1e8:
        return None
    ex = {L: math.exp(v - top) for L, v in lp.items()}
    z = sum(ex.values())
    return {L: v / z for L, v in ex.items()}


def parse(tokens, n):
    """Probabilities at each '<k>: <letter>' position of the reply; None for a question whose letter is missing.
    A small model sometimes drops the numbers and writes one bare letter per line: when no numbered letter is found
    and there are exactly n bare letters, they are read in order."""
    found, bare, text = {}, [], ""
    for entry in tokens:
        tok = entry["token"]
        k = None
        tail = text.rstrip(" ").splitlines()[-1] if text.strip() else ""
        if tok.strip() in LETTERS and tail.endswith(":"):
            head = tail[:-1].strip().lstrip("*").strip()
            k = int(head) if head.isdigit() else None
        if k is not None and 1 <= k <= n and k not in found:
            found[k] = _letter_probs(entry)
        if tok.strip() in LETTERS and (not text or text.endswith("\n")):
            bare.append(_letter_probs(entry))
        text += tok
    if not found and len(bare) == n:
        return bare, text
    return [found.get(i) for i in range(1, n + 1)], text


def probe(topic, questions, images, body, rotation, seed=0):
    shown = [{**q, "options": rotate(q, rotation)} for q in questions]
    listing = "\n\n".join(
        f"{i}. {q['question']}\n" + "\n".join(f"{L}) {q['options'][L]}" for L in LETTERS) for i, q in enumerate(shown, 1)
    )
    best = None
    for attempt in range(3):  # forced choice still refuses now and then (an explanation, no letters): ask again
        strict = "" if attempt == 0 else f"\n{STRICT}"
        reply = llm.ask_logprobs(
            llm.STUDENT,
            f"{body}\n\nQUESTIONS:\n{listing}\n\n{FORMAT}{strict}",
            images=images,
            system=teachquiz.forced(teachquiz.UNLEARN.format(topic=topic)),
            max_tokens=8 * len(questions) + 16,
            seed=seed + attempt,
        )
        probs, text = parse(reply["logprobs"], len(questions))
        missing = sum(x is None for x in probs)
        if best is None or missing < best[2]:
            best = (probs, text, missing, attempt, reply.get("prompt_tokens"))
        if not missing:
            break
    probs, text, missing, retries, tokens = best
    items = []
    for i, q in enumerate(questions):
        p = probs[i]
        if p is None:
            items.append({"id": q["id"], "p": None, "choice": None, "right": False, "p_right": None})
            continue
        back = {LETTERS[(j - rotation) % K]: p[L] for j, L in enumerate(LETTERS)}  # shown letter -> original
        choice = max(back, key=back.get)
        items.append({"id": q["id"], "p": {L: round(v, 6) for L, v in back.items()}, "choice": choice,
                      "right": choice == q["answer"], "p_right": round(back[q["answer"]], 6)})  # fmt: skip
    return {"rotation": rotation, "items": items, "reply": text[:400], "prompt_tokens": tokens, "retries": retries,
            "missing": missing}


def probes(material_dir, topic_dir, kind, split="test", cache_dir=None, tag=""):
    """Every rotation for one material, cached as dv_<tag><kind>_<split>.json in cache_dir (default: the material's)."""
    cache_dir = cache_dir or material_dir
    path = cache_dir / f"dv_{tag}{kind}_{split}.json"
    if path.exists():
        return json.loads(path.read_text())
    plan = json.loads((topic_dir / "plan.json").read_text())
    qs = json.loads((topic_dir / "quiz.json").read_text())[split]
    images, body = material(material_dir, kind)
    out = {"kind": kind, "frames": len(images), "rotations": [probe(plan["topic"], qs, images, body, r) for r in ROTATIONS]}
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    return out


def score(p, continuous=False, rotations=(0,), keep=None):
    """Mean over items (and the given rotations) of right (0/1) or P(right); a missing letter counts 0 / 0.25."""
    vals = []
    for r in rotations:
        for it in p["rotations"][r]["items"]:
            if keep is not None and it["id"] not in keep:
                continue
            if continuous:
                vals.append(CHANCE if it["p_right"] is None else it["p_right"])
            else:
                vals.append(1.0 if it["right"] else 0.0)
    return sum(vals) / len(vals) if vals else None


def nvg(s, s_blind):
    """Undefined when less than MIN_ROOM is left above the prior: with continuous scores a blind P(right) of 0.99999
    leaves 1e-5 of room, and dividing by it turns noise into gains of +-10 (seen on the pilot's controls)."""
    b = max(CHANCE, s_blind)
    return None if 1 - b < MIN_ROOM else (s - b) / (1 - b)


def dvgain(s_visual, s_static, s_blind):
    n = nvg(s_visual, s_blind)
    return None if n is None else n + LAMBDA * max(0.0, s_visual - s_static)
