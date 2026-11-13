# Models: theirs and ours

| Role | Code2Video | SGA | c2v-lab default (local, free) |
|---|---|---|---|
| Planner / coder | GPT-4.1 in its run scripts; its README says the best code came from Claude-4-Opus; GPT-5, GPT-4o, o4-mini and Gemini are selectable | GPT-5.1, GPT-5 mini, Claude 4.6 Sonnet, Gemini 3.0 Flash (the same model generates and repairs) | `qwen3.6` plans and writes quizzes; `qwen3-coder:30b` writes code |
| Critic | Gemini 2.5 Pro (visual-anchor prompt) | Code2Video's critic as a baseline; its own repair is geometric | none: scene graph + MVQS |
| TeachQuiz student | **Gemini 2.5 Pro, watching the mp4** | — | `gemma4:26b` on 3 frames per section; or Gemini via `c2v_eval.py` / a chat app |
| Judges | Gemini 2.5 Pro (AES) | Gemini 3.0 Flash | `qwen2.5vl:7b` (evidence) |

Why `gemma4:26b` is the local student: in our lessonforge baseline it forgot properly (6% with no video), while
`qwen2.5vl:7b` scored 87% before seeing anything.

Any role can use OpenRouter by prefixing the id with `or:`, e.g. `C2V_CODER=or:openai/gpt-4.1`.

These were on OpenRouter on 2026-11-12, with price in USD per million tokens (input / output):

| Model | Input / output | Must think |
|---|---|---|
| `openai/gpt-4.1` | 2 / 8 | no |
| `openai/gpt-5.1` | 1.25 / 10 | no |
| `openai/gpt-5-mini` | 0.25 / 2 | yes |
| `anthropic/claude-opus-4.1` | 15 / 75 | no |
| `anthropic/claude-sonnet-4.6` | 3 / 15 | no |
| `google/gemini-2.5-pro` | 1.25 / 10, video input | yes |
| `google/gemini-3-flash-preview` | 0.5 / 3, video input | no |
| `google/gemini-2.5-flash` | 0.3 / 2.5, video input | no |

A model that must think is first called with thinking off. If the API refuses that, it is called again with
`effort: low` and room to answer (`llm.py`).
