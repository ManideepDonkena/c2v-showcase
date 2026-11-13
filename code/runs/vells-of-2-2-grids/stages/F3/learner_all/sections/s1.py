from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Vell Formula", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        # Grid definition
        grid = Matrix([["a", "b"], ["c", "d"]], 
                      bracket_h_buff=0.2, bracket_v_buff=0.2).scale(0.8)
        grid.to_corner(UL)
        grid_label = Text("Grid: ", font_size=24).next_to(grid, LEFT)
        self.play(Write(grid_label), Write(grid))
        self.wait(1)

        # Highlight a and d
        a = grid.get_entries()[0]
        d = grid.get_entries()[3]
        highlight_a = SurroundingRectangle(a, color=YELLOW, buff=0.1)
        highlight_d = SurroundingRectangle(d, color=YELLOW, buff=0.1)
        self.play(Create(highlight_a), Create(highlight_d))
        self.wait(1)

        # Arrow from a to d
        arrow = Arrow(start=a.get_center(), end=d.get_center(), color=GREEN, buff=0.1)
        self.play(GrowArrow(arrow))
        self.wait(1)

        # Cross out b and c
        b = grid.get_entries()[1]
        c = grid.get_entries()[2]
        cross_b = Cross(b, color=RED)
        cross_c = Cross(c, color=RED)
        self.play(Create(cross_b), Create(cross_c))
        self.wait(1)

        # Formula
        formula = MathTex("a \\times d - b - c", font_size=40).next_to(grid, DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(1.5)

        # Fade out grid and formula
        self.play(FadeOut(grid), FadeOut(grid_label), FadeOut(highlight_a), FadeOut(highlight_d),
                  FadeOut(arrow), FadeOut(cross_b), FadeOut(cross_c), FadeOut(formula))

        # Example 1: [[5, 2], [3, 1]]
        grid1 = Matrix([[5, 2], [3, 1]], bracket_h_buff=0.2, bracket_v_buff=0.2).scale(0.8)
        grid1.to_corner(UL)
        self.play(Write(grid1))
        self.wait(1)

        # Multiply top-left and bottom-right
        prod = MathTex("5 \\times 1 = 5", font_size=30).next_to(grid1, DOWN, buff=0.5)
        self.play(Write(prod))
        self.wait(1.5)

        # Subtract b (2)
        step1 = MathTex("5 - 2 = 3", font_size=30).next_to(prod, DOWN, buff=0.3)
        self.play(Write(step1))
        self.wait(1.5)

        # Subtract c (3)
        step2 = MathTex("3 - 3 = 0", font_size=30).next_to(step1, DOWN, buff=0.3)
        self.play(Write(step2))
        self.wait(1.5)

        # Fade out first example
        self.play(FadeOut(grid1), FadeOut(prod), FadeOut(step1), FadeOut(step2))

        # Example 2: [[10, 5], [2, 3]]
        grid2 = Matrix([[10, 5], [2, 3]], bracket_h_buff=0.2, bracket_v_buff=0.2).scale(0.8)
        grid2.to_corner(UL)
        self.play(Write(grid2))
        self.wait(1)

        # Multiply top-left and bottom-right
        prod2 = MathTex("10 \\times 3 = 30", font_size=30).next_to(grid2, DOWN, buff=0.5)
        self.play(Write(prod2))
        self.wait(1.5)

        # Say "This is not the final answer"
        note = Text("This is not the final answer.", font_size=24).next_to(prod2, DOWN, buff=0.3)
        self.play(Write(note))
        self.wait(1.5)

        # Subtract b (5)
        step3 = MathTex("30 - 5 = 25", font_size=30).next_to(note, DOWN, buff=0.3)
        self.play(Write(step3))
        self.wait(1.5)

        # Say "Subtract the second number"
        note2 = Text("Subtract the second number.", font_size=24).next_to(step3, DOWN, buff=0.3)
        self.play(Write(note2))
        self.wait(1.5)

        # Subtract c (2)
        step4 = MathTex("25 - 2 = 23", font_size=30).next_to(note2, DOWN, buff=0.3)
        self.play(Write(step4))
        self.wait(1.5)

        # Say "Subtract the third number"
        note3 = Text("Subtract the third number.", font_size=24).next_to(step4, DOWN, buff=0.3)
        self.play(Write(note3))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(grid2), FadeOut(prod2), FadeOut(note), FadeOut(step3),
                  FadeOut(note2), FadeOut(step4), FadeOut(note3))

        self.wait(0.5)
