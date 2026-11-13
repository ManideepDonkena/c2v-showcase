"""Attachment check: does every label, arrow or box still sit at the object the code attached it to?

MVQS (SGA) scores boxes in isolation, so moving a label off its circle to clear an overlap raises it while the label
no longer says which circle it names. This check reads the attachments from the code and their positions from the
scene graph:

    X.next_to(Y, ...)            X belongs beside Y        broken when the gap between their boxes exceeds NEAR
    X.move_to(Y | Y.get_*())     X belongs on Y            broken when the gap exceeds ON (and the centres are apart)
    X = Arrow/Line(Y.get_*(), Z.get_*())  or start=/end=   X ends at Y and Z     broken when the gap to either exceeds NEAR

A pair is judged in the last recorded state in which both are on screen (what a viewer sees at rest).

    broken(code, graph)  -> [{"kind", "obj", "anchor", "gap", "line"}]
"""

from __future__ import annotations

import ast

NEAR = 1.0  # units: next_to puts objects 0.25 apart by default; a gap over 1 unit no longer reads as attached
ON = 0.5
LINES = {"Arrow", "Line", "DoubleArrow", "DashedLine", "CurvedArrow", "Vector"}
TEXTS = {"Text", "MathTex", "Tex", "MarkupText", "Paragraph", "SingleStringMathTex", "DecimalNumber", "Integer"}


def _root(node):
    """The variable an expression starts from: Y in Y, Y.get_center(), Y[0], Y.get_top() + UP."""
    while True:
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Call):
            node = node.func
        elif isinstance(node, (ast.Attribute, ast.Subscript)):
            node = node.value
        elif isinstance(node, ast.BinOp):
            node = node.left
        else:
            return None


def relations(code):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return []
    out = []

    def scan(target, value, line):
        for n in ast.walk(value):
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.args:
                anchor = _root(n.args[0])
                if n.func.attr == "next_to" and anchor:
                    out.append(("next_to", target, anchor, line))
                elif n.func.attr == "move_to" and anchor and anchor not in ("ORIGIN", "UP", "DOWN", "LEFT", "RIGHT"):
                    out.append(("move_to", target, anchor, line))
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in LINES:
                ends = list(n.args[:2]) + [k.value for k in n.keywords if k.arg in ("start", "end")]
                for e in ends:
                    a = _root(e)
                    if a and a not in ("ORIGIN", "UP", "DOWN", "LEFT", "RIGHT", "np"):
                        out.append(("arrow", target, a, line))

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            scan(node.targets[0].id, node.value, node.lineno)
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            f = node.value.func  # X.next_to(Y) as a statement
            if isinstance(f, ast.Attribute) and f.attr in ("next_to", "move_to"):
                tgt = _root(f.value)
                if tgt:
                    scan(tgt, node.value, node.lineno)
    seen, uniq = set(), []
    for r in out:
        if r[1] != r[2] and r[:3] not in seen:
            seen.add(r[:3])
            uniq.append(r)
    return uniq


def _union(objs, name):
    boxes = [o["box"] for o in objs if o.get("name") == name]
    if not boxes:
        return None
    return [min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes)]


def _gap(a, b):
    dx = max(0.0, max(a[0], b[0]) - min(a[2], b[2]))
    dy = max(0.0, max(a[1], b[1]) - min(a[3], b[3]))
    return (dx * dx + dy * dy) ** 0.5


def broken(code, graph):
    """Attachments that a viewer would misread at rest: too far from their anchor ("detached"), or a label closer to
    another object of the anchor's own type than to its anchor ("misattributed", e.g. a label over the next circle)."""
    states = graph.get("states") or []
    out = []
    for kind, obj, anchor, line in relations(code):
        last = None
        for s in states:
            a, b = _union(s["objects"], obj), _union(s["objects"], anchor)
            if a and b:
                last = (s, a, b)
        if last is None:
            continue
        s, a, b = last
        gap = _gap(a, b)
        if gap > (ON if kind == "move_to" else NEAR):
            out.append({"kind": kind, "obj": obj, "anchor": anchor, "gap": round(gap, 2), "line": line, "fault": "detached"})
            continue
        types = {o["type"] for o in s["objects"] if o.get("name") == anchor}
        if kind == "arrow" or not types or types & TEXTS:  # text beside text (rows of equations) is no attachment
            continue
        rivals = {o["name"] for o in s["objects"] if o.get("name") not in (anchor, obj, None) and o["type"] in types}
        near = [(r, _gap(a, _union(s["objects"], r))) for r in rivals]
        closer = [r for r, g in near if g + 0.05 < gap]
        if gap > 0.15 and closer:
            out.append({"kind": kind, "obj": obj, "anchor": anchor, "gap": round(gap, 2), "line": line,
                        "fault": "misattributed", "closer_to": min(closer)})  # fmt: skip
    return out
