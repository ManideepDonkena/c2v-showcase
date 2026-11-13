# Results

## Pilot on MMMC (2026-11-12): no signal, and why

> **Superseded measurement.** These TEST numbers were graded before the answer-matching fix: in 42% of student runs
> the student copied the template's ids and all its answers were scored NULL (DEV was unaffected). The corrected
> TeachQuiz (M1), D-VGAIN and the rest of the metric ladder are in `bench/results/mmmc-n12-seed0-ladder/` and in
> the paper (`paper/`, built by `paper/build.sh`).

12 topics (`bench/run_bench.py --n 12 --seed 0`), all models local, 4 planned sections each. TEST = MMMC's 5
official questions per topic, 3 student runs (`gemma4:26b` on 3 frames per section). Analysis:
`bench/results/mmmc-n12-seed0/analysis.json`. No leaked TEST items in any topic, so `teachquiz_clean` equals
`teachquiz`.

| Condition | TeachQuiz | Evidence-backed | MVQS | Sections rendered (of 4) |
|---|---|---|---|---|
| base | 10.6 | 7.8 | 78.5 | 3.25 |
| learner (ours) | 12.2 | 8.9 | 79.3 | 3.67 |
| generic (same number of sections) | 14.4 | 6.7 | 79.2 | 3.58 |
| learner_all (every section) | 16.7 | 11.1 | 72.6 | 3.50 |

Paired over topics (mean difference, bootstrap 95% CI, wins / ties / losses, Wilcoxon p):

| Comparison | TeachQuiz | Evidence | MVQS |
|---|---|---|---|
| learner − base | +1.7 [−1.7, 5.5], 3/7/2, p 0.50 | +1.1 [−1.1, 3.9], 2/9/1 | +0.7 [−2.1, 4.0] |
| learner − generic | −2.2 [−10.6, 6.1], 1/9/2, p 1.0 | +2.2 [−3.9, 9.4], 2/9/1 | 0.0 [−3.1, 3.2] |
| learner − learner_all | −4.5 [−11.1, 0.6], 1/8/3, p 0.25 | −2.2 [−9.4, 3.9], 1/9/2 | **+6.7 [0.8, 13.5]**, 8/0/4, p 0.08 |
| generic − base | +3.9 [−5.0, 14.4], 2/7/3, p 0.75 | −1.1 [−6.7, 5.0], 1/8/3 | +0.7 [−2.3, 3.7] |

**Reading.** Nothing here supports the claim, and nothing refutes it either: every TeachQuiz interval contains 0
and 7 to 9 of 12 topics are ties. The point estimates go the wrong way (learner below generic and learner_all).
The one interval clear of 0 is layout: rewriting every section costs about 7 MVQS points against rewriting only
the flagged ones.

**Why the pilot cannot answer the question** (both are fixable, neither is a result about the method):

1. **Floor effect.** With the base video the local student scores 0 on 8 of 12 topics and on 7 topics every
   condition scores 0. MMMC topics are 3Blue1Brown-level; a 26B model seeing 3 stills per section learns almost
   nothing from them. A tie at 0 carries no information.
2. **Localisation was barely exercised.** 9 to 12 of 9 to 12 DEV questions were gaps on every topic, so `learner`
   rewrote 2 to 4 sections of videos with 2 to 4 sections: nearly the scope of `learner_all`. A localised repair
   needs a base video that teaches *some* of the DEV items.

**What would make it a test.** A student that learns from the video (Gemini watching the mp4, Code2Video's own
protocol: `run.py manual-export` for free by hand, or `run.py c2v` at about $13 for these 12 topics × 3 runs on
Gemini 3 Flash), and/or topics where the base video already teaches part of the DEV quiz. Run the same four
conditions; the claim needs learner > generic and learner > learner_all on TEST.

**A bug found on the way.** The first analysis showed all four conditions identical in every measure: each
revised run was copied from the base folder with the base's saved TEST score, and the evaluation returned that
file. Fixed in `feedback.revise` (scores and rows are not copied) and re-scored; the videos were not regenerated.

## First single-topic run (Pythagoras theorem, before the MMMC protocol): an anecdote

Class 8, 4 sections. TEST was half of our own filtered quiz (9 items); 3 student runs.

| Video | TEST: with video (3 runs) | TeachQuiz | Evidence-backed | First section only | MVQS |
|---|---|---|---|---|---|
| Base | 22, 22, 22 | +22.2 | 22.2 | 11.1 | 87.4 |
| Learner (s3 rewritten; s4's rewrite failed and the old one was kept) | 33, 33, 22 | +29.6 | 18.5 | 11.1 | 84.0 |
| Generic (s1 and s2 rewritten) | 22, 22, 22 | +22.2 | 22.2 | 11.1 | 85.0 |

Over the base video, `learner` gained 0.67 of a question on average out of 9, and `generic` gained nothing. One
topic, so this is not evidence.

## What the first runs taught (each is now handled in code)

| Problem seen | Effect | Fix |
|---|---|---|
| Unfiltered quizzes leak | the unlearned student scored 36% with no video; the first section alone beat the whole video | DEV item filter; a clean TEST score; S1 measured on other seeds |
| Asked for a list, a small judge copies the template's ids | every "yes" was lost: evidence 0% | one call per item (evidence and gap mapping) |
| A failed regeneration dropped its section | "revised" videos missing half their sections | the old code, layout record and clip are kept |
| Manim's rich traceback hides the line | block repair never ran | the failing line comes from partial execution |
| A model reply that is not JSON crashed the run | a lost run | a failed repair call stands aside |
| The local coder repeats API inventions (`get_side_length("BC")`, `.reverse()`, `Mobject(height=)`) | about a third of rewrites fail to render | a hint table; this is still the largest source of noise |
