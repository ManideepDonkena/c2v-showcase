# Method

```
topic ──► PLAN (sections: what each teaches, shows, says)
            │
            ▼
        CODE one Manim scene per section ──► RENDER ──fail──► REPAIR (line → block → section)   [Code2Video ScopeRefine]
            │                                   │              failing line from partial execution [SGA]
            ▼                                   ok
        SCENE GRAPH by partial execution ──► MVQS + conflicts ──► LAYOUT REPAIR                  [SGA]
            │                                                   shift by separation vector (code)
            ▼                                                   → block (model) → section (model)
        VIDEO (sections joined)                                 kept only if MVQS rises
            │
            ▼
        DIAGNOSE  unlearned student on the DEV quiz ──► gaps (wrong, NULL, or right without evidence)
            │     each gap ──► the section that should have taught it + the missing idea      [ours]
            ▼
        REVISE  only those sections, with the missing ideas; re-check layout; a failure keeps the old section
            │
            ▼
        EVALUATE on TEST (MMMC's official questions, never seen): TeachQuiz, evidence, controls, MVQS
```

## Parts and where they come from

| Part | File | Source | What we changed |
|---|---|---|---|
| Planner → coder → render | `generate.py` | Code2Video | small, no icons or assets; one scene per section |
| Render repair, line → block → section | `generate.py` | Code2Video ScopeRefine | the failing line comes from the scene graph's partial execution, because Manim's rich traceback hides it; a table of known API mistakes adds a hint |
| Scene graph | `scene_graph.py` | SGA | `Scene.play` patched to jump each animation to its end; records kind, box, variable name and creation line after every play |
| MVQS | `mvqs.py` | SGA | SGA's weights; severity, separation and labelling formulas are our choice where SGA gives none (stated in the file) |
| Layout repair | `layout.py` | SGA (separation vector) + ScopeRefine (escalation) | the vector is first applied as code (`name.shift(v)`), with no model call |
| TeachQuiz | `teachquiz.py`, `c2v_eval.py` | Code2Video | item filter, clean score, controls, evidence check; the exact protocol is in `c2v_eval.py` |
| **Learner-feedback repair** | `feedback.py` | ours | — |

## Learner-feedback repair, precisely

1. **Gaps.** The unlearned student answers DEV with the video, twice. A DEV question is a gap unless some run got it
   right **and** the evidence judge said the cited moment teaches it.
2. **Localise.** For each gap, one planner call names the section that should have taught it and the missing idea,
   to show and say in the planner's own words. An idea sharing 6 words in a row with the question or its options is
   refused, because it would teach the item and not the idea.
3. **Revise.** Only those sections are rewritten. The coder gets the section's plan plus "This section must ALSO
   show and say: …". The layout is checked again. A section whose new code does not render keeps its old code and
   clip.
4. **Gate** (reported, not used for TEST). The revision is "kept" if DEV TeachQuiz does not fall and MVQS falls by
   less than 5 points.

The design choices that matter for the claim:
- DEV and TEST come from different authors.
- The comparison rewrites the same number of sections, so the amount of rewriting is held fixed.
- The repair sees only the missing *idea*, not the item.
