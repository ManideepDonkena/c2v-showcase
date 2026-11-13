from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Rule: Swapping b and c", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid 1: [[5, 2], [3, 1]]
        grid1 = Matrix([[5, 2], [3, 1]], left_bracket="[[", right_bracket="]]").scale(0.8)
        grid1.to_corner(UL)
        self.play(Write(grid1))
        self.wait(0.5)

        # Highlight 5 and 1 to multiply
        highlight_5 = SurroundingRectangle(grid1.get_entries()[0], color=YELLOW, buff=0.1)
        highlight_1 = SurroundingRectangle(grid1.get_entries()[3], color=YELLOW, buff=0.1)
        self.play(Create(highlight_5), Create(highlight_1))
        self.wait(0.5)

        # Multiply 5 and 1
        mult_result = MathTex("5 \\times 1 = 5", font_size=24).next_to(grid1, DOWN, buff=0.5)
        self.play(Write(mult_result))
        self.wait(0.5)

        # Subtract 2 from 5
        sub_2 = MathTex("5 - 2 = 3", font_size=24).next_to(mult_result, DOWN, buff=0.5)
        self.play(Write(sub_2))
        self.wait(0.5)

        # Subtract 3 from 3
        sub_3 = MathTex("3 - 3 = 0", font_size=24).next_to(sub_2, DOWN, buff=0.5)
        self.play(Write(sub_3))
        self.wait(0.5)

        # Final result label
        final_label1 = Text("Vell = 0", font_size=24).next_to(sub_3, DOWN, buff=0.5)
        self.play(Write(final_label1))
        self.wait(0.5)

        # Fade out grid1 and results
        self.play(FadeOut(grid1), FadeOut(highlight_5), FadeOut(highlight_1), FadeOut(mult_result), FadeOut(sub_2), FadeOut(sub_3), FadeOut(final_label1))

        # Grid 2: [[10, 5], [2, 3]]
        grid2 = Matrix([[10, 5], [2, 3]], left_bracket="[[", right_bracket="]]").scale(0.8)
        grid2.to_corner(UL)
        self.play(Write(grid2))
        self.wait(0.5)

        # Highlight 10 and 3 to multiply
        highlight_10 = SurroundingRectangle(grid2.get_entries()[0], color=YELLOW, buff=0.1)
        highlight_3 = SurroundingRectangle(grid2.get_entries()[3], color=YELLOW, buff=0.1)
        self.play(Create(highlight_10), Create(highlight_3))
        self.wait(0.5)

        # Multiply 10 and 3
        mult_result2 = MathTex("10 \\times 3 = 30", font_size=24).next_to(grid2, DOWN, buff=0.5)
        self.play(Write(mult_result2))
        self.wait(0.5)

        # Subtract 5 from 30
        sub_5 = MathTex("30 - 5 = 25", font_size=24).next_to(mult_result2, DOWN, buff=0.5)
        self.play(Write(sub_5))
        self.wait(0.5)

        # Subtract 2 from 25
        sub_2_2 = MathTex("25 - 2 = 23", font_size=24).next_to(sub_5, DOWN, buff=0.5)
        self.play(Write(sub_2_2))
        self.wait(0.5)

        # Final result label
        final_label2 = Text("Vell = 23", font_size=24).next_to(sub_2_2, DOWN, buff=0.5)
        self.play(Write(final_label2))
        self.wait(0.5)

        # Fade out grid2 and results
        self.play(FadeOut(grid2), FadeOut(highlight_10), FadeOut(highlight_3), FadeOut(mult_result2), FadeOut(sub_5), FadeOut(sub_2_2), FadeOut(final_label2))

        # Grid 3: [[0, 5], [5, 0]]
        grid3 = Matrix([[0, 5], [5, 0]], left_bracket="[[", right_bracket="]]").scale(0.8)
        grid3.to_corner(UL)
        self.play(Write(grid3))
        self.wait(0.5)

        # Highlight 0 and 0 to multiply
        highlight_0_1 = SurroundingRectangle(grid3.get_entries()[0], color=YELLOW, buff=0.1)
        highlight_0_2 = SurroundingRectangle(grid3.get_entries()[3], color=YELLOW, buff=0.1)
        self.play(Create(highlight_0_1), Create(highlight_0_2))
        self.wait(0.5)

        # Multiply 0 and 0
        mult_result3 = MathTex("0 \\times 0 = 0", font_size=24).next_to(grid3, DOWN, buff=0.5)
        self.play(Write(mult_result3))
        self.wait(0.5)

        # Subtract 5 from 0
        sub_5_3 = MathTex("0 - 5 = -5", font_size=24).next_to(mult_result3, DOWN, buff=0.5)
        self.play(Write(sub_5_3))
        self.wait(0.5)

        # Subtract 5 from -5
        sub_5_4 = MathTex("-5 - 5 = -10", font_size=24).next_to(sub_5_3, DOWN, buff=0.5)
        self.play(Write(sub_5_4))
        self.wait(0.5)

        # Final result label
        final_label3 = Text("Vell = -10", font_size=24).next_to(sub_5_4, DOWN, buff=0.5)
        self.play(Write(final_label3))
        self.wait(0.5)

        # Fade out grid3 and results
        self.play(FadeOut(grid3), FadeOut(highlight_0_1), FadeOut(highlight_0_2), FadeOut(mult_result3), FadeOut(sub_5_3), FadeOut(sub_5_4), FadeOut(final_label3))

        # Formula: a×d - b - c
        formula = MathTex("a \\times d - b - c", font_size=36).to_edge(UP)
        formula.shift(0.0 * RIGHT + 0.41 * UP)  # layout: separation vector
        self.play(Write(formula))
        self.wait(0.5)

        # Swap b and c visually
        swapped_formula = MathTex("a \\times d - c - b", font_size=36).next_to(formula, DOWN, buff=0.5)
        swapped_formula.shift(0.0 * RIGHT + -0.3 * UP)  # layout: separation vector
        self.play(Write(swapped_formula))
        self.wait(0.5)

        # Show that order doesn't matter
        explanation = Text("Subtraction order does not change result", font_size=24).next_to(swapped_formula, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(1)

        # Fade out
        self.play(FadeOut(formula), FadeOut(swapped_formula), FadeOut(explanation))

        # Side-by-side grids with b and c swapped
        grid_a = Matrix([[1, 1], [2, 4]], left_bracket="[[", right_bracket="]]").scale(0.6).to_corner(UL)
        grid_b = Matrix([[1, 2], [1, 4]], left_bracket="[[", right_bracket="]]").scale(0.6).to_corner(UR)

        self.play(Write(grid_a), Write(grid_b))
        self.wait(0.5)

        # Formula for both
        formula_a = MathTex("a \\times d - b - c", font_size=24).next_to(grid_a, DOWN, buff=0.5)
        formula_b = MathTex("a \\times d - b - c", font_size=24).next_to(grid_b, DOWN, buff=0.5)

        self.play(Write(formula_a), Write(formula_b))
        self.wait(1)

        # Highlight subtraction steps
        highlight_b = SurroundingRectangle(grid_a.get_entries()[1], color=RED, buff=0.1)
        highlight_c = SurroundingRectangle(grid_a.get_entries()[2], color=GREEN, buff=0.1)
        self.play(Create(highlight_b), Create(highlight_c))
        self.wait(0.5)

        # Show that order doesn't matter
        explanation2 = Text("Order of subtraction does not change result", font_size=24).next_to(formula_a, DOWN, buff=0.5)
        explanation2.shift(2.31 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(explanation2))
        self.wait(1)

        # Fade out
        self.play(FadeOut(grid_a), FadeOut(grid_b), FadeOut(formula_a), FadeOut(formula_b), FadeOut(highlight_b), FadeOut(highlight_c), FadeOut(explanation2))

        # Show subtraction of zero leaves unchanged
        zero_example = MathTex("5 - 0 = 5", font_size=36).to_edge(UP)
        self.play(Write(zero_example))
        self.wait(1)

        self.play(FadeOut(zero_example))

        # Show correct vs incorrect formula
        correct = MathTex("a \\times d - b - c", font_size=36).to_edge(UP)
        incorrect = MathTex("a \\times b \\times c \\times d", font_size=36).next_to(correct, DOWN, buff=0.5)
        x_mark = Cross(incorrect, color=RED)

        self.play(Write(correct), Write(incorrect), Create(x_mark))
        self.wait(1)

        self.play(FadeOut(correct), FadeOut(incorrect), FadeOut(x_mark))

        # Show formula with labels
        labeled_grid = Matrix([["a", "b"], ["c", "d"]], left_bracket="[[", right_bracket="]]").scale(0.8).to_corner(UL)
        self.play(Write(labeled_grid))
        self.wait(0.5)

        formula_label = Text("The formula is a times d, then subtract b, and then subtract c.", font_size=24).next_to(labeled_grid, DOWN, buff=0.5)
        self.play(Write(formula_label))
        self.wait(1)

        # Show equation
        equation = MathTex("a \\times d - b - c", font_size=36).next_to(labeled_grid, RIGHT, buff=1)
        self.play(Write(equation))
        self.wait(0.5)

        # Show result labeled as 0
        result_zero = Text("Vell = 0", font_size=36).next_to(equation, DOWN, buff=0.5)
        self.play(Write(result_zero))
        self.wait(0.5)

        # Rearrange equation
        rearranged = MathTex("a \\times d = b + c", font_size=36).next_to(result_zero, DOWN, buff=0.5)
        self.play(Write(rearranged))
        self.wait(1)

        # Fade out everything
        self.play(FadeOut(labeled_grid), FadeOut(formula_label), FadeOut(equation), FadeOut(result_zero), FadeOut(rearranged))

        self.wait(0.5)
