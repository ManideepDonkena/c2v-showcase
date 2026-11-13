from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Equilateral Case", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Start with equilateral triangle
        a = 5
        triangle = Triangle().scale(a/3).shift(UP*1.5)
        triangle.set_fill(GREEN, opacity=0.5)
        side_labels = VGroup(
            MathTex("5").next_to(triangle.get_vertices()[0], DOWN),
            MathTex("5").next_to(triangle.get_vertices()[1], DOWN),
            MathTex("5").next_to(triangle.get_vertices()[2], DOWN)
        )
        self.play(Create(triangle), Write(side_labels))
        self.wait(0.5)

        # Show calculation
        calc = MathTex("2 \\times 5 \\leq 3 \\times 5", font_size=30).next_to(triangle, DOWN, buff=0.5)
        self.play(Write(calc))
        self.wait(1)

        # Animate triangle turning green and bouncing
        self.play(
            triangle.animate.set_fill(GREEN),
            triangle.animate.scale(1.05),
            run_time=0.3
        )
        self.play(triangle.animate.scale(1/1.05), run_time=0.3)
        self.wait(0.5)

        # Rule 1: All equilateral triangles are mirthful
        rule = Text("Rule 1: All equilateral triangles are mirthful.", font_size=24).to_edge(DOWN)
        self.play(Write(rule))
        self.wait(1.5)
        self.play(FadeOut(rule))

        # Show general triangle with sides a and c
        self.play(FadeOut(triangle, side_labels, calc))
        triangle2 = Triangle().scale(2).shift(UP*0.5)
        triangle2.set_fill(BLUE, opacity=0.5)
        labels2 = VGroup(
            MathTex("a").next_to(triangle2.get_vertices()[0], DOWN),
            MathTex("c").next_to(triangle2.get_vertices()[1], DOWN),
            MathTex("b").next_to(triangle2.get_vertices()[2], DOWN)
        )
        self.play(Create(triangle2), Write(labels2))
        self.wait(0.5)

        # Show inequality
        ineq = MathTex("2 \\times c \\leq 3 \\times a", font_size=30).next_to(triangle2, DOWN, buff=0.5)
        self.play(Write(ineq))
        self.wait(1)

        # Divide both sides by 2
        div = MathTex("\\frac{2c}{2} \\leq \\frac{3a}{2}", font_size=30).next_to(ineq, DOWN, buff=0.3)
        self.play(Write(div))
        self.wait(1)

        # Simplify to c <= 1.5*a
        simp = MathTex("c \\leq 1.5 \\times a", font_size=30).next_to(div, DOWN, buff=0.3)
        self.play(Write(simp))
        self.wait(1.5)
        self.play(FadeOut(triangle2, labels2, ineq, div, simp))

        # Show triangle with sides 10, 20, 30
        triangle3 = Triangle().scale(3).shift(UP*0.5)
        triangle3.set_fill(RED, opacity=0.5)
        labels3 = VGroup(
            MathTex("10").next_to(triangle3.get_vertices()[0], DOWN),
            MathTex("20").next_to(triangle3.get_vertices()[1], DOWN),
            MathTex("30").next_to(triangle3.get_vertices()[2], DOWN)
        )
        self.play(Create(triangle3), Write(labels3))
        self.wait(0.5)

        # Animate 2*30 and 3*10
        left = MathTex("2 \\times 30", font_size=30).next_to(triangle3, LEFT)
        right = MathTex("3 \\times 10", font_size=30).next_to(triangle3, RIGHT)
        self.play(Write(left), Write(right))
        self.wait(0.5)

        # Show inequality
        ineq3 = MathTex("2 \\times 30 > 3 \\times 10", font_size=30).next_to(left, DOWN, buff=0.3)
        ineq3.shift(-0.53 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(ineq3))
        self.wait(1.5)
        self.play(FadeOut(triangle3, labels3, left, right, ineq3))

        # Show triangle with sides 4, 10, 12
        triangle4 = Triangle().scale(2).shift(UP*0.5)
        triangle4.set_fill(RED, opacity=0.5)
        labels4 = VGroup(
            MathTex("4").next_to(triangle4.get_vertices()[0], DOWN),
            MathTex("10").next_to(triangle4.get_vertices()[1], DOWN),
            MathTex("12").next_to(triangle4.get_vertices()[2], DOWN)
        )
        self.play(Create(triangle4), Write(labels4))
        self.wait(0.5)

        # Animate 2*12 and 3*4
        left4 = MathTex("2 \\times 12", font_size=30).next_to(triangle4, LEFT)
        right4 = MathTex("3 \\times 4", font_size=30).next_to(triangle4, RIGHT)
        self.play(Write(left4), Write(right4))
        self.wait(0.5)

        # Show result
        res = MathTex("24 \\leq 12", font_size=30, color=RED).next_to(left4, DOWN, buff=0.3)
        cross = Cross(res)
        self.play(Write(res), Create(cross))
        self.wait(1.5)
        self.play(FadeOut(triangle4, labels4, left4, right4, res, cross))

        # Show triangle with sides 5, 100, 101
        triangle5 = Triangle().scale(3).shift(UP*0.5)
        triangle5.set_fill(RED, opacity=0.5)
        labels5 = VGroup(
            MathTex("5").next_to(triangle5.get_vertices()[0], DOWN),
            MathTex("100").next_to(triangle5.get_vertices()[1], DOWN),
            MathTex("101").next_to(triangle5.get_vertices()[2], DOWN)
        )
        self.play(Create(triangle5), Write(labels5))
        self.wait(0.5)

        # Animate 2*101 and 3*5
        left5 = MathTex("2 \\times 101", font_size=30).next_to(triangle5, LEFT)
        right5 = MathTex("3 \\times 5", font_size=30).next_to(triangle5, RIGHT)
        self.play(Write(left5), Write(right5))
        self.wait(0.5)

        # Show result
        res5 = MathTex("202 \\leq 15", font_size=30, color=RED).next_to(left5, DOWN, buff=0.3)
        cross5 = Cross(res5)
        self.play(Write(res5), Create(cross5))
        self.wait(1.5)
        self.play(FadeOut(triangle5, labels5, left5, right5, res5, cross5))

        # Show triangle with sides 10, 14, 15
        triangle6 = Triangle().scale(2).shift(UP*0.5)
        triangle6.set_fill(GREEN, opacity=0.5)
        labels6 = VGroup(
            MathTex("10").next_to(triangle6.get_vertices()[0], DOWN),
            MathTex("14").next_to(triangle6.get_vertices()[1], DOWN),
            MathTex("15").next_to(triangle6.get_vertices()[2], DOWN)
        )
        self.play(Create(triangle6), Write(labels6))
        self.wait(0.5)

        # Ask question
        q = Text("Check the rule: Is 2 times the longest side at most 3 times the shortest side?", font_size=24).next_to(triangle6, DOWN, buff=0.5)
        q.shift(0.0 * RIGHT + -0.24 * UP)  # layout: separation vector
        self.play(Write(q))
        self.wait(1.5)
        self.play(FadeOut(q))

        # Animate calculation
        left6 = MathTex("2 \\times 15", font_size=30).next_to(triangle6, LEFT)
        right6 = MathTex("3 \\times 10", font_size=30).next_to(triangle6, RIGHT)
        self.play(Write(left6), Write(right6))
        self.wait(0.5)

        # Show result
        res6 = MathTex("30 \\leq 30", font_size=30).next_to(left6, DOWN, buff=0.3)
        self.play(Write(res6))
        self.wait(1.5)

        # Pulse green
        self.play(
            triangle6.animate.set_fill(GREEN),
            triangle6.animate.scale(1.05),
            run_time=0.3
        )
        self.play(triangle6.animate.scale(1/1.05), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(triangle6, labels6, left6, right6, res6))

        # Show triangle with sides 2, 3, 4
        triangle7 = Triangle().scale(2).shift(UP*0.5)
        triangle7.set_fill(RED, opacity=0.5)
        labels7 = VGroup(
            MathTex("2").next_to(triangle7.get_vertices()[0], DOWN),
            MathTex("3").next_to(triangle7.get_vertices()[1], DOWN),
            MathTex("4").next_to(triangle7.get_vertices()[2], DOWN)
        )
        self.play(Create(triangle7), Write(labels7))
        self.wait(0.5)

        # Animate 2*4 and 3*2
        left7 = MathTex("2 \\times 4", font_size=30).next_to(triangle7, LEFT)
        right7 = MathTex("3 \\times 2", font_size=30).next_to(triangle7, RIGHT)
        self.play(Write(left7), Write(right7))
        self.wait(0.5)

        # Show result
        res7 = MathTex("8 \\leq 6", font_size=30, color=RED).next_to(left7, DOWN, buff=0.3)
        cross7 = Cross(res7)
        self.play(Write(res7), Create(cross7))
        self.wait(1.5)
        self.play(FadeOut(triangle7, labels7, left7, right7, res7, cross7))

        # Show equilateral triangle with side x
        triangle8 = Triangle().scale(2).shift(UP*0.5)
        triangle8.set_fill(GREEN, opacity=0.5)
        labels8 = VGroup(
            MathTex("x").next_to(triangle8.get_vertices()[0], DOWN),
            MathTex("x").next_to(triangle8.get_vertices()[1], DOWN),
            MathTex("x").next_to(triangle8.get_vertices()[2], DOWN)
        )
        self.play(Create(triangle8), Write(labels8))
        self.wait(0.5)

        # Show inequality
        ineq8 = MathTex("2 \\times x \\leq 3 \\times x", font_size=30).next_to(triangle8, DOWN, buff=0.5)
        self.play(Write(ineq8))
        self.wait(1)

        # Simplify to 2 <= 3
        simp8 = MathTex("2 \\leq 3", font_size=30).next_to(ineq8, DOWN, buff=0.3)
        self.play(Write(simp8))
        self.wait(1.5)
        self.play(FadeOut(triangle8, labels8, ineq8, simp8))

        # Show two triangles with same shortest and longest but different middle sides
        triangle9 = Triangle().scale(2).shift(UP*0.5)
        triangle9.set_fill(BLUE, opacity=0.5)
        labels9 = VGroup(
            MathTex("4").next_to(triangle9.get_vertices()[0], DOWN),
            MathTex("5").next_to(triangle9.get_vertices()[1], DOWN),
            MathTex("6").next_to(triangle9.get_vertices()[2], DOWN)
        )
        self.play(Create(triangle9), Write(labels9))
        self.wait(0.5)

        # Show calculation for first triangle
        calc9 = MathTex("2 \\times 6", font_size=30).next_to(triangle9, LEFT)
        calc9b = MathTex("3 \\times 4", font_size=30).next_to(triangle9, RIGHT)
        self.play(Write(calc9), Write(calc9b))
        self.wait(0.5)

        # Show result
        res9 = MathTex("12 \\leq 12", font_size=30).next_to(calc9, DOWN, buff=0.3)
        self.play(Write(res9))
        self.wait(1.5)
        self.play(FadeOut(triangle9, labels9, calc9, calc9b, res9))

        # Show second triangle with same shortest and longest
        triangle10 = Triangle().scale(2).shift(UP*0.5)
        triangle10.set_fill(BLUE, opacity=0.5)
        labels10 = VGroup(
            MathTex("4").next_to(triangle10.get_vertices()[0], DOWN),
            MathTex("2").next_to(triangle10.get_vertices()[1], DOWN),
            MathTex("6").next_to(triangle10.get_vertices()[2], DOWN)
        )
        self.play(Create(triangle10), Write(labels10))
        self.wait(0.5)

        # Show calculation for second triangle
        calc10 = MathTex("2 \\times 6", font_size=30).next_to(triangle10, LEFT)
        calc10b = MathTex("3 \\times 4", font_size=30).next_to(triangle10, RIGHT)
        self.play(Write(calc10), Write(calc10b))
        self.wait(0.5)

        # Show result
        res10 = MathTex("12 \\leq 12", font_size=30).next_to(calc10, DOWN, buff=0.3)
        self.play(Write(res10))
        self.wait(1.5)
        self.play(FadeOut(triangle10, labels10, calc10, calc10b, res10))

        # Final rule summary
        final = Text("Rule 3: The middle side does not matter.", font_size=24).to_edge(DOWN)
        self.play(Write(final))
        self.wait(1.5)
        self.play(FadeOut(final, title))
