"""Admission check: a base video enters a study only if it is complete and clean.

    1. every planned section renders (a section that still fails after its repairs is no longer silently dropped);
    2. every section's layout passes SGA: MVQS >= MIN_MVQS and no conflict a viewer sees at rest, and (while
       layout.CROWDING is on) no crowding fault: two texts nearer than 0.15 units, or a text wider than the frame;
    3. a person approves its contact sheet (bench/admit.py writes one per video), because MVQS reads object positions
       from the code and cannot see some faults on screen (text typeset as maths that loses its spaces, leftover
       glyphs of a transform, captions pushed off the edge).

A failing section is written again from scratch with a new seed, TRIES times (once), with the code check on and
explicit layout rules; the better attempt is kept. The caller turns the code check on (generate.FEATURES) for the
whole run, since topics are admitted in parallel threads. Nothing is deleted: replaced files and everything measured on the
old video move to <run>/_superseded/.
"""

from __future__ import annotations

import json
import shutil
import time

from . import generate, layout, mvqs

MIN_MVQS = 70.0
TRIES = 1  # one new attempt per failing section; what still fails is reported as a limit of the models
RULES = """LAYOUT RULES (an earlier version of this section failed a layout check):
- Keep every object inside the frame (x between -6.5 and 6.5, y between -3.6 and 3.6).
- Never place text on top of a shape or other text: use .next_to(obj, DIRECTION, buff=0.3), VGroup(...).arrange(...),
  and remove (FadeOut) old objects before adding new ones in the same place.
- Use Text(...) for words and sentences; use MathTex only for formulas (MathTex drops the spaces between words).
- At most about six objects on screen at once; scale groups down rather than letting them overlap.
- No line of text wider than 12 units: break a long sentence into lines with \n. Keep at least 0.25 units between
  any two texts.
- The title stays at the top edge; nothing else goes within 0.8 units of it."""
DOWNSTREAM = ("video.mp4", "sections.json", "clips.txt", "frames", "eval_dev.json", "eval_test.json",
              "eval_test.tq2.json", "diagnosis.json", "row.json", "qmatrix.json", "learner", "generic", "learner_all",
              "stages")  # fmt: skip


def section_status(out, sid):
    """Rendered, MVQS and lasting conflicts of one section, from the files on disk."""
    rendered = (out / "sections.json").exists() and sid in [
        s["id"] for s in json.loads((out / "sections.json").read_text())
    ]
    lp, gp = out / "sections" / f"{sid}.layout.json", out / "sections" / f"{sid}.graph.json"
    score = (json.loads(lp.read_text()).get("score") or {}) if lp.exists() else {}
    states = (json.loads(gp.read_text()).get("states") or []) if gp.exists() else []
    conflicts = len(mvqs.persistent_conflicts(states)) if states else None
    crowding = _crowding(states)
    m = score.get("mvqs")
    ok = bool(rendered and m is not None and m >= MIN_MVQS and conflicts == 0 and crowding == 0)
    return {"id": sid, "rendered": rendered, "mvqs": m, "conflicts": conflicts, "crowding": crowding, "ok": ok}


def _crowding(states):
    """Crowding faults that are not already lasting conflicts; 0 when the check is off, None with no graph."""
    if not layout.CROWDING:
        return 0
    return len(layout.faults(states)) - len(mvqs.persistent_conflicts(states)) if states else None


def _rank(st):
    faults = 99 if st["conflicts"] is None else st["conflicts"] + (st.get("crowding") or 0)
    return (st["rendered"], st["ok"], -faults, st["mvqs"] or 0)


def _files(out, sid):
    return sorted((out / "sections").glob(f"{sid}.*"))


def _stash(out, sid, dest):
    dest.mkdir(parents=True, exist_ok=True)
    for f in _files(out, sid):
        if f.is_file():
            shutil.copy(f, dest / f.name)


def _restore(out, sid, src):
    for f in _files(out, sid):
        f.unlink()
    for f in src.glob(f"{sid}.*"):
        shutil.copy(f, out / "sections" / f.name)


def admit(topic, out, grade, source=None, log=print):
    """Check one base video; regenerate failing sections; rebuild the video. Returns the admission record."""
    p = generate.plan(topic, grade, 4, out, source=source)
    ids = [s["id"] for s in p["sections"]]
    before = {sid: section_status(out, sid) for sid in ids}
    record = {"topic": topic, "before": before, "regenerated": {}, "min_mvqs": MIN_MVQS}
    failing = [sid for sid in ids if not before[sid]["ok"]]
    if failing:
        attic = out / "_superseded" / time.strftime("%Y%m%d-%H%M%S")
        attic.mkdir(parents=True, exist_ok=True)
        for name in DOWNSTREAM:  # everything measured on the old video
            if (out / name).exists():
                shutil.move(str(out / name), str(attic / name))
        for f in out.glob("dv_*.json"):  # D-VGAIN probes of the old video (the no-video probe does not depend on it)
            if not f.name.startswith("dv_blind") and "_blind_" not in f.name:
                shutil.move(str(f), str(attic / f.name))
        for sid in failing:  # generate.FEATURES is set by the caller for the whole run
            sec = next(s for s in p["sections"] if s["id"] == sid)
            best, best_dir = dict(before[sid]), attic / f"{sid}_try0"
            _stash(out, sid, best_dir)
            tries = []
            for k in range(1, TRIES + 1):
                for f in _files(out, sid):
                    f.unlink()
                mp4 = generate.build_section(p, sec, out, log, extra=RULES, seed=100 + k)
                if mp4:
                    layout.repair(sid, out, rounds=5, log=log)
                st = {**section_status_files(out, sid), "rendered": bool(mp4)}
                st["ok"] = bool(mp4 and st["mvqs"] is not None and st["mvqs"] >= MIN_MVQS and st["conflicts"] == 0
                                and st["crowding"] == 0)  # fmt: skip
                tries.append(st)
                log(f"[admit] {sid} try {k}: rendered {st['rendered']}, MVQS {st['mvqs']}, conflicts {st['conflicts']}, "
                    f"crowding {st['crowding']}")  # fmt: skip
                _stash(out, sid, attic / f"{sid}_try{k}")
                if _rank(st) > _rank(best):
                    best, best_dir = st, attic / f"{sid}_try{k}"
                if st["ok"]:
                    break
            _restore(out, sid, best_dir)
            record["regenerated"][sid] = {"tries": tries, "kept": best_dir.name}
        clips = {}
        for s in p["sections"]:  # the video again, from the kept code of every section
            path = out / "sections" / f"{s['id']}.py"
            if path.exists():
                mp4, _ = generate.render(path, s["id"].upper(), out / "media")
                if mp4:
                    clips[s["id"]] = mp4
        if clips:
            generate.join(out, p, clips)
        record["superseded"] = str(attic)
    after = {sid: section_status(out, sid) for sid in ids}
    record["after"] = after
    record["complete"] = all(a["rendered"] for a in after.values())
    record["clean"] = all(a["ok"] for a in after.values())
    (out / "admission.json").write_text(json.dumps(record, indent=1, ensure_ascii=False))
    return record


def section_status_files(out, sid):
    """MVQS and lasting conflicts of a section's current code (before the video is joined again)."""
    lp, gp = out / "sections" / f"{sid}.layout.json", out / "sections" / f"{sid}.graph.json"
    score = (json.loads(lp.read_text()).get("score") or {}) if lp.exists() else {}
    states = (json.loads(gp.read_text()).get("states") or []) if gp.exists() else []
    return {
        "id": sid,
        "mvqs": score.get("mvqs"),
        "conflicts": len(mvqs.persistent_conflicts(states)) if states else None,
        "crowding": _crowding(states),
    }
