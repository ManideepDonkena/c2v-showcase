from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Worked Example Calculation", font_size=36).to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # Grid
        grid = [[2, 1], [3, 4]]
        grid_mobject = Matrix(grid, bracket_h_buff=0.3, bracket_v_buff=0.3).scale(0.8)
        grid_mobject.next_to(title, DOWN, buff=0.5)
        self.play(Write(grid_mobject))
        self.wait(1)

        # Highlight 2 and 4
        a = grid_mobject.get_entries()[0]  # 2
        d = grid_mobject.get_entries()[3]  # 4
        a_copy = a.copy()
        d_copy = d.copy()

        self.play(a.animate.set_color(YELLOW), d.animate.set_color(YELLOW))
        self.wait(1)

        # Multiply 2 and 4 (shown below the grid)
        mult_sign = MathTex("\\times", font_size=30)
        result_mult = MathTex("8", font_size=30)
        mult_row = VGroup(mult_sign, result_mult).arrange(RIGHT, buff=0.2)
        mult_row.next_to(grid_mobject, DOWN, buff=0.5)
        self.play(Write(mult_sign), Write(result_mult))
        self.wait(1)

        # Fade out multiplication
        self.play(FadeOut(mult_sign), FadeOut(result_mult))

        # Subtraction row layout (below the grid)
        b = grid_mobject.get_entries()[1]  # 1
        b_copy = b.copy()
        c = grid_mobject.get_entries()[2]  # 3
        c_copy = c.copy()
        minus_sign = MathTex("-", font_size=30)
        b_text = MathTex("1", font_size=30)
        minus_sign_2 = MathTex("-", font_size=30)
        c_text = MathTex("3", font_size=30)
        final_result = MathTex("= 4", font_size=40)
        calc_row = VGroup(minus_sign, b_text, minus_sign_2, c_text, final_result).arrange(RIGHT, buff=0.2)
        calc_row.next_to(grid_mobject, DOWN, buff=0.5)

        # Subtract 1 (b)
        self.play(Write(minus_sign), Write(b_text))
        self.wait(1)

        # Subtract 3 (c)
        self.play(Write(minus_sign_2), Write(c_text))
        self.wait(1)

        # Final result
        self.play(Write(final_result))
        self.wait(2)

        # Fade out everything except title and grid
        self.play(
            FadeOut(a), FadeOut(d),
            FadeOut(b), FadeOut(c),
            FadeOut(minus_sign), FadeOut(b_text),
            FadeOut(minus_sign_2), FadeOut(c_text),
            FadeOut(final_result)
        )
        self.wait(1)

        # Show final vell value
        vell_text = Text("Vell = 4", font_size=36).next_to(grid_mobject, DOWN, buff=0.5)
        self.play(Write(vell_text))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(grid_mobject), FadeOut(vell_text))
