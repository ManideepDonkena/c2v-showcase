from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Absorbing Element (-1)", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial circles
        minus_one = Circle(radius=1.2, color=BLUE, fill_color=BLUE, fill_opacity=0.8)
        minus_one_label = MathTex(r"-1", font_size=40).move_to(minus_one.get_center())
        b = Circle(radius=1.2, color=RED, fill_color=RED, fill_opacity=0.8)
        b_label = MathTex(r"b", font_size=40).move_to(b.get_center())

        # Position circles
        minus_one.to_edge(LEFT, buff=2)
        b.to_edge(RIGHT, buff=2)

        self.play(Create(minus_one), Write(minus_one_label))
        b_label.shift(0.0 * RIGHT + 0.43 * UP)  # layout: separation vector
        self.play(Create(b), Write(b_label))
        self.wait(1)

        # Move -1 towards b
        self.play(minus_one.animate.move_to((minus_one.get_center() + b.get_center()) / 2), run_time=1.5)
        self.wait(0.5)

        # Collision effect: b disappears, -1 stays
        self.play(FadeOut(b), FadeOut(b_label))
        self.wait(0.5)

        # Show result
        result_text = MathTex(r"(-1) \oplus b = -1", font_size=32).to_edge(DOWN)
        self.play(Write(result_text))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(minus_one), FadeOut(minus_one_label), FadeOut(result_text))
        self.wait(0.5)
