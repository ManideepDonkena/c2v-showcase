"""The idea under test: repair a generated video where a simulated, unlearned student failed to learn.

  1. diagnose: the student answers the DEV quiz with the video (2 runs). A gap is a DEV question it never got right
     with a backed citation (wrong, NULL, or right while the evidence judge says the cited moment does not teach it).
     The planner maps each gap, one call per gap, to the section that should have taught it and names, in its own
     words, the missing idea. An idea that copies the question or an option (6 words in a row) is refused.
  2. revise: only the sections named are written again with their missing ideas, layout-checked and rendered. A
     section whose new version does not render keeps its old one (the incumbent is never lost).
  3. gate: the revision is marked kept when DEV TeachQuiz does not fall, MVQS falls by less than 5 points, and
     (while layout.CROWDING is on) the rewritten sections have no more layout faults than they had (layout.faults).
TEST is never shown to any step.

Modes (same diagnosis, so the same number of sections is rewritten where it applies):
  learner      the missing ideas, in the sections they belong to (ours)
  generic      as many sections, chosen at random, rewritten with "teach this more clearly" (no learner signal)
  learner_all  every section rewritten with all the missing ideas (learner signal, no localisation)
"""

from __future__ import annotations

import json
import random
import re
import shutil

from . import generate, layout, llm, teachquiz

MODES = ("learner", "generic", "learner_all")
GENERIC = "teach this section's point more clearly and completely"

MAP = """A video teaching "{topic}" has these sections:
{sections}

A student who watched it could not answer this question:
{question}

Which section should have taught what it needs, and what idea is missing from that section? Write the missing idea
in your own words as something to SHOW and SAY (an object, a number, a comparison), never by repeating the question
or its options. Return JSON: {{"section": "s1", "missing": "..."}}"""


def words(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def copies(a, b, n=6):
    wa, wb = words(a), words(b)
    grams = {tuple(wb[i : i + n]) for i in range(len(wb) - n + 1)}
    return any(tuple(wa[i : i + n]) in grams for i in range(len(wa) - n + 1))


def gaps(run_dir, quiz, runs=2):
    plan = json.loads((run_dir / "plan.json").read_text())
    images, body = teachquiz.material(run_dir)
    results = [
        teachquiz.evidence(run_dir, quiz["dev"], teachquiz.student(plan["topic"], plan["grade"], quiz["dev"], images, body, seed=r))
        for r in range(1, runs + 1)
    ]  # fmt: skip
    failed = [
        q
        for q in quiz["dev"]
        if not any(
            res["answers"][i]["backed"] for res in results for i, a in enumerate(res["answers"]) if a["id"] == q["id"]
        )
    ]
    return failed, results


def plan_fixes(plan, failed):
    """One call per gap: asked for a list, a small model copies the template's ids."""
    sections = "\n".join(
        f"{s['id']}: {s['title']} - teaches {s['teaches']}; shows {s['visual']}" for s in plan["sections"]
    )
    ids = {s["id"] for s in plan["sections"]}
    fixes = {}
    for q in failed:
        try:
            reply = llm.ask(
                llm.PLANNER,
                MAP.format(topic=plan["topic"], sections=sections, question=teachquiz.quiz_text([q]))
                + (generate.SOURCE.format(source=plan["source"]) if plan.get("source") else ""),
                note="map",
            )
        except RuntimeError:
            continue
        missing = str(reply.get("missing") or "").strip()
        if reply.get("section") not in ids or not missing:
            continue
        if copies(missing, q["question"] + " " + " ".join(q["options"].values())):
            continue  # teaches the item, not the idea
        fixes.setdefault(reply["section"], []).append(missing)
    return fixes


def revise(run_dir, new_dir, fixes, log=print):
    if new_dir.exists():
        shutil.rmtree(new_dir)
    # A copied score or probe cache would be read as this video's (dv_*.json included: c2vlab/stages.py already skips them).
    shutil.copytree(run_dir, new_dir, ignore=shutil.ignore_patterns("frames", "eval_*.json", "row.json", "dv_*.json",
                                                                    "stages", *MODES))  # fmt: skip
    plan = json.loads((new_dir / "plan.json").read_text())
    clips, changed = {}, []
    kept = new_dir / "kept"
    kept.mkdir(exist_ok=True)
    for s in plan["sections"]:
        sid, folder = s["id"], new_dir / "sections"
        old_mp4 = new_dir / "media" / "videos" / sid / "480p15" / f"{sid.upper()}.mp4"
        mp4 = None
        if sid in fixes:
            # the incumbent is never lost: keep the old code, layout record and clip until the new one renders
            backup = {f: f.read_bytes() for f in (folder / f"{sid}.py", folder / f"{sid}.layout.json") if f.exists()}
            if old_mp4.exists():
                shutil.copy(old_mp4, kept / f"{sid}.mp4")
            extra = "This section must ALSO show and say:\n" + "\n".join(f"- {m}" for m in fixes[sid])
            if generate.build_section(plan, s, new_dir, log, extra=extra):
                layout.repair(sid, new_dir, log=log)
                mp4, _ = generate.render(folder / f"{sid}.py", sid.upper(), new_dir / "media")
            if mp4:
                changed.append(sid)
            else:
                log(f"[feedback] {sid}: the new version did not render; the old one stays")
                for path, data in backup.items():
                    path.write_bytes(data)
                if (kept / f"{sid}.mp4").exists():
                    shutil.copy(kept / f"{sid}.mp4", old_mp4)
        if not mp4 and old_mp4.exists():
            mp4 = old_mp4
        if mp4:
            clips[sid] = mp4
    generate.join(new_dir, plan, clips)
    return changed


def section_mvqs(run_dir):
    scores = []
    for p in sorted((run_dir / "sections").glob("s*.layout.json")):
        s = (json.loads(p.read_text()).get("score") or {}).get("mvqs")
        if s is not None:
            scores.append(s)
    return round(sum(scores) / len(scores), 2) if scores else None


def layout_faults(run_dir, new_dir, changed):
    """Layout faults of the rewritten sections, before and after (None, None when the check is off)."""
    if not layout.CROWDING or not changed:
        return None, None
    return layout.fault_count(run_dir, changed), layout.fault_count(new_dir, changed)


def diagnose(run_dir, log=print):
    """Gaps and the fixes they ask for, worked out once per base video and shared by every mode."""
    path = run_dir / "diagnosis.json"
    if path.exists():
        return json.loads(path.read_text())
    quiz = json.loads((run_dir / "quiz.json").read_text())
    plan = json.loads((run_dir / "plan.json").read_text())
    failed, _ = gaps(run_dir, quiz)
    fixes = plan_fixes(plan, failed)
    record = {"gaps": [q["id"] for q in failed], "dev": len(quiz["dev"]), "fixes": fixes}
    path.write_text(json.dumps(record, indent=1, ensure_ascii=False))
    log(f"[feedback] {len(failed)} of {len(quiz['dev'])} DEV questions are gaps -> sections {sorted(fixes)}")
    return record


def round_(run_dir, mode="learner", log=print):
    assert mode in MODES
    plan = json.loads((run_dir / "plan.json").read_text())
    diag = diagnose(run_dir, log)
    fixes = diag["fixes"]
    if not fixes:
        return {"mode": mode, "kept": False, "changed": [], "reason": "no gaps"}
    ids = [s["id"] for s in plan["sections"]]
    if mode == "generic":
        chosen = random.Random(plan["topic"]).sample(ids, len(fixes))
        fixes = {sid: [GENERIC] for sid in chosen}
    elif mode == "learner_all":
        every = [m for ms in fixes.values() for m in ms]
        fixes = {sid: every for sid in ids}
    new_dir = run_dir / mode
    changed = revise(run_dir, new_dir, fixes, log)
    before = teachquiz.evaluate(run_dir, "dev", runs=2)
    after = teachquiz.evaluate(new_dir, "dev", runs=2)
    m0, m1 = section_mvqs(run_dir), section_mvqs(new_dir)
    f0, f1 = layout_faults(run_dir, new_dir, changed)
    kept = (bool(changed) and after["teachquiz"] >= before["teachquiz"] and (m0 is None or m1 is None or m1 > m0 - 5)
            and (f0 is None or f1 <= f0))  # fmt: skip
    report = {"mode": mode, "gaps": diag["gaps"], "fixes": fixes, "changed": changed,
              "dev_before": before["teachquiz"], "dev_after": after["teachquiz"], "mvqs_before": m0,
              "mvqs_after": m1, "faults_before": f0, "faults_after": f1, "kept": kept, "dir": str(new_dir)}  # fmt: skip
    (new_dir / "feedback.json").write_text(json.dumps(report, indent=1, ensure_ascii=False))
    return report
