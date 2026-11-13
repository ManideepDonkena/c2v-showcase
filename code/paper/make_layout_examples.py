"""Figure: real frames, ours vs Claude-fixed, for three sections of the layout study.

Each row is one frame the student was shown (3 frames per section, at 40, 70 and 95% of the section), from our admitted
video (left) and the Claude-fixed video (right), with that section's layout numbers and the concept's M9 for both
versions. The numbers are read from the result files, not typed:
    bench/results/layout-sections/rows.json   MVQS, lasting conflicts, broken attachments per section
    bench/results/layout-study/rows.json      M9 per concept and version (gemma4:26b)

    python paper/make_layout_examples.py   -> paper/figures/layout_examples.pdf
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from c2vlab import teachquiz  # noqa: E402

OUT = ROOT / "paper" / "figures" / "layout_examples.pdf"
# (run folder, section, frame share, what the fix did) - chosen by looking at the frames; see the caption in results.tex
EXAMPLES = [
    ("dapple-numbers", "s2", 95, "The number line ran off screen; Claude rescaled it so 10 to 90 are all shown"),
    ("glint-numbers", "s4", 70, "A shift had left the highlight boxes beside the digits; Claude put them on the digits"),
    ("mirthful-triangles", "s3", 95, "Labels piled on a tiny triangle at the edge; Claude moved and separated them"),
]
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def numbers():
    secs = {(r["topic"], r["version"], r["section"]): r
            for r in json.loads((ROOT / "bench/results/layout-sections/rows.json").read_text())}  # fmt: skip
    study = {r["topic"]: r for r in json.loads((ROOT / "bench/results/layout-study/rows.json").read_text())}
    return secs, study


def label(sec, m9):
    att = f", {sec['attach']} broken attachment{'s' * (sec['attach'] != 1)}" if sec["attach"] else ""
    return (f"MVQS {sec['mvqs']:.1f}, {sec['conflicts']} lasting conflict{'s' * (sec['conflicts'] != 1)}{att}"
            f"   |   M9 {100 * m9:+.1f}")  # fmt: skip


def main():
    secs, study = numbers()
    w, h, gap, head, sub = 768, 432, 16, 64, 34
    big, small = font(BOLD, 24), font(FONT, 20)
    rows = len(EXAMPLES)
    canvas = Image.new("RGB", (2 * w + gap, 46 + rows * (head + h + sub + gap)), "white")
    draw = ImageDraw.Draw(canvas)
    for i, title in enumerate(("Ours (admitted)", "Claude-fixed")):
        draw.text((i * (w + gap) + w // 2, 10), title, fill="black", font=big, anchor="mt")
    y = 46
    for slug, s, share, what in EXAMPLES:
        topic = next(t for t, r in study.items() if (ROOT / "runs" / slug / "plan.json").exists()
                     and json.loads((ROOT / "runs" / slug / "plan.json").read_text())["topic"] == t)  # fmt: skip
        draw.text((0, y + 6), f"{topic}, section {s[1]}: {what}", fill="black", font=small)
        for i, (version, sub_dir) in enumerate((("ours", ""), ("claude", "claude_fixed"))):
            d = ROOT / "runs" / slug / sub_dir if sub_dir else ROOT / "runs" / slug
            frame = Image.open(teachquiz.frames_dir(d) / f"{s}_{share}.jpg").convert("RGB").resize((w, h))
            x = i * (w + gap)
            canvas.paste(frame, (x, y + head - 22))
            m9 = study[topic][version]["teaching"]["M9"]
            draw.text((x, y + head - 22 + h + 6), label(secs[(topic, version, s)], m9), fill="black", font=small)
        y += head + h + sub + gap
    OUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUT, "PDF", resolution=200.0)
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
