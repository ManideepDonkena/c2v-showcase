from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Worked Example Calculation", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid
        grid = [[2, 1], [3, 4]]
        grid_mobject = Matrix(grid, bracket_h_buff=0.3, bracket_v_buff=0.3).scale(0.8)
        grid_mobject.to_edge(UP, buff=1.5)
        self.play(Write(grid_mobject))
        self.wait(1)

        # Highlight 2 and 4
        a = grid_mobject.get_entries()[0]  # 2
        d = grid_mobject.get_entries()[3]  # 4
        a_copy = a.copy()
        d_copy = d.copy()

        self.play(a.animate.set_color(YELLOW), d.animate.set_color(YELLOW))
        self.wait(1)

        # Multiply 2 and 4
        mult_sign = MathTex("\\times", font_size=30).next_to(a_copy, RIGHT)
        result_mult = MathTex("8", font_size=30).next_to(mult_sign, RIGHT)
        self.play(Write(mult_sign), Write(result_mult))
        self.wait(1.5)

        # Fade out multiplication
        self.play(FadeOut(mult_sign), FadeOut(result_mult))

        # Highlight 1 and 3
        b = grid_mobject.get_entries()[1]  # 1
        c = grid_mobject.get_entries()[2]  # 3
        self.play(b.animate.set_color(RED), c.animate.set_color(RED))
        self.wait(1)

        # Subtract 1
        minus_sign_1 = MathTex("-", font_size=30).next_to(a_copy, DOWN, buff=0.5)
        b_copy = b.copy()
        self.play(Write(minus_sign_1), Write(b_copy))
        self.wait(1.5)

        # Subtract 3
        minus_sign_2 = MathTex("-", font_size=30).next_to(b_copy, RIGHT)
        c_copy = c.copy()
        minus_sign_2.shift(0.24 * RIGHT + 0.0 * UP)  # layout: separation vector
        minus_sign_1.shift(0.0 * RIGHT + -0.29 * UP)  # layout: separation vector
        self.play(Write(minus_sign_2), Write(c_copy))
        self.wait(1.5)

        # Final result
        final_result = MathTex("= 4", font_size=40).next_to(c_copy, RIGHT)
        self.play(Write(final_result))
        self.wait(2)

        # Show formula and rules
        formula = MathTex("vell = a \\times d - b - c", font_size=30).to_edge(DOWN)
        rule1 = Text("Rule 1: Only top-left and bottom-right are multiplied.", font_size=24).next_to(formula, UP)
        rule2 = Text("Rule 2: Swapping b and c keeps the vell.", font_size=24).next_to(rule1, UP)

        self.play(Write(formula))
        self.wait(1.5)
        self.play(Write(rule1))
        self.wait(1.5)
        self.play(Write(rule2))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(grid_mobject), FadeOut(a), FadeOut(d),
                  FadeOut(b), FadeOut(c), FadeOut(a_copy), FadeOut(d_copy),
                  FadeOut(b_copy), FadeOut(c_copy), FadeOut(minus_sign_1),
                  FadeOut(minus_sign_2), FadeOut(final_result), FadeOut(formula),
                  FadeOut(rule1), FadeOut(rule2))
        self.wait(0.5)
