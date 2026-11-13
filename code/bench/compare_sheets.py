"""One review page for the layout side study: for every concept and section, four frames of each version side by side
(ours, ours + timing fixes, Claude-fixed), with the faults Claude reports fixing.

    python bench/compare_sheets.py     -> bench/admission/compare/index.html
"""

from __future__ import annotations

import html
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from c2vlab import generate

OUT = ROOT / "bench" / "admission" / "compare"
VERSIONS = (("ours", ""), ("ours + timing fixes", "autofix"), ("Claude-fixed", "claude_fixed"))
N, W, H = 4, 320, 180


def strip(vdir, sec_id, png):
    """Four frames of one section of one version, side by side; False when the section is not in the video."""
    from PIL import Image

    secs = {s["id"]: s for s in json.loads((vdir / "sections.json").read_text())} if (vdir / "sections.json").exists() else {}
    if sec_id not in secs:
        return False
    s = secs[sec_id]
    img = Image.new("RGB", (N * W, H), "black")
    with tempfile.TemporaryDirectory() as tmp:
        for i in range(N):
            t = s["start"] + 0.3 + (s["end"] - s["start"] - 0.5) * (i + 0.5) / N
            f = Path(tmp) / f"{i}.png"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", str(vdir / "video.mp4"), "-frames:v", "1",
                            "-vf", f"scale={W}:{H}", str(f)], check=False)  # fmt: skip
            if f.exists():
                img.paste(Image.open(f), (i * W, 0))
    img.save(png)
    return True


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    topics = list(json.loads((ROOT / "bench" / "novel" / "questions.json").read_text()))
    style = ("<style>body{font-family:sans-serif;margin:16px;background:#fff;color:#222}table{border-collapse:collapse;"
             "width:100%}td,th{border:1px solid #ddd;padding:4px;vertical-align:top}img{width:100%}th{background:#f4f4f4}"
             "ul{margin:4px 0 0 16px;font-size:13px}</style>")
    note = ("<p>Four frames per section and version. Claude may change only layout and timing; every on-screen string is "
            "checked to be identical. Approve the study set only if the left column has no fault that makes a question "
            "unanswerable.</p>")
    parts = ["<!doctype html><meta charset='utf-8'><title>Layout side study</title>", style,
             "<h1>Layout side study: ours, ours + timing fixes, Claude-fixed</h1>", note]
    for t in topics:
        run = ROOT / "runs" / generate.slug(t)
        adm = json.loads((run / "admission.json").read_text()) if (run / "admission.json").exists() else {}
        fixes = {}
        if (run / "claude_fixed" / "fixes.json").exists():
            fixes = {s["id"]: s for s in json.loads((run / "claude_fixed" / "fixes.json").read_text())["sections"]}
        plan = json.loads((run / "plan.json").read_text())
        status = "complete" if adm.get("complete") else "INCOMPLETE (excluded)"
        parts.append(f"<h2>{html.escape(t)}</h2><p>admission: {status}, {'clean' if adm.get('clean') else 'layout below the bar'}</p>")
        parts.append("<table><tr><th>section</th>" + "".join(f"<th>{v}</th>" for v, _ in VERSIONS) + "</tr>")
        for sec in plan["sections"]:
            sid = sec["id"]
            row = f"<tr><td>{sid}<br><small>{html.escape(sec['title'])}</small>"
            fx = fixes.get(sid)
            if fx:
                row += (f"<br><small>MVQS {fx['before']['mvqs']} &rarr; {fx['after']['mvqs']}</small><ul>"
                        + "".join(f"<li><b>{html.escape(i['kind'])}</b>: {html.escape(i['change'])}</li>" for i in fx["issues"])
                        + "</ul>")  # fmt: skip
            row += "</td>"
            for v, sub in VERSIONS:
                vdir = run / sub if sub else run
                png = OUT / f"{generate.slug(t)}_{sub or 'ours'}_{sid}.png"
                row += f"<td><img src='{png.name}'></td>" if strip(vdir, sid, png) else "<td><i>not in video</i></td>"
            parts.append(row + "</tr>")
        parts.append("</table>")
    (OUT / "index.html").write_text("\n".join(parts))
    print(OUT / "index.html")


if __name__ == "__main__":
    main()
