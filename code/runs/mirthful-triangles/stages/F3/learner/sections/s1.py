from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining Mirth", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Triangle with sides a, b, c
        triangle = Polygon(
            [0, 0, 0], [4, 0, 0], [2, 3, 0],
            color=WHITE
        )
        triangle.shift(LEFT * 1.5)
        a_label = MathTex("a", font_size=24).next_to(triangle.get_left(), DL)
        b_label = MathTex("b", font_size=24).next_to(triangle.get_bottom(), DOWN)
        c_label = MathTex("c", font_size=24).next_to(triangle.get_top(), UP)

        c_label.shift(0.0 * RIGHT + 0.4 * UP)  # layout: separation vector
        self.play(Create(triangle), Write(a_label), Write(b_label), Write(c_label))
        self.wait(1)

        # Inequality text
        left_side = MathTex("2 \\times c", font_size=30)
        right_side = MathTex("3 \\times a", font_size=30)
        inequality = MathTex("\\leq", font_size=30)

        left_side.next_to(triangle, LEFT)
        inequality.next_to(left_side, RIGHT)
        right_side.next_to(inequality, RIGHT)

        self.play(Write(left_side), Write(inequality), Write(right_side))
        self.wait(1.5)

        # Show rule
        rule_text = Text("A triangle is mirthful if", font_size=24).to_edge(DOWN)
        rule_text2 = Text("2 × longest ≤ 3 × shortest", font_size=24).next_to(rule_text, DOWN)
        rule_text2.shift(0.0 * RIGHT + 0.23 * UP)  # layout: separation vector
        self.play(Write(rule_text), Write(rule_text2))
        self.wait(1.5)

        # Fade out rule
        self.play(FadeOut(rule_text), FadeOut(rule_text2))

        # Example triangle: 2, 3, 4
        example_triangle = Polygon(
            [0, 0, 0], [4, 0, 0], [2, 2.5, 0],
            color=WHITE
        )
        example_triangle.shift(RIGHT * 1.5)
        a2_label = MathTex("2", font_size=24).next_to(example_triangle.get_left(), DL)
        b2_label = MathTex("3", font_size=24).next_to(example_triangle.get_bottom(), DOWN)
        c2_label = MathTex("4", font_size=24).next_to(example_triangle.get_top(), UP)

        self.play(Create(example_triangle), Write(a2_label), Write(b2_label), Write(c2_label))
        self.wait(1)

        # Question
        question = Text("Check the rule:", font_size=24).to_edge(DOWN)
        question2 = Text("Is 2 × longest ≤ 3 × shortest?", font_size=24).next_to(question, DOWN)
        question2.shift(0.0 * RIGHT + 0.23 * UP)  # layout: separation vector
        self.play(Write(question), Write(question2))
        self.wait(1.5)

        # Calculation
        calc = MathTex("2 \\times 4 \\leq 3 \\times 2", font_size=30)
        calc.shift(DOWN * 1.5)
        self.play(Write(calc))
        self.wait(1.5)

        # Result
        result = MathTex("8 \\leq 6", font_size=30)
        result.next_to(calc, DOWN)
        self.play(Write(result))
        self.wait(1.5)

        # Red X
        cross = Cross(calc)
        self.play(Create(cross))
        self.wait(1.5)

        # Fade out everything except triangle and labels
        self.play(FadeOut(title), FadeOut(left_side), FadeOut(inequality), FadeOut(right_side),
                  FadeOut(question), FadeOut(question2), FadeOut(calc), FadeOut(result), FadeOut(cross))

        # Show that it's not mirthful
        not_mirthful = Text("Not mirthful", font_size=24).to_edge(DOWN)
        self.play(Write(not_mirthful))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(example_triangle), FadeOut(a2_label), FadeOut(b2_label), FadeOut(c2_label),
                  FadeOut(not_mirthful))
        self.wait(0.5)
