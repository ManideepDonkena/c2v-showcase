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
        grid_mobject.to_edge(DOWN)
        self.play(Write(grid_mobject))
        self.wait(1)

        # Highlight a and d
        a = grid_mobject.get_entries()[0]
        d = grid_mobject.get_entries()[3]
        a_copy = a.copy()
        d_copy = d.copy()
        a_copy.set_color(YELLOW)
        d_copy.set_color(YELLOW)
        self.play(a_copy.animate.scale(1.2), d_copy.animate.scale(1.2))
        self.wait(0.5)
        self.play(FadeOut(a_copy), FadeOut(d_copy))

        # Multiply a and d
        mult_text = MathTex("2 \\times 4 =", "8", font_size=36).next_to(grid_mobject, UP)
        self.play(Write(mult_text))
        self.wait(1.5)

        # Subtract b and c
        b = grid_mobject.get_entries()[1]
        c = grid_mobject.get_entries()[2]
        b_copy = b.copy()
        c_copy = c.copy()
        b_copy.set_color(RED)
        c_copy.set_color(RED)
        self.play(b_copy.animate.scale(1.2), c_copy.animate.scale(1.2))
        self.wait(0.5)
        self.play(FadeOut(b_copy), FadeOut(c_copy))

        # Show subtraction steps
        step1 = MathTex("8 - 1 =", "7", font_size=36).next_to(mult_text, DOWN)
        self.play(Write(step1))
        self.wait(1.5)

        step2 = MathTex("7 - 3 =", "4", font_size=36).next_to(step1, DOWN)
        self.play(Write(step2))
        self.wait(1.5)

        # Final result
        final_result = MathTex("\\text{Vell} = 4", font_size=40).set_color(GREEN).to_edge(UP)
        self.play(Transform(mult_text, final_result))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(grid_mobject), FadeOut(mult_text), FadeOut(step1), FadeOut(step2))
        self.wait(0.5)
