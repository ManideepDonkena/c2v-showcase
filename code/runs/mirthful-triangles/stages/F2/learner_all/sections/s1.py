from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining Mirth", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial triangle with labels
        a, b, c = 4, 10, 12
        triangle = Polygon(
            [0, 0, 0], [c * 0.5, 0, 0], [0, b * 0.5, 0],
            color=WHITE, fill_opacity=0.3
        )
        triangle.shift(LEFT * 1.5 + DOWN * 0.5)
        a_label = MathTex("a", font_size=24).next_to(triangle.get_left(), DOWN)
        b_label = MathTex("b", font_size=24).next_to(triangle.get_bottom(), LEFT)
        c_label = MathTex("c", font_size=24).next_to(triangle.get_right(), UP)

        triangle.shift(0.0 * RIGHT + -1.66 * UP)  # layout: separation vector
        a_label.shift(-0.21 * RIGHT + 0.0 * UP)  # layout: separation vector
        c_label.shift(0.2 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(triangle), Write(a_label), Write(b_label), Write(c_label))
        self.wait(0.5)

        # Inequality
        inequality = MathTex("2 \\times c \\leq 3 \\times a", font_size=30)
        inequality.to_edge(DOWN)
        self.play(Write(inequality))
        self.wait(1)

        # Algebraic transformation
        transformed = MathTex("c \\leq 1.5 \\times a", font_size=30).to_edge(DOWN)
        self.play(Transform(inequality, transformed))
        self.wait(1)

        # Example: sides 10, 20, 30
        self.play(FadeOut(triangle), FadeOut(a_label), FadeOut(b_label), FadeOut(c_label))
        triangle2 = Polygon(
            [0, 0, 0], [30 * 0.5, 0, 0], [0, 20 * 0.5, 0],
            color=WHITE, fill_opacity=0.3
        )
        triangle2.shift(LEFT * 1.5 + DOWN * 0.5)
        c_label2 = MathTex("30", font_size=24).next_to(triangle2.get_right(), UP)
        a_label2 = MathTex("10", font_size=24).next_to(triangle2.get_left(), DOWN)
        self.play(Create(triangle2), Write(a_label2), Write(c_label2))
        self.wait(0.5)

        two_c = MathTex("2 \\times 30 = 60", font_size=24).to_edge(LEFT)
        three_a = MathTex("3 \\times 10 = 30", font_size=24).to_edge(RIGHT)
        self.play(Write(two_c), Write(three_a))
        self.wait(0.5)

        greater = MathTex("60 > 30", color=RED, font_size=24).next_to(inequality, DOWN)
        self.play(Write(greater))
        self.wait(1)

        # Example: sides 4, 10, 12
        self.play(FadeOut(triangle2), FadeOut(a_label2), FadeOut(c_label2), FadeOut(two_c), FadeOut(three_a), FadeOut(greater))
        triangle3 = Polygon(
            [0, 0, 0], [12 * 0.5, 0, 0], [0, 10 * 0.5, 0],
            color=WHITE, fill_opacity=0.3
        )
        triangle3.shift(LEFT * 1.5 + DOWN * 0.5)
        c_label3 = MathTex("12", font_size=24).next_to(triangle3.get_right(), UP)
        a_label3 = MathTex("4", font_size=24).next_to(triangle3.get_left(), DOWN)
        self.play(Create(triangle3), Write(a_label3), Write(c_label3))
        self.wait(0.5)

        two_c3 = MathTex("2 \\times 12 = 24", font_size=24).to_edge(LEFT)
        three_a3 = MathTex("3 \\times 4 = 12", font_size=24).to_edge(RIGHT)
        self.play(Write(two_c3), Write(three_a3))
        self.wait(0.5)

        result = MathTex("24 \\leq 12", color=RED, font_size=24).next_to(inequality, DOWN)
        cross = Cross(result)
        self.play(Write(result), DrawBorderThenFill(cross))
        self.wait(1)

        # Example: sides 5, 100, 101
        self.play(FadeOut(triangle3), FadeOut(a_label3), FadeOut(c_label3), FadeOut(two_c3), FadeOut(three_a3), FadeOut(result), FadeOut(cross))
        triangle4 = Polygon(
            [0, 0, 0], [101 * 0.5, 0, 0], [0, 100 * 0.5, 0],
            color=WHITE, fill_opacity=0.3
        )
        triangle4.shift(LEFT * 1.5 + DOWN * 0.5)
        c_label4 = MathTex("101", font_size=24).next_to(triangle4.get_right(), UP)
        a_label4 = MathTex("5", font_size=24).next_to(triangle4.get_left(), DOWN)
        self.play(Create(triangle4), Write(a_label4), Write(c_label4))
        self.wait(0.5)

        two_c4 = MathTex("2 \\times 101 = 202", font_size=24).to_edge(LEFT)
        three_a4 = MathTex("3 \\times 5 = 15", font_size=24).to_edge(RIGHT)
        self.play(Write(two_c4), Write(three_a4))
        self.wait(0.5)

        result4 = MathTex("202 \\leq 15", color=RED, font_size=24).next_to(inequality, DOWN)
        cross4 = Cross(result4)
        self.play(Write(result4), DrawBorderThenFill(cross4))
        self.wait(1)

        # Example: sides 10, 14, 15
        self.play(FadeOut(triangle4), FadeOut(a_label4), FadeOut(c_label4), FadeOut(two_c4), FadeOut(three_a4), FadeOut(result4), FadeOut(cross4))
        triangle5 = Polygon(
            [0, 0, 0], [15 * 0.5, 0, 0], [0, 14 * 0.5, 0],
            color=WHITE, fill_opacity=0.3
        )
        triangle5.shift(LEFT * 1.5 + DOWN * 0.5)
        c_label5 = MathTex("15", font_size=24).next_to(triangle5.get_right(), UP)
        a_label5 = MathTex("10", font_size=24).next_to(triangle5.get_left(), DOWN)
        self.play(Create(triangle5), Write(a_label5), Write(c_label5))
        self.wait(0.5)

        two_c5 = MathTex("2 \\times 15 = 30", font_size=24).to_edge(LEFT)
        three_a5 = MathTex("3 \\times 10 = 30", font_size=24).to_edge(RIGHT)
        self.play(Write(two_c5), Write(three_a5))
        self.wait(0.5)

        result5 = MathTex("30 \\leq 30", color=GREEN, font_size=24).next_to(inequality, DOWN)
        self.play(Write(result5))
        triangle5.set_color(GREEN)
        self.wait(1)

        # Example: sides 2, 3, 4
        self.play(FadeOut(triangle5), FadeOut(a_label5), FadeOut(c_label5), FadeOut(two_c5), FadeOut(three_a5), FadeOut(result5))
        triangle6 = Polygon(
            [0, 0, 0], [4 * 0.5, 0, 0], [0, 3 * 0.5, 0],
            color=WHITE, fill_opacity=0.3
        )
        triangle6.shift(LEFT * 1.5 + DOWN * 0.5)
        c_label6 = MathTex("4", font_size=24).next_to(triangle6.get_right(), UP)
        a_label6 = MathTex("2", font_size=24).next_to(triangle6.get_left(), DOWN)
        self.play(Create(triangle6), Write(a_label6), Write(c_label6))
        self.wait(0.5)

        two_c6 = MathTex("2 \\times 4 = 8", font_size=24).to_edge(LEFT)
        three_a6 = MathTex("3 \\times 2 = 6", font_size=24).to_edge(RIGHT)
        self.play(Write(two_c6), Write(three_a6))
        self.wait(0.5)

        result6 = MathTex("8 \\leq 6", color=RED, font_size=24).next_to(inequality, DOWN)
        cross6 = Cross(result6)
        self.play(Write(result6), DrawBorderThenFill(cross6))
        self.wait(1)

        # Equilateral triangle
        self.play(FadeOut(triangle6), FadeOut(a_label6), FadeOut(c_label6), FadeOut(two_c6), FadeOut(three_a6), FadeOut(result6), FadeOut(cross6))
        triangle7 = Polygon(
            [0, 0, 0], [1 * 0.5, 0, 0], [0, 1 * 0.5, 0],
            color=WHITE, fill_opacity=0.3
        )
        triangle7.shift(LEFT * 1.5 + DOWN * 0.5)
        x_label = MathTex("x", font_size=24).next_to(triangle7.get_right(), UP)
        self.play(Create(triangle7), Write(x_label))
        self.wait(0.5)

        inequality_eq = MathTex("2 \\times x \\leq 3 \\times x", font_size=24).to_edge(LEFT)
        self.play(Write(inequality_eq))
        self.wait(0.5)

        simplified = MathTex("2 \\leq 3", font_size=24).to_edge(RIGHT)
        self.play(Write(simplified))
        self.wait(1)

        # Two triangles with same shortest/longest but different middle
        self.play(FadeOut(triangle7), FadeOut(x_label), FadeOut(inequality_eq), FadeOut(simplified))
        triangle8 = Polygon(
            [0, 0, 0], [6 * 0.5, 0, 0], [0, 5 * 0.5, 0],
            color=WHITE, fill_opacity=0.3
        )
        triangle8.shift(LEFT * 2 + DOWN * 0.5)
        triangle9 = Polygon(
            [0, 0, 0], [6 * 0.5, 0, 0], [0, 2 * 0.5, 0],
            color=WHITE, fill_opacity=0.3
        )
        triangle9.shift(RIGHT * 2 + DOWN * 0.5)

        a8 = MathTex("4", font_size=24).next_to(triangle8.get_left(), DOWN)
        c8 = MathTex("6", font_size=24).next_to(triangle8.get_right(), UP)
        a9 = MathTex("4", font_size=24).next_to(triangle9.get_left(), DOWN)
        c9 = MathTex("6", font_size=24).next_to(triangle9.get_right(), UP)

        self.play(Create(triangle8), Create(triangle9), Write(a8), Write(c8), Write(a9), Write(c9))
        self.wait(0.5)

        two_c8 = MathTex("2 \\times 6 = 12", font_size=24).to_edge(LEFT)
        three_a8 = MathTex("3 \\times 4 = 12", font_size=24).to_edge(RIGHT)
        self.play(Write(two_c8), Write(three_a8))
        self.wait(0.5)

        result8 = MathTex("12 \\leq 12", color=GREEN, font_size=24).next_to(inequality, DOWN)
        self.play(Write(result8))
        self.wait(1)

        # Final text
        final_text = Text("Every equilateral triangle is mirthful.", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1)

        self.play(FadeOut(title), FadeOut(inequality), FadeOut(final_text))
