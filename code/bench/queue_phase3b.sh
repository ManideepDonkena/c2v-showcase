#!/bin/sh
# Phase 3, parallel tail: waits for the running F0 (run_bench on the 10 admitted concepts), then runs the ladder and
# two independent chains of stages at once: F0 -> F1 -> F2 and F3 -> F4 -> F5 (F4 and F5 share F3's diagnosis files,
# so they stay in one chain). The stages compute both M9 and M7, so they do not wait for the ladder.
PY=/home/mani/manim/lessonforge/.venv/bin/python
cd "$(dirname "$0")/.."
while pgrep -f "python[^ ]* bench/run_bench.py --name novel12" > /dev/null; do sleep 60; done
grep -q "topics ->" bench/novel12_admitted.log || { echo "$(date) F0 did not finish" >> bench/phase3.log; exit 1; }
echo "$(date) F0 done; ladder and stages start" >> bench/phase3.log
$PY bench/metric_ladder.py bench/results/novel12 --workers 2 > bench/ladder_novel12.log 2>&1 &
( for s in F0 F1 F2; do echo "$(date) stage $s" >> bench/phase3.log
    $PY bench/stages.py bench/results/novel12 --stage $s --workers 3 >> bench/stages_a.log 2>&1; done ) &
( for s in F3 F4 F5; do echo "$(date) stage $s" >> bench/phase3.log
    $PY bench/stages.py bench/results/novel12 --stage $s --workers 3 >> bench/stages_b.log 2>&1; done ) &
wait
$PY bench/stages.py bench/results/novel12 --report >> bench/phase3.log 2>&1
$PY paper/make_tables.py >> bench/phase3.log 2>&1
echo "$(date) PHASE3_DONE" >> bench/phase3.log
