"""Tables for the paper from a benchmark run: per condition means, and paired differences with a bootstrap 95% CI,
a Wilcoxon signed-rank p (when scipy is installed) and wins/ties/losses over topics.

    python bench/analyze.py bench/results/<name>
"""

from __future__ import annotations

import json
import random
import statistics as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONDITIONS = ("base", "learner", "generic", "learner_all")
METRICS = ("teachquiz", "teachquiz_clean", "evidence", "full", "mvqs", "sections_rendered")
PAIRS = (("learner", "base"), ("learner", "generic"), ("learner", "learner_all"), ("generic", "base"))


def c2v_gain(topic_dir, condition, kind):
    """Code2Video-protocol gain for one video, from the API run (kind 'api') or the chat-app run ('manual')."""
    if kind == "api":
        d = topic_dir if condition == "base" else topic_dir / condition
        p = d / "eval_c2v.json"
        return json.loads(p.read_text())["gain"] if p.exists() else None
    p = topic_dir / "eval_c2v_manual.json"
    return ((json.loads(p.read_text())["videos"].get(condition) or {}).get("gain")) if p.exists() else None


def paired(a, b, iters=10000):
    pairs = [(x, y) for x, y in zip(a, b, strict=True) if x is not None and y is not None]
    if len(pairs) < 2:
        return None
    d = [x - y for x, y in pairs]
    rng = random.Random(0)
    boots = sorted(st.mean(rng.choices(d, k=len(d))) for _ in range(iters))
    out = {"n": len(d), "mean_diff": round(st.mean(d), 4), "ci95": [round(boots[int(0.025 * iters)], 4),
           round(boots[int(0.975 * iters)], 4)], "wins": sum(x > 0 for x in d), "ties": sum(x == 0 for x in d),
           "losses": sum(x < 0 for x in d)}  # fmt: skip
    try:
        from scipy.stats import wilcoxon

        out["wilcoxon_p"] = round(float(wilcoxon(d).pvalue), 4) if any(d) else 1.0
    except (ImportError, ValueError):
        pass
    return out


def main():
    run = Path(sys.argv[1])
    rows = [r for r in json.loads((run / "rows.json").read_text()) if "error" not in r]
    from c2vlab.generate import slug

    for r in rows:
        d = ROOT / "runs" / slug(r["topic"])
        for c in CONDITIONS:
            if c in r:
                r[c]["c2v_api"] = c2v_gain(d, c, "api")
                r[c]["c2v_manual"] = c2v_gain(d, c, "manual")
    metrics = (*METRICS, "c2v_api", "c2v_manual", "control_first_section", "control_other_topic")
    table = {c: {} for c in CONDITIONS}
    for c in CONDITIONS:
        for m in metrics:
            vals = [r[c].get(m) for r in rows if c in r and r[c].get(m) is not None]
            table[c][m] = round(st.mean(vals), 2) if vals else None
    tests = {
        f"{a} - {b}": {m: paired([r.get(a, {}).get(m) for r in rows], [r.get(b, {}).get(m) for r in rows])
                       for m in ("teachquiz", "teachquiz_clean", "evidence", "mvqs", "c2v_api", "c2v_manual")}
        for a, b in PAIRS
    }  # fmt: skip
    changed = {c: sum(bool(r.get(c, {}).get("changed")) for r in rows) for c in CONDITIONS[1:]}
    report = {"topics": len(rows), "failed_topics": sum("error" in r for r in json.loads((run / "rows.json").read_text())),
              "means": table, "paired": tests, "topics_where_mode_changed_the_video": changed}  # fmt: skip
    (run / "analysis.json").write_text(json.dumps(report, indent=1))
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT))
    main()
