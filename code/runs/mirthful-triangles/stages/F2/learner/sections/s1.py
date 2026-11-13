from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining Mirth", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        # First triangle: a, b, c with labels
        a = 4
        b = 10
        c = 12
        triangle = Polygon(
            [0, 0, 0], [c, 0, 0], [b * 0.5, a, 0],
            color=WHITE, fill_opacity=0.3
        )
        triangle.shift(LEFT * 1.5 + DOWN * 1.16)
        la = MathTex("a", font_size=24).next_to(triangle.get_vertices()[0], DOWN)
        lb = MathTex("b", font_size=24).next_to(triangle.get_vertices()[1], DOWN)
        lc = MathTex("c", font_size=24).next_to(triangle.get_vertices()[2], UP)

        triangle.shift(-3.54 * RIGHT + 0.0 * UP)  # layout: separation vector
        lb.shift(-3.58 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(triangle), Write(la), Write(lb), Write(lc))
        self.wait(0.5)

        # Inequality 2*c <= 3*a
        ineq = MathTex("2 \\times c", font_size=30).next_to(triangle, LEFT)
        ineq2 = MathTex("\\leq", font_size=30).next_to(ineq, RIGHT)
        ineq3 = MathTex("3 \\times a", font_size=30).next_to(ineq2, RIGHT)

        self.play(Write(ineq), Write(ineq2), Write(ineq3))
        self.wait(1)

        # Show algebraic transformation
        self.play(FadeOut(ineq), FadeOut(ineq2), FadeOut(ineq3))

        div = MathTex("\\frac{2c}{2} \\leq \\frac{3a}{2}", font_size=28).move_to(UP * 1.5)
        self.play(Write(div))
        self.wait(0.5)

        simp = MathTex("c \\leq 1.5 a", font_size=28).move_to(UP * 1.5)
        self.play(Transform(div, simp))
        self.wait(1)

        # Fade out
        self.play(FadeOut(triangle), FadeOut(la), FadeOut(lb), FadeOut(lc), FadeOut(div))

        # Second triangle: 10, 20, 30
        triangle2 = Polygon([0, 0, 0], [30, 0, 0], [15, 26, 0], color=WHITE, fill_opacity=0.3)
        triangle2.shift(LEFT * 1.5)
        
        la2 = MathTex("10", font_size=24).next_to(triangle2.get_vertices()[0], DOWN)
        lb2 = MathTex("20", font_size=24).next_to(triangle2.get_vertices()[1], DOWN)
        lc2 = MathTex("30", font_size=24).next_to(triangle2.get_vertices()[2], UP)

        self.play(Create(triangle2), Write(la2), Write(lb2), Write(lc2))
        self.wait(0.5)

        ineq_1 = MathTex("2 \\times 30", font_size=30).next_to(triangle2, LEFT)
        ineq_2 = MathTex(">", font_size=30).next_to(ineq_1, RIGHT)
        ineq_3 = MathTex("3 \\times 10", font_size=30).next_to(ineq_2, RIGHT)

        self.play(Write(ineq_1), Write(ineq_2), Write(ineq_3))
        self.wait(1.5)

        self.play(FadeOut(triangle2), FadeOut(la2), FadeOut(lb2), FadeOut(lc2), FadeOut(ineq_1), FadeOut(ineq_2), FadeOut(ineq_3))

        # Third triangle: 4, 10, 12
        triangle3 = Polygon([0, 0, 0], [12, 0, 0], [6, 10, 0], color=WHITE, fill_opacity=0.3)
        triangle3.shift(LEFT * 1.5)
        
        la3 = MathTex("4", font_size=24).next_to(triangle3.get_vertices()[0], DOWN)
        lb3 = MathTex("10", font_size=24).next_to(triangle3.get_vertices()[1], DOWN)
        lc3 = MathTex("12", font_size=24).next_to(triangle3.get_vertices()[2], UP)

        self.play(Create(triangle3), Write(la3), Write(lb3), Write(lc3))
        self.wait(0.5)

        calc1 = MathTex("2 \\times 12 = 24", font_size=28).next_to(triangle3, LEFT)
        calc2 = MathTex("3 \\times 4 = 12", font_size=28).next_to(triangle3, RIGHT)

        self.play(Write(calc1), Write(calc2))
        self.wait(0.5)

        ineq_res = MathTex("24 \\leq 12", font_size=30, color=RED).move_to(UP * 1.5)
        cross = Cross(ineq_res)
        self.play(Write(ineq_res), Create(cross))
        self.wait(1.5)

        self.play(FadeOut(triangle3), FadeOut(la3), FadeOut(lb3), FadeOut(lc3), FadeOut(calc1), FadeOut(calc2), FadeOut(ineq_res), FadeOut(cross))

        # Fourth triangle: 5, 100, 101
        triangle4 = Polygon([0, 0, 0], [101, 0, 0], [50.5, 99.5, 0], color=WHITE, fill_opacity=0.3)
        triangle4.shift(LEFT * 1.5)
        
        la4 = MathTex("5", font_size=24).next_to(triangle4.get_vertices()[0], DOWN)
        lb4 = MathTex("100", font_size=24).next_to(triangle4.get_vertices()[1], DOWN)
        lc4 = MathTex("101", font_size=24).next_to(triangle4.get_vertices()[2], UP)

        self.play(Create(triangle4), Write(la4), Write(lb4), Write(lc4))
        self.wait(0.5)

        calc3 = MathTex("2 \\times 101 = 202", font_size=28).next_to(triangle4, LEFT)
        calc4 = MathTex("3 \\times 5 = 15", font_size=28).next_to(triangle4, RIGHT)

        self.play(Write(calc3), Write(calc4))
        self.wait(0.5)

        ineq_res2 = MathTex("202 \\leq 15", font_size=30, color=RED).move_to(UP * 1.5)
        cross2 = Cross(ineq_res2)
        self.play(Write(ineq_res2), Create(cross2))
        self.wait(1.5)

        self.play(FadeOut(triangle4), FadeOut(la4), FadeOut(lb4), FadeOut(lc4), FadeOut(calc3), FadeOut(calc4), FadeOut(ineq_res2), FadeOut(cross2))

        # Fifth triangle: 10, 14, 15
        triangle5 = Polygon([0, 0, 0], [15, 0, 0], [7.5, 13, 0], color=WHITE, fill_opacity=0.3)
        triangle5.shift(LEFT * 1.5)
        
        la5 = MathTex("10", font_size=24).next_to(triangle5.get_vertices()[0], DOWN)
        lb5 = MathTex("14", font_size=24).next_to(triangle5.get_vertices()[1], DOWN)
        lc5 = MathTex("15", font_size=24).next_to(triangle5.get_vertices()[2], UP)

        self.play(Create(triangle5), Write(la5), Write(lb5), Write(lc5))
        self.wait(0.5)

        question = Text("Check the rule:", font_size=24).to_edge(UP)
        self.play(Transform(title, question))
        self.wait(0.5)

        calc5 = MathTex("2 \\times 15", font_size=30).next_to(triangle5, LEFT)
        calc6 = MathTex("\\leq", font_size=30).next_to(calc5, RIGHT)
        calc7 = MathTex("3 \\times 10", font_size=30).next_to(calc6, RIGHT)

        self.play(Write(calc5), Write(calc6), Write(calc7))
        self.wait(0.5)

        result = MathTex("30 \\leq 30", font_size=30).move_to(UP * 1.5)
        self.play(Transform(calc5, result))
        self.wait(0.5)

        # Pulse green
        self.play(triangle5.animate.set_fill(GREEN, opacity=0.6), run_time=0.5)
        self.wait(1)

        self.play(FadeOut(triangle5), FadeOut(la5), FadeOut(lb5), FadeOut(lc5), FadeOut(calc5))

        # Sixth triangle: 2, 3, 4
        triangle6 = Polygon([0, 0, 0], [4, 0, 0], [2, 3.5, 0], color=WHITE, fill_opacity=0.3)
        triangle6.shift(LEFT * 1.5)
        
        la6 = MathTex("2", font_size=24).next_to(triangle6.get_vertices()[0], DOWN)
        lb6 = MathTex("3", font_size=24).next_to(triangle6.get_vertices()[1], DOWN)
        lc6 = MathTex("4", font_size=24).next_to(triangle6.get_vertices()[2], UP)

        self.play(Create(triangle6), Write(la6), Write(lb6), Write(lc6))
        self.wait(0.5)

        calc8 = MathTex("2 \\times 4 = 8", font_size=28).next_to(triangle6, LEFT)
        calc9 = MathTex("3 \\times 2 = 6", font_size=28).next_to(triangle6, RIGHT)

        self.play(Write(calc8), Write(calc9))
        self.wait(0.5)

        ineq_res3 = MathTex("8 \\leq 6", font_size=30, color=RED).move_to(UP * 1.5)
        cross3 = Cross(ineq_res3)
        self.play(Write(ineq_res3), Create(cross3))
        self.wait(1.5)

        self.play(FadeOut(triangle6), FadeOut(la6), FadeOut(lb6), FadeOut(lc6), FadeOut(calc8), FadeOut(calc9), FadeOut(ineq_res3), FadeOut(cross3))

        # Final text
        final = Text("A triangle is mirthful if 2×longest ≤ 3×shortest", font_size=24).to_edge(DOWN)
        self.play(Write(final))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(final))
