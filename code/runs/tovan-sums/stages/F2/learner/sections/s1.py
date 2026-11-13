from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Definition and Formula", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Main expression: a ⊕ b
        a_op_b = MathTex("a \\oplus b", font_size=40)
        a_op_b.move_to(ORIGIN)
        self.play(Write(a_op_b))
        self.wait(1)

        # Arrow pointing down to formula
        arrow = Arrow(start=a_op_b.get_bottom(), end=a_op_b.get_bottom() + DOWN * 0.5, buff=0.1)
        self.play(GrowArrow(arrow))
        self.wait(0.5)

        # Formula: a + b + (a × b)
        formula = MathTex("a + b + (a \\times b)", font_size=40)
        formula.next_to(arrow, DOWN, buff=0.3)
        self.play(Write(formula))
        self.wait(1.5)

        # Circles for a and b
        circle_a = Circle(radius=0.6, color=BLUE).move_to(LEFT * 2)
        circle_b = Circle(radius=0.6, color=GREEN).move_to(RIGHT * 2)
        label_a = Text("a", font_size=24).move_to(circle_a.get_center())
        label_b = Text("b", font_size=24).move_to(circle_b.get_center())

        self.play(Create(circle_a), Create(circle_b), Write(label_a), Write(label_b))
        self.wait(1)

        # Merge into result circle
        result_circle = Circle(radius=1.0, color=YELLOW).move_to(ORIGIN)
        result_label = Text("Result", font_size=24).move_to(result_circle.get_center())
        result_label.shift(0.0 * RIGHT + 0.44 * UP)  # layout: separation vector
        result_circle.shift(0.0 * RIGHT + 0.29 * UP)  # layout: separation vector
        self.play(
            ReplacementTransform(circle_a, result_circle),
            Transform(circle_b, result_circle),
            FadeOut(label_a),
            FadeOut(label_b),
            Write(result_label)
        )
        self.wait(1.5)

        # Comparison: 2 ⊕ 3 vs 2 × 3
        example_text = Text("Example:", font_size=24).to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(example_text))
        self.wait(0.5)

        eq1 = MathTex("2 \\oplus 3 = 2 + 3 + (2 \\times 3) = 11", font_size=28)
        eq2 = MathTex("2 \\times 3 = 6", font_size=28)
        eq1.next_to(example_text, DOWN, buff=0.3)
        eq2.next_to(eq1, DOWN, buff=0.3)

        self.play(Write(eq1))
        self.wait(1)
        eq2.shift(0.0 * RIGHT + 0.24 * UP)  # layout: separation vector
        self.play(Write(eq2))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(a_op_b),
            FadeOut(arrow),
            FadeOut(formula),
            FadeOut(result_circle),
            FadeOut(result_label),
            FadeOut(example_text),
            FadeOut(eq1),
            FadeOut(eq2),
            FadeOut(title)
        )
        self.wait(0.5)
