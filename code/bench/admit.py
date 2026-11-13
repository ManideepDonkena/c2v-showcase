"""Admit the base videos of a benchmark before a study uses them (c2vlab/admission.py), then write one contact sheet
per video and an index page for a person to approve.

    python bench/admit.py                     # NOVEL-12: admit, then sheets in bench/admission/
    python bench/admit.py --sheets-only       # sheets and index only (no regeneration)

A video is admitted when it is complete (every planned section renders) and clean (every section MVQS >= 70 with no
lasting conflict) and a person approves its sheet. The sheet shows six frames of each section, so faults MVQS cannot
see (merged words, leftover glyphs, text off the edge) are visible.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import html
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from c2vlab import admission, generate

GRADE = "undergraduate students"
OUT = ROOT / "bench" / "admission"
FRAMES = 6


def sheet(run, out_png):
    """Six frames of each section, one row per section, labelled with its id and layout score."""
    from PIL import Image, ImageDraw

    secs = json.loads((run / "sections.json").read_text()) if (run / "sections.json").exists() else []
    plan = json.loads((run / "plan.json").read_text())
    rec = json.loads((run / "admission.json").read_text()) if (run / "admission.json").exists() else {}
    after = rec.get("after") or {}
    w, h, label = 320, 180, 150
    rows = plan["sections"]
    img = Image.new("RGB", (label + FRAMES * w, len(rows) * h), "white")
    draw = ImageDraw.Draw(img)
    by_id = {s["id"]: s for s in secs}
    with tempfile.TemporaryDirectory() as tmp:
        for r, sec in enumerate(rows):
            st = after.get(sec["id"]) or admission.section_status(run, sec["id"])
            text = f"{sec['id']}\nMVQS {st['mvqs'] if st['mvqs'] is not None else '--'}\nconflicts {st['conflicts']}"
            text += "\nOK" if st["ok"] else ("\nNOT RENDERED" if not st["rendered"] else "\nfails layout")
            draw.multiline_text((8, r * h + 8), text, fill="black" if st["ok"] else "red")
            s = by_id.get(sec["id"])
            if not s:
                continue
            a, b = s["start"] + 0.3, s["end"] - 0.2
            for i in range(FRAMES):
                t = a + (b - a) * (i + 0.5) / FRAMES
                png = Path(tmp) / f"{r}_{i}.png"
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", str(run / "video.mp4"),
                                "-frames:v", "1", "-vf", f"scale={w}:{h}", str(png)], check=False)  # fmt: skip
                if png.exists():
                    img.paste(Image.open(png), (label + i * w, r * h))
    img.save(out_png)


def index(rows):
    style = ("<style>body{font-family:sans-serif;margin:16px;background:#fff}img{max-width:100%;border:1px solid #ccc}"
             ".bad{color:#b00}.ok{color:#070}</style><h1>Base videos: admission sheets</h1>")
    note = ("<p>Each row is one section: six frames, its layout score (MVQS) and lasting conflicts. Approve a video "
            "only if no frame shows overlapping or unreadable text, or content off the edge.</p>")
    parts = ["<!doctype html><meta charset='utf-8'><title>Admission sheets</title>", style, note]
    for t, rec, png in rows:
        status = ("complete" if rec.get("complete") else "INCOMPLETE") + ", " + ("clean" if rec.get("clean") else "layout issues")
        cls = "ok" if rec.get("complete") and rec.get("clean") else "bad"
        regen = ", ".join(rec.get("regenerated") or {}) or "none"
        parts.append(f"<h2>{html.escape(t)}</h2><p class='{cls}'>{status}; regenerated: {regen}</p>"
                     f"<img src='{png.name}' alt='{html.escape(t)}'>")  # fmt: skip
    (OUT / "index.html").write_text("\n".join(parts))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--questions", default=str(ROOT / "bench" / "novel" / "questions.json"))
    ap.add_argument("--cards", default=str(ROOT / "bench" / "novel" / "cards.json"))
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--sheets-only", action="store_true")
    a = ap.parse_args()
    topics = list(json.loads(Path(a.questions).read_text()))
    cards = json.loads(Path(a.cards).read_text()) if a.cards else {}
    OUT.mkdir(parents=True, exist_ok=True)
    generate.FEATURES.update({"preflight", "safe_patch"})  # the code check, for regenerated sections only
    runs = {t: ROOT / "runs" / generate.slug(t) for t in topics}
    if not a.sheets_only:

        def one(t):
            log = lambda m: print(f"[{generate.slug(t)[:22]}] {m}", flush=True)
            return admission.admit(t, runs[t], GRADE, source=cards.get(t), log=log)

        with cf.ThreadPoolExecutor(a.workers) as pool:
            for t, rec in zip(topics, pool.map(one, topics), strict=True):
                print(f"[admit] {t}: complete {rec['complete']}, clean {rec['clean']}, regenerated "
                      f"{list(rec['regenerated'])}", flush=True)  # fmt: skip
    rows = []
    for t in topics:
        png = OUT / f"{generate.slug(t)}.png"
        sheet(runs[t], png)
        rec = json.loads((runs[t] / "admission.json").read_text()) if (runs[t] / "admission.json").exists() else {}
        rows.append((t, rec, png))
    index(rows)
    print(f"sheets: {OUT / 'index.html'}")


if __name__ == "__main__":
    main()
