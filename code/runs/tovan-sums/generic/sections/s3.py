from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Absorbing Element (-1)", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Setup circles
        minus_one = Circle(radius=1.2, color=RED, fill_color=RED, fill_opacity=0.8)
        minus_one_label = MathTex(r"-1", font_size=40).move_to(minus_one.get_center())
        b = Circle(radius=1.2, color=BLUE, fill_color=BLUE, fill_opacity=0.8)
        b_label = MathTex(r"b", font_size=40).move_to(b.get_center())

        # Position
        minus_one.shift(LEFT * 3)
        b.shift(RIGHT * 3)

        # Show initial setup
        self.play(Create(minus_one), Write(minus_one_label))
        b_label.shift(0.0 * RIGHT + 0.43 * UP)  # layout: separation vector
        self.play(Create(b), Write(b_label))
        self.wait(1)

        # Move towards each other
        self.play(
            minus_one.animate.shift(RIGHT * 3),
            b.animate.shift(LEFT * 3),
            run_time=2
        )

        # Collision effect
        self.play(
            FadeOut(b),
            FadeOut(b_label),
            run_time=0.5
        )
        self.wait(0.5)

        # Show result
        result_text = MathTex(r"(-1) \oplus b = -1", font_size=36).next_to(minus_one, DOWN)
        self.play(Write(result_text))
        self.wait(2)

        # Narration text
        narration = Text("The number negative one acts as an absorbing element.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)
        self.play(FadeOut(narration))

        # Reinforce the rule
        rule_text = Text("(-1) ⊕ b = -1", font_size=30).move_to(ORIGIN)
        rule_text.shift(0.0 * RIGHT + 0.47 * UP)  # layout: separation vector
        self.play(ReplacementTransform(result_text, rule_text))
        self.wait(2)

        self.play(FadeOut(rule_text), FadeOut(minus_one), FadeOut(minus_one_label), FadeOut(title))
        self.wait(0.5)
