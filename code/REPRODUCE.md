# Reproducing the paper

This folder is the research repository at commit `8a6bb7f`. It contains the code, the benchmark, every result file
the tables are built from, and the per-video caches (`runs/`) without the rendered media.

## 1. Rebuild the tables and numbers (no models needed)

```bash
pip install manim numpy scipy pillow     # manim >= 0.19; also ffmpeg
python paper/make_tables.py              # writes paper/tables/*.tex and numbers.tex from bench/results and runs/
```

Every number in the paper comes from this script. The saved student answers are in `runs/<concept>/dv_*_test.json`,
and the summaries are in `bench/results/`.

## 2. Re-run the studies (local models)

Every model except Claude runs locally through Ollama. These are the exact builds used:

| Role | Model | Ollama digest |
|---|---|---|
| Planner | `qwen3.6:latest` | `07d35212591f` |
| Coder | `qwen3-coder:30b` | `06c1097efce0` |
| Student | `gemma4:26b` | `5571076f3d70` |
| Evidence judge | `qwen2.5vl:7b` | `5ced39dfa4ba` |
| Smaller student | `qwen2.5vl:3b` | `fb90415cde1e` |

The registry no longer serves this `gemma4:26b` build: a pull today gives digest `001e5dafc3c7`. A newer build is a
different measuring instrument. Use one build for every quiz in a comparison, and do not compare its numbers directly
with ours. Claude models (`claude-opus-5-5` for the layout fixes; Haiku 5.5 and Sonnet 5.5 as extra students) need
`ANTHROPIC_API_KEY`.

```bash
PY=python                                                                # manim >= 0.19, numpy, scipy, ffmpeg, Ollama
$PY bench/run_bench.py --n 12 --seed 0 --workers 3                       # MMMC pilot (F0)
$PY bench/metric_ladder.py bench/results/mmmc-n12-seed0                  # metric ladder on MMMC
$PY bench/mmmc_prior.py [--student qwen2.5vl:7b]                         # what the student already knows (MMMC)
$PY bench/novel/build.py                                                 # NOVEL-12 cards and questions
$PY bench/run_bench.py --name novel12 --n 10 --questions bench/novel/questions_admitted.json \
    --cards bench/novel/cards.json                                       # NOVEL-12 base videos (F0)
$PY bench/metric_ladder.py bench/results/novel12                         # metric ladder on NOVEL-12
$PY bench/stages.py bench/results/novel12 --stage F1   # ... to F5       # the repair stages
$PY bench/noise_model.py                                                 # noise model: which differences are real
$PY bench/layout_study.py                                                # layout study (ours, autofix, Claude-fixed)
$PY bench/shift_attach.py                                                # do the layout repair's shifts break attachments?
$PY paper/make_tables.py                                                 # every table and number
```

`bench/queue_phase*.sh` are the queues that ran these steps in order. Each step caches its output in `runs/<concept>/`
and can be restarted. With the caches included here, re-running a step re-uses the saved answers. Delete a concept's
`dv_*.json` files to ask the student again.

## 3. Known differences

- The lasting-conflict counts in the paper's tables were measured before a tracker fix. With the fix (commit
  `937336d`, included here), `bench/layout_study.py` gives 27 for our videos, 27 with timing fixes and 4 for the
  Claude-fixed versions, instead of 31, 29 and 4. MVQS, the attachment counts and the conclusions are unchanged.
- The student is not fully repeatable at temperature 0. Repeated questions move the confidence a little;
  `bench/results/noise-repeats/` and the noise model measure how much.
