from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Peano Curve Construction", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial line segment
        initial_line = Line(start=LEFT * 3, end=RIGHT * 3, color=BLUE)
        self.play(Create(initial_line))
        self.wait(1)

        # First iteration: U shape
        u_shape = VGroup(
            Line(start=LEFT * 3, end=UP * 3, color=BLUE),
            Line(start=UP * 3, end=RIGHT * 3, color=BLUE),
            Line(start=RIGHT * 3, end=DOWN * 3, color=BLUE),
            Line(start=DOWN * 3, end=LEFT * 3, color=BLUE)
        )
        self.play(Transform(initial_line, u_shape))
        self.wait(1.5)

        # Second iteration
        second_iteration = VGroup(
            Line(start=LEFT * 3, end=UP * 3, color=BLUE),
            Line(start=UP * 3, end=RIGHT * 3, color=BLUE),
            Line(start=RIGHT * 3, end=DOWN * 3, color=BLUE),
            Line(start=DOWN * 3, end=LEFT * 3, color=BLUE),
            Line(start=LEFT * 3, end=UP * 3, color=BLUE),
            Line(start=UP * 3, end=RIGHT * 3, color=BLUE),
            Line(start=RIGHT * 3, end=DOWN * 3, color=BLUE),
            Line(start=DOWN * 3, end=LEFT * 3, color=BLUE)
        )
        self.play(Transform(u_shape, second_iteration))
        self.wait(1.5)

        # Third iteration
        third_iteration = VGroup(
            Line(start=LEFT * 3, end=UP * 3, color=BLUE),
            Line(start=UP * 3, end=RIGHT * 3, color=BLUE),
            Line(start=RIGHT * 3, end=DOWN * 3, color=BLUE),
            Line(start=DOWN * 3, end=LEFT * 3, color=BLUE),
            Line(start=LEFT * 3, end=UP * 3, color=BLUE),
            Line(start=UP * 3, end=RIGHT * 3, color=BLUE),
            Line(start=RIGHT * 3, end=DOWN * 3, color=BLUE),
            Line(start=DOWN * 3, end=LEFT * 3, color=BLUE),
            Line(start=LEFT * 3, end=UP * 3, color=BLUE),
            Line(start=UP * 3, end=RIGHT * 3, color=BLUE),
            Line(start=RIGHT * 3, end=DOWN * 3, color=BLUE),
            Line(start=DOWN * 3, end=LEFT * 3, color=BLUE)
        )
        self.play(Transform(second_iteration, third_iteration))
        self.wait(1.5)

        # Show transformation rule
        rule_text = Text("Each segment is rotated and reflected", font_size=24)
        rule_text.to_edge(DOWN)
        self.play(Write(rule_text))
        self.wait(1.5)

        # Fade out everything except title
        self.play(
            FadeOut(initial_line),
            FadeOut(u_shape),
            FadeOut(second_iteration),
            FadeOut(third_iteration),
            FadeOut(rule_text)
        )
        self.wait(0.5)

        # Final message
        final_message = Text("A 1D line fills 2D space", font_size=30)
        final_message.to_edge(DOWN)
        self.play(Write(final_message))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(final_message))
