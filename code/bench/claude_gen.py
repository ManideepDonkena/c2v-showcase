"""Generator study: the same NOVEL-12 concepts, quizzes and student, with the planner and the coder swapped from the
local models (qwen3.6, qwen3-coder:30b) to one Claude model. Only the pipeline's best configuration is run, with no
stage-by-stage ablation: the code check and safe patching are on from the first render, the admission check is the same,
and the repair loop is stage F5 (every feature). The student (gemma4:26b) and the measures (M9, M7) do not change.

    python bench/claude_gen.py --family sonnet [--topics "Tovan sums"] [--workers 2] [--no-repair]
    python bench/claude_gen.py --report

Videos go to runs/claude-gen/<family>/<slug>/ (not in git). Results: bench/results/claude-gen/rows_<family>.json,
report.json, report.md. Every Claude request is in runs/ledger_claude.jsonl (tokens, dollars, seconds), tagged with
the family and topic; the run stops at C2V_CLAUDE_CAP_USD (default 10) over the whole ledger.

Fair-comparison choices:
  - quiz.json (practice quiz DEV and final quiz TEST) is copied from the local-model run, so both videos face the same
    questions; the no-video probe (dv_blind_test.json) depends only on the topic and TEST, so it is copied too;
  - the plan and every section are written by the Claude model from the same definition card.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import os
import shutil
import statistics as st
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "bench"))

from analyze import paired  # noqa: E402

from c2vlab import admission, generate, llm, pipeline  # noqa: E402

FAMILIES = {"qwen": None, "qwen-anchor": None, "haiku": "claude-haiku-5-5", "sonnet": "claude-sonnet-5-5",
            "opus": "claude-opus-5-5", "sonnet-anchor": "claude-sonnet-5-5"}
# "-anchor": the same generator with Code2Video's layout template (title, lecture lines on the left, a 6x6 anchor grid
# on the right; generate.CODE_ANCHOR), to test whether a simpler, fixed layout has fewer layout faults.
# "qwen": the local models (qwen3.6 plans, qwen3-coder:30b codes) in the same best configuration; their tokens are
# priced as if the same models ran on OpenRouter (llm.OPENROUTER_EQUIV). "local" in the report is the earlier
# local-model run (pilot set-up: no code check at the first render).
GRADE = "undergraduate students"
BASE = ROOT / "runs" / "claude-gen"
OUT = ROOT / "bench" / "results" / "claude-gen"
LOCK = threading.Lock()


def ledger(study, tag=None):
    rows = [json.loads(x) for x in llm.CLAUDE_LEDGER.read_text().splitlines() if x.strip()] if llm.CLAUDE_LEDGER.exists() else []
    rows = [r for r in rows if r.get("study") == study and (tag is None or r.get("tag") == tag)]
    return {"calls": len(rows), "in": sum(r["in"] for r in rows), "out": sum(r["out"] for r in rows),
            "usd": round(sum(r["usd"] for r in rows), 4), "seconds": round(sum(r["s"] for r in rows)),
            "fallback": sum(r["served"] != r["model"] for r in rows)}  # fmt: skip


def local_ledger(study, tag=None):
    """Generation tokens of the local planner and coder (not the student or the judge), priced at OpenRouter rates."""
    p = llm.LOCAL_LEDGER
    rows = [json.loads(x) for x in p.read_text().splitlines() if x.strip()] if p.exists() else []
    rows = [r for r in rows if r.get("study") == study and (tag is None or r.get("tag") == tag)
            and r["model"] not in (llm.STUDENT, llm.JUDGE)]  # fmt: skip
    return {"calls": len(rows), "in": sum(r["in"] for r in rows), "out": sum(r["out"] for r in rows),
            "usd": round(sum(r["usd_openrouter"] for r in rows), 4), "seconds": round(sum(r["s"] for r in rows)),
            "fallback": 0, "priced_as": "OpenRouter"}  # fmt: skip


def one(family, topic, card, repair, log):
    import layout_study
    import stages as stage_bench

    slug = generate.slug(topic)
    orig, out = ROOT / "runs" / slug, BASE / family / slug
    out.mkdir(parents=True, exist_ok=True)
    llm.CONTEXT.tag = slug
    for name in ("quiz.json", "dv_blind_test.json"):
        if (orig / name).exists() and not (out / name).exists():
            shutil.copy(orig / name, out / name)
    t = {"start": time.time()}
    pipeline.make_video(topic, GRADE, out, log=log, source=card)
    t["video"] = time.time()
    adm = (json.loads((out / "admission.json").read_text()) if (out / "admission.json").exists()
           else admission.admit(topic, out, GRADE, source=card, log=log))  # fmt: skip
    t["admission"] = time.time()
    first_try = sum(b["rendered"] for b in adm["before"].values())
    row = {"topic": topic, "slug": slug, "family": family, "model": FAMILIES[family] or "qwen3.6 + qwen3-coder:30b",
           "admission": {"sections": len(adm["before"]), "rendered_first": first_try, "ok_first": sum(b["ok"] for b in adm["before"].values()),
                         "complete": adm["complete"], "clean": adm["clean"], "regenerated": len(adm["regenerated"])}}  # fmt: skip
    if not (out / "video.mp4").exists():
        row["error"] = "no video"
        return row
    plan = json.loads((out / "plan.json").read_text())
    row["layout"] = layout_study.layout_of(out, plan)
    row["teaching"] = stage_bench.one_topic(out, "F5") if repair else {"base": stage_bench.score(out, out)}
    t["scored"] = time.time()
    row["minutes"] = {"video": round((t["video"] - t["start"]) / 60, 1),
                      "admission": round((t["admission"] - t["video"]) / 60, 1),
                      "repair_and_scoring": round((t["scored"] - t["admission"]) / 60, 1)}  # fmt: skip
    row["claude"] = (ledger if FAMILIES[family] else local_ledger)(os.environ["C2V_STUDY"], slug)
    return row


def run(family, topics, workers, repair):
    model = FAMILIES[family]
    if model:
        llm.PLANNER = llm.CODER = f"claude:{model}"  # the student and the judge stay local
    os.environ["C2V_STUDY"] = f"claude-gen-{family}"
    generate.FEATURES = {"preflight", "safe_patch"}  # the best configuration, from the first render
    from c2vlab import layout

    layout.CROWDING = False  # the rules every family of this study started under (and the local baseline's)
    if family.endswith("-anchor"):
        generate.FEATURES.add("anchor")
    cards = json.loads((ROOT / "bench" / "novel" / "cards.json").read_text())
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"rows_{family}.json"
    rows = {r["topic"]: r for r in json.loads(path.read_text())} if path.exists() else {}

    def job(topic):
        log = lambda m: print(f"[{family}:{generate.slug(topic)[:20]}] {m}", flush=True)
        return one(family, topic, cards.get(topic), repair, log)

    with cf.ThreadPoolExecutor(workers) as pool:
        futures = {pool.submit(job, t): t for t in topics if "teaching" not in rows.get(t, {})}
        for f in cf.as_completed(futures):
            topic = futures[f]
            try:
                rows[topic] = f.result()
                print(f"[claude-gen] {family} done {topic}: {rows[topic].get('claude')}", flush=True)
            except Exception as exc:  # noqa: BLE001 - one topic's failure is recorded, the rest go on
                rows[topic] = {"topic": topic, "family": family, "error": f"{type(exc).__name__}: {exc}"}
                print(f"[claude-gen] {family} FAILED {topic}: {exc}", flush=True)
            with LOCK:
                path.write_text(json.dumps(list(rows.values()), indent=1, ensure_ascii=False))
    print(f"[claude-gen] {family}: {(ledger if model else local_ledger)(os.environ['C2V_STUDY'])}; total Claude spend {llm.claude_spent():.3f} USD")


def local_rows():
    """The local-model pipeline on the same concepts: base and F5 scores, layout, admission."""
    f5 = {r["topic"]: r for r in json.loads((ROOT / "bench/results/novel12-stages/rows_F5.json").read_text())}
    lay = {generate.slug(r["topic"]): r for r in json.loads((ROOT / "bench/results/layout-study/rows.json").read_text())}
    rows = {}
    for slug, r in f5.items():
        adm = json.loads((ROOT / "runs" / slug / "admission.json").read_text())
        rows[slug] = {"slug": slug, "family": "local", "teaching": r, "layout": lay.get(slug, {}).get("ours", {}).get("layout"),
                      "admission": {"sections": len(adm["before"]), "rendered_first": sum(b["rendered"] for b in adm["before"].values()),
                                    "ok_first": sum(b["ok"] for b in adm["before"].values()), "complete": adm["complete"],
                                    "clean": adm["clean"], "regenerated": len(adm["regenerated"])}}  # fmt: skip
    return rows


def summary(rows):
    ok = [r for r in rows.values() if "teaching" in r]
    mean = lambda xs: round(st.mean(xs), 1) if xs else None
    t = lambda r, c, m: (r["teaching"].get(c) or {}).get(m)
    adm = [r["admission"] for r in rows.values() if "admission" in r]
    s = {"concepts": len(ok),
         "sections_rendered_first_try": f"{sum(a['rendered_first'] for a in adm)}/{sum(a['sections'] for a in adm)}",
         "sections_clean_first_try": f"{sum(a['ok_first'] for a in adm)}/{sum(a['sections'] for a in adm)}",
         "complete_after_admission": f"{sum(a['complete'] for a in adm)}/{len(adm)}",
         "clean_after_admission": f"{sum(a['clean'] for a in adm)}/{len(adm)}",
         "mvqs": mean([r["layout"]["mvqs_mean"] for r in ok if r.get("layout") and r["layout"].get("mvqs_mean") is not None]),
         "conflicts": sum(r["layout"]["conflicts"] for r in ok if r.get("layout")),
         "timing_faults": sum(r["layout"]["timing"] for r in ok if r.get("layout")),
         "broken_attachments": sum(r["layout"].get("broken_attachments", 0) for r in ok if r.get("layout")),
         "M9_base": mean([100 * t(r, "base", "m9") for r in ok if t(r, "base", "m9") is not None]),
         "M7_base": mean([100 * t(r, "base", "m7") for r in ok if t(r, "base", "m7") is not None]),
         "frames_confidence": mean([100 * t(r, "base", "s_frames_p") for r in ok if t(r, "base", "s_frames_p") is not None])}  # fmt: skip
    for a, b in (("learner", "base"), ("learner", "generic")):
        xs = [r for r in ok if t(r, a, "m9") is not None and t(r, b, "m9") is not None]
        s[f"M9 {a} - {b}"] = paired([t(r, a, "m9") for r in xs], [t(r, b, "m9") for r in xs]) if xs else None
    cl = [r["claude"] for r in ok if r.get("claude")]
    if cl:
        s["per_video"] = {"tokens_in": round(st.mean(c["in"] for c in cl)), "tokens_out": round(st.mean(c["out"] for c in cl)),
                          "usd": round(st.mean(c["usd"] for c in cl), 3), "calls": round(st.mean(c["calls"] for c in cl), 1),
                          "api_minutes": round(st.mean(c["seconds"] for c in cl) / 60, 1)}  # fmt: skip
        s["total_usd"] = round(sum(c["usd"] for c in cl), 3)
    mins = [r["minutes"] for r in ok if r.get("minutes")]
    if mins:
        s["minutes_per_video"] = {k: round(st.mean(m[k] for m in mins), 1) for k in mins[0]}
    return s


def report():
    fams = {"local": local_rows()}
    for fam in FAMILIES:  # the order of the columns
        p = OUT / f"rows_{fam}.json"
        if p.exists():
            fams[fam] = {r.get("slug") or generate.slug(r["topic"]): r for r in json.loads(p.read_text())}
    # Conflicts and broken attachments from one tracker for every version (bench/layout_complexity.py), when measured:
    # the in-run counts mix the tracker before and after its id()-reuse fix. MVQS is unaffected.
    lc = ROOT / "bench" / "results" / "layout-complexity" / "rows.json"
    if lc.exists():
        per = {}
        for x in json.loads(lc.read_text()):
            k = (x["version"], x["topic"])
            per.setdefault(k, {"conflicts": 0, "broken_attachments": 0})
            per[k]["conflicts"] += x["conflicts"]
            per[k]["broken_attachments"] += x["broken_attachments"]
        for fam, rows in fams.items():
            for slug, r in rows.items():
                if r.get("layout") and (fam, slug) in per:
                    r["layout"] = {**r["layout"], **per[(fam, slug)], "tracker": "layout-complexity"}
    rep = {fam: summary(rows) for fam, rows in fams.items()}
    default = "qwen" if "qwen" in fams else "local"  # the local models in the same configuration, when run
    for fam, rows in fams.items():  # paired against a reference on the concepts both have
        ref = fam[: -len("-anchor")] if fam.endswith("-anchor") and fam[: -len("-anchor")] in fams else default
        if fam in ("local", default):
            continue
        both = [s for s, r in rows.items() if "teaching" in r and "teaching" in fams[ref].get(s, {})]
        g = lambda f, s: fams[f][s]["teaching"]["base"]["m9"]
        c = lambda f, s: (fams[f][s].get("layout") or {}).get("conflicts")
        a = lambda f, s: (fams[f][s].get("layout") or {}).get("broken_attachments")
        rep[fam]["reference"] = ref
        rep[fam]["M9 base vs local"] = paired([g(fam, s) for s in both], [g(ref, s) for s in both]) if both else None
        rep[fam]["conflicts vs reference"] = paired([c(fam, s) for s in both], [c(ref, s) for s in both]) if both else None
        rep[fam]["attachments vs reference"] = paired([a(fam, s) for s in both], [a(ref, s) for s in both]) if both else None
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "report.json").write_text(json.dumps(rep, indent=1, ensure_ascii=False))
    pct = lambda p: "--" if not p else f"{100 * p['mean_diff']:+.1f} ({p['wins']}/{p['ties']}/{p['losses']}, p {p.get('wilcoxon_p')})"
    keys = [("concepts", "Concepts scored"), ("sections_rendered_first_try", "Sections rendered on the first try"),
            ("sections_clean_first_try", "Sections clean on the first try"), ("complete_after_admission", "Complete after admission"),
            ("clean_after_admission", "Clean after admission"), ("mvqs", "Layout score (MVQS)"), ("conflicts", "Lasting conflicts"),
            ("timing_faults", "Timing faults"), ("broken_attachments", "Broken attachments"),
            ("frames_confidence", "Confidence with 3 frames"), ("M9_base", "M9, base video"), ("M7_base", "M7, base video")]  # fmt: skip
    head = "| | " + " | ".join(rep) + " |"
    lines = ["# Generator study: local models against Claude models (NOVEL-12, best configuration)", "", head,
             "|---" * (len(rep) + 1) + "|"]
    for k, name in keys:
        lines.append(f"| {name} | " + " | ".join(str(rep[f].get(k, "--")) for f in rep) + " |")
    for k, name in (("M9 base vs local", "M9 base: minus reference (local best; anchors: same generator without)"), ("M9 learner - base", "F5 repair: learner minus base (M9)"),
                    ("M9 learner - generic", "F5 repair: learner minus generic (M9)")):  # fmt: skip
        lines.append(f"| {name} | " + " | ".join(pct(rep[f].get(k)) for f in rep) + " |")
    for k, name in (("tokens_in", "Generation tokens in, per video"), ("tokens_out", "Generation tokens out, per video"),
                    ("calls", "Generation requests per video"), ("usd", "USD per video (qwen: at OpenRouter prices)")):  # fmt: skip
        lines.append(f"| {name} | " + " | ".join(str((rep[f].get("per_video") or {}).get(k, "--")) for f in rep) + " |")
    lines.append("| Total USD | " + " | ".join(str(rep[f].get("total_usd", "--")) for f in rep) + " |")
    (OUT / "report.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    tex(rep, keys)


def tex(rep, keys):
    """paper/claude_gen.tex (the table) and paper/claude_gen_numbers.tex (macros for the text); generated, do not edit."""
    name = {"local": "Local (pilot)", "qwen": "Local (best)", "qwen-anchor": "Local + anchors", "haiku": "Haiku 5.5",
            "sonnet": "Sonnet 5.5", "opus": "Opus 5.5", "sonnet-anchor": "Sonnet + anchors"}
    word = {"local": "Local", "qwen": "Qwen", "qwen-anchor": "QwenAnchor", "haiku": "Haiku", "sonnet": "Sonnet",
            "opus": "Opus", "sonnet-anchor": "SonnetAnchor"}
    pts = lambda p: "--" if not p else f"{100 * p['mean_diff']:+.1f} ({p['wins']}/{p['ties']}/{p['losses']})".replace("-", "$-$", 1) if p["mean_diff"] < 0 else f"{100 * p['mean_diff']:+.1f} ({p['wins']}/{p['ties']}/{p['losses']})"
    cell = lambda v: "--" if v is None else str(v).replace("-", "$-$") if isinstance(v, (int, float)) and v < 0 else ("--" if v is None else str(v))
    fams = list(rep)
    rows = [f"{label} & " + " & ".join(cell(rep[f].get(k)) for f in fams) + r" \\" for k, label in keys]
    rows.append(r"\midrule")
    for k, label in (("M9 base vs local", "M9 base, minus reference"), ("M9 learner - base", "F5 repair minus base (M9)"),
                     ("M9 learner - generic", "F5 repair minus generic (M9)")):  # fmt: skip
        rows.append(f"{label} & " + " & ".join(pts(rep[f].get(k)) for f in fams) + r" \\")
    rows.append(r"\midrule")
    for k, label in (("tokens_in", "Generation tokens in, per video"), ("tokens_out", "Generation tokens out, per video"),
                     ("usd", r"Cost per video (\$)")):  # fmt: skip
        rows.append(f"{label} & " + " & ".join(str((rep[f].get("per_video") or {}).get(k, "--")) for f in fams) + r" \\")
    body = "\n".join(rows)
    table = (
        "% generated by bench/claude_gen.py; do not edit\n"
        r"\begin{table}[!htbp]\centering\footnotesize" "\n"
        r"\caption{Generator study on the admitted NOVEL-12 concepts: the planner and the coder are the local models or "
        r"one Claude model; the student, the quizzes and the measures are the same. Best configuration only (code check "
        r"from the first render, the same admission, repair stage F5). Lasting conflicts and broken attachments "
        r"($\downarrow$): overlaps that stay on screen and labels pulled off their shapes. M9 ($\uparrow$): gain on 3 "
        r"frames per section, 0--100. Differences: mean over concepts (better/tied/worse).}\label{tab:claude_gen}" "\n"
        r"\setlength{\tabcolsep}{4pt}\begin{tabular}{@{}l" + "r" * len(fams) + r"@{}}\toprule" "\n"
        " & " + " & ".join(name[f] for f in fams) + r" \\\midrule" "\n" + body + "\n"
        r"\bottomrule\end{tabular}" "\n" r"\end{table}" "\n"
    )  # fmt: skip
    (ROOT / "paper" / "claude_gen.tex").write_text(table)
    mac = ["% generated by bench/claude_gen.py; do not edit"]
    for f in fams:
        r, w = rep[f], word[f]
        sign = lambda v: "--" if v is None else (f"$-${abs(v):.1f}" if v < 0 else f"+{v:.1f}")
        mac += [rf"\newcommand{{\Gen{w}MNine}}{{{cell(r.get('M9_base'))}}}",
                rf"\newcommand{{\Gen{w}MSeven}}{{{cell(r.get('M7_base'))}}}",
                rf"\newcommand{{\Gen{w}Concepts}}{{{r.get('concepts')}}}",
                rf"\newcommand{{\Gen{w}FirstTry}}{{{r.get('sections_rendered_first_try')}}}",
                rf"\newcommand{{\Gen{w}CleanFirst}}{{{r.get('sections_clean_first_try')}}}",
                rf"\newcommand{{\Gen{w}Conflicts}}{{{r.get('conflicts')}}}",
                rf"\newcommand{{\Gen{w}Attach}}{{{r.get('broken_attachments')}}}",
                rf"\newcommand{{\Gen{w}MVQS}}{{{r.get('mvqs')}}}"]  # fmt: skip
        for k, short in (("M9 base vs local", "VsLocal"), ("M9 learner - base", "Repair"), ("M9 learner - generic", "RepairGeneric")):
            p = r.get(k)
            mac += [rf"\newcommand{{\Gen{w}{short}}}{{{sign(100 * p['mean_diff']) if p else '--'}}}",
                    rf"\newcommand{{\Gen{w}{short}Wins}}{{{p['wins'] if p else '--'}}}",
                    rf"\newcommand{{\Gen{w}{short}Losses}}{{{p['losses'] if p else '--'}}}",
                    rf"\newcommand{{\Gen{w}{short}P}}{{{p.get('wilcoxon_p') if p else '--'}}}"]  # fmt: skip
        pv = r.get("per_video") or {}
        mac += [rf"\newcommand{{\Gen{w}USD}}{{{pv.get('usd', '--')}}}", rf"\newcommand{{\Gen{w}TotalUSD}}{{{r.get('total_usd', '--')}}}"]
    (ROOT / "paper" / "claude_gen_numbers.tex").write_text("\n".join(mac) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", choices=FAMILIES)
    ap.add_argument("--topics", nargs="*")
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--no-repair", action="store_true")
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    if a.family:
        topics = a.topics or json.loads((ROOT / "bench" / "results" / "novel12" / "topics.json").read_text())
        run(a.family, topics, a.workers, not a.no_repair)
    if a.report or not a.family:
        report()


if __name__ == "__main__":
    main()
