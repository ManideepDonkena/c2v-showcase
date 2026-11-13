from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Peano Curve Construction", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial line segment
        initial_line = Line(start=LEFT * 3, end=RIGHT * 3, color=WHITE)
        self.play(Create(initial_line))
        self.wait(1)

        # First iteration: U shape
        u_shape = VGroup(
            Line(start=LEFT * 3, end=LEFT * 3 + UP * 1.5, color=WHITE),
            Line(start=LEFT * 3 + UP * 1.5, end=RIGHT * 3 + UP * 1.5, color=WHITE),
            Line(start=RIGHT * 3 + UP * 1.5, end=RIGHT * 3, color=WHITE)
        )
        self.play(Transform(initial_line, u_shape))
        self.wait(1)

        # Second iteration
        u_shape2 = VGroup(
            Line(start=LEFT * 3, end=LEFT * 3 + UP * 0.5, color=WHITE),
            Line(start=LEFT * 3 + UP * 0.5, end=LEFT * 3 + UP * 1.0, color=WHITE),
            Line(start=LEFT * 3 + UP * 1.0, end=LEFT * 3 + UP * 1.5, color=WHITE),
            Line(start=LEFT * 3 + UP * 1.5, end=LEFT * 3 + UP * 2.0, color=WHITE),
            Line(start=LEFT * 3 + UP * 2.0, end=RIGHT * 3 + UP * 2.0, color=WHITE),
            Line(start=RIGHT * 3 + UP * 2.0, end=RIGHT * 3 + UP * 1.5, color=WHITE),
            Line(start=RIGHT * 3 + UP * 1.5, end=RIGHT * 3 + UP * 1.0, color=WHITE),
            Line(start=RIGHT * 3 + UP * 1.0, end=RIGHT * 3 + UP * 0.5, color=WHITE),
            Line(start=RIGHT * 3 + UP * 0.5, end=RIGHT * 3, color=WHITE)
        )
        self.play(Transform(u_shape, u_shape2))
        self.wait(1)

        # Third iteration - simplified for clarity
        final_curve = VGroup(
            Line(start=LEFT * 3, end=LEFT * 3 + UP * 0.25, color=WHITE),
            Line(start=LEFT * 3 + UP * 0.25, end=LEFT * 3 + UP * 0.5, color=WHITE),
            Line(start=LEFT * 3 + UP * 0.5, end=LEFT * 3 + UP * 0.75, color=WHITE),
            Line(start=LEFT * 3 + UP * 0.75, end=LEFT * 3 + UP * 1.0, color=WHITE),
            Line(start=LEFT * 3 + UP * 1.0, end=LEFT * 3 + UP * 1.25, color=WHITE),
            Line(start=LEFT * 3 + UP * 1.25, end=LEFT * 3 + UP * 1.5, color=WHITE),
            Line(start=LEFT * 3 + UP * 1.5, end=LEFT * 3 + UP * 1.75, color=WHITE),
            Line(start=LEFT * 3 + UP * 1.75, end=LEFT * 3 + UP * 2.0, color=WHITE),
            Line(start=LEFT * 3 + UP * 2.0, end=RIGHT * 3 + UP * 2.0, color=WHITE),
            Line(start=RIGHT * 3 + UP * 2.0, end=RIGHT * 3 + UP * 1.75, color=WHITE),
            Line(start=RIGHT * 3 + UP * 1.75, end=RIGHT * 3 + UP * 1.5, color=WHITE),
            Line(start=RIGHT * 3 + UP * 1.5, end=RIGHT * 3 + UP * 1.25, color=WHITE),
            Line(start=RIGHT * 3 + UP * 1.25, end=RIGHT * 3 + UP * 1.0, color=WHITE),
            Line(start=RIGHT * 3 + UP * 1.0, end=RIGHT * 3 + UP * 0.75, color=WHITE),
            Line(start=RIGHT * 3 + UP * 0.75, end=RIGHT * 3 + UP * 0.5, color=WHITE),
            Line(start=RIGHT * 3 + UP * 0.5, end=RIGHT * 3 + UP * 0.25, color=WHITE),
            Line(start=RIGHT * 3 + UP * 0.25, end=RIGHT * 3, color=WHITE)
        )
        self.play(Transform(u_shape2, final_curve))
        self.wait(1)

        # Show key message
        msg = Text("Infinite recursion", font_size=24).to_edge(UP)
        self.play(ReplacementTransform(title, msg))
        self.wait(0.5)

        msg2 = Text("Twists and folds", font_size=24).next_to(msg, DOWN)
        self.play(Write(msg2))
        self.wait(0.5)

        msg3 = Text("Dense coverage", font_size=24).next_to(msg2, DOWN)
        self.play(Write(msg3))
        self.wait(1)

        # Fade out
        self.play(FadeOut(msg), FadeOut(msg2), FadeOut(msg3), FadeOut(final_curve))
        self.wait(0.5)
