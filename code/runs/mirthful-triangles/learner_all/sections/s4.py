from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Worked Examples", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First pair of triangles: 4,5,6 (green check) vs 3,4,5 (red X)
        left_triangle = Triangle().scale(1.2).shift(LEFT * 3)
        right_triangle = Triangle().scale(1.2).shift(RIGHT * 3)

        left_label_a = MathTex("a", font_size=24).next_to(left_triangle, DOWN)
        left_label_c = MathTex("c", font_size=24).next_to(left_triangle, UP)
        right_label_a = MathTex("a", font_size=24).next_to(right_triangle, DOWN)
        right_label_c = MathTex("c", font_size=24).next_to(right_triangle, UP)

        self.play(Create(left_triangle), Create(right_triangle))
        self.play(Write(left_label_a), Write(left_label_c), Write(right_label_a), Write(right_label_c))

        # Left triangle: 4,5,6
        left_calc1 = MathTex("2 \\times c = 2 \\times 6 = 12", font_size=24).next_to(left_triangle, DOWN, buff=0.5)
        left_calc2 = MathTex("3 \\times a = 3 \\times 4 = 12", font_size=24).next_to(left_calc1, DOWN)
        left_check = MathTex("12 \\leq 12", font_size=24, color=GREEN).next_to(left_calc2, DOWN)

        self.play(Write(left_calc1))
        self.wait(0.5)
        self.play(Write(left_calc2))
        self.wait(0.5)
        self.play(Write(left_check))

        # Right triangle: 3,4,5
        right_calc1 = MathTex("2 \\times c = 2 \\times 5 = 10", font_size=24).next_to(right_triangle, DOWN, buff=0.5)
        right_calc2 = MathTex("3 \\times a = 3 \\times 3 = 9", font_size=24).next_to(right_calc1, DOWN)
        right_cross = MathTex("10 > 9", font_size=24, color=RED).next_to(right_calc2, DOWN)

        self.play(Write(right_calc1))
        self.wait(0.5)
        self.play(Write(right_calc2))
        self.wait(0.5)
        self.play(Write(right_cross))

        # Rule: 2c <= 3a
        rule = MathTex("2 \\times c \\leq 3 \\times a", font_size=30).to_edge(UP, buff=0.5)
        self.play(Transform(title, rule))
        self.wait(1)

        # Divide both sides by 2: c <= 1.5 * a
        div = MathTex("\\frac{2c}{2} \\leq \\frac{3a}{2}", font_size=24).next_to(rule, DOWN)
        simp = MathTex("c \\leq 1.5 \\times a", font_size=24).next_to(div, DOWN)

        self.play(Write(div))
        self.wait(0.5)
        self.play(Write(simp))
        self.wait(1)

        # Show triangle with sides 10, 20, 30
        tri_102030 = Triangle().scale(1.2).shift(LEFT * 3)
        label_10 = MathTex("10", font_size=24).next_to(tri_102030, DOWN)
        label_20 = MathTex("20", font_size=24).next_to(tri_102030, LEFT)
        label_30 = MathTex("30", font_size=24).next_to(tri_102030, UP)

        self.play(Transform(left_triangle, tri_102030))
        self.play(Write(label_10), Write(label_20), Write(label_30))

        calc1 = MathTex("2 \\times 30 = 60", font_size=24).next_to(tri_102030, DOWN, buff=0.5)
        calc2 = MathTex("3 \\times 10 = 30", font_size=24).next_to(calc1, DOWN)
        comp = MathTex("60 > 30", font_size=24, color=RED).next_to(calc2, DOWN)

        self.play(Write(calc1))
        self.wait(0.5)
        self.play(Write(calc2))
        self.wait(0.5)
        self.play(Write(comp))

        # Triangle with sides 4, 10, 12
        tri_41012 = Triangle().scale(1.2).shift(RIGHT * 3)
        label_4 = MathTex("4", font_size=24).next_to(tri_41012, DOWN)
        label_10 = MathTex("10", font_size=24).next_to(tri_41012, LEFT)
        label_12 = MathTex("12", font_size=24).next_to(tri_41012, UP)

        self.play(Transform(right_triangle, tri_41012))
        self.play(Write(label_4), Write(label_10), Write(label_12))

        calc3 = MathTex("2 \\times 12 = 24", font_size=24).next_to(tri_41012, DOWN, buff=0.5)
        calc4 = MathTex("3 \\times 4 = 12", font_size=24).next_to(calc3, DOWN)
        comp2 = MathTex("24 \\leq 12", font_size=24, color=RED).next_to(calc4, DOWN)

        self.play(Write(calc3))
        self.wait(0.5)
        self.play(Write(calc4))
        self.wait(0.5)
        self.play(Write(comp2))

        # Triangle with sides 5, 100, 101
        tri_5100101 = Triangle().scale(1.2).shift(LEFT * 3)
        label_5 = MathTex("5", font_size=24).next_to(tri_5100101, DOWN)
        label_100 = MathTex("100", font_size=24).next_to(tri_5100101, LEFT)
        label_101 = MathTex("101", font_size=24).next_to(tri_5100101, UP)

        self.play(Transform(left_triangle, tri_5100101))
        self.play(Write(label_5), Write(label_100), Write(label_101))

        calc5 = MathTex("2 \\times 101 = 202", font_size=24).next_to(tri_5100101, DOWN, buff=0.5)
        calc6 = MathTex("3 \\times 5 = 15", font_size=24).next_to(calc5, DOWN)
        comp3 = MathTex("202 \\leq 15", font_size=24, color=RED).next_to(calc6, DOWN)

        self.play(Write(calc5))
        self.wait(0.5)
        self.play(Write(calc6))
        self.wait(0.5)
        self.play(Write(comp3))

        # Triangle with sides 10, 14, 15
        tri_101415 = Triangle().scale(1.2).shift(RIGHT * 3)
        label_10 = MathTex("10", font_size=24).next_to(tri_101415, DOWN)
        label_14 = MathTex("14", font_size=24).next_to(tri_101415, LEFT)
        label_15 = MathTex("15", font_size=24).next_to(tri_101415, UP)

        self.play(Transform(right_triangle, tri_101415))
        self.play(Write(label_10), Write(label_14), Write(label_15))

        check = Text("Check the rule: Is 2 times the longest side at most 3 times the shortest side?", font_size=20).next_to(tri_101415, DOWN, buff=0.5)
        self.play(Write(check))
        self.wait(1)

        calc7 = MathTex("2 \\times 15 = 30", font_size=24).next_to(tri_101415, DOWN, buff=0.5)
        calc8 = MathTex("3 \\times 10 = 30", font_size=24).next_to(calc7, DOWN)
        comp4 = MathTex("30 \\leq 30", font_size=24, color=GREEN).next_to(calc8, DOWN)

        self.play(Write(calc7))
        self.wait(0.5)
        self.play(Write(calc8))
        self.wait(0.5)
        self.play(Write(comp4))

        # Pulse green triangle
        self.play(Indicate(tri_101415, color=GREEN), run_time=1)

        # Triangle with sides 2, 3, 4
        tri_234 = Triangle().scale(1.2).shift(LEFT * 3)
        label_2 = MathTex("2", font_size=24).next_to(tri_234, DOWN)
        label_3 = MathTex("3", font_size=24).next_to(tri_234, LEFT)
        label_4 = MathTex("4", font_size=24).next_to(tri_234, UP)

        self.play(Transform(left_triangle, tri_234))
        self.play(Write(label_2), Write(label_3), Write(label_4))

        calc9 = MathTex("2 \\times 4 = 8", font_size=24).next_to(tri_234, DOWN, buff=0.5)
        calc10 = MathTex("3 \\times 2 = 6", font_size=24).next_to(calc9, DOWN)
        comp5 = MathTex("8 \\leq 6", font_size=24, color=RED).next_to(calc10, DOWN)

        self.play(Write(calc9))
        self.wait(0.5)
        self.play(Write(calc10))
        self.wait(0.5)
        self.play(Write(comp5))

        # Equilateral triangle with side x
        tri_eq = Triangle().scale(1.2).shift(RIGHT * 3)
        label_x = MathTex("x", font_size=24).next_to(tri_eq, DOWN)
        label_x2 = MathTex("x", font_size=24).next_to(tri_eq, LEFT)
        label_x3 = MathTex("x", font_size=24).next_to(tri_eq, UP)

        self.play(Transform(right_triangle, tri_eq))
        self.play(Write(label_x), Write(label_x2), Write(label_x3))

        calc11 = MathTex("2 \\times x = 2x", font_size=24).next_to(tri_eq, DOWN, buff=0.5)
        calc12 = MathTex("3 \\times x = 3x", font_size=24).next_to(calc11, DOWN)
        comp6 = MathTex("2x \\leq 3x", font_size=24).next_to(calc12, DOWN)
        simp_eq = MathTex("2 \\leq 3", font_size=24).next_to(comp6, DOWN)

        self.play(Write(calc11))
        self.wait(0.5)
        self.play(Write(calc12))
        self.wait(0.5)
        self.play(Write(comp6))
        self.wait(0.5)
        self.play(Write(simp_eq))

        # Two triangles with same shortest/longest but different middle
        tri_a = Triangle().scale(1.2).shift(LEFT * 3)
        label_4a = MathTex("4", font_size=24).next_to(tri_a, DOWN)
        label_5 = MathTex("5", font_size=24).next_to(tri_a, LEFT)
        label_6 = MathTex("6", font_size=24).next_to(tri_a, UP)

        tri_b = Triangle().scale(1.2).shift(RIGHT * 3)
        label_4b = MathTex("4", font_size=24).next_to(tri_b, DOWN)
        label_2 = MathTex("2", font_size=24).next_to(tri_b, LEFT)
        label_6b = MathTex("6", font_size=24).next_to(tri_b, UP)

        self.play(Transform(left_triangle, tri_a), Transform(right_triangle, tri_b))
        self.play(Write(label_4a), Write(label_5), Write(label_6), Write(label_4b), Write(label_2), Write(label_6b))

        calc13 = MathTex("2 \\times 6 = 12", font_size=24).next_to(tri_a, DOWN, buff=0.5)
        calc14 = MathTex("3 \\times 4 = 12", font_size=24).next_to(calc13, DOWN)
        comp7 = MathTex("12 \\leq 12", font_size=24, color=GREEN).next_to(calc14, DOWN)

        calc15 = MathTex("2 \\times 6 = 12", font_size=24).next_to(tri_b, DOWN, buff=0.5)
        calc16 = MathTex("3 \\times 4 = 12", font_size=24).next_to(calc15, DOWN)
        comp8 = MathTex("12 \\leq 12", font_size=24, color=GREEN).next_to(calc16, DOWN)

        self.play(Write(calc13))
        self.wait(0.5)
        self.play(Write(calc14))
        self.wait(0.5)
        self.play(Write(comp7))

        self.play(Write(calc15))
        self.wait(0.5)
        self.play(Write(calc16))
        self.wait(0.5)
        self.play(Write(comp8))

        # Final fade
        self.wait(1)
        self.play(FadeOut(title), FadeOut(left_triangle), FadeOut(right_triangle),
                  FadeOut(left_label_a), FadeOut(left_label_c),
                  FadeOut(right_label_a), FadeOut(right_label_c),
                  FadeOut(calc1), FadeOut(calc2), FadeOut(left_check),
                  FadeOut(right_calc1), FadeOut(right_calc2), FadeOut(right_cross),
                  FadeOut(div), FadeOut(simp),
                  FadeOut(calc1), FadeOut(calc2), FadeOut(comp),
                  FadeOut(calc3), FadeOut(calc4), FadeOut(comp2),
                  FadeOut(calc5), FadeOut(calc6), FadeOut(comp3),
                  FadeOut(check),
                  FadeOut(calc7), FadeOut(calc8), FadeOut(comp4),
                  FadeOut(calc9), FadeOut(calc10), FadeOut(comp5),
                  FadeOut(calc11), FadeOut(calc12), FadeOut(comp6), FadeOut(simp_eq),
                  FadeOut(calc13), FadeOut(calc14), FadeOut(comp7),
                  FadeOut(calc15), FadeOut(calc16), FadeOut(comp8))
