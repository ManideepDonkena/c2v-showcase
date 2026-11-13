from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Scaling Invariance", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial triangle: 4, 5, 6
        tri1 = Triangle().scale(0.8).shift(LEFT * 2)
        tri1.set_fill(GREEN, opacity=0.5)
        tri1.set_stroke(WHITE, width=2)
        a_label = MathTex("a", font_size=24).next_to(tri1.get_vertices()[0], DOWN)
        c_label = MathTex("c", font_size=24).next_to(tri1.get_vertices()[2], UP)
        c_label.shift(0.2 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(tri1), Write(a_label), Write(c_label))
        self.wait(0.5)

        # Show inequality: 2*c <= 3*a
        ineq = MathTex("2 \\times c \\leq 3 \\times a", font_size=30).next_to(tri1, DOWN, buff=0.5)
        self.play(Write(ineq))
        self.wait(1)

        # Divide both sides by 2: c <= 1.5*a
        div = MathTex("c \\leq 1.5 \\times a", font_size=30).next_to(ineq, DOWN, buff=0.3)
        self.play(Transform(ineq, div))
        self.wait(1)

        # Scale up to 8, 10, 12
        tri2 = Triangle().scale(1.6).shift(LEFT * 2)
        tri2.set_fill(GREEN, opacity=0.5)
        tri2.set_stroke(WHITE, width=2)
        self.play(Transform(tri1, tri2))
        self.wait(0.5)

        # Scale down to 2, 2.5, 3
        tri3 = Triangle().scale(0.4).shift(LEFT * 2)
        tri3.set_fill(GREEN, opacity=0.5)
        tri3.set_stroke(WHITE, width=2)
        a_label.shift(0.0 * RIGHT + 0.21 * UP)  # layout: separation vector
        self.play(Transform(tri1, tri3))
        self.wait(0.5)

        # Show text: Scaling preserves mirth
        msg = Text("Scaling preserves mirth", font_size=24).next_to(tri1, DOWN, buff=0.5)
        self.play(Write(msg))
        self.wait(1.5)
        self.play(FadeOut(msg))

        # Show triangle with sides 10, 20, 30
        tri4 = Triangle().scale(1.5).shift(RIGHT * 2)
        tri4.set_fill(BLUE, opacity=0.5)
        tri4.set_stroke(WHITE, width=2)
        self.play(Create(tri4))
        self.wait(0.5)

        # Show 2*30 vs 3*10
        two_c = MathTex("2 \\times 30", font_size=24).next_to(tri4.get_vertices()[2], UP)
        three_a = MathTex("3 \\times 10", font_size=24).next_to(tri4.get_vertices()[0], DOWN)
        two_c.shift(0.48 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(two_c), Write(three_a))
        self.wait(0.5)

        # Show 60 > 30
        comp = MathTex("60 > 30", font_size=24).next_to(two_c, RIGHT, buff=0.3)
        self.play(Write(comp))
        self.wait(1)
        self.play(FadeOut(two_c), FadeOut(three_a), FadeOut(comp))

        # Show triangle with sides 4, 10, 12
        tri5 = Triangle().scale(1.2).shift(RIGHT * 2)
        tri5.set_fill(BLUE, opacity=0.5)
        tri5.set_stroke(WHITE, width=2)
        self.play(Create(tri5))
        self.wait(0.5)

        # Show 2*12 vs 3*4
        two_c = MathTex("2 \\times 12", font_size=24).next_to(tri5.get_vertices()[2], UP)
        three_a = MathTex("3 \\times 4", font_size=24).next_to(tri5.get_vertices()[0], DOWN)
        self.play(Write(two_c), Write(three_a))
        self.wait(0.5)

        # Show 24 <= 12 in red with cross
        result = MathTex("24 \\leq 12", font_size=24, color=RED).next_to(two_c, RIGHT, buff=0.3)
        cross = Cross(result)
        self.play(Write(result), Create(cross))
        self.wait(1)
        self.play(FadeOut(two_c), FadeOut(three_a), FadeOut(result), FadeOut(cross))

        # Show triangle with sides 5, 100, 101
        tri6 = Triangle().scale(1.2).shift(RIGHT * 2)
        tri6.set_fill(BLUE, opacity=0.5)
        tri6.set_stroke(WHITE, width=2)
        self.play(Create(tri6))
        self.wait(0.5)

        # Show 2*101 vs 3*5
        two_c = MathTex("2 \\times 101", font_size=24).next_to(tri6.get_vertices()[2], UP)
        three_a = MathTex("3 \\times 5", font_size=24).next_to(tri6.get_vertices()[0], DOWN)
        self.play(Write(two_c), Write(three_a))
        self.wait(0.5)

        # Show 202 <= 15 in red
        result = MathTex("202 \\leq 15", font_size=24, color=RED).next_to(two_c, RIGHT, buff=0.3)
        cross = Cross(result)
        self.play(Write(result), Create(cross))
        self.wait(1)
        self.play(FadeOut(two_c), FadeOut(three_a), FadeOut(result), FadeOut(cross))

        # Show triangle with sides 10, 14, 15
        tri7 = Triangle().scale(1.2).shift(RIGHT * 2)
        tri7.set_fill(GREEN, opacity=0.5)
        tri7.set_stroke(WHITE, width=2)
        self.play(Create(tri7))
        self.wait(0.5)

        # Show 2*15 vs 3*10
        two_c = MathTex("2 \\times 15", font_size=24).next_to(tri7.get_vertices()[2], UP)
        three_a = MathTex("3 \\times 10", font_size=24).next_to(tri7.get_vertices()[0], DOWN)
        self.play(Write(two_c), Write(three_a))
        self.wait(0.5)

        # Show 30 <= 30
        result = MathTex("30 \\leq 30", font_size=24).next_to(two_c, RIGHT, buff=0.3)
        self.play(Write(result))
        self.wait(1)
        self.play(FadeOut(two_c), FadeOut(three_a), FadeOut(result))

        # Pulsing green triangle
        self.play(tri7.animate.set_fill(GREEN, opacity=0.5).set_stroke(WHITE, width=2))
        self.wait(1)

        # Show triangle with sides 2, 3, 4
        tri8 = Triangle().scale(1.2).shift(RIGHT * 2)
        tri8.set_fill(BLUE, opacity=0.5)
        tri8.set_stroke(WHITE, width=2)
        self.play(Create(tri8))
        self.wait(0.5)

        # Show 2*4 vs 3*2
        two_c = MathTex("2 \\times 4", font_size=24).next_to(tri8.get_vertices()[2], UP)
        three_a = MathTex("3 \\times 2", font_size=24).next_to(tri8.get_vertices()[0], DOWN)
        self.play(Write(two_c), Write(three_a))
        self.wait(0.5)

        # Show 8 <= 6 in red
        result = MathTex("8 \\leq 6", font_size=24, color=RED).next_to(two_c, RIGHT, buff=0.3)
        cross = Cross(result)
        self.play(Write(result), Create(cross))
        self.wait(1)
        self.play(FadeOut(two_c), FadeOut(three_a), FadeOut(result), FadeOut(cross))

        # Show equilateral triangle with side x
        tri9 = Triangle().scale(1.2).shift(RIGHT * 2)
        tri9.set_fill(GREEN, opacity=0.5)
        tri9.set_stroke(WHITE, width=2)
        self.play(Create(tri9))
        self.wait(0.5)

        # Show 2*x <= 3*x
        ineq = MathTex("2 \\times x \\leq 3 \\times x", font_size=24).next_to(tri9, DOWN, buff=0.5)
        self.play(Write(ineq))
        self.wait(1)

        # Simplify to 2 <= 3
        simp = MathTex("2 \\leq 3", font_size=24).next_to(ineq, DOWN, buff=0.3)
        self.play(Transform(ineq, simp))
        self.wait(1.5)
        self.play(FadeOut(ineq))

        # Show two triangles with same shortest/longest but different middle
        tri10 = Triangle().scale(0.8).shift(LEFT * 2)
        tri10.set_fill(GREEN, opacity=0.5)
        tri10.set_stroke(WHITE, width=2)
        self.play(Create(tri10))
        self.wait(0.5)

        # Show 4, 5, 6
        a_label = MathTex("4", font_size=24).next_to(tri10.get_vertices()[0], DOWN)
        c_label = MathTex("6", font_size=24).next_to(tri10.get_vertices()[2], UP)
        self.play(Write(a_label), Write(c_label))
        self.wait(0.5)

        # Show 2*6 vs 3*4
        two_c = MathTex("2 \\times 6", font_size=24).next_to(tri10.get_vertices()[2], UP)
        three_a = MathTex("3 \\times 4", font_size=24).next_to(tri10.get_vertices()[0], DOWN)
        self.play(Write(two_c), Write(three_a))
        self.wait(0.5)

        # Show result 12 <= 12
        result = MathTex("12 \\leq 12", font_size=24).next_to(two_c, RIGHT, buff=0.3)
        self.play(Write(result))
        self.wait(1)
        self.play(FadeOut(two_c), FadeOut(three_a), FadeOut(result))

        # Show triangle with sides 4, 2, 6
        tri11 = Triangle().scale(0.8).shift(RIGHT * 2)
        tri11.set_fill(GREEN, opacity=0.5)
        tri11.set_stroke(WHITE, width=2)
        self.play(Create(tri11))
        self.wait(0.5)

        # Show 4, 2, 6
        a_label = MathTex("2", font_size=24).next_to(tri11.get_vertices()[0], DOWN)
        c_label = MathTex("6", font_size=24).next_to(tri11.get_vertices()[2], UP)
        self.play(Write(a_label), Write(c_label))
        self.wait(0.5)

        # Show 2*6 vs 3*2
        two_c = MathTex("2 \\times 6", font_size=24).next_to(tri11.get_vertices()[2], UP)
        three_a = MathTex("3 \\times 2", font_size=24).next_to(tri11.get_vertices()[0], DOWN)
        self.play(Write(two_c), Write(three_a))
        self.wait(0.5)

        # Show result 12 <= 6 in red
        result = MathTex("12 \\leq 6", font_size=24, color=RED).next_to(two_c, RIGHT, buff=0.3)
        cross = Cross(result)
        self.play(Write(result), Create(cross))
        self.wait(1)
        self.play(FadeOut(two_c), FadeOut(three_a), FadeOut(result), FadeOut(cross))

        # Final message
        final_msg = Text("Rule 2: Scaling does not change mirthfulness", font_size=24).to_edge(DOWN)
        self.play(Write(final_msg))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(tri1), FadeOut(tri2), FadeOut(tri3), FadeOut(tri4),
                  FadeOut(tri5), FadeOut(tri6), FadeOut(tri7), FadeOut(tri8), FadeOut(tri9),
                  FadeOut(tri10), FadeOut(tri11), FadeOut(final_msg))
