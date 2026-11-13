from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Worked Example Calculation", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid
        grid = [[2, 1], [3, 4]]
        grid_mobject = Matrix(grid).scale(1.2)
        grid_mobject.to_edge(DOWN)
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
        mult_symbol = MathTex("\\times", font_size=36).next_to(a_copy, RIGHT)
        result = MathTex("8", font_size=36).next_to(mult_symbol, RIGHT)
        self.play(Write(mult_symbol), Write(result))
        self.wait(1)

        # Fade out multiplication
        self.play(FadeOut(mult_symbol), FadeOut(result))

        # Subtract 1 and 3
        b = grid_mobject.get_entries()[1]  # 1
        c = grid_mobject.get_entries()[2]  # 3

        self.play(b.animate.set_color(RED), c.animate.set_color(RED))
        self.wait(0.5)

        minus1 = MathTex("-1", font_size=36).next_to(a_copy, DOWN, buff=0.5)
        self.play(Write(minus1))
        self.wait(1)

        minus2 = MathTex("-3", font_size=36).next_to(minus1, RIGHT, buff=0.3)
        self.play(Write(minus2))
        self.wait(1)

        # Final result
        final_result = MathTex("= 4", font_size=40).next_to(minus2, RIGHT, buff=0.5)
        self.play(Write(final_result))
        self.wait(1.5)

        # Show definition and rules
        definition = Text("Vell of [[a,b],[c,d]] is a×d − b − c", font_size=24).to_edge(UP)
        self.play(Transform(title, definition))
        self.wait(1)

        rule1 = Text("(1) Only top-left and bottom-right are multiplied", font_size=20).next_to(definition, DOWN, buff=0.3)
        rule2 = Text("(2) Swapping b and c keeps the vell", font_size=20).next_to(rule1, DOWN, buff=0.3)

        self.play(Write(rule1))
        self.wait(1)
        self.play(Write(rule2))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(grid_mobject),
            FadeOut(a), FadeOut(d), FadeOut(b), FadeOut(c),
            FadeOut(minus1), FadeOut(minus2), FadeOut(final_result),
            FadeOut(rule1), FadeOut(rule2),
            FadeOut(title)
        )
        self.wait(0.5)
