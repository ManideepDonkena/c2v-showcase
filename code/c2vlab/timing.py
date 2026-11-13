"""Wall time of the pipeline's subprocesses (Manim renders, scene-graph runs): one JSON line each in
runs/ledger_render.jsonl, so the video-making step can be broken down like the model calls in runs/ledger_*.jsonl.
Logging never interrupts the pipeline."""

from __future__ import annotations

import json
import os
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "runs" / "ledger_render.jsonl"
_LOCK = threading.Lock()


def log(kind, path, cls, seconds, ok):
    """kind: "render" or "scene_graph"; path: the section's code file; ok: rendered / graph recorded."""
    try:
        from . import llm

        tag = getattr(getattr(llm, "CONTEXT", None), "tag", "")
        path = Path(path).resolve()
        rel = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
        row = {"t": round(time.time()), "kind": kind, "study": os.getenv("C2V_STUDY", ""), "tag": tag, "file": rel,
               "cls": cls, "s": round(seconds, 1), "ok": bool(ok)}  # fmt: skip
        with _LOCK, LEDGER.open("a") as f:
            f.write(json.dumps(row) + "\n")
    except Exception:  # noqa: BLE001, S110 - timing is a side record; a failure here must not stop a render
        pass
