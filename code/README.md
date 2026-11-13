# c2v-lab

A small research codebase: code-generated teaching videos (Code2Video's pipeline), layout checked without rendering
(SGA), and the idea under test, **learner-feedback repair**. An unlearned student's failures on a development quiz
are traced to the section that should have taught them, and only that section is rewritten. The result is scored on
held-out questions written by other people (MMMC's official TeachQuiz).

No frontend, no server. The core is `c2vlab/` (about 1,600 lines); the benchmark is `bench/`; everything else is in
`docs/`.

## Run

Any Python with `manim` (≥0.19), `numpy` and `scipy`, plus `ffmpeg` and Ollama with the local models
(`docs/models.md`). On this box: `PY=/home/mani/manim/lessonforge/.venv/bin/python`.

```bash
$PY bench/run_bench.py --n 12 --seed 0 --workers 3     # pilot on 12 MMMC topics, all local, free
$PY bench/analyze.py bench/results/mmmc-n12-seed0      # paired differences, bootstrap CI, Wilcoxon
$PY run.py topic "Pythagoras theorem"                  # one topic, every condition
$PY run.py manual-export runs/<slug>                   # Code2Video's evaluation by hand in Gemini (free)
$PY run.py estimate runs/<slug> --topics 12            # its cost through the API, before spending
```

## Code

| File | What it is |
|---|---|
| `c2vlab/llm.py` | `ask()` for Ollama or OpenRouter (`or:` prefix); JSON replies, video input, a ledger and a cap |
| `c2vlab/generate.py` | plan, code per section, render, render repair (line → block → section) |
| `c2vlab/scene_graph.py` | SGA's partial execution: objects with box, name and line after every play, no rendering |
| `c2vlab/mvqs.py` | MVQS, conflicts, minimum separation vectors |
| `c2vlab/layout.py` | layout repair: shift (code) → block → section; kept only if MVQS rises |
| `c2vlab/teachquiz.py` | DEV quiz, item filter, unlearned student, evidence check, controls |
| `c2vlab/feedback.py` | diagnosis, and the learner / generic / learner_all revisions |
| `c2vlab/c2v_eval.py` | Code2Video's TeachQuiz exactly (their prompts and grading, whole video to Gemini) and its cost |
| `c2vlab/manual.py` | the same evaluation through a chat app: blinded export, graded import |
| `c2vlab/pipeline.py` | one topic end to end, resumable |
| `bench/` | MMMC questions (MIT, from Code2Video), the benchmark runner, the analysis |
| `extras/lessonforge_baseline/` | the earlier study that scored finished lessonforge lessons |

## Docs

- `docs/method.md`: the pipeline, and what comes from Code2Video, from SGA and from us
- `docs/related_work.md`: the novelty check, part by part
- `docs/benchmark.md`: how prior work benchmarks; our protocol, conditions, statistics and threats to validity
- `docs/evaluation_by_hand.md`: Code2Video's evaluation in a chat app, step by step, and API costs
- `docs/models.md`: models in Code2Video, in SGA and here; OpenRouter ids and prices
- `docs/results.md`: results so far, and what the first runs taught
- `docs/open_problems.md`: what breaks, measured on the pilot, with the names of the same problems in other fields
- `paper/`: the paper (`main.tex`) and the technical report (`report.tex`); every number comes from
  `paper/make_tables.py`; `paper/build.sh` rebuilds both PDFs

## Studies after the pilot

| Script | What it does |
|---|---|
| `bench/metric_ladder.py <run>` | TeachQuiz improved one change at a time (M0-M8), each rung judged by the same four tests |
| `bench/mmmc_prior.py` | what a student answers with no video (forced choice), on MMMC or NOVEL-12 |
| `bench/novel/build.py` | NOVEL-12: 12 invented concepts, their cards, 96 TEST items with computed keys |
| `bench/stages.py <run> --stage F0..F5` | the pipeline ablation: gate, pre-flight, spectrum-based localisation, leak gate, minimal edits |
| `bench/queue_phase1.sh`, `bench/queue_phase2.sh` | the order the studies run in |
