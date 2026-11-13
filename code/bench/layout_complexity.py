"""How busy is each video, and do busier sections have more layout faults? Every version of every NOVEL-12 video is
measured again here with one tracker (c2vlab/scene_graph.py as it is now), so all versions are comparable.

Per section: the most objects on screen at once and the mean, lasting conflicts (overlaps that stay on screen),
broken attachments (labels pulled off their shapes), timing faults, and the layout score (MVQS). Then, over all
sections of all versions, the rank correlation between objects on screen and faults.

    python bench/layout_complexity.py   -> bench/results/layout-complexity/{rows.json, report.json, report.md},
                                           paper/layout_complexity_numbers.tex
"""

from __future__ import annotations

import json
import statistics as st
import sys
import tempfile
from pathlib import Path

from scipy.stats import spearmanr

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT), str(ROOT / "bench")]

from c2vlab import attach, generate, layout, mvqs, temporal  # noqa: E402

OUT = ROOT / "bench" / "results" / "layout-complexity"
VERSIONS = {  # name -> folder of the video, given the topic slug
    "local": lambda s: ROOT / "runs" / s,
    "local_claude_layout": lambda s: ROOT / "runs" / s / "claude_fixed",
    **{f: (lambda s, f=f: ROOT / "runs" / "claude-gen" / f / s)
       for f in ("qwen", "qwen-anchor", "haiku", "sonnet", "opus", "sonnet-anchor")},
}  # fmt: skip
TEXT = {"Text", "MathTex", "Tex", "MarkupText", "Paragraph", "Title", "DecimalNumber", "Integer"}


def section(path, sid):
    with tempfile.TemporaryDirectory() as tmp:
        g, score, _ = layout.measure(path, sid.upper(), Path(tmp) / "g.json")
    states = g.get("states") or []
    counts = [len(s["objects"]) for s in states] or [0]
    texts = [sum(o.get("type") in TEXT for o in s["objects"]) for s in states] or [0]
    code = path.read_text()
    return {"objects_max": max(counts), "objects_mean": round(st.mean(counts), 1), "text_max": max(texts),
            "lines": len(code.splitlines()), "anchor": "place_at_grid" in code or "place_in_area" in code,
            "conflicts": len(mvqs.persistent_conflicts(states)) if states else 0,
            "broken_attachments": len(attach.broken(code, g)), "timing": len(temporal.check(code)),
            "mvqs": score, "error": bool(g.get("error"))}  # fmt: skip


def main():
    topics = json.loads((ROOT / "bench" / "results" / "novel12" / "topics.json").read_text())
    rows = []
    for t in topics:
        slug = generate.slug(t)
        for name, where in VERSIONS.items():
            d = where(slug)
            if not (d / "video.mp4").exists() or not (d / "sections.json").exists():
                continue
            for s in json.loads((d / "sections.json").read_text()):
                p = d / "sections" / f"{s['id']}.py"
                if p.exists():
                    rows.append({"version": name, "topic": slug, "section": s["id"], **section(p, s["id"])})
        print(f"[complexity] {slug}: {sum(r['topic'] == slug for r in rows)} sections", flush=True)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "rows.json").write_text(json.dumps(rows, indent=1))
    ok = [r for r in rows if not r["error"]]
    rep = {"versions": {}}
    for name in VERSIONS:
        rs = [r for r in ok if r["version"] == name]
        if not rs:
            continue
        rep["versions"][name] = {
            "videos": len({r["topic"] for r in rs}), "sections": len(rs),
            "objects_max_mean": round(st.mean(r["objects_max"] for r in rs), 1),
            "text_max_mean": round(st.mean(r["text_max"] for r in rs), 1),
            "lines_mean": round(st.mean(r["lines"] for r in rs)),
            "conflicts": sum(r["conflicts"] for r in rs), "broken_attachments": sum(r["broken_attachments"] for r in rs),
            "timing": sum(r["timing"] for r in rs),
            "sections_with_fault": sum((r["conflicts"] + r["broken_attachments"]) > 0 for r in rs),
            "mvqs_mean": round(st.mean(r["mvqs"] for r in rs if r["mvqs"] is not None), 1),
            "anchor_sections": sum(r["anchor"] for r in rs)}  # fmt: skip
    faults = [r["conflicts"] + r["broken_attachments"] for r in ok]
    rho, p = spearmanr([r["objects_max"] for r in ok], faults)
    rho_l, p_l = spearmanr([r["lines"] for r in ok], faults)
    rep["objects_vs_faults"] = {"sections": len(ok), "spearman": round(float(rho), 2), "p": float(f"{p:.2g}"),
                                "lines_spearman": round(float(rho_l), 2), "lines_p": float(f"{p_l:.2g}")}  # fmt: skip
    import hashlib
    import subprocess

    sg = ROOT / "c2vlab" / "scene_graph.py"
    dirty = subprocess.run(["git", "diff", "--quiet", "--", str(sg)], cwd=ROOT).returncode != 0
    rep["tracker"] = {"file": "c2vlab/scene_graph.py", "sha256": hashlib.sha256(sg.read_bytes()).hexdigest()[:12],
                      "uncommitted_changes": dirty,
                      "note": "measured with the id()-reuse fix (uncommitted at the time)" if dirty else "committed version"}  # fmt: skip
    (OUT / "report.json").write_text(json.dumps(rep, indent=1))
    head = "| Version | Videos | Sections | Most objects on screen (mean) | Most text objects | Code lines | MVQS | Lasting conflicts | Broken attachments | Sections with a fault |"
    lines = ["# Layout complexity and faults, one tracker for every version", "",
             f"Tracker: c2vlab/scene_graph.py {rep['tracker']['sha256']} ({rep['tracker']['note']}).", "", head, "|---" * 10 + "|"]
    for name, v in rep["versions"].items():
        lines.append(f"| {name} | {v['videos']} | {v['sections']} | {v['objects_max_mean']} | {v['text_max_mean']} | "
                     f"{v['lines_mean']} | {v['mvqs_mean']} | {v['conflicts']} | {v['broken_attachments']} | "
                     f"{v['sections_with_fault']}/{v['sections']} |")  # fmt: skip
    o = rep["objects_vs_faults"]
    lines += ["", f"Over {o['sections']} sections: rank correlation between the most objects on screen and faults "
              f"(conflicts + broken attachments) {o['spearman']} (p {o['p']}); code lines and faults {o['lines_spearman']} (p {o['lines_p']})."]
    (OUT / "report.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    word = {"local": "Local", "local_claude_layout": "ClaudeLayout", "qwen": "Qwen", "qwen-anchor": "QwenAnchor",
            "haiku": "Haiku", "sonnet": "Sonnet", "opus": "Opus", "sonnet-anchor": "SonnetAnchor"}  # fmt: skip
    mac = ["% generated by bench/layout_complexity.py; do not edit"]
    for name, v in rep["versions"].items():
        w = word[name]
        mac += [rf"\newcommand{{\LC{w}Objects}}{{{v['objects_max_mean']}}}", rf"\newcommand{{\LC{w}Conflicts}}{{{v['conflicts']}}}",
                rf"\newcommand{{\LC{w}Attach}}{{{v['broken_attachments']}}}",
                rf"\newcommand{{\LC{w}Faulty}}{{{v['sections_with_fault']}/{v['sections']}}}",
                rf"\newcommand{{\LC{w}Lines}}{{{v['lines_mean']}}}", rf"\newcommand{{\LC{w}MVQS}}{{{v['mvqs_mean']}}}"]  # fmt: skip
    mac += [rf"\newcommand{{\LCRho}}{{{o['spearman']}}}", rf"\newcommand{{\LCRhoP}}{{{o['p']}}}",
            rf"\newcommand{{\LCSections}}{{{o['sections']}}}"]  # fmt: skip
    (ROOT / "paper" / "layout_complexity_numbers.tex").write_text("\n".join(mac) + "\n")


if __name__ == "__main__":
    main()
