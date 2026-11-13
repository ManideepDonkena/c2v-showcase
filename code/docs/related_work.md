# Related work and novelty check

Searched and read on 2026-11-12. Rows marked "not opened" were taken from a search result or a list only.

| Part of the idea | Exists? | Where |
|---|---|---|
| Unlearned-student quiz as a **metric** for teaching videos | **Yes** | Code2Video (arXiv 2510.01174), TeachQuiz |
| Line → block → section escalating code repair | **Yes** | Code2Video ScopeRefine (`src/scope_refine.py`) |
| Scene graph by partial execution; MVQS; separation vector handed to an LLM line patch | **Yes** | SGA (arXiv 2607.18116) |
| A simulated learner's outcome as the **reward to optimise** instructional material | **Yes, for text** | He-Yueya, Goodman, Brunskill (arXiv 2403.02795): LM-judged learning gains optimise math worksheets |
| Quiz linked to a generated STEM video; a wrong answer triggers new content | **Partly** | PIVOT (arXiv 2609.24083): a wrong answer generates a *new remediation video for that learner*. Quiz results do not revise the original video, and no answer is traced to a segment |
| Visual self-correction of Manim code (learned, VLM- or render-driven) | **Yes** | ManimCode (arXiv 2611.08294), ManimAgent (arXiv 2606.30296). Their feedback is render and visual, not learner |
| Learner-perspective LLM judge of teaching videos | **Yes, evaluation only** | EduPanel (arXiv 2607.18529) |
| Simulated students to iterate quiz items | **Yes, for items** | VizQStudio (arXiv 2603.00994), not opened |
| **Unlearned-student failures, traced to a section by evidence citation, repairing only that section of a code-generated video; scored on held-out questions by other authors, against a same-budget generic revision and a non-localised revision** | **Not found** | — |

**Verdict.** Each ingredient is published. The combination is not:
- a learner signal used to repair a **code-generated video**;
- the repair **localised to a section**;
- the result tested on **held-out questions by other authors**, with controls for rewriting budget and localisation.

The closest work is He-Yueya et al. (the same principle for text worksheets, optimised as a reward) and PIVOT (a
quiz tied to a video, but it remediates the learner, not the video).

The claim to make, and to test, is narrow: *on held-out questions, a localised learner signal improves a generated
video's teaching more than a generic revision of the same size, and more than the same signal applied everywhere.*
If `generic` or `learner_all` does as well, the claim fails. The pilot runs exactly these two comparisons.

Small engineering points that are not contributions:
- applying SGA's separation vector directly as code;
- taking the failing line from partial execution rather than from Manim's traceback.

## Sources

- Code2Video: https://arxiv.org/abs/2510.01174, https://github.com/showlab/Code2Video
- SGA: https://arxiv.org/abs/2607.18116
- PIVOT: https://arxiv.org/abs/2609.24083
- He-Yueya et al.: https://arxiv.org/abs/2403.02795
- ManimCode: https://arxiv.org/abs/2611.08294
- ManimAgent: https://arxiv.org/html/2606.30296
- EduPanel: https://arxiv.org/abs/2607.18529
- VizQStudio: https://arxiv.org/pdf/2603.00994
- Lists searched: zsyverse/awesome-code2video, voidforall/awesome-video-as-code, sitkevij/awesome-video,
  zhuyansen/awesome-claude-video-skills
