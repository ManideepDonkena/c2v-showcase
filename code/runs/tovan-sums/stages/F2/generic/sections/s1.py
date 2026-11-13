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
        self.play(
            ReplacementTransform(circle_a, result_circle),
            Transform(circle_b, result_circle),
            Write(result_label)
        )
        self.wait(1.5)

        # Clear the scene
        self.play(FadeOut(a_op_b), FadeOut(title), FadeOut(result_circle), FadeOut(result_label), FadeOut(label_a), FadeOut(label_b))

        # Show rules one by one
        rule1 = Text("1) Order does not matter: a ⊕ b = b ⊕ a", font_size=24)
        rule2 = Text("2) 0 is neutral: 0 ⊕ b = b", font_size=24)
        rule3 = Text("3) -1 swallows everything: (-1) ⊕ b = -1", font_size=24)
        rule4 = Text("4) Chain works left to right", font_size=24)
        example = Text("Example: 2 ⊕ 3 = 2 + 3 + 6 = 11", font_size=24)

        rules = VGroup(rule1, rule2, rule3, rule4, example).arrange(DOWN, buff=0.4).move_to(UP * 0.5)
        self.play(Write(rules[0]))
        self.wait(2)
        self.play(Write(rules[1]))
        self.wait(2)
        self.play(Write(rules[2]))
        self.wait(2)
        self.play(Write(rules[3]))
        self.wait(2)
        self.play(Write(rules[4]))
        self.wait(2)

        self.play(FadeOut(rules))
        self.wait(0.5)
