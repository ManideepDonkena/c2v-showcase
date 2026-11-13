from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Rule: Multiplication Scope", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First grid
        grid1 = Matrix([[2, 1], [3, 4]], left_bracket="[[", right_bracket="]]").scale(0.8)
        grid1_label = Text("Grid 1", font_size=24).next_to(grid1, UP)
        self.play(Write(grid1), Write(grid1_label))
        self.wait(0.5)

        # Highlight a and d with lines
        a = grid1.get_entries()[0]
        d = grid1.get_entries()[3]
        line1 = Line(a.get_center(), d.get_center(), color=YELLOW, stroke_width=3)
        self.play(Create(line1))
        self.wait(0.5)

        # Second grid
        grid2 = Matrix([[4, 3], [1, 2]], left_bracket="[[", right_bracket="]]").scale(0.8).next_to(grid1, RIGHT, buff=2)
        grid2_label = Text("Grid 2", font_size=24).next_to(grid2, UP)
        self.play(Write(grid2), Write(grid2_label))
        self.wait(0.5)

        # Highlight d and a with lines
        d2 = grid2.get_entries()[0]
        a2 = grid2.get_entries()[3]
        line2 = Line(d2.get_center(), a2.get_center(), color=YELLOW, stroke_width=3)
        self.play(Create(line2))
        self.wait(0.5)

        # Fade out b-c connections
        b1 = grid1.get_entries()[1]
        c1 = grid1.get_entries()[2]
        line_bc = Line(b1.get_center(), c1.get_center(), color=RED, stroke_width=3)
        self.play(Create(line_bc))
        self.wait(0.5)
        self.play(FadeOut(line_bc))

        c2 = grid2.get_entries()[2]
        b2 = grid2.get_entries()[1]
        line_cb = Line(b2.get_center(), c2.get_center(), color=RED, stroke_width=3)
        self.play(Create(line_cb))
        self.wait(0.5)
        self.play(FadeOut(line_cb))

        # Vell formula
        vell_formula = MathTex("Vell = a \\times d - b - c", font_size=32).to_edge(DOWN)
        self.play(Write(vell_formula))
        self.wait(0.5)

        # Worked example
        example = MathTex("Vell([[2, 1], [3, 4]]) = 2 \\times 4 - 1 - 3 = 4", font_size=28).next_to(vell_formula, UP)
        self.play(Write(example))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(title, grid1, grid2, grid1_label, grid2_label, line1, line2, vell_formula, example))
        self.wait(0.5)
