"""One topic end to end: video, quiz, the base evaluation, and one round per feedback mode. Resumable: each step
writes its file and is skipped when that file exists."""

from __future__ import annotations

import json
from pathlib import Path

from . import feedback, generate, layout, teachquiz


def make_video(topic, grade, out, sections=4, log=print, source=None):
    if (out / "video.mp4").exists() and (out / "sections.json").exists():
        return out
    p = generate.plan(topic, grade, sections, out, source=source)
    clips = {}
    for s in p["sections"]:
        if generate.build_section(p, s, out, log):
            layout.repair(s["id"], out, log=log)
            mp4, _ = generate.render(out / "sections" / f"{s['id']}.py", s["id"].upper(), out / "media")
            if mp4:
                clips[s["id"]] = mp4
        log(f"[gen] {s['id']} {'ok' if s['id'] in clips else 'FAILED'}")
    if not clips:
        raise RuntimeError("no section rendered")
    generate.join(out, p, clips)
    return out


def evaluate(run_dir, split="test", other=None):
    path = run_dir / f"eval_{split}.json"
    if path.exists():
        return json.loads(path.read_text())
    result = teachquiz.evaluate(run_dir, split, other=other)
    result["mvqs"] = feedback.section_mvqs(run_dir)
    sections = json.loads((run_dir / "sections.json").read_text())
    result["sections_rendered"] = len(sections)
    path.write_text(json.dumps(result, indent=1, ensure_ascii=False))
    return result


def headline(e):
    keys = ("teachquiz", "teachquiz_clean", "none", "full", "evidence", "control_first_section",
            "control_other_topic", "mvqs", "sections_rendered")  # fmt: skip
    return {k: e.get(k) for k in keys}


def run_topic(topic, grade, out, modes=feedback.MODES, official=None, other=None, sections=4, log=print, source=None):
    """Everything for one topic; returns the row the benchmark tables are made from."""
    out = Path(out)
    make_video(topic, grade, out, sections, log, source=source)
    teachquiz.make_quiz(topic, grade, out, official=official, source=source)
    row = {"topic": topic, "base": headline(evaluate(out, "test", other))}
    for mode in modes:
        done = out / mode / "feedback.json"
        report = json.loads(done.read_text()) if done.exists() else feedback.round_(out, mode, log)
        if report.get("changed"):
            row[mode] = {**headline(evaluate(out / mode, "test", other)), "changed": report["changed"],
                         "kept_by_dev": report["kept"]}  # fmt: skip
        else:
            row[mode] = {**row["base"], "changed": [], "kept_by_dev": False}  # nothing changed: the base video
    row["diagnosis"] = json.loads((out / "diagnosis.json").read_text()) if (out / "diagnosis.json").exists() else None
    (out / "row.json").write_text(json.dumps(row, indent=1, ensure_ascii=False))
    return row
