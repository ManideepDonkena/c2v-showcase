# Open problems (2026-11-12)

What breaks in the pipeline and the evaluation, measured on the 12-topic pilot (`runs/`, 48 videos, 192 sections),
ranked by how much each one blocks the claim. Each entry ends with what the problem is called in other fields, to
search for solutions there.

## 1. The "unlearned" student does not forget; it abstains

> **Correction (later the same day).** The pilot's TEST grading lost every answer of a student run whenever the
> student copied the answer template's example id (`q1`) for TEST items named `t1..t5`: 42% of runs. The 87% NULL
> figure below includes those lost answers; graded correctly, abstention with the video is about 76-78%
> (`paper/tables/numbers.tex`, `NullWithVideo`). The refusal confound itself holds, and a larger problem sits under
> it: forced to choose, the student answers about 94% of MMMC's TEST without any video (`bench/mmmc_prior.py`).
> Fixed in `teachquiz.grade_reply`; the measure that replaces TeachQuiz is in `c2vlab/dvgain.py` and the paper.

**Seen.** Without the video the student answers NULL on 720 of 720 TEST items; with the video it still answers NULL on
623 of 720 (87%). S1 is 0 because the student refuses, not because it guesses at chance (25%) or lacks the knowledge.
First result of the forced-choice variant (one topic, inscribed square): no video, NULL not allowed, the student gets
**100%**. If that holds, TeachQuiz measures how willing the student is to answer, not what the video taught.
`bench/student_study.py` (running) settles it on all 48 videos.

**Why it matters.** Every TeachQuiz number, ours and Code2Video's published ones, rests on prompted forgetting.

**Elsewhere.** Machine-unlearning evaluation ("unlearning vs. refusal", "obfuscation vs. forgetting", TOFU's
fictitious authors, WMDP, relearning attacks); "evaluating in-context learning of novel concepts" (invented words or
fictional entities the model cannot already know); psychometrics, "pretest knowledge confound" and the
"guessing parameter" in item response theory; selective prediction and abstention calibration.

## 2. Floor effect: most topics score 0 in every condition

**Seen.** The base video scores 0 on 8 of 12 topics; on 7 topics every condition scores 0; 7 to 9 of 12 paired
differences are ties. MMMC has 5 TEST items per topic, so one item is 20 points.

**Elsewhere.** Psychometrics, "floor and ceiling effects" and "item difficulty calibration"; computerised adaptive
testing; power analysis and "minimum detectable effect" in clinical trials; "sensitivity of benchmarks / signal-to-noise
of evals".

## 3. Gains on DEV do not carry over to TEST

**Seen.** The learner repair raises its own DEV score a lot and TEST not at all: Hamming codes DEV 0 → 40, TEST 0 → 0;
backpropagation DEV 9 → 50, TEST 20 → 20; inscribed square DEV 0 → 18, TEST 0 → 0. The only guard against teaching the
item instead of the idea is a 6-word overlap check (`feedback.copies`).

**Elsewhere.** Education, "teaching to the test", "near vs. far transfer"; ML, "overfitting to the validation set" and
"reusable holdout / adaptive data analysis" (Dwork et al.); Goodhart's law in reward modelling ("reward hacking",
"specification gaming").

## 4. Localisation was never exercised

**Seen.** 9 to 12 of 9 to 12 DEV items are gaps on every topic, so the diagnosis flags 2 to 4 of 4 sections, nearly
the same scope as `learner_all`. The gap → section map is one LLM call per item with no check.

**Elsewhere.** Software engineering, **spectrum-based fault localisation** (Tarantula, Ochiai: it needs passing *and*
failing tests, which is our case); education, the **Q-matrix** and cognitive diagnosis models (DINA, knowledge
tracing) that map items to skills; "credit assignment".

## 5. Generated Manim code often does not render

**Seen.** 40% of sections fail their first render (base 19 of 48, rewrites 61 of 144). After 4 repairs, 19% still fail
(base 9 of 48, rewrites 27 of 144). A failed rewrite silently keeps the old section, so conditions differ less than
intended. Failures by kind (277 failed attempts):

| Kind | Count | Example |
|---|---|---|
| Invented API: methods, keyword arguments, attributes | about 64 | `get_side_length("BC")`, `Mobject(bracket_style=)`, `scale(about=)` |
| Undefined names | 41 | `Symbol`, `WriteText` |
| **Syntax / indentation broken by our own line and block patch** | 39 (38 right after a patch) | `IndentationError: unexpected indent` |
| Files or URLs that do not exist | 22 | `https://svgshare.com/...svg`, `julia_set.png` |
| 2-D points where Manim wants 3-D | 20 | `could not broadcast (1,2) into (1,3)` |
| LaTeX | 14 | `latex error converting to dvi` |
| Timeouts, `Alpha not between 0 and 1`, overflow | the rest | |

**Elsewhere.** Automated program repair (APR); "API hallucination in code LLMs" and documentation-retrieval-augmented
code generation; static checking before running (type stubs, linting as a filter); **AST-level edits instead of
text splicing** (structured or tree-diff patching); grammar-constrained decoding; "self-debugging" with compiler
feedback.

## 6. A rewrite changes more than the fix

**Seen.** A flagged section is rewritten from scratch, not edited, so `learner` and `generic` differ in everything the
coder happens to change, not only in the instruction. Rewriting every section costs about 7 MVQS points
(learner − learner_all +6.7, CI [0.8, 13.5]).

**Elsewhere.** "Minimal edits" and "edit-distance-controlled ablations"; "minimal pairs" in linguistics; the
"single-variable change" in A/B testing; "model editing locality" (ROME, MEMIT).

## 7. The student sees stills of a silent video

**Seen.** 3 frames per section (at 40, 70, 95%), no audio, no motion; the narration exists only as planned text.
Code2Video's student watches the whole narrated mp4. The study's `frames8` and `narration` variants measure how much
this costs.

**Elsewhere.** "Keyframe selection / extraction" and "shot boundary detection" in video understanding; "temporal
grounding"; long-video question answering benchmarks.

## 8. The evidence judge is not validated

**Seen.** `qwen2.5vl:7b` decides whether the cited moment teaches the answer; we have never measured its agreement
with a person.

**Elsewhere.** "LLM-as-a-judge validation", "inter-rater reliability" (Cohen's kappa, Krippendorff's alpha), "judge
calibration against human labels".

## 9. A decision for us, not a search: the DEV gate is not used

`feedback.round_` records `kept` (DEV did not drop and MVQS did not fall more than 5), but `pipeline.run_topic` scores
the revised video on TEST either way; 9 of 36 revisions were "not kept". Either report only kept revisions (and fall
back to the base video otherwise) or drop the gate. The choice changes the claim being tested.
