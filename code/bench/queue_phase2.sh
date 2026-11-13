#!/bin/sh
# Phase 2 queue: wait for the F0 run on the invented concepts, then the ladder on it, then stages F1..F5 in order,
# then the paper's tables. Every step is cached, so the queue can be started again after a stop.
PY=/home/mani/manim/lessonforge/.venv/bin/python
cd "$(dirname "$0")/.."
while pgrep -f "python[^ ]* bench/run_bench.py --name novel12" > /dev/null; do sleep 60; done
[ -f bench/results/novel12/rows.json ] || { echo "novel12 F0 did not finish" >> bench/phase2.log; exit 1; }
$PY bench/metric_ladder.py bench/results/novel12 --workers 2 > bench/ladder_novel12.log 2>&1
$PY bench/mmmc_prior.py --questions bench/novel/questions.json --name novel --cards bench/novel/cards.json > bench/novel_card.log 2>&1
for s in F0 F1 F2 F3 F4 F5; do
  echo "$(date) stage $s" >> bench/phase2.log
  $PY bench/stages.py bench/results/novel12 --stage $s --workers 3 >> bench/phase2.log 2>&1
done
$PY paper/make_tables.py >> bench/phase2.log 2>&1
echo PHASE2_DONE >> bench/phase2.log
