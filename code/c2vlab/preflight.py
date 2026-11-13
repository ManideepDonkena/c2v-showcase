"""Static checks of a generated Manim section before it is rendered (feature `preflight`).

Each check catches a failure class seen in the pilot's 277 failed renders, without running the scene:
    syntax       the code does not parse (38 of 39 such errors came right after a line/block patch)
    name         a name used but defined nowhere (not in manim, builtins or the code itself)       41 in the pilot
    kwarg        a keyword a Manim class's constructor chain does not accept (inspect.signature)   25
    method       a method that no Manim class, numpy array or Python container has                 about 17
    asset        an external file or URL (SVGMobject, ImageMobject, "*.svg", "http...")             22
Signatures come from the installed manim, so the check follows its version. A check that cannot decide stays silent:
a false alarm costs a repair that was not needed, which is worse than a miss (the render still catches it).
"""

from __future__ import annotations

import ast
import builtins
import functools
import inspect
import os
import re
import warnings

ASSET = re.compile(r"^(https?://|.+\.(svg|png|jpe?g|gif|bmp|mp4)$)", re.IGNORECASE)


@functools.cache
def _manim():
    import manim
    import numpy as np

    names = set(dir(manim)) | set(dir(builtins)) | {"np", "numpy", "math", "random", "self"}
    attrs = set()
    for v in vars(manim).values():
        if inspect.isclass(v) or inspect.ismodule(v):
            attrs |= set(dir(v))
    import math
    import random

    for t in (np.ndarray, list, dict, str, tuple, set, float, int, np, np.linalg, np.random, math, random):
        attrs |= set(dir(t))
    return vars(manim), names, attrs


@functools.cache
def _accepts(cls):
    """Keyword names a class's constructor chain accepts, or None when some link takes **kwargs to the end."""
    names = set()
    for k in cls.__mro__:
        init = k.__dict__.get("__init__")
        if init is None:
            continue
        try:
            sig = inspect.signature(init)
        except (TypeError, ValueError):
            return None
        names |= {p.name for p in sig.parameters.values() if p.kind in (p.POSITIONAL_OR_KEYWORD, p.KEYWORD_ONLY)}
        if not any(p.kind is p.VAR_KEYWORD for p in sig.parameters.values()):
            return names
    return None


def check(code):
    """Problems as [{"line", "kind", "message"}], first by line."""
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # invalid escapes in LaTeX strings are the renderer's business
            tree = ast.parse(code)
    except SyntaxError as exc:
        return [{"line": exc.lineno, "kind": "syntax", "message": f"{type(exc).__name__}: {exc.msg}"}]
    space, names, attrs = _manim()
    defined = set(names)
    own_attrs = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, (ast.Store, ast.Del)):
            defined.add(node.id)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            defined.add(node.name)
            own_attrs.add(node.name)
        elif isinstance(node, ast.arg):
            defined.add(node.arg)
        elif isinstance(node, ast.alias):
            defined.add((node.asname or node.name).split(".")[0])
        elif isinstance(node, ast.ExceptHandler) and node.name:
            defined.add(node.name)
        elif isinstance(node, ast.Attribute) and isinstance(node.ctx, ast.Store):
            own_attrs.add(node.attr)
        elif isinstance(node, (ast.Global, ast.Nonlocal)):
            defined |= set(node.names)
    out = []
    for node in ast.walk(tree):
        line = getattr(node, "lineno", None)
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load) and node.id not in defined:
            out.append({"line": line, "kind": "name", "message": f"NameError: name '{node.id}' is not defined"})
        elif isinstance(node, ast.Call):
            f = node.func
            if isinstance(f, ast.Name) and inspect.isclass(space.get(f.id)):
                ok = _accepts(space[f.id])
                for kw in node.keywords:
                    if kw.arg and ok is not None and kw.arg not in ok:
                        out.append({"line": line, "kind": "kwarg", "message":
                                    f"TypeError: {f.id}() does not accept the keyword '{kw.arg}' in this Manim"})  # fmt: skip
                arg = node.args[0] if node.args else None
                if (f.id in ("SVGMobject", "ImageMobject") and isinstance(arg, ast.Constant) and isinstance(arg.value, str)
                        and (ASSET.match(arg.value.strip()) and (arg.value.startswith("http") or not os.path.exists(arg.value)))):
                    out.append({"line": line, "kind": "asset", "message":
                                f"{f.id}('{arg.value[:60]}'): no such file here; draw it from shapes instead"})  # fmt: skip
            elif (isinstance(f, ast.Attribute) and f.attr not in attrs and f.attr not in own_attrs
                  and not f.attr.startswith("set_") and not (f.attr.startswith("get_") and not node.args)):
                # Mobject turns unknown set_x / get_x() into setters and getters at run time; get_x(arg) fails
                out.append({"line": line, "kind": "method", "message":
                            f"AttributeError: no Manim object has a method '{f.attr}'"})  # fmt: skip
    seen, uniq = set(), []
    for p in sorted(out, key=lambda p: p["line"] or 0):
        if (p["line"], p["message"]) not in seen:
            seen.add((p["line"], p["message"]))
            uniq.append(p)
    return uniq


def safe_splice(code, a, b, new_lines):
    """Replace lines a..b with new_lines only if the result parses; first as given, then re-indented to the old block's
    indentation. None when neither parses (the caller then escalates to a larger scope instead of breaking the file)."""
    rows = code.splitlines()
    old = rows[a - 1 : b]
    indent = min((len(r) - len(r.lstrip()) for r in old if r.strip()), default=0)
    body = [r for r in new_lines]
    nonblank = [r for r in body if r.strip()]
    shift = min((len(r) - len(r.lstrip()) for r in nonblank), default=0)
    reindented = [(" " * indent + r[shift:]) if r.strip() else "" for r in body]
    for cand in (body, reindented):
        text = "\n".join(rows[: a - 1] + cand + rows[b:]) + "\n"
        try:
            ast.parse(text)
            return text
        except SyntaxError:
            continue
    return None
