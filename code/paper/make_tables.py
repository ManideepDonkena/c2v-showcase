"""Every number in the paper comes from here: LaTeX tables and macros built from the result files. A table whose
results do not exist yet is written as a "pending" box, so the paper always compiles and never shows a typed number.

    python paper/make_tables.py   ->  paper/tables/*.tex, paper/tables/numbers.tex
"""

from __future__ import annotations

import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
RES = ROOT / "bench" / "results"
OUT = ROOT / "paper" / "tables"
CONDS = ("base", "learner", "generic", "learner_all")
PAIRS = ("learner - base", "learner - generic", "learner - learner_all", "generic - base")


def load(path):
    p = RES / path
    return json.loads(p.read_text()) if p.exists() else None


def esc(s):
    return str(s).replace("_", r"\_").replace("%", r"\%").replace("&", r"\&")


def pending(caption, label, what):
    return (f"\\begin{{table}}[!htbp]\\centering\\caption{{{caption}}}\\label{{{label}}}\n"
            f"\\fbox{{\\parbox{{0.9\\linewidth}}{{\\centering\\small\\textit{{Pending: {esc(what)}.}}}}}}\n\\end{{table}}\n")  # fmt: skip


def pts(x, sign=True):
    """A score or difference on the 0-100 scale, one decimal, as in Code2Video's tables."""
    if x is None:
        return "--"
    v = round(100 * x, 1) + 0.0  # no "-0.0"
    return (f"{v:+.1f}" if sign and v else f"{v:.1f}").replace("-", "$-$")


def mean_diff(p):
    """The mean of a paired difference (intervals stay in the result files, not in the tables)."""
    return None if not p else p["mean_diff"]


def delta(x, better, scale=100, fmt="+.1f"):
    """A small coloured change next to a score, like Code2Video's +39.5.

    `better` is the column's direction and has no default, so every caller states it: "up" for an up-arrow column,
    "down" for a down-arrow column (a fall is shown as an improvement), None for a column with no better direction
    (sections rewritten, revisions used), which is drawn in grey whatever its sign."""
    if better not in ("up", "down", None):
        raise ValueError(f"better must be 'up', 'down' or None, not {better!r}")
    if x is None or f"{scale * x:{fmt}}".lstrip("+-").strip("0.") == "":
        return ""
    text = f"{scale * x:{fmt}}".replace("-", "$-$")
    if better is None:
        return f"\\neutral{{{text}}}"
    good = x > 0 if better == "up" else x < 0
    return f"\\better{{{text}}}" if good else f"\\worse{{{text}}}"


def group(n, text):
    return f"\\midrule\n\\multicolumn{{{n}}}{{c}}{{\\textit{{{text}}}}}\\\\\n"


NAMES = {"base": "Base video (first attempt)", "generic": "Generic repair", "learner_all": "Learner repair, every section",
         "learner": "Learner repair (ours)"}  # fmt: skip
ORDER = ("base", "generic", "learner_all", "learner")


PILOT = "mmmc-n12-seed0"  # the MMMC pilot: its topic manifest pins every pilot number


def pilot_dirs():
    """The pilot's video folders, and nothing else: the 12 topics in its manifest, each with the base video and the
    three named conditions. Never a wildcard over runs/, which NOVEL-12 and the F0-F5 stages also write into."""
    from c2vlab import generate

    topics = json.loads((RES / PILOT / "topics.json").read_text())
    out = []
    for t in topics:
        d = ROOT / "runs" / generate.slug(t)
        out += [d] + [d / c for c in CONDS if c != "base"]
    return out


def fit(text):
    """Shrink a table to the line width when, and only when, it is wider (adjustbox's max width)."""
    if "\\begin{adjustbox}" in text:
        return text
    text = re.sub(r"\\begin\{tabular\}", r"\\begin{adjustbox}{max width=\\linewidth}\\begin{tabular}", text)
    return text.replace("\\end{tabular}", "\\end{tabular}\\end{adjustbox}")


def write(name, text):
    (OUT / f"{name}.tex").write_text(fit(text))


def pilot(macros):
    a = load("mmmc-n12-seed0/analysis.json")
    if not a:
        write("pilot", pending("Pilot on MMMC.", "tab:pilot", "bench/results/mmmc-n12-seed0/analysis.json"))
        return
    base = a["means"]["base"]
    rows = []
    for c in ORDER:
        m = a["means"][c]
        d = "" if c == "base" else delta((m["teachquiz"] - base["teachquiz"]) / 100, "up")
        rows.append(f"{NAMES[c]} & {m['teachquiz']:.1f}{d} & {m['evidence']:.1f} & {m['mvqs']:.1f} & {m['sections_rendered']:.2f} \\\\")
    write("pilot", "\\begin{table*}[!tbp]\\centering\\small\n\\caption{Pilot on 12 MMMC topics, scored with TeachQuiz as in "
          "Code2Video (local student, 3 frames per section, graded as in the pilot, before the fix of Break 1; the regraded score is version M1 of the ladder). TeachQuiz: quiz score with the video "
          "minus without it. Evidence: answers a judge could find in the frames. Layout: SGA's MVQS. Small numbers: "
          "change against the base video.}\\label{tab:pilot}\n"
          "\\begin{tabular}{lrrrr}\\toprule Method & TeachQuiz ($\\uparrow$) & Evidence ($\\uparrow$) & Layout ($\\uparrow$) & "
          "Sections rendered ($\\uparrow$)\\\\\n" + group(5, "Repair of the base video") .replace("\\midrule\n", "\\midrule\n", 1)
          + "\n".join(rows) + "\n\\bottomrule\\end{tabular}\n\\end{table*}\n")  # fmt: skip
    macros["PilotTies"] = a["paired"]["learner - base"]["teachquiz"]["ties"]
    macros["PilotLayoutBase"] = f"{a['means']['base']['mvqs']:.1f}"
    macros["PilotLayoutAll"] = f"{a['means']['learner_all']['mvqs']:.1f}"


def matching(macros):
    """How often the student's answers had to be matched by order (it copied the template's ids)."""
    runs, by_order, null_full, null_none = 0, 0, collections.Counter(), collections.Counter()
    right_full = collections.Counter()
    for f in [d / "eval_test.tq2.json" for d in pilot_dirs() if (d / "eval_test.tq2.json").exists()]:
        e = json.loads(f.read_text())
        for r in e["runs"]["full"] + e["runs"]["none"]:
            runs += 1
            by_order += bool(r.get("by_order"))
        for r in e["runs"]["full"]:
            for x in r["answers"]:
                null_full[x["choice"] == "NULL"] += 1
                if x["choice"] != "NULL":
                    right_full[bool(x.get("right"))] += 1
        for r in e["runs"]["none"]:
            for x in r["answers"]:
                null_none[x["choice"] == "NULL"] += 1
    if runs:
        macros["OrderRuns"] = by_order
        macros["AllRuns"] = runs
        macros["OrderShare"] = f"{100 * by_order / runs:.0f}"
        macros["NullWithVideo"] = f"{100 * null_full[True] / max(1, sum(null_full.values())):.0f}"
        macros["NullNoVideo"] = f"{100 * null_none[True] / max(1, sum(null_none.values())):.0f}"
        macros["NullWithVideoN"] = null_full[True]
        macros["AnsweredWithVideo"] = sum(right_full.values())
        macros["AnsweredRight"] = right_full[True]
        macros["AnsweredWrong"] = right_full[False]
        macros["AnsweredRightShare"] = f"{100 * right_full[True] / max(1, sum(right_full.values())):.0f}"


PRIOR_SETS = (("mmmc-prior-gemma4_26b", "mmmc", "MMMCGemma"), ("mmmc-prior-qwen2.5vl_7b", "mmmc", "MMMCQwen"),
              ("mmmc-prior-qwen2.5vl_3b", "mmmc", "MMMCQwenSmall"), ("novel-prior-gemma4_26b", "novel", "NovelGemma"),
              ("novel-card-gemma4_26b", "card", "NovelCardGemma"))  # fmt: skip
OLD_KEYS = {"MMMCGemma": "mmmcpriorGemma", "MMMCQwen": "mmmcpriorQwen", "MMMCQwenSmall": "mmmcpriorQwenSmall",
            "NovelGemma": "novelpriorGemma", "NovelCardGemma": "novelcardGemma"}  # fmt: skip


def priors(macros):
    groups = {"mmmc": [], "novel": []}
    for name, kind, key in PRIOR_SETS:
        s = load(f"{name}.summary.json")
        if not s:
            continue
        what = {"mmmc": "No video", "novel": "No video", "card": "Definition card as text"}[kind]
        groups["novel" if kind == "card" else kind].append(
            f"{what} & {esc(s['student'])} & {s['topics']} & {s['item_rotations'] // 2} & {100 * s['accuracy']:.1f} & "
            f"{100 * s['mean_p_right']:.1f} & {s['topics_all_right']} \\\\")  # fmt: skip
        k = OLD_KEYS[key]
        macros[f"{k}Acc"] = f"{100 * s['accuracy']:.1f}"
        macros[f"{k}P"] = f"{100 * s['mean_p_right']:.1f}"
        macros[f"{k}AllRight"] = s["topics_all_right"]
        macros[f"{k}Topics"] = s["topics"]
    if not any(groups.values()):
        write("priors", pending("Prior knowledge.", "tab:priors", "bench/mmmc_prior.py"))
        return
    body = ""
    if groups["mmmc"]:
        body += group(7, "MMMC (real topics from 3Blue1Brown)") + "\n".join(groups["mmmc"]) + "\n"
    if groups["novel"]:
        body += group(7, "NOVEL-12 (invented concepts)") + "\n".join(groups["novel"]) + "\n"
    write("priors", "\\begin{table*}[!tbp]\\centering\\small\n\\caption{What the student already knows. Code2Video's unlearning "
          "prompt, but the student must choose A--D (no NULL). Accuracy: share of questions right. Confidence: mean "
          "probability the student puts on the right answer. Fully known: topics where every question is right with no "
          "video. Chance is 25.}\\label{tab:priors}\n\\begin{tabular}{llrrrrr}\\toprule Material & Student & Topics & "
          "Questions & Accuracy (\\%) & Confidence (\\%) & Fully known\\\\\n" + body
          + "\\bottomrule\\end{tabular}\n\\end{table*}\n")  # fmt: skip


LADDER_NAMES = {
    "M0": "TeachQuiz (Code2Video)", "M1": "+ answers matched in order", "M2": "+ must choose (no NULL)",
    "M3": "+ gain over what it knew", "M4": "+ dense silent video", "M5": "+ motion bonus (D-VGAIN)",
    "M6": "+ confidence, not right/wrong", "M7": "+ two option orders", "M8": "+ only questions it did not know",
    "M9": "M7 on 3 frames per section", "R7": "Dense video minus no video", "R9": "3 frames minus no video",
}  # fmt: skip


def ladder(name, label, caption, macros, key, folder=None, only_defined=False):
    r = load(f"{folder or name + '-ladder'}/report.json")
    if not r:
        write(label, pending(caption, f"tab:{label}", f"bench/results/{name}-ladder"))
        return
    rows = []
    for m, x in r["rungs"].items():
        if only_defined and x["defined"].startswith("0/"):
            continue
        if m == "R7" and not x["defined"].startswith("0/"):
            rows.append(group(9, "Raw difference in confidence, not normalised (for reference)").strip())
        c = x["conditions"]
        rel = "--" if x["reliability"] is None else f"{x['reliability']:.2f}"
        ties = "--" if x["learner_base_ties"] is None else f"{x['learner_base_ties']}/{r['topics']}"
        rows.append(f"{m} & {LADDER_NAMES.get(m, esc(x['name']))} & {x['defined']} & "
                    f"{pts(mean_diff(x['separation_own_minus_other']))} & {rel} & "
                    f"{pts(mean_diff(c.get('learner - base')))} & {pts(mean_diff(c.get('learner - generic')))} & "
                    f"{pts(mean_diff(c.get('learner - learner_all')))} & {ties} \\\\")  # fmt: skip
    has_cond = any(mean_diff(p) is not None for x in r["rungs"].values() for p in x["conditions"].values())
    if not has_cond:  # base videos only: no repair columns
        rows = [re.sub(r"( & [^&]*){4}( \\\\)$", r"\2", row) if not row.startswith("\\midrule") else
                row.replace("multicolumn{9}", "multicolumn{5}") for row in rows]  # fmt: skip
        write(label, f"\\begin{{table}}[!htbp]\\centering\\footnotesize\n\\caption{{{caption} {r['topics']} topics, base videos "
              "only (the repairs are future work). Each row adds one change to the row above; points on a 0--100 scale. "
              "Scored: videos that get a score. Own $-$ other: a topic's video minus another topic's video on the same "
              f"quiz. Agreement: rank correlation of two measurements of the same videos.}}\\label{{tab:{label}}}\n"
              "\\setlength{\\tabcolsep}{4pt}\\begin{tabular}{@{}llrrr@{}}\\toprule & Measure & Scored & "
              "\\hd{Own $-$\\\\other ($\\uparrow$)} & \\hd{Agree-\\\\ment ($\\uparrow$)}\\\\\\midrule\n" + "\n".join(rows)
              + "\n\\bottomrule\\end{tabular}\n\\end{table}\n")  # fmt: skip
    else:
        write(label, f"\\begin{{table*}}[!tbp]\\centering\\footnotesize\n\\caption{{{caption} {r['topics']} topics, "
              f"{r['videos']} videos. Each row adds one change to the row above; points on a 0--100 scale. The first three "
              "columns use each topic's base video only, since its repairs are near-copies of it. Scored: base videos that "
              "get a score (-- : the student already knew everything). Own $-$ other: a topic's video minus another topic's "
              "video on the same quiz. Agreement: rank correlation of two measurements of the same base videos. Learner "
              "$-$ \\ldots: mean change over topics, the versions paired by topic. Ties: topics where learner and base score "
              f"the same.}}\\label{{tab:{label}}}\n"
              "\\setlength{\\tabcolsep}{4pt}\\begin{tabular}{@{}llrrrrrrr@{}}\\toprule & & \\multicolumn{3}{c}{Does it measure teaching?} & "
              "\\multicolumn{4}{c}{Does the learner repair help?}\\\\\n\\cmidrule(lr){3-5}\\cmidrule(lr){6-9}\n"
              "& Measure & Scored & \\hd{Own $-$\\\\other ($\\uparrow$)} & \\hd{Agree-\\\\ment ($\\uparrow$)} & \\hd{Learner\\\\$-$ base} & "
              "\\hd{Learner\\\\$-$ generic} & \\hd{Learner $-$\\\\every section} & Ties ($\\downarrow$)\\\\\\midrule\n" + "\n".join(rows)
              + "\n\\bottomrule\\end{tabular}\n\\end{table*}\n")  # fmt: skip
    pr = r["prior"]
    macros[f"{key}BlindAllRight"] = pr["topics_blind_all_right"]
    macros[f"{key}Topics"] = r["topics"]
    macros[f"{key}Abstained"] = "--" if pr["tq_abstained_mean"] is None else f"{pr['tq_abstained_mean']:.0f}"
    macros[f"{key}Videos"] = r["videos"]
    rg = r["rungs"]
    for m in ("M1", "M2", "M3", "M7", "M8", "M9", "R7", "R9"):
        if m not in rg:
            continue
        word = {"M1": "One", "M2": "Two", "M3": "Three", "M7": "Seven", "M8": "Eight", "M9": "Nine", "R7": "RawSeven",
                "R9": "RawNine"}[m]  # fmt: skip
        macros[f"{key}Sep{word}"] = pts(mean_diff(rg[m]["separation_own_minus_other"]))
        for pair, short in (("learner - base", "LB"), ("learner - generic", "LG"), ("learner - learner_all", "LA")):
            macros[f"{key}{short}{word}"] = pts(mean_diff(rg[m]["conditions"].get(pair)))
        macros[f"{key}Ties{word}"] = "--" if rg[m]["learner_base_ties"] is None else rg[m]["learner_base_ties"]
        macros[f"{key}Defined{word}"] = rg[m]["defined"]
        macros[f"{key}Agree{word}"] = "--" if rg[m]["reliability"] is None else f"{rg[m]['reliability']:.2f}"
    macros[f"{key}DefinedNVG"] = rg["M3"]["defined"]
    for k in ("s_blind_p_mean", "s_visual_p_mean", "s_frames_p_mean", "s_static_p_mean"):
        if pr.get(k) is not None:
            macros[key + "".join(w.capitalize() for w in k.split("_")[:2])] = f"{100 * pr[k]:.1f}"


STAGE_NAMES = {"F0": "F0: pilot loop", "F1": "+ keep only revisions that pass the check",
               "F2": "+ check the code before rendering", "F3": "+ find the weak section like a debugger",
               "F4": "+ block fixes that copy the practice quiz", "F5": "+ small edits instead of rewrites"}  # fmt: skip


def stages(macros):
    r = load("novel12-stages/report.json")
    if not r:
        write("stages", pending("Pipeline ablation on NOVEL-12.", "tab:stages", "bench/results/novel12-stages"))
        return
    rows, prev = [], None
    for s, x in r.items():
        m = {c: (x["means"][c].get("m9") if x["means"].get(c) else None) for c in ORDER}
        lg9, lg7 = mean_diff(x["m9"].get("learner - generic")), mean_diff(x["m7"].get("learner - generic"))
        d = "" if prev is None or lg9 is None else delta(lg9 - prev, "up")
        prev = lg9 if lg9 is not None else prev
        p, mv = x["process"]["learner"], x["means"]["learner"]["mvqs"]
        rows.append(f"{STAGE_NAMES.get(s, s)} & {pts(m['base'], False)} & {pts(m['generic'], False)} & "
                    f"{pts(m['learner_all'], False)} & {pts(m['learner'], False)} & {pts(lg9)}{d} & {pts(lg7)} & "
                    f"{'--' if mv is None else f'{mv:.1f}'} & {p['sections_changed']} & {p['served_revision']}/{x['topics']} \\\\")  # fmt: skip
    write("stages", "\\begin{table*}[!tbp]\\centering\\small\n\\caption{Effect of each pipeline feature on NOVEL-12. Features "
          "are added one at a time; the base video is the same in every row. Gain: share of what the student did not know "
          "that it learned from 3 frames per section (version M9), in points. Learner $-$ generic: the learner repair against "
          "an equally large repair without the student's signal, scored on 3 frames (M9) and on the dense video (M7); "
          "small numbers: change against the row above. Layout: MVQS of the learner videos. Rewritten: sections rewritten "
          "and rendered. Used: topics whose final video is the revision.}\\label{tab:stages}\n"
          "\\begin{tabular}{lrrrrrrrrr}\\toprule & \\multicolumn{4}{c}{Gain ($\\uparrow$)} & \\multicolumn{2}{c}{Learner $-$ generic "
          "($\\uparrow$)} & & & \\\\\n\\cmidrule(lr){2-5}\\cmidrule(lr){6-7}\nStage & Base & Generic & Every section & "
          "Learner & 3 frames & Dense & Layout ($\\uparrow$) & Rewritten & Used\\\\\\midrule\n" + "\n".join(rows)
          + "\n\\bottomrule\\end{tabular}\n\\end{table*}\n")  # fmt: skip


def failure_classes(first=None):
    """Failed render attempts of the pilot (12 MMMC topics, base and revised videos) by class."""
    first = collections.Counter() if first is None else first
    cls = collections.Counter()
    for d in pilot_dirs():
        for rep in sorted((d / "sections").glob("s*.repairs.json")):
            h = json.loads(rep.read_text())
            first[bool(h and h[0].get("ok"))] += 1
            for i, x in enumerate(h):
                if x.get("ok"):
                    continue
                e, prev = x["error"], (h[i - 1].get("scope") if i else "first")
                k = ("syntax / indentation" if ("SyntaxError" in e or "IndentationError" in e) else
                     "external file or URL" if "could not find" in e else
                     "undefined name" if "NameError" in e else
                     "unknown keyword / method" if ("unexpected keyword" in e or "has no attribute" in e or "getter()" in e) else
                     "2-D point where 3-D needed" if "broadcast" in e else "LaTeX" if "latex" in e.lower() else "other")  # fmt: skip
                cls[k] += 1
                if k == "syntax / indentation" and prev in ("line", "block"):
                    cls["  of which right after a patch"] += 1
    return cls


def failures(macros):
    """Render failures of the pilot (F0) by class, and the pre-flight check's false alarms on sections that rendered."""
    from c2vlab import preflight

    first = collections.Counter()
    cls = failure_classes(first)
    n_ok, flagged = 0, 0
    for rep in [r for d in pilot_dirs() for r in sorted((d / "sections").glob("s*.repairs.json"))]:
        code = rep.with_name(rep.name.replace(".repairs.json", ".py"))
        h = json.loads(rep.read_text())
        if code.exists() and any(x.get("ok") for x in h):
            n_ok += 1
            flagged += bool(preflight.check(code.read_text()))
    macros["FirstTryFail"] = f"{100 * first[False] / max(1, sum(first.values())):.0f}"
    macros["PreflightFP"] = flagged
    macros["PreflightN"] = n_ok
    macros["FailedAttempts"] = sum(v for k, v in cls.items() if not k.startswith(" "))
    macros["SyntaxAfterPatch"] = cls["  of which right after a patch"]
    quad = "\\quad "
    rows = [f"{quad if k.startswith(' ') else ''}{esc(k.strip())} & {v} \\\\" for k, v in cls.most_common()]
    write("failures", "\\begin{table}[!htbp]\\centering\\small\n\\caption{Failed render attempts in the pilot (12 MMMC topics, "
          f"base and revised videos), by class. Pre-flight raises an alarm on {flagged} of {n_ok} sections that "
          "rendered.}\\label{tab:failures}\n\\begin{tabular}{lr}\\toprule Class & Attempts\\\\\\midrule\n"
          + "\n".join(rows) + "\n\\bottomrule\\end{tabular}\n\\end{table}\n")  # fmt: skip


def gate(macros):
    """Pilot revisions that failed the DEV/MVQS gate (and were scored on TEST anyway)."""
    fbs = [json.loads((d / "feedback.json").read_text()) for d in pilot_dirs() if (d / "feedback.json").exists()]
    macros["PilotRevisions"] = len(fbs)
    macros["PilotNotKept"] = sum(not f.get("kept") for f in fbs)


def localisation(macros):
    """How much of DEV the pilot's diagnosis called gaps, how many sections it flagged, and the learner's DEV gain."""
    import statistics as st

    from c2vlab import generate

    topics = json.loads((RES / "mmmc-n12-seed0" / "topics.json").read_text())
    gaps = dev = 0
    flagged, sections, gain = [], [], []
    for t in topics:
        d = ROOT / "runs" / generate.slug(t)
        if not (d / "diagnosis.json").exists():
            continue
        dg = json.loads((d / "diagnosis.json").read_text())
        gaps, dev = gaps + len(dg["gaps"]), dev + dg["dev"]
        flagged.append(len(dg["fixes"]))
        sections.append(len(json.loads((d / "plan.json").read_text())["sections"]))
        fb = d / "learner" / "feedback.json"
        if fb.exists():
            f = json.loads(fb.read_text())
            gain.append(f["dev_after"] - f["dev_before"])
    if dev:
        macros["PilotGaps"], macros["PilotDev"] = gaps, dev
        macros["PilotFlagged"] = f"{st.mean(flagged):.1f}"
        macros["PilotSections"] = f"{st.mean(sections):.0f}"
        macros["PilotDevGain"] = f"{st.mean(gain):+.1f}" if gain else "--"


def novel_first_look():
    """Every NOVEL-12 base video measured so far, on the 0-100 scale, with TeachQuiz beside the new measure."""
    import statistics as st

    from c2vlab import dvgain, generate

    qs = json.loads((ROOT / "bench" / "novel" / "questions.json").read_text())
    admitted = ROOT / "bench" / "results" / "novel12" / "topics.json"  # only the admitted concepts, as in every study
    keep = set(json.loads(admitted.read_text())) if admitted.exists() else set(qs)
    rows, cols = [], []
    for t in qs:
        if t not in keep:
            continue
        d = ROOT / "runs" / generate.slug(t)
        files = {k: d / f"dv_{k}_test.json" for k in ("blind", "frames", "static", "visual")}
        if not all(f.exists() for f in files.values()):
            continue
        p = {k: json.loads(f.read_text()) for k, f in files.items()}
        sb, sf, ss, sv = (dvgain.score(p[k], True, (0, 1)) for k in ("blind", "frames", "static", "visual"))
        tq = d / "eval_test.tq2.json"
        tq = json.loads(tq.read_text())["teachquiz"] / 100 if tq.exists() else None
        vals = [sb, sf, ss, sv, tq, dvgain.nvg(sf, sb), dvgain.nvg(sv, sb), dvgain.dvgain(sv, ss, sb)]
        cols.append(vals)
        rows.append(f"{esc(t)} & " + " & ".join(pts(v, i >= 4) for i, v in enumerate(vals)) + " \\\\")
    if not rows:
        write("novel_first", pending("First NOVEL-12 base videos.", "tab:novel_first", "no NOVEL-12 video measured yet"))
        return
    avg = [st.mean(v) if (v := [c[i] for c in cols if c[i] is not None]) else None for i in range(8)]
    rows.append("\\midrule\nMean & " + " & ".join(f"\\textbf{{{pts(v, i >= 4)}}}" for i, v in enumerate(avg)) + " \\\\")
    write("novel_first", "\\begin{table*}[!tbp]\\centering\\footnotesize\\setlength{\\tabcolsep}{4pt}\n\\caption{NOVEL-12 base "
          "videos (the pipeline's first attempt, before any repair). Confidence: mean probability on the right answer over "
          "8 TEST questions and two option orders, in \\%; chance is 25. TeachQuiz: Code2Video's measure on the same "
          "video. Gain: share of what the student did not know that the video taught (100 = all of it), from 3 frames per "
          "section (M9) or the same gain on the dense video; D-VGAIN (M7) adds the motion bonus to the dense-video gain.}"
          "\\label{tab:novel_first}\n\\begin{tabular}{lrrrrrrrr}\\toprule & \\multicolumn{4}{c}{Confidence on the right answer} & "
          "& \\multicolumn{3}{c}{Ours ($\\uparrow$)}\\\\\n\\cmidrule(lr){2-5}\\cmidrule(lr){7-9}\nConcept & No video & 3 frames & "
          "Start/end & Dense video & TeachQuiz & Gain, 3 frames & Gain, dense & D-VGAIN\\\\\\midrule\n" + "\n".join(rows)
          + "\n\\bottomrule\\end{tabular}\n\\end{table*}\n")  # fmt: skip


def novel_items(topic="Tovan sums"):
    """One concept, question by question: confidence on the right answer under every material."""
    from c2vlab import generate

    d = ROOT / "runs" / generate.slug(topic)
    kinds = ("blind", "frames", "static", "visual")
    files = {k: d / f"dv_{k}_test.json" for k in kinds}
    if not all(f.exists() for f in files.values()):
        write("novel_items", pending(f"{topic}, question by question.", "tab:novel_items", "its probes"))
        return
    p = {k: json.loads(f.read_text()) for k, f in files.items()}
    qs = json.loads((ROOT / "bench" / "novel" / "questions.json").read_text())[topic]
    rows = []
    for i, q in enumerate(qs):
        vals = [sum((r["items"][i]["p_right"] if r["items"][i]["p_right"] is not None else 0.25) for r in p[k]["rotations"])
                / len(p[k]["rotations"]) for k in kinds]  # fmt: skip
        rows.append(f"{esc(q['question'])} & {esc(q['options'][q['answer']])} & " + " & ".join(f"{100 * v:.0f}" for v in vals)
                    + " \\\\")  # fmt: skip
    write("novel_items", f"\\begin{{table*}}[!tbp]\\centering\\footnotesize\n\\caption{{{esc(topic)}, question by question: the "
          "student's confidence in the right answer (\\%, mean of two option orders) under each material. The video is the "
          "pipeline's first attempt, before any repair.}\\label{tab:novel_items}\n"
          "\\begin{tabular}{p{6.4cm}p{2.4cm}rrrr}\\toprule Question & Answer & No video & 3 frames & Start/end & "
          "Dense video\\\\\\midrule\n" + "\n".join(rows) + "\n\\bottomrule\\end{tabular}\n\\end{table*}\n")  # fmt: skip


def models():
    """Which model does each part, read from the code's own settings (c2vlab/llm.py), so it cannot drift."""
    from c2vlab import llm

    tt = lambda m: f"\\texttt{{{esc(m)}}}"
    none = "\\textit{no model}"
    groups = [
        ("Making the video (every step and stage)", [
            ("Planner", "lesson plan: what each section teaches, shows and says", tt(llm.PLANNER)),
            ("Coder", "one Manim scene per section; render repairs (line, block, section)", tt(llm.CODER)),
            ("Code check (F2)", "reads the code and the installed Manim library before rendering", none),
            ("Timing check (F2)", "leftovers after Transform, prose typeset as maths; fixed automatically", none),
            ("Admission", "all sections render, layout at least 70, a person approves the frames", none),
            ("Layout check", "SGA scene graph and MVQS; the coder writes the fixes", f"{none}; {tt(llm.CODER)}"),
        ]),
        ("Learner feedback (the repair)", [
            ("Practice quiz (DEV)", "written from the topic, or from the card of an invented concept", tt(llm.PLANNER)),
            ("Practice-quiz check", "keeps questions the student solves with the card and not without the video", tt(llm.STUDENT)),
            ("Diagnosis", "the missing idea of each failed question; question-to-section map (F3)", tt(llm.PLANNER)),
            ("Weak-section score (F3)", "Ochiai score from passed and failed practice questions", none),
            ("Leak guard (F4)", "refuses fixes that copy the practice question; merges ideas into one", f"rules; {tt(llm.PLANNER)}"),
            ("Small edit (F5)", "edits the working scene instead of rewriting it", tt(llm.CODER)),
            ("Gate (F1)", "practice score must not drop; layout must fall by less than 5", none),
        ]),
        ("Measuring", [
            ("Student", "TeachQuiz, forced choice, D-VGAIN, practice scores (Steps 0--3)", tt(llm.STUDENT)),
            ("Evidence judge", "does a frame show the answer (TeachQuiz pilot only)", tt(llm.JUDGE)),
            ("Second student", "what a different family knows with no video (Step 0)", tt("qwen2.5vl:7b")),
            ("Small student", "MMMC ladder with a 3B model (Step 1)", tt("qwen2.5vl:3b")),
        ]),
        ("Final quizzes (TEST), never seen by the pipeline", [
            ("MMMC", "Code2Video's official questions, 5 per topic", "Code2Video"),
            ("NOVEL-12", "cards and 8 questions per concept; numeric answers computed by code", "Claude (Anthropic)"),
        ]),
        ("Layout reference (side study on the 10 admitted videos)", [
            ("Claude fixer", "repairs layout and timing only; sees code, frames and reports, never the plan, card or quiz",
             "\\texttt{claude-opus-5-5}"),
        ]),
        ("Reference, not run here", [
            ("Code2Video's student", "watches the video file with sound (needs a paid key)", "Gemini"),
        ]),
    ]  # fmt: skip
    body = ""
    for title, rows in groups:
        body += group(3, title) + "\n".join(f"{a} & {b} & {c} \\\\" for a, b, c in rows) + "\n"
    write("models", "\\begin{table*}[!tbp]\\centering\\footnotesize\n\\caption{Which model does each part. Every model runs "
          "locally through Ollama, except the authors of the final quizzes. The student and the judge come from different "
          "families; the NOVEL-12 final quiz is written by a family the pipeline never uses.}\\label{tab:models}\n"
          "\\begin{tabular}{@{}lp{9.2cm}l@{}}\\toprule Part & What it does & Model\\\\\n" + body
          + "\\bottomrule\\end{tabular}\n\\end{table*}\n")  # fmt: skip


def quality(macros):
    """Admission of the NOVEL-12 base videos and the Claude fixes, from runs/<topic>/admission.json and fixes.json."""
    import collections

    from c2vlab import generate

    topics = list(json.loads((ROOT / "bench" / "novel" / "questions.json").read_text()))
    adm = {t: json.loads(p.read_text()) for t in topics if (p := ROOT / "runs" / generate.slug(t) / "admission.json").exists()}
    if not adm:
        return
    incomplete_before = sum(not all(s["rendered"] for s in a["before"].values()) for a in adm.values())
    macros["AdmTotal"] = len(adm)
    macros["AdmIncompleteBefore"] = incomplete_before
    macros["AdmComplete"] = sum(a["complete"] for a in adm.values())
    macros["AdmClean"] = sum(a["clean"] for a in adm.values())
    macros["AdmRegenerated"] = sum(len(a["regenerated"]) for a in adm.values())
    kinds, shifts_in, shifts_out, shift_notes, cost_in, cost_out, secs = collections.Counter(), 0, 0, 0, 0, 0, 0
    for t in topics:
        run = ROOT / "runs" / generate.slug(t)
        fx = run / "claude_fixed" / "fixes.json"
        if not fx.exists():
            continue
        f = json.loads(fx.read_text())
        cost_in, cost_out = cost_in + f["input_tokens"], cost_out + f["output_tokens"]
        for s in f["sections"]:
            secs += 1
            for i in s["issues"]:
                kinds[i["kind"]] += 1
                shift_notes += "shift" in (i["where"] + " " + i["change"]).lower()
            ours, fixed = run / "sections" / f"{s['id']}.py", run / "claude_fixed" / "sections" / f"{s['id']}.py"
            n = ours.read_text().count("# layout: separation vector")
            shifts_in += n
            shifts_out += n - fixed.read_text().count("# layout: separation vector")
    if secs:
        macros.update(ClaudeSections=secs, ClaudeFaults=sum(kinds.values()), ClaudeOverlap=kinds["overlap"],
                      ClaudeOther=kinds["other"], ClaudeOffScreen=kinds["off_screen"], ClaudeLeftover=kinds["leftover"],
                      ClaudeCrowded=kinds["crowded"], ClaudeUnreadable=kinds["unreadable_text"], ShiftsIn=shifts_in,
                      ShiftsRemoved=shifts_out, ShiftNotes=shift_notes,
                      ClaudeCost=f"{cost_in / 1e6 * 4 + cost_out / 1e6 * 20:.2f}")  # fmt: skip
    rows = []
    for t, a in adm.items():
        regen = ", ".join(a["regenerated"]) or "--"
        before = sum(s["rendered"] for s in a["before"].values())
        after = sum(s["rendered"] for s in a["after"].values())
        rows.append(f"{esc(t)} & {before}/4 & {regen} & {after}/4 & {'yes' if a['clean'] else 'no'} & "
                    f"{'in study' if a['complete'] else 'excluded'} \\\\")  # fmt: skip
    write("quality", "\\begin{table*}[!tbp]\\centering\\small\n\\caption{Admission of the NOVEL-12 base videos. Before: sections "
          "the pipeline rendered (a failing section used to be dropped silently). Retried: sections written again once, "
          "with the code check and layout rules. Clean: every section has layout (MVQS) at least 70 and no lasting "
          "conflict. A video enters the studies only if complete and approved by a person.}\\label{tab:quality}\n"
          "\\begin{tabular}{lrlrll}\\toprule Concept & Before & Retried & After & Clean & Status\\\\\\midrule\n"
          + "\n".join(rows) + "\n\\bottomrule\\end{tabular}\n\\end{table*}\n")  # fmt: skip


def noise_model(macros):
    """Numbers from bench/noise_model.py: repeat noise, and per comparison the mean, how many topics agree, and the
    smallest effect the design can detect (MDE). The tests themselves stay in the result file, as for the tables."""
    rep = load("noise-model/report.json")
    if not rep:
        return
    rn = rep["repeat_noise"]
    macros.update(NMRepeatMoved=rn["moved_over_0.01"], NMRepeatN=rn["questions"],
                  NMFloorOne=pts(rn["floor_one_topic_M9"], False), NMFloorAll=pts(rn["floor_mean_of_topics_M9"], False))  # fmt: skip
    keys = {"N1": "Gain", "N2": "Spec", "N3": "Dense", "N4": "FramesDense", "L1": "Layout", "P1": "Small",
            "N5": "Size", "N6": "Count", "H1": "HGain", "H2": "HSpec", "H3": "HLayout", "S1": "SGain", "S2": "SSpec",
            "S3": "SLayout", "N7": "Repair", "N8": "RepairGeneric"}  # fmt: skip
    for i, word in enumerate(("One", "Two", "Three", "Four", "Five"), 1):  # stages F1-F5 (bench/noise_model.py R1..R5g)
        keys[f"R{i}"], keys[f"R{i}g"] = f"Stage{word}", f"Stage{word}Generic"
    for name, row in (rep.get("students") or {}).items():
        for k, v in row.items():
            if v is not None:
                macros[f"Acc{name.capitalize()}{k.capitalize()}"] = f"{100 * v:.1f}"
    for m, c in (rep.get("claude_repeat") or {}).items():
        key = "H" if "haiku" in m else "S"
        macros[f"NM{key}RepChanged"], macros[f"NM{key}RepN"] = c["changed"], c["answers"]
    for c in rep["comparisons"]:
        k = keys.get(c["id"])
        if k is None or not c.get("n"):
            continue
        macros[f"NM{k}"], macros[f"NM{k}Pos"], macros[f"NM{k}N"] = pts(c["mean"]), c["positive"], c["n"]
        macros[f"NM{k}MDE"] = pts(c["mde"], False)
        if c.get("p_measurement") is not None:  # randomisation over questions; sign flip over topics
            macros[f"NM{k}P"], macros[f"NM{k}PTopics"] = f"{c['p_measurement']:.3f}", f"{c['p_topics']:.3f}"
        if c.get("rule_false_positive_rate") is not None:
            macros["NMRuleFPR"] = f"{100 * c['rule_false_positive_rate']:.1f}"


def layout_study(macros):
    """The three versions of the 10 admitted videos: layout, faults, what the student learns; and the pre-registered rule."""
    import statistics as stt

    rows = load("layout-study/rows.json")
    if not rows:
        write("layout_study", pending("Layout side study.", "tab:layout_study", "bench/results/layout-study"))
        return
    names = {"ours": "Ours (admitted)", "autofix": "Ours + timing fixes", "claude": "Claude-fixed (reference)"}
    body = []
    for v, label in names.items():
        rs = [r[v] for r in rows if v in r]
        if not rs:
            continue
        lay = [r["layout"] for r in rs]
        te = [r["teaching"] for r in rs]
        mean = lambda xs: stt.mean(xs) if xs else None
        m9 = mean([x["M9"] for x in te if x["M9"] is not None])
        m7 = mean([x["M7"] for x in te if x["M7"] is not None])
        att = [x.get("broken_attachments") for x in lay]
        body.append(f"{label} & {mean([x['mvqs_mean'] for x in lay]):.1f} & {sum(x['conflicts'] for x in lay)} & "
                    f"{sum(x['timing'] for x in lay)} & {'--' if None in att else sum(att)} & "
                    f"{100 * mean([x['frames'] for x in te]):.1f} & {100 * mean([x['visual'] for x in te]):.1f} & "
                    f"{pts(m9, False)} & {pts(m7, False)} \\\\")  # fmt: skip
        key = {"ours": "Ours", "autofix": "Auto", "claude": "Claude"}[v]
        macros[f"LS{key}MNine"], macros[f"LS{key}MSeven"] = pts(m9, False), pts(m7, False)
        macros[f"LS{key}Frames"] = f"{100 * mean([x['frames'] for x in te]):.1f}"
        macros[f"LS{key}Mvqs"] = f"{mean([x['mvqs_mean'] for x in lay]):.1f}"
        macros[f"LS{key}Conflicts"] = sum(x["conflicts"] for x in lay)
        if None not in att:
            macros[f"LS{key}Attach"] = sum(att)
    pairs = [(r["claude"]["teaching"]["M9"], r["ours"]["teaching"]["M9"]) for r in rows if "claude" in r and "ours" in r]
    defined = [(c, o) for c, o in pairs if c is not None and o is not None]
    if defined:
        diff = stt.mean(c - o for c, o in defined)
        wins = sum(c >= o for c, o in defined)
        need = -(-7 * len(defined) // 10)
        passed = diff >= 0.05 and wins >= need
        macros.update(LSDiff=pts(diff), LSWins=wins, LSN=len(defined), LSNeed=need,
                      LSLeftOut=len(pairs) - len(defined), LSGate="passed" if passed else "not passed")  # fmt: skip
        named = [(r["topic"], r["claude"]["teaching"]["M9"] - r["ours"]["teaching"]["M9"]) for r in rows
                 if "claude" in r and "ours" in r and None not in (r["claude"]["teaching"]["M9"], r["ours"]["teaching"]["M9"])]
        top = max(named, key=lambda x: abs(x[1]))  # the concept that moves the mean most
        rest = [d for t, d in named if t != top[0]]
        macros.update(LSTopTopic=esc(top[0]), LSTopDiff=pts(top[1]), LSDiffWithoutTop=pts(stt.mean(rest)) if rest else "--",
                      LSLosses=sum(d < 0 for _, d in named))  # fmt: skip
    write("layout_study", "\\begin{table*}[!tbp]\\centering\\small\n\\caption{Layout side study on the 10 admitted NOVEL-12 "
          "videos, three versions of each. Layout: mean MVQS over sections. Conflicts: lasting overlaps or off-screen "
          "objects (SGA). Timing: leftovers and merged words (our timing check). Attachments: labels, arrows or boxes "
          "detached from, or nearer another shape than, the object the code attached them to (our attachment check). "
          "Confidence: the student's probability on the right answer (\\%). Gain: share of what it did not know that it "
          "learned (M9: 3 frames per section; M7: dense video with the motion bonus).}\\label{tab:layout_study}\n"
          "\\begin{tabular}{lrrrrrrrr}\\toprule & \\multicolumn{4}{c}{Video quality} & \\multicolumn{2}{c}{Confidence} & "
          "\\multicolumn{2}{c}{Gain ($\\uparrow$)}\\\\\n\\cmidrule(lr){2-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\n"
          "Version & Layout ($\\uparrow$) & Conflicts ($\\downarrow$) & Timing ($\\downarrow$) & Attachments ($\\downarrow$) & "
          "3 frames & Dense & M9 & M7\\\\\\midrule\n" + "\n".join(body) + "\n\\bottomrule\\end{tabular}\n\\end{table*}\n")  # fmt: skip


def novel_unknown(macros):
    """NOVEL-12 TEST questions the untaught student does not know (mean confidence over option orders below 0.5)."""
    d = load("novel-prior-gemma4_26b.json")
    if not d:
        return
    unknown = total = 0
    for rots in d.values():
        ps = collections.defaultdict(list)
        for r in rots:
            for it in r["items"]:
                ps[it["id"]].append(0.25 if it["p_right"] is None else it["p_right"])
        total += len(ps)
        unknown += sum(sum(v) / len(v) < 0.5 for v in ps.values())
    macros["NovelUnknown"], macros["NovelItems"] = unknown, total


def novel_appendix():
    cards = json.loads((ROOT / "bench" / "novel" / "cards.json").read_text())
    qs = json.loads((ROOT / "bench" / "novel" / "questions.json").read_text())
    out = ["\\begin{description}"]
    for t, c in cards.items():
        q = qs[t][0]
        opts = "; ".join(f"{k}) {esc(v)}" for k, v in q["options"].items())
        out.append(f"\\item[{esc(t)}] {esc(c)}\\\\ \\emph{{Sample TEST item:}} {esc(q['question'])} {opts} "
                   f"(key {q['answer']}).")
    out.append("\\end{description}")
    write("novel_cards", "\n".join(out) + "\n")


FROZEN = OUT / "pilot_frozen.json"
PILOT_KEYS = ("AllRuns", "OrderRuns", "OrderShare", "NullWithVideo", "NullNoVideo", "NullWithVideoN", "AnsweredWithVideo",
              "AnsweredRight", "AnsweredWrong", "AnsweredRightShare", "PilotTies", "PilotLayoutBase", "PilotLayoutAll",
              "FirstTryFail", "PreflightFP", "PreflightN", "FailedAttempts", "SyntaxAfterPatch", "PilotRevisions",
              "PilotNotKept", "PilotGaps", "PilotDev", "PilotFlagged", "PilotSections", "PilotDevGain")  # fmt: skip


def freeze_pilot(macros, refreeze=False):
    """The MMMC pilot is finished: its numbers are saved once and every later build is checked against them, so a
    script that starts reading other runs (NOVEL-12, the F0-F5 stages) is caught. --refreeze accepts a change."""
    now = {k: str(v) for k, v in macros.items() if k in PILOT_KEYS or k.startswith(("LadMMMC", "LadSmall"))}
    if refreeze or not FROZEN.exists():
        FROZEN.write_text(json.dumps(now, indent=1, sort_keys=True))
        print(f"pilot numbers frozen in {FROZEN} ({len(now)} values)")
        return
    old = json.loads(FROZEN.read_text())
    changed = {k: (old.get(k), now.get(k)) for k in sorted(set(old) | set(now)) if old.get(k) != now.get(k)}
    if changed:
        print("WARNING: frozen MMMC pilot numbers changed (run with --refreeze only if the change is intended):")
        for k, (a, b) in changed.items():
            print(f"    {k}: {a} -> {b}")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    macros = {}
    pilot(macros)
    matching(macros)
    priors(macros)
    ladder("mmmc-n12-seed0", "ladder_mmmc", "Metric ladder on the MMMC pilot videos.", macros, "LadMMMC")
    ladder("novel12", "ladder_novel", "Metric ladder on NOVEL-12.", macros, "LadNovel")
    ladder("mmmc-n12-seed0", "ladder_small", "A smaller student (qwen2.5vl:3b) on the MMMC pilot videos, 3 frames per "
           "section only; measures it could not score are left out.", macros, "LadSmall",
           folder="mmmc-n12-seed0-ladder-qwen2_5vl_3b", only_defined=True)
    stages(macros)
    failures(macros)
    gate(macros)
    localisation(macros)
    novel_first_look()
    novel_items()
    novel_appendix()
    novel_unknown(macros)
    quality(macros)
    noise_model(macros)
    layout_study(macros)
    models()
    freeze_pilot(macros, refreeze="--refreeze" in sys.argv)
    lines = []
    for k, v in sorted(macros.items()):
        name = "".join(c for c in k if c.isalpha())
        lines.append(f"\\newcommand{{\\{name}}}{{{v}}}")
    write("numbers", "% generated by paper/make_tables.py; a missing macro means its result is pending\n" + "\n".join(lines) + "\n")
    print(f"{len(macros)} numbers, tables in {OUT}")


if __name__ == "__main__":
    main()
