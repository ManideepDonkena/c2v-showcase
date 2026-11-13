from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Scaling Invariance", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial triangle: 4, 5, 6
        a = 4
        b = 5
        c = 6
        tri1 = Triangle().scale(0.8).shift(LEFT * 2)
        tri1.set_color(GREEN)
        label_a = MathTex("a", font_size=24).next_to(tri1, DOWN, buff=0.2)
        label_c = MathTex("c", font_size=24).next_to(tri1, UP, buff=0.2)
        self.play(Create(tri1), Write(label_a), Write(label_c))
        self.wait(0.5)

        # Show inequality
        ineq = MathTex("2 \\times c \\leq 3 \\times a", font_size=30).next_to(tri1, RIGHT, buff=1)
        self.play(Write(ineq))
        self.wait(1)

        # Divide by 2
        div = MathTex("\\frac{2c}{2} \\leq \\frac{3a}{2}", font_size=30).move_to(ineq)
        self.play(Transform(ineq, div))
        self.wait(1)

        # Simplify to c <= 1.5*a
        simp = MathTex("c \\leq 1.5 \\times a", font_size=30).move_to(ineq)
        self.play(Transform(ineq, simp))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(ineq), FadeOut(label_a), FadeOut(label_c))

        # Scale up to 8, 10, 12
        tri2 = Triangle().scale(1.6).shift(LEFT * 2)
        tri2.set_color(GREEN)
        self.play(Transform(tri1, tri2))
        self.wait(0.5)

        # Scale down to 2, 2.5, 3
        tri3 = Triangle().scale(0.4).shift(LEFT * 2)
        tri3.set_color(GREEN)
        self.play(Transform(tri1, tri3))
        self.wait(0.5)

        # Show text: Scaling preserves mirth
        text = Text("Scaling preserves mirth", font_size=24).next_to(tri1, DOWN)
        self.play(Write(text))
        self.wait(1.5)
        self.play(FadeOut(text))

        # Triangle 10, 20, 30
        tri4 = Triangle().scale(1.2).shift(RIGHT * 2)
        tri4.set_color(YELLOW)
        label_10 = MathTex("10", font_size=24).next_to(tri4, DOWN, buff=0.2)
        label_20 = MathTex("20", font_size=24).next_to(tri4, LEFT, buff=0.2)
        label_30 = MathTex("30", font_size=24).next_to(tri4, UP, buff=0.2)
        self.play(Create(tri4), Write(label_10), Write(label_20), Write(label_30))
        self.wait(0.5)

        # Show 2*30 vs 3*10
        calc1 = MathTex("2 \\times 30", font_size=24).next_to(tri4, RIGHT, buff=0.5)
        calc2 = MathTex("3 \\times 10", font_size=24).next_to(calc1, DOWN, buff=0.2)
        self.play(Write(calc1), Write(calc2))
        self.wait(0.5)

        # Show inequality
        comp = MathTex("60 > 30", font_size=24).set_color(RED).next_to(calc2, DOWN, buff=0.2)
        self.play(Write(comp))
        self.wait(1.5)
        self.play(FadeOut(calc1), FadeOut(calc2), FadeOut(comp))

        # Triangle 4, 10, 12
        tri5 = Triangle().scale(0.8).shift(RIGHT * 2)
        tri5.set_color(YELLOW)
        label_4 = MathTex("4", font_size=24).next_to(tri5, DOWN, buff=0.2)
        label_10 = MathTex("10", font_size=24).next_to(tri5, LEFT, buff=0.2)
        label_12 = MathTex("12", font_size=24).next_to(tri5, UP, buff=0.2)
        label_4.shift(0.0 * RIGHT + -0.25 * UP)  # layout: separation vector
        label_10.shift(-0.3 * RIGHT + 0.0 * UP)  # layout: separation vector
        label_12.shift(0.0 * RIGHT + 0.25 * UP)  # layout: separation vector
        self.play(Create(tri5), Write(label_4), Write(label_10), Write(label_12))
        self.wait(0.5)

        # Show 2*12 vs 3*4
        calc3 = MathTex("2 \\times 12", font_size=24).next_to(tri5, RIGHT, buff=0.5)
        calc4 = MathTex("3 \\times 4", font_size=24).next_to(calc3, DOWN, buff=0.2)
        self.play(Write(calc3), Write(calc4))
        self.wait(0.5)

        # Show inequality
        comp2 = MathTex("24 \\leq 12", font_size=24).set_color(RED).next_to(calc4, DOWN, buff=0.2)
        cross = Cross(comp2)
        self.play(Write(comp2), DrawBorderThenFill(cross))
        self.wait(1.5)
        self.play(FadeOut(calc3), FadeOut(calc4), FadeOut(comp2), FadeOut(cross))

        # Triangle 5, 100, 101
        tri6 = Triangle().scale(0.8).shift(RIGHT * 2)
        tri6.set_color(YELLOW)
        label_5 = MathTex("5", font_size=24).next_to(tri6, DOWN, buff=0.2)
        label_100 = MathTex("100", font_size=24).next_to(tri6, LEFT, buff=0.2)
        label_101 = MathTex("101", font_size=24).next_to(tri6, UP, buff=0.2)
        self.play(Create(tri6), Write(label_5), Write(label_100), Write(label_101))
        self.wait(0.5)

        # Show 2*101 vs 3*5
        calc5 = MathTex("2 \\times 101", font_size=24).next_to(tri6, RIGHT, buff=0.5)
        calc6 = MathTex("3 \\times 5", font_size=24).next_to(calc5, DOWN, buff=0.2)
        self.play(Write(calc5), Write(calc6))
        self.wait(0.5)

        # Show inequality
        comp3 = MathTex("202 \\leq 15", font_size=24).set_color(RED).next_to(calc6, DOWN, buff=0.2)
        self.play(Write(comp3))
        self.wait(1.5)
        self.play(FadeOut(calc5), FadeOut(calc6), FadeOut(comp3))

        # Triangle 10, 14, 15
        tri7 = Triangle().scale(0.8).shift(RIGHT * 2)
        tri7.set_color(GREEN)
        label_10 = MathTex("10", font_size=24).next_to(tri7, DOWN, buff=0.2)
        label_14 = MathTex("14", font_size=24).next_to(tri7, LEFT, buff=0.2)
        label_15 = MathTex("15", font_size=24).next_to(tri7, UP, buff=0.2)
        self.play(Create(tri7), Write(label_10), Write(label_14), Write(label_15))
        self.wait(0.5)

        # Show check
        check = Text("Check the rule: Is 2 times longest ≤ 3 times shortest?", font_size=20).next_to(tri7, DOWN, buff=0.5)
        self.play(Write(check))
        self.wait(1)

        # Show calculation
        calc7 = MathTex("2 \\times 15 \\leq 3 \\times 10", font_size=24).next_to(check, DOWN, buff=0.2)
        self.play(Write(calc7))
        self.wait(0.5)

        # Resolve to 30 <= 30
        res = MathTex("30 \\leq 30", font_size=24).next_to(calc7, DOWN, buff=0.2)
        self.play(Write(res))
        self.wait(1)

        # Pulse green
        self.play(tri7.animate.set_color(GREEN).scale(1.1), run_time=0.5)
        self.play(tri7.animate.set_color(GREEN).scale(1/1.1), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(check), FadeOut(calc7), FadeOut(res))

        # Triangle 2, 3, 4
        tri8 = Triangle().scale(0.8).shift(RIGHT * 2)
        tri8.set_color(YELLOW)
        label_2 = MathTex("2", font_size=24).next_to(tri8, DOWN, buff=0.2)
        label_3 = MathTex("3", font_size=24).next_to(tri8, LEFT, buff=0.2)
        label_4 = MathTex("4", font_size=24).next_to(tri8, UP, buff=0.2)
        self.play(Create(tri8), Write(label_2), Write(label_3), Write(label_4))
        self.wait(0.5)

        # Show 2*4 vs 3*2
        calc8 = MathTex("2 \\times 4", font_size=24).next_to(tri8, RIGHT, buff=0.5)
        calc9 = MathTex("3 \\times 2", font_size=24).next_to(calc8, DOWN, buff=0.2)
        self.play(Write(calc8), Write(calc9))
        self.wait(0.5)

        # Show inequality
        comp4 = MathTex("8 \\leq 6", font_size=24).set_color(RED).next_to(calc9, DOWN, buff=0.2)
        self.play(Write(comp4))
        self.wait(1.5)
        self.play(FadeOut(calc8), FadeOut(calc9), FadeOut(comp4))

        # Equilateral triangle x
        tri9 = Triangle().scale(0.8).shift(RIGHT * 2)
        tri9.set_color(GREEN)
        label_x = MathTex("x", font_size=24).next_to(tri9, DOWN, buff=0.2)
        self.play(Create(tri9), Write(label_x))
        self.wait(0.5)

        # Show inequality
        ineq_eq = MathTex("2 \\times x \\leq 3 \\times x", font_size=24).next_to(tri9, RIGHT, buff=0.5)
        self.play(Write(ineq_eq))
        self.wait(0.5)

        # Simplify to 2 <= 3
        simp_eq = MathTex("2 \\leq 3", font_size=24).next_to(ineq_eq, DOWN, buff=0.2)
        self.play(Transform(ineq_eq, simp_eq))
        self.wait(1.5)
        self.play(FadeOut(ineq_eq))

        # Two triangles with same shortest/longest but different middle
        tri10 = Triangle().scale(0.8).shift(RIGHT * 2)
        tri10.set_color(GREEN)
        label_4a = MathTex("4", font_size=24).next_to(tri10, DOWN, buff=0.2)
        label_5 = MathTex("5", font_size=24).next_to(tri10, LEFT, buff=0.2)
        label_6 = MathTex("6", font_size=24).next_to(tri10, UP, buff=0.2)
        self.play(Create(tri10), Write(label_4a), Write(label_5), Write(label_6))
        self.wait(0.5)

        # Show 2*6 vs 3*4
        calc10 = MathTex("2 \\times 6", font_size=24).next_to(tri10, RIGHT, buff=0.5)
        calc11 = MathTex("3 \\times 4", font_size=24).next_to(calc10, DOWN, buff=0.2)
        self.play(Write(calc10), Write(calc11))
        self.wait(0.5)

        # Show result
        res1 = MathTex("12 \\leq 12", font_size=24).set_color(GREEN).next_to(calc11, DOWN, buff=0.2)
        self.play(Write(res1))
        self.wait(1.5)
        self.play(FadeOut(calc10), FadeOut(calc11), FadeOut(res1))

        # Second triangle with middle side 2
        tri11 = Triangle().scale(0.8).shift(RIGHT * 2)
        tri11.set_color(GREEN)
        label_4b = MathTex("4", font_size=24).next_to(tri11, DOWN, buff=0.2)
        label_2 = MathTex("2", font_size=24).next_to(tri11, LEFT, buff=0.2)
        label_6 = MathTex("6", font_size=24).next_to(tri11, UP, buff=0.2)
        self.play(Transform(tri10, tri11), Write(label_4b), Write(label_2), Write(label_6))
        self.wait(0.5)

        # Show 2*6 vs 3*4
        calc12 = MathTex("2 \\times 6", font_size=24).next_to(tri10, RIGHT, buff=0.5)
        calc13 = MathTex("3 \\times 4", font_size=24).next_to(calc12, DOWN, buff=0.2)
        self.play(Write(calc12), Write(calc13))
        self.wait(0.5)

        # Show result
        res2 = MathTex("12 \\leq 12", font_size=24).set_color(GREEN).next_to(calc13, DOWN, buff=0.2)
        self.play(Write(res2))
        self.wait(1.5)
        self.play(FadeOut(calc12), FadeOut(calc13), FadeOut(res2))

        # End
        self.play(FadeOut(tri10), FadeOut(label_4a), FadeOut(label_5), FadeOut(label_6),
                  FadeOut(label_4b), FadeOut(label_2), FadeOut(title))
        self.wait(0.5)
