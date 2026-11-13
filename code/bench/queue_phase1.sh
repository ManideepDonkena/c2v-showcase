#!/bin/sh
# Phase 1 queue: metric ladder on the pilot videos, then MMMC's prior for two students.
PY=/home/mani/manim/lessonforge/.venv/bin/python
cd "$(dirname "$0")/.."
$PY bench/metric_ladder.py bench/results/mmmc-n12-seed0 --workers 2 > bench/ladder_pilot.log 2>&1
$PY bench/mmmc_prior.py > bench/prior_gemma.log 2>&1
$PY bench/mmmc_prior.py --student qwen2.5vl:7b > bench/prior_qwen.log 2>&1
echo PHASE1_DONE >> bench/ladder_pilot.log
