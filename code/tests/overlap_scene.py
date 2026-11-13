from manim import *


class S1(Scene):
    def construct(self):
        title = Text("Overlap test", font_size=36).to_edge(UP)
        box = Square(side_length=2)
        label = Text("side a", font_size=32).move_to(box.get_right())
        note = Text("this note sits on the label", font_size=28).move_to(label.get_center() + 0.1 * DOWN)
        self.play(Write(title))
        self.play(Create(box), FadeIn(label))
        self.play(FadeIn(note))
        self.wait(1)
