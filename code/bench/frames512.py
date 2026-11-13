"""Frame size or frame count? The gemma probe on 3 frames per section at 512 px, the dense video's width.

N4 found that 3 frames per section (768 px wide) teach more than the dense silent video (up to 4 frames a second, 512
px wide). Size and count change together there. This pass keeps the 3 frames per section, their timestamps, labels
and the 2 option orders, and only shrinks them to 512 px:
    768 ~ 512   -> size does not matter, so the count (or the moments chosen) does
    512 ~ dense -> the advantage of 3 frames came from their size
Cached as dv_f512_frames_test.json in each base video's folder; bench/noise_model.py compares it (N5, N6).

    python bench/frames512.py [--workers 2]
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from c2vlab import dvgain, generate, teachquiz

WIDTH = 512


def frames(run_dir):
    sections = json.loads((run_dir / "sections.json").read_text())
    folder = teachquiz.frames_dir(run_dir) / f"f{WIDTH}"
    folder.mkdir(parents=True, exist_ok=True)
    out = []
    for s in sections:
        for share in teachquiz.SHARES:
            t = s["start"] + share * (s["end"] - s["start"])
            path = folder / f"{s['id']}_{int(share * 100)}.jpg"
            if not path.exists():
                subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{t:.2f}", "-i", str(run_dir / "video.mp4"),
                                "-frames:v", "1", "-vf", f"scale={WIDTH}:-2", "-q:v", "4", str(path)], check=True)  # fmt: skip
            out.append(path)
    return out


def one(run_dir):
    path = run_dir / f"dv_f{WIDTH}_frames_test.json"
    if path.exists():
        return json.loads(path.read_text())
    plan = json.loads((run_dir / "plan.json").read_text())
    qs = json.loads((run_dir / "quiz.json").read_text())["test"]
    images = frames(run_dir)
    body = teachquiz.material(run_dir)[1]  # the same labels ("image k at mm:ss") as the 768 px pass
    out = {"kind": "frames", "width": WIDTH, "frames": len(images),
           "rotations": [dvgain.probe(plan["topic"], qs, images, body, r) for r in dvgain.ROTATIONS]}  # fmt: skip
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=2)
    args = ap.parse_args()
    topics = json.loads((ROOT / "bench" / "results" / "novel12" / "topics.json").read_text())
    dirs = [ROOT / "runs" / generate.slug(t) for t in topics]
    with cf.ThreadPoolExecutor(args.workers) as pool:
        for d, r in zip(dirs, pool.map(one, dirs)):
            print(f"[f512] {d.name[:30]:30s} P(right) {dvgain.score(r, True, (0, 1)):.3f}", flush=True)


if __name__ == "__main__":
    main()
