# Code2Video's TeachQuiz through a chat app (free) or the API (paid)

Code2Video scored its videos with **Gemini 2.5 Pro reading the whole mp4** (`request_gemini_with_video` in their
`src/gpt_request.py`). Gemini models read video natively, so no frames have to be chosen. There are two ways to run
the same protocol here.

## A. By hand in a chat app (no cost)

```bash
PY=/home/mani/manim/lessonforge/.venv/bin/python
$PY bench/run_bench.py --n 12 --seed 0 --manual-export   # one folder per topic under manual/
# or for one topic:
$PY run.py manual-export runs/<slug>
```

Each `manual/<slug>/` holds:
- `INSTRUCTIONS.md`: a checklist of the chats to do;
- `prompts/`: the text to paste, one file per chat;
- `videos/V1.mp4 …`: the videos under blind labels (`key.json` says which is which; do not open it while pasting);
- `replies/`: an empty file per prompt, for the chatbot's answer.

For each topic:
1. Open `INSTRUCTIONS.md` and write the model's name at the top (for example "Gemini 2.5 Pro, gemini.google.com").
2. For **each** prompt file, open a **new chat** (a chat that has seen one video remembers it). Paste the whole
   file. For a `stage3_Vn` file, also attach `videos/Vn.mp4`. Send it.
3. Copy the whole answer into `replies/<same file name>.txt`.
4. When every reply file is filled, run `$PY run.py manual-import manual/<slug>`. It prints S1 (baseline),
   S2 (unlearned), and S3 and the gain for each video. It also writes `runs/<slug>/eval_c2v_manual.json`, which
   `bench/analyze.py` reads.

Per topic that is 2 text chats plus one video chat per condition: 6 chats with all four conditions. Stages 1 and 2
do not depend on the video, so they are done once per topic.

**Differences from Code2Video, to state in the paper.** Each stage's 5 questions go in one message (they asked one
question per call). The app chooses its own temperature and system prompt. Answers are graded with their rule (the
first standalone A–D, `NULL` = wrong) after splitting the reply at "Question n".

## B. Through the API (paid, exact)

```bash
$PY run.py estimate runs/<slug> --topics 12 --runs 1     # prints the cost first; spends nothing
C2V_CAP_USD=5 $PY run.py c2v runs/<slug>                 # their prompts, one call per question, whole mp4
```

Estimates from the live OpenRouter catalogue (2026-11-12) for our 92-second videos, at 263 video tokens a second
(Gemini's documented default) and 1,200 output tokens a call (a guess, since 2.5 Pro must think). One evaluation of
one video is the 5 stage-3 calls:

| Evaluator | Per video | 1 topic, 4 videos, 1 run | 12 topics, 3 runs | 117 topics, 1 run |
|---|---|---|---|---|
| `google/gemini-2.5-pro` (Code2Video's) | $0.21 | $0.98 | $35 | $115 |
| `google/gemini-3-flash-preview` (SGA's judge family) | $0.08 | $0.36 | $13 | $42 |
| `google/gemini-2.5-flash` | $0.05 | $0.24 | $9 | $28 |

These are estimates. One real call's `usage` fixes the video-token rate and the output length; check it before a
large run. Calls are written to `runs/ledger.jsonl` and refused past `C2V_CAP_USD`. A key of its own for this study
is best (`C2V_OPENROUTER_KEY`).
