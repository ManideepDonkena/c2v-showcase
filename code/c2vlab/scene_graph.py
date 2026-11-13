"""SGA's symbolic scene graph, without rendering (arXiv 2607.18116, "partial execution").

The section's construct() runs with Scene.play patched: every animation jumps to its end (begin, interpolate(1),
finish), so nothing is drawn and a scene runs in about a second. After each play the visible objects are recorded:
    kind   Text | Geom | Mark | Deco
    box    [x0, y0, x1, y1] in scene units (frame is 14.22 x 8)
    name   the variable in construct() that holds it (or its group), None if none
    line   the line in the section's file where the object was created
An exception stops the run but keeps the states recorded so far (SGA keeps partial graphs too).

    python -m c2vlab.scene_graph <section.py> <ClassName> <out.json>
"""

from __future__ import annotations

import importlib.util
import json
import sys
import time
import traceback
from pathlib import Path

TEXT = ("Text", "MarkupText", "Paragraph", "MathTex", "Tex", "SingleStringMathTex", "DecimalNumber", "Integer",
        "Variable", "Title", "BulletedList")  # fmt: skip
MARK = ("Arrow", "Vector", "DoubleArrow", "Line", "DashedLine", "Dot", "Brace", "BraceLabel", "Arc", "Angle",
        "RightAngle", "SurroundingRectangle", "Cross", "CurvedArrow", "TangentLine", "DashedVMobject")  # fmt: skip
DECO = ("NumberPlane", "BackgroundRectangle", "ScreenRectangle", "FullScreenRectangle")
GROUPS = ("VGroup", "Group", "VDict")


def kind_of(mob):
    names = [c.__name__ for c in type(mob).__mro__]
    for k, table in (("Text", TEXT), ("Deco", DECO), ("Mark", MARK)):
        if any(n in table for n in names):
            return k
    return "Geom"


def visible(mob):
    for m in mob.family_members_with_points():
        try:
            if max(m.get_fill_opacity(), m.get_stroke_opacity()) > 0.05:
                return True
        except Exception:  # noqa: BLE001 - ImageMobject and friends have no opacity API
            return True
    return False


def box(mob):
    lo, hi = mob.get_corner([-1, -1, 0]), mob.get_corner([1, 1, 0])
    return [round(float(lo[0]), 3), round(float(lo[1]), 3), round(float(hi[0]), 3), round(float(hi[1]), 3)]


def leaves(mob):
    """Objects at SGA's level: a text or a shape is one object; groups are opened."""
    if type(mob).__name__ in GROUPS or (kind_of(mob) == "Geom" and type(mob).__name__ in ("VMobject", "Mobject")):
        for sub in mob.submobjects:
            yield from leaves(sub)
    else:
        yield mob


def run(path, cls, out):
    import manim
    from manim.animation.animation import prepare_animation

    created, names, states = {}, {}, []
    # `created` and `names` are keyed by id(). Python gives a freed object's id to a later one, which then inherited
    # the dead object's line or name (the same code gave 7, 10 and 11 conflicts). Every object recorded is kept alive.
    alive = {}
    target = str(path)

    def site():
        f = sys._getframe(2)
        while f is not None:
            if f.f_code.co_filename == target:
                return f
            f = f.f_back
        return None

    original_init = manim.Mobject.__init__

    def init(self, *a, **k):
        original_init(self, *a, **k)
        f = site()
        if f is not None:
            alive[id(self)] = self
            created.setdefault(id(self), f.f_lineno)

    manim.Mobject.__init__ = init

    def remember_names(frame):
        for var, val in frame.f_locals.items():
            if isinstance(val, manim.Mobject):
                names[id(val)] = var
                for m in val.get_family():
                    alive[id(m)] = m
                    names.setdefault(id(m), var)

    def record(scene, line):
        objs = []
        for top in scene.mobjects:
            for m in leaves(top):
                if m.has_points() or m.submobjects:
                    if not visible(m):
                        continue
                    b = box(m)
                    objs.append({"kind": kind_of(m), "box": b, "name": names.get(id(m)) or names.get(id(top)),
                                 "line": created.get(id(m)) or created.get(id(top)), "type": type(m).__name__})  # fmt: skip
        states.append({"after_line": line, "objects": objs})

    def play(self, *args, **kwargs):
        f = site()
        if f is not None:
            remember_names(f)
        anims = [prepare_animation(a) for a in args]
        self.add_mobjects_from_animations(anims)  # as Manim's own play: a copy being transformed joins the scene first
        for anim in anims:
            anim._setup_scene(self)
            anim.begin()
            anim.interpolate(1.0)
            anim.finish()
            anim.clean_up_from_scene(self)
        self.update_mobjects(0)
        record(self, f.f_lineno if f is not None else None)

    manim.Scene.play = play
    manim.Scene.wait = lambda self, *a, **k: None

    error = None
    try:
        spec = importlib.util.spec_from_file_location("section", target)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        getattr(module, cls)().construct()
    except Exception as exc:  # noqa: BLE001 - partial execution: keep what was recorded
        tb = traceback.extract_tb(exc.__traceback__)
        line = next((fr.lineno for fr in reversed(tb) if fr.filename == target), None)
        error = {"type": type(exc).__name__, "message": str(exc)[:500], "line": line}
    Path(out).write_text(json.dumps({"states": states, "error": error}, indent=1))


def graph(path, cls, out):
    """Run in a subprocess (Manim is patched in place) and return the recorded graph."""
    import subprocess

    from . import timing

    out = Path(out)
    out.unlink(missing_ok=True)  # never read the graph of an earlier version of the code
    began = time.time()
    try:
        r = subprocess.run(
            [sys.executable, "-m", "c2vlab.scene_graph", str(path), cls, str(out)],
            capture_output=True,
            text=True,
            timeout=180,
            check=False,
            cwd=str(Path(__file__).resolve().parents[1]),
        )
        stderr = r.stderr
    except subprocess.TimeoutExpired:
        stderr = "timed out after 180 s"
    try:
        g = json.loads(out.read_text())
    except (OSError, ValueError):
        g = {"states": [], "error": {"type": "Crash", "message": stderr[-500:], "line": None}}
    timing.log("scene_graph", path, cls, time.time() - began, not g.get("error"))
    return g


if __name__ == "__main__":
    run(Path(sys.argv[1]).resolve(), sys.argv[2], sys.argv[3])
