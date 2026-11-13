from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Rule: Multiplication Scope", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grids with diagonal lines
        grid1 = Matrix([[5, 2], [3, 1]], left_bracket="[[", right_bracket="]]").scale(0.8)
        grid2 = Matrix([[10, 5], [2, 3]], left_bracket="[[", right_bracket="]]").scale(0.8)
        grid3 = Matrix([[0, 5], [5, 0]], left_bracket="[[", right_bracket="]]").scale(0.8)

        # Grid labels
        a1, b1, c1, d1 = 5, 2, 3, 1
        a2, b2, c2, d2 = 10, 5, 2, 3
        a3, b3, c3, d3 = 0, 5, 5, 0

        # First grid: [[5, 2], [3, 1]]
        self.play(Write(grid1))
        self.wait(0.5)

        # Highlight a and d
        a1_mob = grid1.get_entries()[0]
        d1_mob = grid1.get_entries()[3]
        self.play(a1_mob.animate.set_color(YELLOW), d1_mob.animate.set_color(YELLOW))
        self.wait(0.5)
        
        # Multiply a*d = 5*1 = 5
        prod1 = MathTex("5 \\times 1 = 5", font_size=24).next_to(grid1, DOWN)
        self.play(Write(prod1))
        self.wait(0.5)

        # Subtract b = 2
        self.play(a1_mob.animate.set_color(WHITE), d1_mob.animate.set_color(WHITE))
        b1_mob = grid1.get_entries()[1]
        self.play(b1_mob.animate.set_color(RED))
        sub1 = MathTex("5 - 2 = 3", font_size=24).next_to(prod1, DOWN)
        self.play(Write(sub1))
        self.wait(0.5)

        # Subtract c = 3
        c1_mob = grid1.get_entries()[2]
        self.play(c1_mob.animate.set_color(RED))
        sub2 = MathTex("3 - 3 = 0", font_size=24).next_to(sub1, DOWN)
        self.play(Write(sub2))
        self.wait(0.5)

        # Final answer
        final1 = MathTex("\\text{Final Answer: } 0", font_size=30).next_to(sub2, DOWN)
        self.play(Write(final1))
        self.wait(1)

        # Second grid: [[10, 5], [2, 3]]
        self.play(FadeOut(grid1, prod1, sub1, sub2, final1))
        self.play(Write(grid2))
        self.wait(0.5)

        a2_mob = grid2.get_entries()[0]
        d2_mob = grid2.get_entries()[3]
        self.play(a2_mob.animate.set_color(YELLOW), d2_mob.animate.set_color(YELLOW))
        self.wait(0.5)

        prod2 = MathTex("10 \\times 3 = 30", font_size=24).next_to(grid2, DOWN)
        self.play(Write(prod2))
        self.wait(0.5)

        # Subtract b = 5
        self.play(a2_mob.animate.set_color(WHITE), d2_mob.animate.set_color(WHITE))
        b2_mob = grid2.get_entries()[1]
        self.play(b2_mob.animate.set_color(RED))
        sub3 = MathTex("30 - 5 = 25", font_size=24).next_to(prod2, DOWN)
        self.play(Write(sub3))
        self.wait(0.5)

        # Subtract c = 2
        c2_mob = grid2.get_entries()[2]
        self.play(c2_mob.animate.set_color(RED))
        sub4 = MathTex("25 - 2 = 23", font_size=24).next_to(sub3, DOWN)
        self.play(Write(sub4))
        self.wait(0.5)

        final2 = MathTex("\\text{Final Answer: } 23", font_size=30).next_to(sub4, DOWN)
        self.play(Write(final2))
        self.wait(1)

        # Third grid: [[0, 5], [5, 0]]
        self.play(FadeOut(grid2, prod2, sub3, sub4, final2))
        self.play(Write(grid3))
        self.wait(0.5)

        a3_mob = grid3.get_entries()[0]
        d3_mob = grid3.get_entries()[3]
        self.play(a3_mob.animate.set_color(YELLOW), d3_mob.animate.set_color(YELLOW))
        self.wait(0.5)

        prod3 = MathTex("0 \\times 0 = 0", font_size=24).next_to(grid3, DOWN)
        self.play(Write(prod3))
        self.wait(0.5)

        # Subtract b = 5
        self.play(a3_mob.animate.set_color(WHITE), d3_mob.animate.set_color(WHITE))
        b3_mob = grid3.get_entries()[1]
        self.play(b3_mob.animate.set_color(RED))
        sub5 = MathTex("0 - 5 = -5", font_size=24).next_to(prod3, DOWN)
        self.play(Write(sub5))
        self.wait(0.5)

        # Subtract c = 5
        c3_mob = grid3.get_entries()[2]
        self.play(c3_mob.animate.set_color(RED))
        sub6 = MathTex("-5 - 5 = -10", font_size=24).next_to(sub5, DOWN)
        self.play(Write(sub6))
        self.wait(0.5)

        final3 = MathTex("\\text{Final Answer: } -10", font_size=30).next_to(sub6, DOWN)
        self.play(Write(final3))
        self.wait(1)

        # Formula
        formula = MathTex("a \\times d - b - c", font_size=30).to_edge(UP)
        self.play(Transform(title, formula))
        self.wait(1)

        # Swap b and c visually
        grid4 = Matrix([[1, 2], [2, 1]], left_bracket="[[", right_bracket="]]").scale(0.8).to_edge(DOWN)
        self.play(Write(grid4))
        self.wait(0.5)

        # Show subtraction order does not matter
        b4_mob = grid4.get_entries()[1]
        c4_mob = grid4.get_entries()[2]
        self.play(b4_mob.animate.set_color(RED), c4_mob.animate.set_color(BLUE))
        self.wait(0.5)
        
        # Formula with swapped terms
        formula_swap = MathTex("a \\times d - c - b", font_size=30).next_to(grid4, UP)
        self.play(Write(formula_swap))
        self.wait(1)

        # Show that order doesn't matter
        note = Text("Order of subtraction does not change result", font_size=24).next_to(formula_swap, DOWN)
        self.play(Write(note))
        self.wait(1.5)
        self.play(FadeOut(grid4, formula_swap, note))

        # Show zero subtraction
        zero_note = Text("Subtracting 0 leaves number unchanged", font_size=24).to_edge(DOWN)
        self.play(Write(zero_note))
        self.wait(1)
        self.play(FadeOut(zero_note))

        # Show correct vs wrong method
        grid5 = Matrix([["a", "b"], ["c", "d"]], left_bracket="[[", right_bracket="]]").scale(0.8).to_edge(DOWN)
        self.play(Write(grid5))
        self.wait(0.5)

        # Draw diagonal lines
        diag1 = Line(
            grid5.get_entries()[0].get_corner(UL),
            grid5.get_entries()[3].get_corner(DR)
        ).set_color(YELLOW)
        diag2 = Line(
            grid5.get_entries()[1].get_corner(UR),
            grid5.get_entries()[2].get_corner(DL)
        ).set_color(GRAY)

        self.play(Create(diag1), Create(diag2))
        self.wait(0.5)

        # Red X over full product
        cross = Cross(grid5).set_color(RED)
        self.play(Create(cross))
        self.wait(0.5)

        # Show correct method
        self.play(FadeOut(cross, diag2))
        self.wait(0.5)

        # Final formula
        final_formula = MathTex("a \\times d - b - c", font_size=36).to_edge(UP)
        self.play(Transform(title, final_formula))
        self.wait(1)

        # Rearranging equation
        rearranged = MathTex("a \\times d = b + c", font_size=30).next_to(final_formula, DOWN)
        self.play(Write(rearranged))
        self.wait(1.5)

        self.play(FadeOut(title, grid5, diag1, rearranged))
