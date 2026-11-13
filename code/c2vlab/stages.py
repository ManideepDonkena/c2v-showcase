"""The feedback loop with the pipeline features added one at a time (F0 is `feedback.round_`, the pilot's loop).

    F1  + gate enforced: a revision that fails the gate is not served; TEST sees the base video
    F2  + code reliability: static pre-flight before every render, splices that must parse, extra hints, last repair
          rendered (c2vlab/preflight.py; generate.FEATURES), and automatic timing fixes: a Transform whose target
          is used later becomes ReplacementTransform, prose typeset as maths keeps its spaces (c2vlab/temporal.py)
    F3  + spectrum-based localisation: DEV scored by forced-choice P(right) on the video (c2vlab/dvgain.probe);
          every DEV item, passing or failing, mapped to a section (a Q-matrix); sections ranked by Ochiai
          suspiciousness ef / sqrt(F * (ef + ep)); only the top k (1 for <= 3 sections, else 2) are repaired. The gate
          reads the same DEV score.
    F4  + leak gate and abstraction: an idea that repeats a number of the DEV item (absent from the plan and the card)
          or one of its options is refused, and the ideas of one section are merged into one general principle
    F5  + minimal edits: the working scene is edited (as little as possible), not written again; the edit size is kept

Each stage is cumulative and writes its revisions to runs/<topic>/stages/<F>/<mode>/; the base video is shared.
"""

from __future__ import annotations

import difflib
import json
import math
import random
import re
import shutil

from . import dvgain, feedback, generate, layout, llm, teachquiz

STAGES = ("F0", "F1", "F2", "F3", "F4", "F5")
FEATURES = {
    "F0": set(), "F1": {"gate"}, "F2": {"gate", "preflight", "safe_patch"},
    "F3": {"gate", "preflight", "safe_patch", "sbfl"}, "F4": {"gate", "preflight", "safe_patch", "sbfl", "leak_gate"},
    "F5": {"gate", "preflight", "safe_patch", "sbfl", "leak_gate", "minimal_edit"},
}  # fmt: skip
PASS = 0.5  # a DEV item passes when the student puts at least this probability on the right letter

QMAP = """A video teaching "{topic}" has these sections:
{sections}

Which ONE section should teach what is needed to answer this question?
{question}
Return JSON: {{"section": "s1"}}"""

MISSING = """A video teaching "{topic}" has these sections:
{sections}

A student who watched it could not answer this question, and section {sid} is the one that should have taught it:
{question}

What idea is missing from section {sid}? Write it in your own words as something to SHOW and SAY (an object, a
number, a comparison), never by repeating the question or its options. Return JSON: {{"missing": "..."}}"""

MERGE = """Section {sid} of a video teaching "{topic}" teaches: {teaches}
Students missed these ideas in it:
{ideas}

Merge them into ONE general principle that section {sid} should also show and say: a rule, a non-example, or a
worked example with NEW numbers. Do not use any of these numbers: {banned}. Return JSON: {{"principle": "..."}}"""

EDIT = """This Manim scene works. Change it AS LITTLE AS POSSIBLE so that it ALSO shows and says what is listed below.
Keep every existing object, position and animation; add the new part where it fits (FadeOut what it would cover), with
at most 10 extra seconds. Same class name {cls}, `from manim import *` only.

ADD:
{add}

Code:
{code}

Return only the Python code."""


def _sections(plan):
    return "\n".join(f"{s['id']}: {s['title']} - teaches {s['teaches']}; shows {s['visual']}" for s in plan["sections"])


def _card(plan):
    return generate.SOURCE.format(source=plan["source"]) if plan.get("source") else ""


def dev_items(video_dir):
    """Mean P(right) per DEV item over the two option orders (forced choice, TeachQuiz's frames), cached."""
    p = dvgain.probes(video_dir, video_dir, "frames", split="dev")
    out = {}
    for r in p["rotations"]:
        for it in r["items"]:
            out.setdefault(it["id"], []).append(dvgain.CHANCE if it["p_right"] is None else it["p_right"])
    return {i: sum(v) / len(v) for i, v in out.items()}


def dev_score(video_dir):
    items = dev_items(video_dir)
    return sum(items.values()) / len(items) if items else None


def qmatrix(run_dir, plan, quiz):
    path = run_dir / "qmatrix.json"
    if path.exists():
        return json.loads(path.read_text())
    ids, out = {s["id"] for s in plan["sections"]}, {}
    for q in quiz["dev"]:
        try:
            r = llm.ask(llm.PLANNER, QMAP.format(topic=plan["topic"], sections=_sections(plan),
                                                 question=teachquiz.quiz_text([q])) + _card(plan), note="qmap")  # fmt: skip
        except RuntimeError:
            continue
        if r.get("section") in ids:
            out[q["id"]] = r["section"]
    path.write_text(json.dumps(out, indent=1))
    return out


def ochiai(items, qmap, sections):
    failing = {i for i, p in items.items() if p < PASS}
    total_f = len(failing)
    rank = {}
    for s in sections:
        ef = sum(1 for i in failing if qmap.get(i) == s)
        ep = sum(1 for i in items if i not in failing and qmap.get(i) == s)
        rank[s] = ef / math.sqrt(total_f * (ef + ep)) if ef else 0.0
    return rank, failing


def leaks(idea, q, plan):
    """A number in the idea that the DEV item has and neither the plan nor the card has, or one of its options."""
    nums = lambda t: set(re.findall(r"-?\d+(?:\.\d+)?", t))
    allowed = nums(json.dumps(plan["sections"]) + plan.get("source", ""))
    item = q["question"] + " " + " ".join(q["options"].values())
    if len((nums(idea) & nums(item)) - allowed) >= 2:  # one shared digit is common; two re-state the instance
        return True
    low = idea.lower()
    if any(len(o.strip()) >= 3 and o.strip().lower() in low for o in q["options"].values()):
        return True
    return feedback.copies(idea, item)


def diagnose(run_dir, feats, log=print):
    """The repair plan for this stage: {section: [ideas]} and what it was based on. Cached per kind of diagnosis."""
    kind = "f4" if "leak_gate" in feats else "f3" if "sbfl" in feats else "f0"
    path = run_dir / f"diagnosis_{kind}.json"
    if path.exists():
        return json.loads(path.read_text())
    if kind == "f0":
        d = feedback.diagnose(run_dir, log)
        rec = {"kind": kind, "fixes": d["fixes"], "gaps": d["gaps"], "dev": d["dev"]}
        path.write_text(json.dumps(rec, indent=1, ensure_ascii=False))
        return rec
    plan = json.loads((run_dir / "plan.json").read_text())
    quiz = json.loads((run_dir / "quiz.json").read_text())
    key = {q["id"]: q for q in quiz["dev"]}
    items = dev_items(run_dir)
    qmap = qmatrix(run_dir, plan, quiz)
    ids = [s["id"] for s in plan["sections"]]
    rank, failing = ochiai(items, qmap, ids)
    k = 1 if len(ids) <= 3 else 2
    chosen = [s for s in sorted(ids, key=lambda s: -rank[s]) if rank[s] > 0][:k]
    fixes, refused = {}, []
    for i in sorted(failing):
        sid = qmap.get(i)
        if sid not in chosen:
            continue
        try:
            r = llm.ask(llm.PLANNER, MISSING.format(topic=plan["topic"], sections=_sections(plan), sid=sid,
                                                    question=teachquiz.quiz_text([key[i]])) + _card(plan), note="missing")  # fmt: skip
        except RuntimeError:
            continue
        idea = str(r.get("missing") or "").strip()
        if not idea or feedback.copies(idea, key[i]["question"] + " " + " ".join(key[i]["options"].values())):
            refused.append({"item": i, "idea": idea, "why": "copies"})
            continue
        if kind == "f4" and leaks(idea, key[i], plan):
            refused.append({"item": i, "idea": idea, "why": "leaks a number or an option of the DEV item"})
            continue
        fixes.setdefault(sid, []).append(idea)
    if kind == "f4":
        for sid, ideas in list(fixes.items()):
            sec = next(s for s in plan["sections"] if s["id"] == sid)
            banned = sorted({n for i in failing if qmap.get(i) == sid
                             for n in re.findall(r"-?\d+(?:\.\d+)?", key[i]["question"] + " " + " ".join(key[i]["options"].values()))})  # fmt: skip
            try:
                r = llm.ask(llm.PLANNER, MERGE.format(sid=sid, topic=plan["topic"], teaches=sec["teaches"],
                                                      ideas="\n".join(f"- {x}" for x in ideas),
                                                      banned=", ".join(banned) or "none") + _card(plan), note="merge")  # fmt: skip
                principle = str(r.get("principle") or "").strip()
            except RuntimeError:
                principle = ""
            if principle:
                fixes[sid] = [principle]
    rec = {"kind": kind, "fixes": fixes, "items": items, "qmap": qmap, "ochiai": rank, "chosen": chosen, "k": k,
           "failing": sorted(failing), "refused": refused, "dev": len(items)}  # fmt: skip
    path.write_text(json.dumps(rec, indent=1, ensure_ascii=False))
    log(f"[stage] {kind}: {len(failing)} of {len(items)} DEV items fail; Ochiai top {k}: {chosen}; fixes {sorted(fixes)}")
    return rec


def edit_code(code, cls, add):
    try:
        text = llm.ask(llm.CODER, EDIT.format(cls=cls, add=add, code=code), temperature=0.2, as_json=False, note="edit")
    except RuntimeError:
        return None
    return generate.strip_fence(text)


def revise(run_dir, new_dir, fixes, feats, log=print):
    """feedback.revise, with the minimal-edit option and the size of every edit recorded."""
    if new_dir.exists():
        shutil.rmtree(new_dir)
    shutil.copytree(run_dir, new_dir, ignore=shutil.ignore_patterns("frames", "eval_*.json", "row.json", "dv_*.json",
                                                                    "stages", *feedback.MODES))  # fmt: skip
    plan = json.loads((new_dir / "plan.json").read_text())
    clips, changed, edits = {}, [], {}
    kept = new_dir / "kept"
    kept.mkdir(exist_ok=True)
    for s in plan["sections"]:
        sid, folder = s["id"], new_dir / "sections"
        old_mp4 = new_dir / "media" / "videos" / sid / "480p15" / f"{sid.upper()}.mp4"
        mp4 = None
        if sid in fixes:
            files = (folder / f"{sid}.py", folder / f"{sid}.layout.json")
            backup = {f: f.read_bytes() for f in files if f.exists()}
            old_code = (folder / f"{sid}.py").read_text() if (folder / f"{sid}.py").exists() else ""
            if old_mp4.exists():
                shutil.copy(old_mp4, kept / f"{sid}.mp4")
            add = "\n".join(f"- {m}" for m in fixes[sid])
            if "minimal_edit" in feats and old_code:
                new = edit_code(old_code, generate.cls_of(s), add)
                if new:
                    (folder / f"{sid}.py").write_text(new)
                built = generate.build_section(plan, s, new_dir, log) if new else None
            else:
                built = generate.build_section(plan, s, new_dir, log, extra="This section must ALSO show and say:\n" + add)
            if built:
                layout.repair(sid, new_dir, log=log)
                mp4, _ = generate.render(folder / f"{sid}.py", sid.upper(), new_dir / "media")
            if mp4:
                changed.append(sid)
                new_code = (folder / f"{sid}.py").read_text()
                edits[sid] = round(1 - difflib.SequenceMatcher(None, old_code.splitlines(), new_code.splitlines()).ratio(), 3)
            else:
                log(f"[stage] {sid}: the new version did not render; the old one stays")
                for path, data in backup.items():
                    path.write_bytes(data)
                if (kept / f"{sid}.mp4").exists():
                    shutil.copy(kept / f"{sid}.mp4", old_mp4)
        if not mp4 and old_mp4.exists():
            mp4 = old_mp4
        if mp4:
            clips[sid] = mp4
    generate.join(new_dir, plan, clips)
    return changed, edits


def round_(run_dir, mode, stage, log=print):
    """One stage's revision of one base video in one mode; returns its report (cached)."""
    feats = FEATURES[stage]
    out_dir = run_dir / "stages" / stage / mode
    done = out_dir / "feedback.json"
    if done.exists():
        return json.loads(done.read_text())
    plan = json.loads((run_dir / "plan.json").read_text())
    diag = diagnose(run_dir, feats, log)
    fixes = diag["fixes"]
    ids = [s["id"] for s in plan["sections"]]
    if mode == "generic" and fixes:
        fixes = {sid: [feedback.GENERIC] for sid in random.Random(plan["topic"]).sample(ids, len(fixes))}
    elif mode == "learner_all" and fixes:
        every = [m for ms in fixes.values() for m in ms]
        fixes = {sid: every for sid in ids}
    generate.FEATURES = {f for f in feats if f in ("preflight", "safe_patch")}
    out_dir.parent.mkdir(parents=True, exist_ok=True)
    if fixes:
        changed, edits = revise(run_dir, out_dir, fixes, feats, log)
    else:
        changed, edits = [], {}
    report = {"stage": stage, "mode": mode, "features": sorted(feats), "fixes": fixes, "changed": changed,
              "edit_size": edits, "diagnosis": diag["kind"]}  # fmt: skip
    if changed:
        m0, m1 = feedback.section_mvqs(run_dir), feedback.section_mvqs(out_dir)
        if "sbfl" in feats:
            before, after = dev_score(run_dir), dev_score(out_dir)
        else:
            before = teachquiz.evaluate(run_dir, "dev", runs=2)["teachquiz"]
            after = teachquiz.evaluate(out_dir, "dev", runs=2)["teachquiz"]
        f0, f1 = feedback.layout_faults(run_dir, out_dir, changed)  # no more layout faults than before the rewrite
        report.update(dev_before=before, dev_after=after, mvqs_before=m0, mvqs_after=m1, faults_before=f0,
                      faults_after=f1, kept=after >= before and (m0 is None or m1 is None or m1 > m0 - 5)
                      and (f0 is None or f1 <= f0))  # fmt: skip
    else:
        report["kept"] = False
    report["served"] = "revision" if (changed and (report["kept"] or "gate" not in feats)) else "base"
    out_dir.mkdir(parents=True, exist_ok=True)
    done.write_text(json.dumps(report, indent=1, ensure_ascii=False))
    return report
