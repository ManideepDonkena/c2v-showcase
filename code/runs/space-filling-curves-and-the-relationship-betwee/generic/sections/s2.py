from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Length Paradox", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Bounding box
        box = Square(side_length=1, color=WHITE)
        box.move_to(ORIGIN)
        self.play(Create(box))
        self.wait(0.5)

        # Initial curve (iteration 1)
        line1 = Line(start=LEFT * 0.5, end=RIGHT * 0.5, color=YELLOW)
        line1.shift(UP * 0.25)
        length_text_1 = MathTex("3", font_size=24).next_to(line1, DOWN)
        self.play(Create(line1), Write(length_text_1))
        self.wait(1)

        # Iteration 2
        line2a = Line(start=LEFT * 0.5, end=UP * 0.25, color=YELLOW)
        line2b = Line(start=UP * 0.25, end=RIGHT * 0.5, color=YELLOW)
        line2c = Line(start=LEFT * 0.5, end=DOWN * 0.25, color=YELLOW)
        line2d = Line(start=DOWN * 0.25, end=RIGHT * 0.5, color=YELLOW)
        self.play(
            FadeOut(line1),
            FadeOut(length_text_1),
            Create(line2a),
            Create(line2b),
            Create(line2c),
            Create(line2d)
        )
        length_text_2 = MathTex("9", font_size=24).next_to(box, DOWN)
        self.play(Write(length_text_2))
        self.wait(1)

        # Iteration 3
        line3a = Line(start=LEFT * 0.5, end=UP * 0.125, color=YELLOW)
        line3b = Line(start=UP * 0.125, end=RIGHT * 0.5, color=YELLOW)
        line3c = Line(start=LEFT * 0.5, end=DOWN * 0.125, color=YELLOW)
        line3d = Line(start=DOWN * 0.125, end=RIGHT * 0.5, color=YELLOW)
        line3e = Line(start=LEFT * 0.25, end=UP * 0.25, color=YELLOW)
        line3f = Line(start=UP * 0.25, end=RIGHT * 0.25, color=YELLOW)
        line3g = Line(start=LEFT * 0.25, end=DOWN * 0.25, color=YELLOW)
        line3h = Line(start=DOWN * 0.25, end=RIGHT * 0.25, color=YELLOW)
        self.play(
            FadeOut(line2a),
            FadeOut(line2b),
            FadeOut(line2c),
            FadeOut(line2d),
            Create(line3a),
            Create(line3b),
            Create(line3c),
            Create(line3d),
            Create(line3e),
            Create(line3f),
            Create(line3g),
            Create(line3h)
        )
        length_text_3 = MathTex("27", font_size=24).next_to(box, DOWN)
        length_text_3.shift(0.32 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(length_text_3))
        self.wait(1)

        # Final dense curve (approximation)
        # We'll just show the last iteration with a more complex pattern
        # but keep it within bounds
        final_curve = VGroup(
            Line(start=LEFT * 0.5, end=UP * 0.25, color=YELLOW),
            Line(start=UP * 0.25, end=RIGHT * 0.5, color=YELLOW),
            Line(start=LEFT * 0.5, end=DOWN * 0.25, color=YELLOW),
            Line(start=DOWN * 0.25, end=RIGHT * 0.5, color=YELLOW),
            Line(start=LEFT * 0.25, end=UP * 0.125, color=YELLOW),
            Line(start=UP * 0.125, end=RIGHT * 0.25, color=YELLOW),
            Line(start=LEFT * 0.25, end=DOWN * 0.125, color=YELLOW),
            Line(start=DOWN * 0.125, end=RIGHT * 0.25, color=YELLOW),
        )
        self.play(
            FadeOut(line3a),
            FadeOut(line3b),
            FadeOut(line3c),
            FadeOut(line3d),
            FadeOut(line3e),
            FadeOut(line3f),
            FadeOut(line3g),
            FadeOut(line3h),
            FadeOut(length_text_3)
        )
        self.play(Create(final_curve))
        self.wait(1)

        # Show the paradox message
        paradox_text = Text("Notice the paradox:", font_size=24).to_edge(UP)
        self.play(Transform(title, paradox_text))
        self.wait(0.5)

        # Add explanation text
        explanation = Text("As the curve fills the square,\nits total length explodes to infinity.", font_size=24)
        explanation.next_to(box, DOWN)
        explanation.shift(0.0 * RIGHT + -0.32 * UP)  # layout: separation vector
        self.play(Write(explanation))
        self.wait(1.5)

        # Show finite boundary vs infinite length
        finite_boundary = Text("Finite Boundary", font_size=24).next_to(box, LEFT)
        infinite_length = Text("Infinite Length", font_size=24).next_to(box, RIGHT)
        self.play(Write(finite_boundary), Write(infinite_length))
        self.wait(1.5)

        # Final summary
        summary = Text("We have an object of infinite length trapped within a finite boundary.", font_size=24)
        summary.to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(box),
            FadeOut(final_curve),
            FadeOut(explanation),
            FadeOut(finite_boundary),
            FadeOut(infinite_length),
            FadeOut(summary)
        )
        self.wait(0.5)
