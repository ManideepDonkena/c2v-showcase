from manim import *


class S1(Scene):
    def construct(self):
        title = Text("Overlap test", font_size=36).to_edge(UP)
        box = Square(side_length=2)
        label = Text("side a", font_size=32).move_to(box.get_right())
        note = Text("this note sits on the label", font_size=28).move_to(label.get_center() + 0.1 * DOWN)
        self.play(Write(title))
        label.shift(0.74 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(box), FadeIn(label))
        note.shift(0.0 * RIGHT + -1.2 * UP)  # layout: separation vector
        self.play(FadeIn(note))
        self.wait(1)
