from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Rule: Multiplication Scope", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First grid: [[a, b], [c, d]]
        grid1 = Matrix([["a", "b"], ["c", "d"]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        grid1.to_corner(UL)
        grid1_label = Text("Grid 1", font_size=24).next_to(grid1, UP)

        # Second grid: [[d, c], [b, a]]
        grid2 = Matrix([["d", "c"], ["b", "a"]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        grid2.to_corner(UR)
        grid2_label = Text("Grid 2", font_size=24).next_to(grid2, UP)

        # Draw grids
        self.play(Write(grid1), Write(grid1_label))
        self.wait(0.5)
        self.play(Write(grid2), Write(grid2_label))
        self.wait(0.5)

        # Connect a to d in grid1 (top-left to bottom-right)
        line1 = Line(
            grid1.get_entries()[0].get_center(),  # a
            grid1.get_entries()[3].get_center()   # d
        ).set_color(YELLOW)
        self.play(Create(line1))
        self.wait(0.5)

        # Connect d to a in grid2 (top-left to bottom-right)
        line2 = Line(
            grid2.get_entries()[0].get_center(),  # d
            grid2.get_entries()[3].get_center()   # a
        ).set_color(YELLOW)
        self.play(Create(line2))
        self.wait(0.5)

        # Fade out b-c connections (not used in vell)
        # In grid1, fade out b and c
        b1 = grid1.get_entries()[1]
        c1 = grid1.get_entries()[2]
        self.play(FadeOut(b1), FadeOut(c1))
        self.wait(0.5)

        # In grid2, fade out c and b
        c2 = grid2.get_entries()[1]
        b2 = grid2.get_entries()[2]
        self.play(FadeOut(b2), FadeOut(c2))
        self.wait(0.5)

        # Show vell formula
        vell_formula = MathTex("Vell = a \\times d - b - c", font_size=36).to_edge(DOWN)
        self.play(Write(vell_formula))
        self.wait(1)

        # Example: [[2, 1], [3, 4]]
        example_grid = Matrix([[2, 1], [3, 4]], bracket_h_buff=0.2, bracket_v_buff=0.2).to_corner(DL)
        example_label = Text("Example", font_size=24).next_to(example_grid, UP)
        self.play(Write(example_grid), Write(example_label))
        self.wait(0.5)

        # Highlight elements in example
        a = example_grid.get_entries()[0]
        d = example_grid.get_entries()[3]
        b = example_grid.get_entries()[1]
        c = example_grid.get_entries()[2]

        self.play(a.animate.set_color(YELLOW), d.animate.set_color(YELLOW))
        self.wait(0.5)
        self.play(b.animate.set_color(GREEN), c.animate.set_color(GREEN))
        self.wait(0.5)

        # Show vell calculation
        calc = MathTex("Vell = 2 \\times 4 - 1 - 3 = 8 - 1 - 3 = 4", font_size=24).next_to(vell_formula, DOWN)
        self.play(Write(calc))
        self.wait(1.5)
        # Final text
        final_text = Text("Only top-left and bottom-right are multiplied.", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(FadeOut(title, grid1, grid2, grid1_label, grid2_label, line1, line2,
                          vell_formula, example_grid, example_label, calc, final_text))
