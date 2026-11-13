"""Temporal checks for a Manim section: faults of *when* things are on screen, which the spatial layout score (MVQS)
cannot see because it reads positions, not the life of each object. All checks read the code (no model, no render).

    residue      Transform(a, b) morphs a into b's shape and leaves a on screen; b itself is never added. A later
                 FadeOut(b) / Indicate(b) / b.animate does nothing visible, so the old text stays (leftover glyphs),
                 and a later Write(b) draws a second copy. Fix (automatic): ReplacementTransform(a, b), which puts b
                 on screen in a's place.
    prose_math   MathTex / Tex given a sentence: TeX math mode drops the spaces ("Thecatsatonthemat"). Fix
                 (automatic): Text(...) for the sentence.
    never_shown  a Text / MathTex / shape is built but never added or animated: planned content that never appears.
                 Reported to the coder (no automatic fix: where it belongs is a teaching decision).

    check(code)  -> [{"kind", "line", "name", "message"}]
    fix(code)    -> (new_code, applied)   the automatic fixes only; returns the code unchanged when it cannot parse
"""

from __future__ import annotations

import ast
import re

SHOWN_BY = {"Write", "Create", "FadeIn", "DrawBorderThenFill", "GrowFromCenter", "GrowFromPoint", "GrowFromEdge",
            "GrowArrow", "SpinInFromNothing", "AddTextLetterByLetter", "AddTextWordByWord", "ShowIncreasingSubsets",
            "Uncreate", "FadeOut", "ReplacementTransform", "TransformFromCopy", "Transform", "LaggedStart",
            "AnimationGroup", "Succession", "MoveToTarget", "ApplyMethod", "Indicate", "Circumscribe", "Flash",
            "FocusOn", "Wiggle", "TransformMatchingTex", "TransformMatchingShapes", "FadeTransform"}  # fmt: skip
USES_ON_SCREEN = {"FadeOut", "Indicate", "Circumscribe", "Wiggle", "Flash", "FocusOn", "Uncreate", "ShowPassingFlash"}
BUILDERS = {"Text", "MathTex", "Tex", "MarkupText", "Paragraph", "Circle", "Square", "Rectangle", "Arrow", "Line",
            "Dot", "Polygon", "Triangle", "NumberPlane", "Axes", "BarChart", "Table", "Brace", "DecimalNumber",
            "Integer", "RoundedRectangle", "Ellipse", "Arc", "Vector", "Matrix"}  # fmt: skip
WORDS = re.compile(r"(?<![\\a-zA-Z])[A-Za-z]{3,}(?:\s+[A-Za-z]{2,}){2,}")  # three plain words in a row


def _name(node):
    return node.id if isinstance(node, ast.Name) else None


def _calls(tree):
    return [n for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)]


def _plain_sentence(node):
    """The literal text of a MathTex/Tex call when it is a sentence outside \\text{...}: one string of three or more
    plain words, or the words of a sentence given one per argument (MathTex("The", " ", "cat", ...))."""
    strs = [a.value for a in node.args if isinstance(a, ast.Constant) and isinstance(a.value, str)]
    for s in strs:
        if WORDS.search(re.sub(r"\\text\{[^}]*\}|\\mathrm\{[^}]*\}", " ", s)):
            return s
    if len(strs) == len(node.args) and len(strs) >= 3 and sum(bool(_WORD.fullmatch(s)) for s in strs) >= 3 and all(
        _WORD.fullmatch(s) or not s.strip() for s in strs
    ):
        return " ".join(s for s in strs if s.strip())
    return None


_WORD = re.compile(r"[A-Za-z][A-Za-z'-]*[.,!?:;]?")


def check(code):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return []
    calls = _calls(tree)
    out = []
    # residue: the target of Transform used later as if it were on screen
    targets = {}
    for c in sorted(calls, key=lambda n: (n.lineno, n.col_offset)):
        fn = c.func.id
        if fn == "Transform" and len(c.args) >= 2 and _name(c.args[1]):
            targets.setdefault(_name(c.args[1]), c.lineno)
        elif fn in USES_ON_SCREEN | {"Write", "Create", "FadeIn"}:
            for a in c.args:
                n = _name(a)
                if n in targets and c.lineno > targets[n]:
                    out.append({"kind": "residue", "line": targets[n], "name": n,
                                "message": f"Transform(..., {n}) at line {targets[n]} leaves the old object on screen; "
                                           f"{fn}({n}) at line {c.lineno} acts on an object that was never shown"})  # fmt: skip
    for n in ast.walk(tree):  # b.animate... after Transform(a, b)
        if (isinstance(n, ast.Attribute) and n.attr == "animate" and _name(n.value) in targets
                and n.lineno > targets[_name(n.value)]):  # fmt: skip
            out.append({"kind": "residue", "line": targets[_name(n.value)], "name": _name(n.value),
                        "message": f"{_name(n.value)}.animate at line {n.lineno} moves an object that was never shown "
                                   f"(Transform at line {targets[_name(n.value)]})"})  # fmt: skip
    # prose typeset as maths
    for c in calls:
        if c.func.id in ("MathTex", "Tex") and (s := _plain_sentence(c)):
            out.append({"kind": "prose_math", "line": c.lineno, "name": None,
                        "message": f"{c.func.id}({s[:40]!r}...) typesets a sentence in math mode: its spaces vanish"})  # fmt: skip
    # built but never shown
    built = {}
    for n in ast.walk(tree):
        if (isinstance(n, ast.Assign) and len(n.targets) == 1 and _name(n.targets[0]) and isinstance(n.value, ast.Call)
                and isinstance(n.value.func, ast.Name) and n.value.func.id in BUILDERS):  # fmt: skip
            built.setdefault(_name(n.targets[0]), n.lineno)
    used = {x.id for x in ast.walk(tree) if isinstance(x, ast.Name) and isinstance(x.ctx, ast.Load)}
    for name, line in built.items():
        if name not in used:
            out.append({"kind": "never_shown", "line": line, "name": name,
                        "message": f"{name} (line {line}) is built but never added, animated or grouped"})  # fmt: skip
    seen, uniq = set(), []
    for f in out:
        key = (f["kind"], f["line"], f["name"])
        if key not in seen:
            seen.add(key)
            uniq.append(f)
    return uniq


def fix(code):
    """Apply the automatic fixes; every fix must leave code that parses, or it is not applied."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return code, []
    rows, applied = code.split("\n"), []
    residue_lines = {f["line"] for f in check(code) if f["kind"] == "residue"}
    for c in _calls(tree):
        if c.func.id == "Transform" and c.lineno in residue_lines and c.lineno == c.end_lineno:
            row = rows[c.lineno - 1]
            new = row[: c.col_offset] + "Replacement" + row[c.col_offset :]
            rows[c.lineno - 1] = new
            applied.append({"kind": "residue", "line": c.lineno})
        elif c.func.id in ("MathTex", "Tex") and _plain_sentence(c) and c.lineno == c.end_lineno:
            row = rows[c.lineno - 1]
            consts = [a for a in c.args if isinstance(a, ast.Constant) and isinstance(a.value, str)]
            if len(consts) == len(c.args) and len(consts) >= 3:
                # one word per part: keep the parts (code may index them); words in \text{}, spaces as math spaces
                for a in sorted(consts, key=lambda a: a.col_offset, reverse=True):
                    s = a.value
                    lit = repr("\\text{" + s + "}") if s.strip() else repr("\\;")
                    row = row[: a.col_offset] + lit + row[a.end_col_offset :]
                rows[c.lineno - 1] = row
                applied.append({"kind": "prose_math", "line": c.lineno})
            elif row[c.col_offset : c.col_offset + len(c.func.id)] == c.func.id and len(c.args) == 1:
                rows[c.lineno - 1] = row[: c.col_offset] + "Text" + row[c.col_offset + len(c.func.id) :]
                applied.append({"kind": "prose_math", "line": c.lineno})
    new = "\n".join(rows)
    try:
        ast.parse(new)
    except SyntaxError:
        return code, []
    return new, applied
