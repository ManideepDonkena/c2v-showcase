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
            color=WHITE, fill_opacity=0.5
        )
        a_label = MathTex("a", font_size=24).next_to(triangle.get_vertices()[0], DOWN)
        b_label = MathTex("b", font_size=24).next_to(triangle.get_vertices()[1], DOWN)
        c_label = MathTex("c", font_size=24).next_to(triangle.get_vertices()[2], UP)

        # Label longest and shortest
        c_label.set_color(BLUE)
        a_label.set_color(GREEN)

        self.play(Create(triangle), Write(a_label), Write(b_label), Write(c_label))
        self.wait(1)

        # Inequality text
        left = MathTex("2 \\times c", font_size=30)
        right = MathTex("3 \\times a", font_size=30)
        inequality = MathTex("\\leq", font_size=30)

        left.next_to(triangle, LEFT)
        inequality.next_to(left, RIGHT)
        right.next_to(inequality, RIGHT)

        self.play(Write(left), Write(inequality), Write(right))
        self.wait(1.5)

        # Show example triangle with sides 2, 3, 4
        self.play(FadeOut(title), FadeOut(a_label), FadeOut(b_label), FadeOut(c_label))

        triangle2 = Polygon(
            [0, 0, 0], [4, 0, 0], [2, 2.5, 0],
            color=WHITE, fill_opacity=0.5
        )
        a2_label = MathTex("2", font_size=24).next_to(triangle2.get_vertices()[0], DOWN)
        b2_label = MathTex("3", font_size=24).next_to(triangle2.get_vertices()[1], DOWN)
        c2_label = MathTex("4", font_size=24).next_to(triangle2.get_vertices()[2], UP)

        c2_label.set_color(BLUE)
        a2_label.set_color(GREEN)

        self.play(Create(triangle2), Write(a2_label), Write(b2_label), Write(c2_label))
        self.wait(1)

        # Narration text
        narration = Text("Check the rule: Is twice the longest side at most three times the shortest?", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)

        # Calculation
        calc = MathTex("2 \\times 4 \\leq 3 \\times 2", font_size=30)
        calc.next_to(narration, UP)
        self.play(Write(calc))
        self.wait(1.5)

        # Result of calculation
        result = MathTex("8 \\leq 6", font_size=30).next_to(calc, RIGHT)
        self.play(Write(result))
        self.wait(1.5)

        # Red X or pulse red to indicate failure
        cross = Cross(calc)
        self.play(Create(cross), run_time=0.5)
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(triangle2),
            FadeOut(a2_label),
            FadeOut(b2_label),
            FadeOut(c2_label),
            FadeOut(calc),
            FadeOut(result),
            FadeOut(narration),
            FadeOut(cross)
        )
        self.wait(0.5)
