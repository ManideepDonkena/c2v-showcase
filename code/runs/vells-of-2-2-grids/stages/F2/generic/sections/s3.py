from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Rule: Multiplication Scope", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # First grid
        grid1 = Matrix([["a", "b"], ["c", "d"]], 
                       left_bracket="[[", right_bracket="]]").scale(0.8)
        grid1.to_corner(UL)
        grid1_label = Text("Grid 1", font_size=24).next_to(grid1, UP)

        # Second grid
        grid2 = Matrix([["d", "c"], ["b", "a"]], 
                       left_bracket="[[", right_bracket="]]").scale(0.8)
        grid2.to_corner(UR)
        grid2_label = Text("Grid 2", font_size=24).next_to(grid2, UP)

        # Lines connecting a to d in first grid
        line1 = Line(
            grid1.get_entries()[0].get_center(),
            grid1.get_entries()[3].get_center(),
            color=YELLOW,
            stroke_width=3
        )

        # Lines connecting d to a in second grid
        line2 = Line(
            grid2.get_entries()[0].get_center(),
            grid2.get_entries()[3].get_center(),
            color=YELLOW,
            stroke_width=3
        )

        # Fade out b-c lines
        line_b_c_1 = Line(
            grid1.get_entries()[1].get_center(),
            grid1.get_entries()[2].get_center(),
            color=RED,
            stroke_width=3
        ).set_opacity(0.5)

        line_b_c_2 = Line(
            grid2.get_entries()[1].get_center(),
            grid2.get_entries()[2].get_center(),
            color=RED,
            stroke_width=3
        ).set_opacity(0.5)

        # Show first grid and its connection
        self.play(Write(grid1), Write(grid1_label))
        self.wait(0.5)
        self.play(Create(line1))
        self.wait(1)

        # Show second grid and its connection
        self.play(Write(grid2), Write(grid2_label))
        self.wait(0.5)
        self.play(Create(line2))
        self.wait(1)

        # Fade out b-c lines to emphasize exclusivity
        self.play(FadeIn(line_b_c_1), FadeIn(line_b_c_2))
        self.wait(1.5)
        self.play(FadeOut(line_b_c_1), FadeOut(line_b_c_2))

        # Show vell formula
        vell_formula = MathTex("Vell = a \\times d - b - c", font_size=36).to_edge(DOWN)
        self.play(Write(vell_formula))
        self.wait(1.5)

        # Example
        example = MathTex("\\text{Example: } [[2, 1], [3, 4]] \\Rightarrow 2 \\times 4 - 1 - 3 = 4", font_size=28)
        example.next_to(vell_formula, UP)
        self.play(Write(example))
        self.wait(2)

        # Final cleanup
        self.play(FadeOut(title), FadeOut(grid1), FadeOut(grid2), 
                  FadeOut(grid1_label), FadeOut(grid2_label),
                  FadeOut(line1), FadeOut(line2),
                  FadeOut(vell_formula), FadeOut(example))
        self.wait(0.5)
