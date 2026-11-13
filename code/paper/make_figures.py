"""Every data figure of the reports, drawn from the result files (like make_tables.py, never from typed numbers).
A figure whose data does not exist yet is skipped; the report shows a "pending" box in its place.

    python paper/make_figures.py   ->  paper/figures/*.pdf
Palette: the dataviz reference light palette (validated: CVD and normal-vision separation pass; aqua and yellow are
below 3:1 on white, so every mark of those colours also carries a direct label or a distinct marker shape).
"""

from __future__ import annotations

import json
import statistics as st
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "paper"))  # make_tables.pilot_dirs
RES = ROOT / "bench" / "results"
OUT = ROOT / "paper" / "figures"

INK, INK2, MUTED, GRID = "#0b0b0b", "#52514e", "#8a8984", "#e4e3df"
BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
NEUTRAL = "#b9b8b2"
COND = {"base": BLUE, "learner": ORANGE, "generic": AQUA, "learner_all": YELLOW}
MARK = {"base": "o", "learner": "D", "generic": "s", "learner_all": "^"}

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": MUTED, "axes.labelcolor": INK2,
    "xtick.color": INK2, "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True, "legend.frameon": False,
    "figure.dpi": 150, "savefig.bbox": "tight", "lines.linewidth": 2,
})  # fmt: skip


def load(path):
    p = RES / path
    return json.loads(p.read_text()) if p.exists() else None


def save(fig, name):
    fig.savefig(OUT / f"{name}.pdf")
    plt.close(fig)
    print("figure", name)


def refusal():
    """What the student's answers are: TeachQuiz without / with the video, and forced choice without the video."""
    from make_tables import pilot_dirs  # the pilot's 12 topics x 4 conditions only, never a wildcard over runs/

    counts = {"TeachQuiz, no video": [0, 0, 0], "TeachQuiz, with video": [0, 0, 0]}
    for f in [d / "eval_test.tq2.json" for d in pilot_dirs() if (d / "eval_test.tq2.json").exists()]:
        e = json.loads(f.read_text())
        for key, label in (("none", "TeachQuiz, no video"), ("full", "TeachQuiz, with video")):
            for r in e["runs"][key]:
                for a in r["answers"]:
                    counts[label][0 if a["choice"] == "NULL" else 1 if not a["right"] else 2] += 1
    prior = load("mmmc-prior-gemma4_26b.json")
    if prior:
        c = [0, 0, 0]
        for rots in prior.values():
            for it in rots[0]["items"]:
                c[0 if it["choice"] is None else 1 if not it["right"] else 2] += 1
        counts["Forced choice, no video\n(all 117 MMMC topics)"] = c
    if not sum(counts["TeachQuiz, no video"]):
        return
    fig, ax = plt.subplots(figsize=(6.4, 2.1))
    labels = list(counts)[::-1]
    left = [0.0] * len(labels)
    parts = (("NULL (refused)", NEUTRAL), ("wrong", ORANGE), ("right", BLUE))
    for j, (name, color) in enumerate(parts):
        vals = [100 * counts[k][j] / max(1, sum(counts[k])) for k in labels]
        ax.barh(labels, vals, left=left, color=color, height=0.55, edgecolor="white", linewidth=2, label=name)
        for i, v in enumerate(vals):
            if v >= 7:
                ax.text(left[i] + v / 2, i, f"{v:.0f}%", ha="center", va="center", fontsize=8,
                        color="white" if color != NEUTRAL else INK)  # fmt: skip
        left = [a + b for a, b in zip(left, vals, strict=True)]
    ax.set_xlim(0, 100)
    ax.set_xlabel("share of answers (%)")
    ax.grid(axis="y", visible=False)
    ax.legend(ncol=3, loc="lower center", bbox_to_anchor=(0.45, 1.0), fontsize=8)
    save(fig, "refusal")


def priors():
    """Per question: the probability the untaught student puts on the right answer, MMMC against NOVEL-12."""
    sets = [("mmmc-prior-gemma4_26b.json", "MMMC, no video", BLUE),
            ("novel-prior-gemma4_26b.json", "NOVEL-12, no video", ORANGE),
            ("novel-card-gemma4_26b.json", "NOVEL-12, card as text", AQUA)]  # fmt: skip
    have = [(load(f), label, c) for f, label, c in sets if load(f)]
    if not have:
        return
    fig, axes = plt.subplots(1, len(have), figsize=(2.2 * len(have) + 0.4, 2.2), sharey=True)
    axes = axes if len(have) > 1 else [axes]
    bins = [i / 10 for i in range(11)]
    for ax, (d, label, color) in zip(axes, have, strict=True):
        p = []
        for rots in d.values():
            for i in range(len(rots[0]["items"])):
                vals = [r["items"][i]["p_right"] for r in rots]
                p.append(st.mean(0.25 if v is None else v for v in vals))
        w = [100 / len(p)] * len(p)
        ax.hist(p, bins=bins, weights=w, color=color, edgecolor="white", linewidth=1.5)
        ax.axvline(0.25, color=INK2, linestyle=":", linewidth=1)
        ax.set_title(f"{label}\nmean {st.mean(p):.2f}, {len(p)} questions", fontsize=8.5, color=INK)
        ax.set_xlabel("P(right answer)")
        ax.grid(axis="x", visible=False)
    axes[0].set_ylabel("share of questions (%)")
    axes[0].text(0.27, axes[0].get_ylim()[1] * 0.9, "chance", fontsize=7.5, color=INK2)
    save(fig, "priors")


def pilot():
    """The pilot's TeachQuiz per topic and condition: most points sit at 0 (ties carry no information)."""
    rows = load("mmmc-n12-seed0/rows.json")
    if not rows:
        return
    rows = [r for r in rows if "error" not in r]
    fig, ax = plt.subplots(figsize=(6.4, 2.6))
    for j, c in enumerate(COND):
        xs = [i + (j - 1.5) * 0.16 for i in range(len(rows))]
        ax.scatter(xs, [r[c]["teachquiz"] for r in rows], s=26, color=COND[c], marker=MARK[c], label=c,
                   edgecolor="white", linewidth=0.8, zorder=3)  # fmt: skip
    ax.set_xticks(range(len(rows)))
    ax.set_xticklabels([r["topic"][:18] + ("…" if len(r["topic"]) > 18 else "") for r in rows], rotation=40,
                       ha="right", fontsize=7)  # fmt: skip
    ax.set_ylabel("TeachQuiz (points)")
    ax.axhline(0, color=MUTED, linewidth=0.8)
    ax.grid(axis="x", visible=False)
    ax.legend(ncol=4, loc="lower center", bbox_to_anchor=(0.5, 1.0), fontsize=8, handletextpad=0.2)
    save(fig, "pilot")


def failures():
    import make_tables

    cls = make_tables.failure_classes()
    if not cls:
        return
    items = [(k.strip(), v) for k, v in cls.most_common() if not k.startswith(" ")]
    sub = cls.get("  of which right after a patch", 0)
    fig, ax = plt.subplots(figsize=(5.2, 2.3))
    names = [k for k, _ in items][::-1]
    vals = [v for _, v in items][::-1]
    ax.barh(names, vals, color=BLUE, height=0.6, edgecolor="white")
    for i, v in enumerate(vals):
        ax.text(v + 1, i, str(v), va="center", fontsize=8, color=INK)
    if sub and "syntax / indentation" in names:
        i = names.index("syntax / indentation")
        ax.barh(i, sub, color=ORANGE, height=0.6, edgecolor="white")
        ax.text(sub / 2, i, f"{sub} made by our own patch", va="center", ha="center", fontsize=7, color="white")
    ax.set_xlabel("failed render attempts (pilot)")
    ax.grid(axis="y", visible=False)
    save(fig, "failures")


def ladder(name, out):
    """Each rung: own video minus another topic's video (mean, points), and the share of videos it scores."""
    r = load(f"{name}-ladder/report.json")
    if not r:
        return
    rungs = list(r["rungs"])
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.6, 2.6), gridspec_kw={"width_ratios": [1.6, 1]})
    for i, m in enumerate(rungs):
        sep = r["rungs"][m]["separation_own_minus_other"]
        if sep:
            v = 100 * sep["mean_diff"]
            a1.barh(i, v, color=BLUE if v > 0 else ORANGE, height=0.6, edgecolor="white")
            a1.text(v + (1 if v >= 0 else -1), i, f"{v:+.1f}", va="center", ha="left" if v >= 0 else "right",
                    fontsize=7.5, color=INK)  # fmt: skip
        else:
            a1.text(0.5, i, "not defined", fontsize=7.5, color=INK2, va="center", ha="left")
        d, n = (int(x) for x in r["rungs"][m]["defined"].split("/"))
        a2.barh(i, 100 * d / max(1, n), color=BLUE, height=0.6, edgecolor="white")
        a2.text(100 * d / max(1, n) + 2, i, f"{d}/{n}", va="center", fontsize=7.5, color=INK)
    for a in (a1, a2):
        a.set_yticks(range(len(rungs)))
        a.set_yticklabels(rungs)
        a.invert_yaxis()
        a.grid(axis="y", visible=False)
    a1.axvline(0, color=INK2, linewidth=0.8)
    lo, hi = a1.get_xlim()
    a1.set_xlim(min(lo, -5), hi + 6)
    a1.set_xlabel("own video − other topic's video (points)")
    a2.set_xlim(0, 118)
    a2.set_xlabel("videos that get a score (%)")
    a2.set_yticklabels([])
    save(fig, out)


def novel_first():
    """Each NOVEL-12 concept measured so far: P(right) with no video, start/end frames, and the silent video."""
    from c2vlab import dvgain, generate

    qs = json.loads((ROOT / "bench" / "novel" / "questions.json").read_text())
    rows = []
    for t in qs:
        d = ROOT / "runs" / generate.slug(t)
        files = {k: d / f"dv_{k}_test.json" for k in ("blind", "frames", "static", "visual")}
        if all(f.exists() for f in files.values()):
            p = {k: dvgain.score(json.loads(f.read_text()), True, (0, 1)) for k, f in files.items()}
            rows.append((t, p))
    if not rows:
        return
    fig, ax = plt.subplots(figsize=(5.6, max(1.8, 0.45 * len(rows) + 1.1)))
    for i, (_, p) in enumerate(rows):
        ax.plot([100 * min(p.values()), 100 * max(p.values())], [i, i], color=GRID, linewidth=3, zorder=1)
        names = {"blind": "no video", "frames": "3 frames/section", "static": "start/end frames",
                 "visual": "dense silent video"}  # fmt: skip
        for k, c, m in (("blind", BLUE, "o"), ("frames", ORANGE, "D"), ("static", AQUA, "s"), ("visual", YELLOW, "^")):
            ax.scatter([100 * p[k]], [i], color=c, marker=m, s=40, zorder=3, edgecolor="white", linewidth=0.8,
                       label=names[k] if i == 0 else None)  # fmt: skip
    ax.axvline(25, color=INK2, linestyle=":", linewidth=1)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([t for t, _ in rows])
    ax.invert_yaxis()
    ax.set_xlim(0, 102)
    ax.set_xlabel("confidence in the right answer (%), 8 TEST questions")
    ax.grid(axis="y", visible=False)
    ax.legend(ncol=4, loc="lower center", bbox_to_anchor=(0.4, 1.0), fontsize=7.5, handletextpad=0.2)
    save(fig, "novel_first")


def stages():
    r = load("novel12-stages/report.json")
    if not r:
        return
    for metric in ("m7", "m9"):
        if all(metric in x for x in r.values()):
            stage_chart(r, metric)


def stage_chart(r, metric):
    """Learner against base, generic and every-section at each stage: mean difference in points."""
    fig, ax = plt.subplots(figsize=(5.6, 2.4))
    pairs = (("learner - base", "learner − base", BLUE), ("learner - generic", "learner − generic", ORANGE),
             ("learner - learner_all", "learner − every section", AQUA))  # fmt: skip
    names = list(r)
    for j, (pair, label, c) in enumerate(pairs):
        xs, vs = [], []
        for i, s in enumerate(names):
            p = r[s][metric].get(pair)
            if p:
                xs.append(i + (j - 1) * 0.26)
                vs.append(100 * p["mean_diff"])
        ax.bar(xs, vs, width=0.24, color=c, edgecolor="white", label=label)
    ax.axhline(0, color=INK2, linewidth=0.8)
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names)
    ax.set_ylabel(f"mean difference\n({metric.upper()}, points)")
    ax.grid(axis="x", visible=False)
    ax.legend(ncol=3, loc="lower center", bbox_to_anchor=(0.5, 1.0), fontsize=8, handletextpad=0.3)
    save(fig, f"stages_{metric}")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0, str(ROOT / "paper"))
    refusal()
    priors()
    pilot()
    failures()
    ladder("mmmc-n12-seed0", "ladder_mmmc")
    ladder("novel12", "ladder_novel")
    novel_first()
    stages()


if __name__ == "__main__":
    main()
