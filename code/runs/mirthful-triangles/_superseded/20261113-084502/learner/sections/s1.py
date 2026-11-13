from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining Mirth", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial triangle with labels a, b, c (c longest, a shortest)
        triangle = Polygon(
            [0, 0, 0], [3, 0, 0], [1.5, 2.6, 0],
        )
        a_label = MathTex("a", font_size=24).next_to(triangle.get_vertices()[0], DOWN)
        b_label = MathTex("b", font_size=24).next_to(triangle.get_vertices()[1], DOWN)
        c_label = MathTex("c", font_size=24).next_to(triangle.get_vertices()[2], UP)

        self.play(Create(triangle), Write(a_label), Write(b_label), Write(c_label))
        self.wait(0.5)

        # Inequality text
        inequality_text = MathTex("2 \\times c \\leq 3 \\times a", font_size=32)
        self.play(Write(inequality_text))
        self.wait(1)

        # Algebraic transformation: divide both sides by 2
        transformed = MathTex("c \\leq 1.5 \\times a", font_size=32).move_to(inequality_text.get_center())
        self.play(Transform(inequality_text, transformed))
        self.wait(1)

        # Fade out triangle and labels
        self.play(FadeOut(triangle), FadeOut(a_label), FadeOut(b_label), FadeOut(c_label))

        # Example 1: sides 10, 20, 30
        triangle1 = Polygon(
            [0, 0, 0], [3, 0, 0], [1.5, 2.6, 0],
            color=WHITE
        )
        a_label1 = MathTex("10", font_size=24).next_to(triangle1.get_vertices()[0], DOWN)
        b_label1 = MathTex("20", font_size=24).next_to(triangle1.get_vertices()[1], DOWN)
        c_label1 = MathTex("30", font_size=24).next_to(triangle1.get_vertices()[2], UP)

        self.play(Create(triangle1), Write(a_label1), Write(b_label1), Write(c_label1))
        self.wait(0.5)

        two_c = MathTex("2 \\times 30", font_size=24).to_edge(LEFT)
        three_a = MathTex("3 \\times 10", font_size=24).to_edge(RIGHT)
        greater_than = MathTex(">").next_to(two_c, RIGHT, buff=0.2)

        self.play(Write(two_c), Write(three_a), Write(greater_than))
        self.wait(1)

        # Highlight failure
        self.play(Flash(triangle1, color=RED))
        self.wait(0.5)
        self.play(FadeOut(two_c), FadeOut(three_a), FadeOut(greater_than))

        # Example 2: sides 4, 10, 12
        triangle2 = Polygon(
            [0, 0, 0], [3, 0, 0], [1.5, 2.6, 0],
            color=WHITE
        )
        a_label2 = MathTex("4", font_size=24).next_to(triangle2.get_vertices()[0], DOWN)
        b_label2 = MathTex("10", font_size=24).next_to(triangle2.get_vertices()[1], DOWN)
        c_label2 = MathTex("12", font_size=24).next_to(triangle2.get_vertices()[2], UP)

        self.play(Create(triangle2), Write(a_label2), Write(b_label2), Write(c_label2))
        self.wait(0.5)

        two_c2 = MathTex("2 \\times 12 = 24", font_size=24).to_edge(LEFT)
        three_a2 = MathTex("3 \\times 4 = 12", font_size=24).to_edge(RIGHT)
        inequality_fail = MathTex("24 \\leq 12", font_size=32, color=RED).next_to(two_c2, RIGHT, buff=0.2)

        self.play(Write(two_c2), Write(three_a2))
        self.wait(0.5)
        self.play(Write(inequality_fail))
        self.wait(1)

        # Highlight failure
        self.play(Flash(triangle2, color=RED))
        self.wait(0.5)
        self.play(FadeOut(two_c2), FadeOut(three_a2), FadeOut(inequality_fail))

        # Example 3: sides 5, 100, 101
        triangle3 = Polygon(
            [0, 0, 0], [3, 0, 0], [1.5, 2.6, 0],
            color=WHITE
        )
        a_label3 = MathTex("5", font_size=24).next_to(triangle3.get_vertices()[0], DOWN)
        b_label3 = MathTex("100", font_size=24).next_to(triangle3.get_vertices()[1], DOWN)
        c_label3 = MathTex("101", font_size=24).next_to(triangle3.get_vertices()[2], UP)

        self.play(Create(triangle3), Write(a_label3), Write(b_label3), Write(c_label3))
        self.wait(0.5)

        two_c3 = MathTex("2 \\times 101 = 202", font_size=24).to_edge(LEFT)
        three_a3 = MathTex("3 \\times 5 = 15", font_size=24).to_edge(RIGHT)
        inequality_fail3 = MathTex("202 \\leq 15", font_size=32, color=RED).next_to(two_c3, RIGHT, buff=0.2)

        self.play(Write(two_c3), Write(three_a3))
        self.wait(0.5)
        self.play(Write(inequality_fail3))
        self.wait(1)

        # Highlight failure
        self.play(Flash(triangle3, color=RED))
        self.wait(0.5)
        self.play(FadeOut(two_c3), FadeOut(three_a3), FadeOut(inequality_fail3))

        # Example 4: sides 10, 14, 15
        triangle4 = Polygon(
            [0, 0, 0], [3, 0, 0], [1.5, 2.6, 0],
            color=WHITE
        )
        a_label4 = MathTex("10", font_size=24).next_to(triangle4.get_vertices()[0], DOWN)
        b_label4 = MathTex("14", font_size=24).next_to(triangle4.get_vertices()[1], DOWN)
        c_label4 = MathTex("15", font_size=24).next_to(triangle4.get_vertices()[2], UP)

        self.play(Create(triangle4), Write(a_label4), Write(b_label4), Write(c_label4))
        self.wait(0.5)

        question = Text("Check the rule: Is 2 times the longest side at most 3 times the shortest side?", font_size=24)
        self.play(Write(question))
        self.wait(1)

        self.play(FadeOut(question))

        two_c4 = MathTex("2 \\times 15", font_size=24).to_edge(LEFT)
        three_a4 = MathTex("3 \\times 10", font_size=24).to_edge(RIGHT)
        inequality_true = MathTex("30 \\leq 30", font_size=32, color=GREEN).next_to(two_c4, RIGHT, buff=0.2)

        self.play(Write(two_c4), Write(three_a4))
        self.wait(0.5)
        self.play(Write(inequality_true))
        self.wait(1)

        # Pulse green
        self.play(Flash(triangle4, color=GREEN))
        self.wait(0.5)
        self.play(FadeOut(two_c4), FadeOut(three_a4), FadeOut(inequality_true))

        # Example 5: sides 2, 3, 4
        triangle5 = Polygon(
            [0, 0, 0], [3, 0, 0], [1.5, 2.6, 0],
            color=WHITE
        )
        a_label5 = MathTex("2", font_size=24).next_to(triangle5.get_vertices()[0], DOWN)
        b_label5 = MathTex("3", font_size=24).next_to(triangle5.get_vertices()[1], DOWN)
        c_label5 = MathTex("4", font_size=24).next_to(triangle5.get_vertices()[2], UP)

        self.play(Create(triangle5), Write(a_label5), Write(b_label5), Write(c_label5))
        self.wait(0.5)

        two_c5 = MathTex("2 \\times 4 = 8", font_size=24).to_edge(LEFT)
        three_a5 = MathTex("3 \\times 2 = 6", font_size=24).to_edge(RIGHT)
        inequality_fail5 = MathTex("8 \\leq 6", font_size=32, color=RED).next_to(two_c5, RIGHT, buff=0.2)

        self.play(Write(two_c5), Write(three_a5))
        self.wait(0.5)
        self.play(Write(inequality_fail5))
        self.wait(1)

        # Highlight failure
        self.play(Flash(triangle5, color=RED))
        self.wait(0.5)
        self.play(FadeOut(two_c5), FadeOut(three_a5), FadeOut(inequality_fail5))

        # Final summary text
        final_text = Text("A triangle is mirthful if 2×longest ≤ 3×shortest", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1)

        self.play(FadeOut(title), FadeOut(final_text))
