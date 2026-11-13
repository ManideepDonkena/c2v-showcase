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

        # Arrow down to formula
        arrow = Arrow(start=a_op_b.get_bottom(), end=a_op_b.get_bottom() + DOWN * 1.5, buff=0.1)
        self.play(GrowArrow(arrow))
        self.wait(0.5)

        # Formula: a + b + (a × b)
        formula = MathTex("a + b + (a \\times b)", font_size=40)
        formula.next_to(arrow, DOWN)
        self.play(Write(formula))
        self.wait(2)

        # Fade out formula and arrow
        self.play(FadeOut(formula), FadeOut(arrow))

        # Show circles for a and b
        circle_a = Circle(radius=0.6, color=BLUE).shift(LEFT * 2)
        circle_b = Circle(radius=0.6, color=GREEN).shift(RIGHT * 2)
        label_a = Text("a", font_size=24).move_to(circle_a.get_center())
        label_b = Text("b", font_size=24).move_to(circle_b.get_center())

        self.play(Create(circle_a), Create(circle_b), Write(label_a), Write(label_b))
        self.wait(1)

        # Merge into one circle
        merged_circle = Circle(radius=1.2, color=YELLOW).shift(DOWN * 0.5)
        result_label = Text("Result", font_size=24).move_to(merged_circle.get_center())
        self.play(
            Transform(circle_a, merged_circle),
            Transform(circle_b, merged_circle),
            Write(result_label),
            FadeOut(label_a),
            FadeOut(label_b)
        )
        self.wait(1.5)

        # Rules
        rule1 = Text("1) Order does not matter: a ⊕ b = b ⊕ a", font_size=24)
        rule2 = Text("2) 0 is neutral: 0 ⊕ b = b", font_size=24)
        rule3 = Text("3) -1 swallows everything: (-1) ⊕ b = -1", font_size=24)
        rule4 = Text("4) Chain works left to right", font_size=24)
        example = Text("Example: 2 ⊕ 3 = 2 + 3 + 6 = 11", font_size=24)

        rules_group = VGroup(rule1, rule2, rule3, rule4, example).arrange(DOWN, buff=0.4).to_edge(LEFT)
        rules_group.shift(UP * 0.5)

        rule3.shift(0.0 * RIGHT + 0.48 * UP)  # layout: separation vector
        rule3.shift(0.0 * RIGHT + -0.23 * UP)  # layout: separation vector
        self.play(Write(rules_group))
        self.wait(3)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(a_op_b), FadeOut(rules_group))
        self.wait(0.5)
