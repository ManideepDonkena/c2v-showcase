# Benchmark protocol

## How prior work benchmarks code-to-video teaching

Read from the papers and code on 2026-11-12. "Not stated" means the page we read did not say.

| Work | Topics / data | Teaching measure | Visual / layout measure | Evaluator | Repeats, statistics |
|---|---|---|---|---|---|
| Code2Video (arXiv 2510.01174, `src/eval_TQ.py`) | MMMC: 117 topics (3Blue1Brown lessons), 5 MCQs each | **TeachQuiz**: stage 1 answer normally, stage 2 "unlearn" the concept (no video), stage 3 unlearn + watch the video; gain = S3 − S2. Each question is its own call; graded by the first standalone A–D in the reply | **AES**: 5 dimensions × 20 points, VLM-judged from the video | **Gemini 2.5 Pro**, native video input (the mp4 sent base64) | One run; one-sample t-test of gains, Cohen's d, 95% CI |
| SGA (arXiv 2607.18116) | MMMC-Code: 117 topics; 2,252 scene evaluations (4 backbones × 3 conditions) | none | **MVQS**, rendering-free (scene graph), plus VLM-judge dimensions and human preference (84.4% vs raw, 65.0% vs VLM critic) | **Gemini 3.0 Flash** VLM judge | Not stated on the page read |
| PIVOT (arXiv 2609.24083) | 4 STEM domains | expert evaluation; quizzes generated for learners | layout / factual / clarity checks per shot | experts | expert study |
| ManimCode (arXiv 2611.08294) | ManimData-test | none | render success (52.6 → 96.6%), completed videos | — | — |
| EduPanel (arXiv 2607.18529) | teaching videos | three-agent LLM judge vs experts (MAE) | — | LLM panel | agreement with experts |

No prior work measures whether a **repair** improves learning on questions the repair never saw. Code2Video's
TeachQuiz scores finished videos only, SGA scores layout only, and PIVOT's quizzes serve the learner, not the video.

## Our protocol

**Topics.** MMMC's 117 topics; a pilot uses a seeded sample (`bench/run_bench.py --n 12 --seed 0`).

**Two quizzes per topic, never mixed.**
- DEV is written by our planner from the topic name only. Items are dropped when the student does not know them, or
  when the unlearned student gets them right with no video in any of 3 seeds. Only the repair sees DEV.
- TEST is MMMC's official 5 questions (Code2Video's own), so TEST was written by other people. No step of the
  pipeline sees it.

**Conditions.** All use the same generator, the same base video and the same diagnosis.

| Condition | What is rewritten | What the rewrite is told |
|---|---|---|
| base | nothing | — |
| **learner** (ours) | the sections the diagnosis maps the DEV gaps to | the missing ideas, in the planner's own words |
| generic | as many sections as `learner`, chosen at random | "teach this section's point more clearly and completely" |
| learner_all | every section | all the missing ideas (learner signal, no localisation) |

`learner − generic` tests whether the learner signal matters, given the same amount of rewriting.
`learner − learner_all` tests whether localising the repair matters.

**Measures on TEST.**

| Measure | Definition | Why |
|---|---|---|
| TeachQuiz (local) | S2 − S1, unlearned student `gemma4:26b`, 3 frames per section, 3 runs | free and repeatable; our main measure |
| TeachQuiz, clean | the same without TEST items the no-video student got right (seeds 1–3) | removes guessing; S1 is measured on seeds 11–13, so it is not zero by construction |
| Evidence-backed | right answers whose cited moment a judge of another family (`qwen2.5vl:7b`) says teaches it | a right answer for the wrong reason does not count |
| Controls | first section only; another topic's video | a gain that survives these is not teaching |
| TeachQuiz, Code2Video protocol | their prompts, stages, grading and video input, through the Gemini API (`run.py c2v`) or a chat app (`manual-export` / `manual-import`) | comparable to Code2Video's published numbers |
| MVQS | SGA's formula over the scene graph, mean over sections | the repair must not break the layout |
| Rendered sections | sections in the final video | a rewrite that fails keeps its old section; the count shows how often |

**Statistics** (`bench/analyze.py`). Per-topic paired differences, with a mean, a bootstrap 95% CI (10,000
resamples), a Wilcoxon signed-rank p, and wins/ties/losses. A claim needs the CI of `learner − generic` above 0 on
TeachQuiz (clean) **and** on the Code2Video-protocol gain.

## Threats to validity, and what answers each

| Threat | Answer in the protocol |
|---|---|
| Teaching to the test | TEST is written by other people (MMMC) and never shown to any step |
| A student who does not really forget | item filter on DEV, clean TEST score, controls, a second protocol (Code2Video's, with Gemini) |
| The evaluator shares a family with the generator | the student is `gemma4`, while the planner and coder are Qwen; the Code2Video protocol uses Gemini |
| Frames are not video | the Code2Video protocol gives Gemini the whole mp4 |
| More rewriting simply helps | `generic` rewrites as many sections as `learner` |
| One run is noise | 3 student runs per video; topic-level pairing; bootstrap CI |
| Rewrites that fail to render | the old section is kept, and the count is reported |
| The chat app is not the API | report manual and API results separately, and name the app's model |
