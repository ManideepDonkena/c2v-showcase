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

        # Label longest and shortest
        c_label.set_color(YELLOW)
        a_label.set_color(GREEN)
        self.play(
            c_label.animate.set_color(YELLOW),
            a_label.animate.set_color(GREEN)
        )
        self.wait(0.5)

        # Inequality definition
        inequality = MathTex("2 \\times c", "\\leq", "3 \\times a", font_size=32)
        inequality.arrange(RIGHT, buff=0.5)
        inequality.to_edge(DOWN)

        self.play(Write(inequality[0]))
        self.wait(0.5)
        self.play(Write(inequality[1]))
        self.wait(0.5)
        self.play(Write(inequality[2]))
        self.wait(1)

        # Show mirthful condition
        self.play(triangle.animate.set_color(GREEN))
        self.wait(1)
        self.play(triangle.animate.set_color(WHITE))

        # Example triangle with sides 5,7,8
        self.play(FadeOut(title), FadeOut(triangle), FadeOut(a_label), FadeOut(b_label), FadeOut(c_label))
        self.wait(0.5)

        triangle2 = Polygon(
            [0, 0, 0], [4, 0, 0], [2, 3, 0],
            color=WHITE, fill_opacity=0.5
        )
        a_label2 = MathTex("5", font_size=24).next_to(triangle2.get_vertices()[0], DOWN)
        b_label2 = MathTex("7", font_size=24).next_to(triangle2.get_vertices()[1], DOWN)
        c_label2 = MathTex("8", font_size=24).next_to(triangle2.get_vertices()[2], UP)

        self.play(Create(triangle2), Write(a_label2), Write(b_label2), Write(c_label2))
        self.wait(1)

        # Highlight longest and shortest
        c_label2.set_color(YELLOW)
        a_label2.set_color(GREEN)
        self.play(
            c_label2.animate.set_color(YELLOW),
            a_label2.animate.set_color(GREEN)
        )
        self.wait(0.5)

        # Check the rule: 2 × 8 ≤ 3 × 5
        check_text = Text("Check the rule:", font_size=24).to_edge(UP)
        self.play(Write(check_text))
        self.wait(0.5)

        calc = MathTex("2 \\times 8", "\\leq", "3 \\times 5", font_size=32)
        calc.arrange(RIGHT, buff=0.5)
        calc.to_edge(DOWN)
        self.play(Write(calc[0]))
        self.wait(0.5)
        self.play(Write(calc[1]))
        self.wait(0.5)
        self.play(Write(calc[2]))
        self.wait(1)

        # Evaluate
        result = MathTex("16", "\\leq", "15", font_size=32)
        result.arrange(RIGHT, buff=0.5)
        result.to_edge(DOWN)
        self.play(Transform(calc, result))
        self.wait(1)

        # Show red X or pulse red
        self.play(triangle2.animate.set_color(RED))
        self.wait(1)
        self.play(triangle2.animate.set_color(WHITE))

        # Fade out everything
        self.play(
            FadeOut(check_text),
            FadeOut(calc),
            FadeOut(triangle2),
            FadeOut(a_label2),
            FadeOut(b_label2),
            FadeOut(c_label2)
        )
        self.wait(0.5)
