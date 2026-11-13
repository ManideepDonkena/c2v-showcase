"""Do our layout repair's shifts cause the broken attachments? For each admitted NOVEL-12 base section, the attachment
check (c2vlab/attach.broken) on the code as rendered and on the same code with every inserted shift removed (lines
marked "# layout: separation vector").

    python bench/shift_attach.py   -> bench/results/shift-attach/report.json
"""

import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from c2vlab import attach, generate, layout

MARK = "# layout: separation vector"


def main():
    topics = json.loads((ROOT / "bench/results/novel12/topics.json").read_text())
    rows = []
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for t in topics:
            run = ROOT / "runs" / generate.slug(t)
            for s in json.loads((run / "sections.json").read_text()):
                sid, code = s["id"], (run / "sections" / f"{s['id']}.py").read_text()
                row = {"topic": t, "section": sid, "shifts": code.count(MARK)}
                for kind, src in (("with", code), ("without", "".join(ln for ln in code.splitlines(keepends=True)
                                                                       if MARK not in ln))):  # fmt: skip
                    p = tmp / f"{run.name}_{sid}_{kind}.py"
                    p.write_text(src)
                    g, m, _ = layout.measure(p, sid.upper(), tmp / f"{run.name}_{sid}_{kind}.json")
                    row[kind] = {"broken": len(attach.broken(src, g)), "mvqs": round(m, 1), "error": bool(g.get("error"))}
                rows.append(row)
                print(t, sid, row, flush=True)
    tot = {k: sum(r[k]["broken"] for r in rows) for k in ("with", "without")}
    rep = {"sections": len(rows), "shifts": sum(r["shifts"] for r in rows), "broken_with_shifts": tot["with"],
           "broken_without_shifts": tot["without"],
           "sections_that_differ": [r for r in rows if r["with"]["broken"] != r["without"]["broken"]], "rows": rows}
    out = ROOT / "bench/results/shift-attach"
    out.mkdir(parents=True, exist_ok=True)
    (out / "report.json").write_text(json.dumps(rep, indent=1, ensure_ascii=False))
    print({k: v for k, v in rep.items() if k != "rows"})


if __name__ == "__main__":
    main()
