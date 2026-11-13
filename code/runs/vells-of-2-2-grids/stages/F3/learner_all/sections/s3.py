from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Rule: Multiplication Scope", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        # Grids with connections
        grid1 = Matrix([['a', 'b'], ['c', 'd']], 
                       bracket_h_buff=0.2, bracket_v_buff=0.2)
        grid2 = Matrix([['d', 'c'], ['b', 'a']],
                       bracket_h_buff=0.2, bracket_v_buff=0.2)

        grid1.shift(LEFT * 3)
        grid2.shift(RIGHT * 3)

        # Lines connecting a to d
        line1 = Line(grid1.get_entries()[0].get_center(), grid1.get_entries()[3].get_center())
        line2 = Line(grid2.get_entries()[0].get_center(), grid2.get_entries()[3].get_center())

        # Fade out b-c lines
        bc_line1 = Line(grid1.get_entries()[1].get_center(), grid1.get_entries()[2].get_center()).set_opacity(0.3)
        bc_line2 = Line(grid2.get_entries()[1].get_center(), grid2.get_entries()[2].get_center()).set_opacity(0.3)

        # Show first grid
        self.play(Write(grid1), Write(line1))
        self.wait(1)
        self.play(Write(bc_line1))
        self.wait(1)

        # Show second grid
        self.play(Write(grid2), Write(line2))
        self.wait(1)
        self.play(Write(bc_line2))
        self.wait(1.5)

        # Fade out grids and lines
        self.play(FadeOut(grid1), FadeOut(grid2), FadeOut(line1), FadeOut(line2), 
                  FadeOut(bc_line1), FadeOut(bc_line2))

        # Show example grid [[5, 2], [3, 1]]
        grid_example = Matrix([[5, 2], [3, 1]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        grid_example.shift(UP * 0.5)

        self.play(Write(grid_example))
        self.wait(0.5)

        # Show multiplication step
        product = MathTex("5 \\times 1 = 5", font_size=36).next_to(grid_example, DOWN)
        self.play(Write(product))
        self.wait(1.5)

        # Subtract b (2)
        minus_b = MathTex("- 2 = 3", font_size=36).next_to(product, RIGHT)
        self.play(Write(minus_b))
        self.wait(1.5)

        # Subtract c (3)
        minus_c = MathTex("- 3 = 0", font_size=36).next_to(minus_b, RIGHT)
        self.play(Write(minus_c))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(grid_example), FadeOut(product), FadeOut(minus_b), FadeOut(minus_c))

        # Show second example grid [[10, 5], [2, 3]]
        grid_example2 = Matrix([[10, 5], [2, 3]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        grid_example2.shift(UP * 0.5)

        self.play(Write(grid_example2))
        self.wait(0.5)

        # Show multiplication step
        product2 = MathTex("10 \\times 3 = 30", font_size=36).next_to(grid_example2, DOWN)
        self.play(Write(product2))
        self.wait(1.5)

        # Subtract b (5)
        minus_b2 = MathTex("- 5 = 25", font_size=36).next_to(product2, RIGHT)
        self.play(Write(minus_b2))
        self.wait(1.5)

        # Subtract c (2)
        minus_c2 = MathTex("- 2 = 23", font_size=36).next_to(minus_b2, RIGHT)
        self.play(Write(minus_c2))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(grid_example2), FadeOut(product2), FadeOut(minus_b2), FadeOut(minus_c2))

        # Show final note about subtraction
        note = Text("Subtract both off-diagonal elements from the product.", font_size=24).to_edge(DOWN)
        self.play(Write(note))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(note))
