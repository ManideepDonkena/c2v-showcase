#!/bin/sh
# Phase 3, after admission (approved set: bench/admission/approved.json): F0 on the 10 admitted NOVEL-12 concepts,
# the ladder on them, the pipeline stages F0..F5, then the paper's tables. Every step is cached and can be restarted.
PY=/home/mani/manim/lessonforge/.venv/bin/python
cd "$(dirname "$0")/.."
# Freeze the paper as it was before phase 3 rewrites paper/tables: PDFs, sources, generated tables and figures, and
# the result folders this queue overwrites. Rebuild it with pdflatex inside before_phase3/paper (not build.sh,
# which regenerates the tables from the current results). Done once; a restart keeps the first snapshot.
if [ ! -d before_phase3 ]; then
  mkdir -p before_phase3/results
  rsync -a --exclude dist --exclude __pycache__ --exclude '*.aux' --exclude '*.log' --exclude '*.out' \
        --exclude '*.toc' --exclude '*.blg' paper/ before_phase3/paper/
  cp paper/main.pdf paper/report.pdf paper/long_report.pdf before_phase3/
  for r in novel12 novel12-ladder layout-study; do
    [ -d bench/results/$r ] && cp -r bench/results/$r before_phase3/results/
  done
  echo "$(date) froze the paper in before_phase3/" >> bench/phase3.log
fi
$PY bench/run_bench.py --name novel12 --n 10 --workers 3 --questions bench/novel/questions_admitted.json \
    --cards bench/novel/cards.json > bench/novel12_admitted.log 2>&1 || { echo "F0 failed" >> bench/phase3.log; exit 1; }
echo "$(date) ladder" >> bench/phase3.log
$PY bench/metric_ladder.py bench/results/novel12 --workers 2 > bench/ladder_novel12.log 2>&1
for s in F0 F1 F2 F3 F4 F5; do
  echo "$(date) stage $s" >> bench/phase3.log
  $PY bench/stages.py bench/results/novel12 --stage $s --workers 3 >> bench/phase3.log 2>&1
done
$PY paper/make_tables.py >> bench/phase3.log 2>&1
echo PHASE3_DONE >> bench/phase3.log
