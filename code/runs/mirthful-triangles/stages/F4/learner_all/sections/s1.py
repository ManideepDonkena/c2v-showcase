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

        self.play(Create(triangle), Write(a_label), Write(b_label), Write(c_label))
        self.wait(1)

        # Label sides: c is longest, a is shortest
        c_label.shift(0.5 * UP)
        a_label.shift(0.5 * DOWN)
        self.play(
            c_label.animate.set_color(BLUE),
            a_label.animate.set_color(GREEN)
        )
        self.wait(1)

        # Inequality text
        left = MathTex("2 \\times c", font_size=32).to_edge(LEFT, buff=1.5)
        inequality = MathTex("\\leq", font_size=32).next_to(left, RIGHT, buff=0.3)
        right = MathTex("3 \\times a", font_size=32).next_to(inequality, RIGHT, buff=0.3)

        self.play(Write(left), Write(inequality), Write(right))
        self.wait(1.5)

        # Show triangle with sides 5, 7, 8
        self.play(FadeOut(triangle), FadeOut(a_label), FadeOut(b_label), FadeOut(c_label))

        triangle2 = Polygon(
            [0, 0, 0], [4, 0, 0], [2, 3.5, 0],
            color=WHITE, fill_opacity=0.5
        )
        a_label2 = MathTex("5", font_size=24).next_to(triangle2.get_vertices()[0], DOWN)
        b_label2 = MathTex("7", font_size=24).next_to(triangle2.get_vertices()[1], DOWN)
        c_label2 = MathTex("8", font_size=24).next_to(triangle2.get_vertices()[2], UP)

        self.play(Create(triangle2), Write(a_label2), Write(b_label2), Write(c_label2))
        self.wait(1)

        # Show rule check
        rule_text = Text("Check the rule:", font_size=24).to_edge(UP, buff=0.5)
        self.play(Write(rule_text))
        self.wait(0.5)

        calc = MathTex("2 \\times 8 \\leq 3 \\times 5", font_size=32).move_to(ORIGIN)
        self.play(Write(calc))
        self.wait(1.5)

        # Show result of calculation
        result = MathTex("16 \\leq 15", font_size=32).move_to(ORIGIN)
        self.play(Transform(calc, result))
        self.wait(1.5)

        # Red X or pulse red to indicate failure
        cross = Cross(calc, color=RED, stroke_width=8)
        self.play(Create(cross))
        self.wait(1.5)

        # Fade out everything except title and rule text
        self.play(
            FadeOut(calc),
            FadeOut(cross),
            FadeOut(rule_text),
            FadeOut(left),
            FadeOut(inequality),
            FadeOut(right),
            FadeOut(title)
        )
        self.wait(0.5)

        # Show worked examples
        example1 = Text("Example 1: sides 4, 5, 6", font_size=24).to_edge(UP)
        self.play(Write(example1))
        self.wait(0.5)

        calc1 = MathTex("2 \\times 6 = 12 \\leq 3 \\times 4 = 12", font_size=28).move_to(ORIGIN)
        self.play(Write(calc1))
        self.wait(1.5)

        # Green pulse for mirthful
        triangle_pulse = triangle2.copy().set_color(GREEN).set_fill(GREEN, opacity=0.3)
        self.play(
            FadeOut(calc1),
            FadeIn(triangle_pulse)
        )
        self.wait(1.5)

        # Show second example
        self.play(FadeOut(example1), FadeOut(triangle_pulse))
        example2 = Text("Example 2: sides 3, 4, 5", font_size=24).to_edge(UP)
        self.play(Write(example2))
        self.wait(0.5)

        calc2 = MathTex("2 \\times 5 = 10 > 3 \\times 3 = 9", font_size=28).move_to(ORIGIN)
        self.play(Write(calc2))
        self.wait(1.5)

        # Red cross for non-mirthful
        cross2 = Cross(calc2, color=RED, stroke_width=8)
        self.play(Create(cross2))
        self.wait(1.5)

        self.play(
            FadeOut(calc2),
            FadeOut(cross2),
            FadeOut(example2)
        )
        self.wait(0.5)
