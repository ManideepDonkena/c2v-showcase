from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Absorbing Element (-1)", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show the operation definition
        operation_def = MathTex("a \\oplus b = a + b + ab", font_size=32)
        operation_def.next_to(title, DOWN, buff=0.5)
        self.play(Write(operation_def))
        self.wait(1)

        # Show rule 3: -1 swallows everything
        rule = Text("Rule 3: (-1) ⊕ b = -1", font_size=28)
        rule.next_to(operation_def, DOWN, buff=0.5)
        self.play(Write(rule))
        self.wait(1.5)

        # Create circles
        minus_one_circle = Circle(radius=1.2, color=RED, fill_color=RED, fill_opacity=0.8)
        minus_one_circle.move_to(LEFT * 3)
        minus_one_label = MathTex("-1", font_size=40).move_to(minus_one_circle.get_center())

        b_circle = Circle(radius=1.2, color=BLUE, fill_color=BLUE, fill_opacity=0.8)
        b_circle.move_to(RIGHT * 3)
        b_label = MathTex("b", font_size=40).move_to(b_circle.get_center())

        # Show initial setup
        self.play(Create(minus_one_circle), Create(b_circle))
        self.play(Write(minus_one_label), Write(b_label))
        self.wait(1)

        # Move circles towards each other
        self.play(
            minus_one_circle.animate.move_to(ORIGIN),
            b_circle.animate.move_to(ORIGIN),
            run_time=1.5
        )

        # Show absorption effect
        self.play(
            FadeOut(b_circle),
            FadeOut(b_label),
            run_time=0.7
        )
        self.wait(0.3)

        # Show result: only -1 remains
        result_text = MathTex("= -1", font_size=40).next_to(minus_one_label, DOWN, buff=0.5)
        self.play(Write(result_text))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(operation_def),
            FadeOut(rule),
            FadeOut(minus_one_circle),
            FadeOut(minus_one_label),
            FadeOut(result_text),
            run_time=0.7
        )
        self.wait(0.3)
