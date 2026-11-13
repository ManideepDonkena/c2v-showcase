"""Claude-fixed reference videos: a strong model repairs layout and timing only, so the study can tell "the video
is messy" apart from "the measure cannot see it". Kept beside our videos, never inside the F0-F5 comparison.

    python bench/claude_fix.py                      # every NOVEL-12 base video -> runs/<topic>/claude_fixed/
    python bench/claude_fix.py --topics "Tovan sums" --sections s1

Guards, so a gain can only come from layout and timing:
  - the fixer sees one section's code, six of its rendered frames, and the automatic layout (SGA) and timing
    (c2vlab/temporal.py) reports; never the plan, the definition card, or any quiz;
  - every on-screen string (Text, MathTex, Tex, ...) must be identical before and after, checked in code; a fix that
    changes one is refused;
  - a fix that does not render or fails the check gets one more request with the error; after that the original
    section is kept.
Every request and its result is logged in runs/<topic>/claude_fixed/fixes.json (model, tokens, issues, MVQS before
and after, timing faults before and after).
"""

from __future__ import annotations

import argparse
import ast
import collections
import concurrent.futures as cf
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from c2vlab import generate, layout, mvqs, temporal

CLAUDE_PY = ROOT / ".venv-claude" / "bin" / "python"
ENV_FILE = Path("/home/mani/manim/lessonforge/.env")
TEXTY = {"Text", "MathTex", "Tex", "MarkupText", "Paragraph", "Title", "BulletedList", "Code", "SingleStringMathTex"}
FRAMES = 6
KINDS = ["overlap", "off_screen", "leftover", "unreadable_text", "wrong_timing", "crowded", "other"]

SYSTEM = """You fix layout and timing faults in one Manim Community (v0.19) scene from an educational video.
You see the scene's Python code, six frames of the rendered scene in order, and automatic reports of overlapping or
off-screen objects and of timing faults.

Rules:
1. Do not change any text shown on screen. Every string given to Text, MathTex, Tex, MarkupText, Paragraph, Title or
   BulletedList must stay exactly the same, with the same number of parts.
2. Do not add or remove teaching content: no new objects that carry information, no removed objects, and keep the
   order of the animations.
3. You may change positions, shifts, scales, font sizes, buff, arrangement, z-order, run_time and wait times, and the
   lifecycle of objects: use ReplacementTransform when a Transform target is used later, fade out an object that would
   otherwise stay under new content, and remove leftover copies.
4. Keep the class name and the imports; the file must run with `from manim import *`.

Return the complete corrected file and the list of faults you fixed. If nothing needs fixing, return the file
unchanged and an empty list."""

SCHEMA = {
    "type": "object",
    "properties": {
        "issues": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "kind": {"type": "string", "enum": KINDS},
                    "where": {"type": "string"},
                    "change": {"type": "string"},
                },
                "required": ["kind", "where", "change"],
                "additionalProperties": False,
            },
        },
        "code": {"type": "string"},
    },
    "required": ["issues", "code"],
    "additionalProperties": False,
}


def api_env():
    """The environment for the Claude subprocess, with the key read from the .env file (never printed)."""
    env = dict(os.environ)
    if "ANTHROPIC_API_KEY" not in env and ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            if line.startswith("ANTHROPIC_API_KEY="):
                env["ANTHROPIC_API_KEY"] = line.split("=", 1)[1].strip().strip('"').strip("'")
    return env


def ask_claude(text, images):
    req = {"system": SYSTEM, "text": text, "images": [str(p) for p in images], "schema": SCHEMA, "effort": "high"}
    r = subprocess.run([str(CLAUDE_PY), str(ROOT / "bench" / "claude_call.py")], input=json.dumps(req),
                       capture_output=True, text=True, env=api_env(), timeout=1800, check=False)  # fmt: skip
    if r.returncode:
        raise RuntimeError(f"claude_call failed: {r.stderr[-600:]}")
    out = json.loads(r.stdout)
    out["parsed"] = json.loads(out["text"]) if out.get("text") else None
    return out


def on_screen_text(code):
    """Every string literal given to a text-making call, as a multiset (the fixer must not change any)."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return None
    out = collections.Counter()
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in TEXTY:
            for a in [*n.args, *[k.value for k in n.keywords if k.arg in ("text", "tex_strings")]]:
                if isinstance(a, ast.Constant) and isinstance(a.value, str):
                    out[(n.func.id, a.value)] += 1
    return out


def section_frames(run, sec, tmp):
    paths = []
    a, b = sec["start"] + 0.3, sec["end"] - 0.2
    for i in range(FRAMES):
        t = a + (b - a) * (i + 0.5) / FRAMES
        png = Path(tmp) / f"{sec['id']}_{i}.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", str(run / "video.mp4"), "-frames:v", "1",
                        "-vf", "scale=640:360", str(png)], check=False)  # fmt: skip
        if png.exists():
            paths.append(png)
    return paths


def reports(path, cls, gpath):
    """MVQS, lasting conflicts (described) and timing faults of a section's current code."""
    g, score, _ = layout.measure(path, cls, gpath)
    found = mvqs.persistent_conflicts(g["states"]) if g.get("states") else []
    return {"mvqs": round(score, 1) if score is not None else None, "conflicts": [layout.describe(c) for c in found],
            "timing": [f["message"] for f in temporal.check(path.read_text())]}  # fmt: skip


def fix_section(run, out, sec, log):
    sid, cls = sec["id"], sec["id"].upper()
    path = out / "sections" / f"{sid}.py"
    gpath = out / "sections" / f"{sid}.graph.json"
    code0 = path.read_text()
    before = reports(path, cls, gpath)
    rec = {"id": sid, "before": {"mvqs": before["mvqs"], "conflicts": len(before["conflicts"]),
                                 "timing": len(before["timing"])}, "requests": []}  # fmt: skip
    with tempfile.TemporaryDirectory() as tmp:
        images = section_frames(run, sec, tmp)
        text = (f"SCENE CODE (class {cls}):\n```python\n{code0}\n```\n\nLAYOUT REPORT (SGA, objects at rest):\n"
                + ("\n".join(f"- {c}" for c in before["conflicts"]) or "- no lasting conflict found")
                + "\n\nTIMING REPORT:\n" + ("\n".join(f"- {t}" for t in before["timing"]) or "- no timing fault found")
                + "\n\nThe six images are frames of this scene in order. Look for faults the reports miss too: "
                  "overlapping or unreadable text, objects off the edge, leftovers that stay on screen.")  # fmt: skip
        for attempt in range(2):
            r = ask_claude(text, images)
            rec["requests"].append({"model": r["model"], "usage": r["usage"], "stop_reason": r["stop_reason"],
                                    "request_id": r["request_id"]})  # fmt: skip
            p = r.get("parsed") or {}
            new = p.get("code") or ""
            problem = None
            if r["stop_reason"] == "refusal" or not new:
                problem = f"no code returned (stop reason {r['stop_reason']})"
            elif on_screen_text(new) is None:
                problem = "the file does not parse"
            elif on_screen_text(new) != on_screen_text(code0):
                changed = (on_screen_text(code0) - on_screen_text(new)) + (on_screen_text(new) - on_screen_text(code0))
                problem = f"on-screen text changed, which is not allowed: {list(changed)[:4]}"
            else:
                path.write_text(new)
                mp4, err = generate.render(path, cls, out / "media")
                if not mp4:
                    problem = f"the scene does not render: {err[-800:]}"
            if problem is None:
                after = reports(path, cls, gpath)
                rec.update(issues=p.get("issues") or [], kept=True, attempt=attempt,
                           after={"mvqs": after["mvqs"], "conflicts": len(after["conflicts"]), "timing": len(after["timing"])})  # fmt: skip
                log(f"[claude] {sid}: kept; MVQS {before['mvqs']} -> {after['mvqs']}, "
                    f"{len(rec['issues'])} issues fixed")  # fmt: skip
                return rec
            log(f"[claude] {sid}: attempt {attempt} refused: {problem[:120]}")
            path.write_text(code0)
            text += (f"\n\nYOUR PREVIOUS ANSWER WAS REJECTED: {problem}\nReturn the complete file again, "
                     "fixing that, and still follow every rule.")  # fmt: skip
    reports(path, cls, gpath)
    rec.update(issues=[], kept=False, after=rec["before"])
    return rec


def fix_topic(topic, log):
    run = ROOT / "runs" / generate.slug(topic)
    out = run / "claude_fixed"
    if (out / "fixes.json").exists():
        return json.loads((out / "fixes.json").read_text())
    (out / "sections").mkdir(parents=True, exist_ok=True)
    plan = json.loads((run / "plan.json").read_text())
    secs = json.loads((run / "sections.json").read_text())
    for s in secs:
        shutil.copy(run / "sections" / f"{s['id']}.py", out / "sections" / f"{s['id']}.py")
    records = [fix_section(run, out, s, log) for s in secs]
    clips = {}
    for s in secs:
        mp4, _ = generate.render(out / "sections" / f"{s['id']}.py", s["id"].upper(), out / "media")
        if mp4:
            clips[s["id"]] = mp4
    generate.join(out, plan, clips)
    result = {"topic": topic, "sections": records,
              "input_tokens": sum(q["usage"]["input_tokens"] for r in records for q in r["requests"]),
              "output_tokens": sum(q["usage"]["output_tokens"] for r in records for q in r["requests"])}  # fmt: skip
    (out / "fixes.json").write_text(json.dumps(result, indent=1, ensure_ascii=False))
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--questions", default=str(ROOT / "bench" / "novel" / "questions.json"))
    ap.add_argument("--topics", nargs="*")
    ap.add_argument("--workers", type=int, default=3)
    a = ap.parse_args()
    topics = a.topics or list(json.loads(Path(a.questions).read_text()))

    def one(t):
        return fix_topic(t, lambda m: print(f"[{generate.slug(t)[:22]}] {m}", flush=True))

    with cf.ThreadPoolExecutor(a.workers) as pool:
        for t, res in zip(topics, pool.map(one, topics), strict=True):
            kept = sum(r["kept"] for r in res["sections"])
            print(f"[claude] {t}: {kept}/{len(res['sections'])} sections fixed, tokens in {res['input_tokens']} "
                  f"out {res['output_tokens']}", flush=True)  # fmt: skip


if __name__ == "__main__":
    main()
