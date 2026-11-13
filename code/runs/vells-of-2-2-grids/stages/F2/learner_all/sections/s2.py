from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Worked Example Calculation", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First example: [[2, 1], [3, 4]]
        grid1 = Matrix([[2, 1], [3, 4]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        grid1.to_corner(UL)
        self.play(Write(grid1))
        self.wait(0.5)

        # Highlight 2 and 4
        cell_2 = grid1.get_entries()[0]
        cell_4 = grid1.get_entries()[3]
        pulse_2 = cell_2.copy().set_color(YELLOW).scale(1.2)
        pulse_4 = cell_4.copy().set_color(YELLOW).scale(1.2)
        self.play(
            FadeIn(pulse_2),
            FadeIn(pulse_4),
            run_time=0.5
        )
        self.wait(0.5)

        # Multiply 2 and 4
        mult = MathTex("2 \\times 4 =", "8", font_size=36).next_to(grid1, DOWN)
        self.play(Write(mult))
        self.wait(0.5)

        # Subtract 1
        minus_1 = MathTex("- 1 =", "7", font_size=36).next_to(mult, RIGHT)
        self.play(Write(minus_1))
        self.wait(0.5)

        # Subtract 3
        minus_3 = MathTex("- 3 =", "4", font_size=36).next_to(minus_1, RIGHT)
        self.play(Write(minus_3))
        self.wait(0.5)

        # Final answer
        final = MathTex("\\text{Vell} = 4", font_size=40).to_edge(DOWN)
        self.play(Write(final))
        self.wait(1)

        # Second example: [[5, 2], [3, 1]]
        self.play(FadeOut(grid1), FadeOut(pulse_2), FadeOut(pulse_4), FadeOut(mult), FadeOut(minus_1), FadeOut(minus_3), FadeOut(final))
        grid2 = Matrix([[5, 2], [3, 1]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        grid2.to_corner(UL)
        self.play(Write(grid2))
        self.wait(0.5)

        # Highlight 5 and 1
        cell_5 = grid2.get_entries()[0]
        cell_1 = grid2.get_entries()[3]
        pulse_5 = cell_5.copy().set_color(YELLOW).scale(1.2)
        pulse_1 = cell_1.copy().set_color(YELLOW).scale(1.2)
        self.play(
            FadeIn(pulse_5),
            FadeIn(pulse_1),
            run_time=0.5
        )
        self.wait(0.5)

        # Multiply 5 and 1
        mult2 = MathTex("5 \\times 1 =", "5", font_size=36).next_to(grid2, DOWN)
        self.play(Write(mult2))
        self.wait(0.5)

        # Subtract 2
        minus_2 = MathTex("- 2 =", "3", font_size=36).next_to(mult2, RIGHT)
        self.play(Write(minus_2))
        self.wait(0.5)

        # Subtract 3
        minus_3_2 = MathTex("- 3 =", "0", font_size=36).next_to(minus_2, RIGHT)
        self.play(Write(minus_3_2))
        self.wait(0.5)

        final2 = MathTex("\\text{Vell} = 0", font_size=40).to_edge(DOWN)
        self.play(Write(final2))
        self.wait(1)

        # Third example: [[10, 5], [2, 3]]
        self.play(FadeOut(grid2), FadeOut(pulse_5), FadeOut(pulse_1), FadeOut(mult2), FadeOut(minus_2), FadeOut(minus_3_2), FadeOut(final2))
        grid3 = Matrix([[10, 5], [2, 3]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        grid3.to_corner(UL)
        self.play(Write(grid3))
        self.wait(0.5)

        # Highlight 10 and 3
        cell_10 = grid3.get_entries()[0]
        cell_3 = grid3.get_entries()[3]
        pulse_10 = cell_10.copy().set_color(YELLOW).scale(1.2)
        pulse_3 = cell_3.copy().set_color(YELLOW).scale(1.2)
        self.play(
            FadeIn(pulse_10),
            FadeIn(pulse_3),
            run_time=0.5
        )
        self.wait(0.5)

        # Multiply 10 and 3
        mult3 = MathTex("10 \\times 3 =", "30", font_size=36).next_to(grid3, DOWN)
        self.play(Write(mult3))
        self.wait(0.5)

        # Subtract 5
        minus_5 = MathTex("- 5 =", "25", font_size=36).next_to(mult3, RIGHT)
        self.play(Write(minus_5))
        self.wait(0.5)

        # Subtract 2
        minus_2_3 = MathTex("- 2 =", "23", font_size=36).next_to(minus_5, RIGHT)
        self.play(Write(minus_2_3))
        self.wait(0.5)

        final3 = MathTex("\\text{Vell} = 23", font_size=40).to_edge(DOWN)
        self.play(Write(final3))
        self.wait(1)

        # Fourth example: [[0, 5], [5, 0]]
        self.play(FadeOut(grid3), FadeOut(pulse_10), FadeOut(pulse_3), FadeOut(mult3), FadeOut(minus_5), FadeOut(minus_2_3), FadeOut(final3))
        grid4 = Matrix([[0, 5], [5, 0]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        grid4.to_corner(UL)
        self.play(Write(grid4))
        self.wait(0.5)

        # Highlight 0 and 0
        cell_0 = grid4.get_entries()[0]
        cell_0_2 = grid4.get_entries()[3]
        pulse_0 = cell_0.copy().set_color(YELLOW).scale(1.2)
        pulse_0_2 = cell_0_2.copy().set_color(YELLOW).scale(1.2)
        self.play(
            FadeIn(pulse_0),
            FadeIn(pulse_0_2),
            run_time=0.5
        )
        self.wait(0.5)

        # Multiply 0 and 0
        mult4 = MathTex("0 \\times 0 =", "0", font_size=36).next_to(grid4, DOWN)
        self.play(Write(mult4))
        self.wait(0.5)

        # Subtract 5
        minus_5_2 = MathTex("- 5 =", "-5", font_size=36).next_to(mult4, RIGHT)
        self.play(Write(minus_5_2))
        self.wait(0.5)

        # Subtract 5 again
        minus_5_3 = MathTex("- 5 =", "-10", font_size=36).next_to(minus_5_2, RIGHT)
        self.play(Write(minus_5_3))
        self.wait(0.5)

        final4 = MathTex("\\text{Vell} = -10", font_size=40).to_edge(DOWN)
        self.play(Write(final4))
        self.wait(1)

        # Show subtraction of zero
        self.play(FadeOut(grid4), FadeOut(pulse_0), FadeOut(pulse_0_2), FadeOut(mult4), FadeOut(minus_5_2), FadeOut(minus_5_3), FadeOut(final4))
        zero_demo = MathTex("5 - 0 =", "5", font_size=36).to_edge(UP)
        zero_demo.shift(0.0 * RIGHT + 0.41 * UP)  # layout: separation vector
        self.play(Write(zero_demo))
        self.wait(1)

        # Formula explanation
        self.play(FadeOut(zero_demo))
        grid_formula = Matrix([["a", "b"], ["c", "d"]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        grid_formula.to_corner(UL)
        self.play(Write(grid_formula))
        self.wait(0.5)

        formula_text = Text("The formula is a times d, then subtract b, and then subtract c.", font_size=24).next_to(grid_formula, DOWN)
        formula_text.shift(3.4 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(formula_text))
        self.wait(1)

        formula_eq = MathTex("a \\times d - b - c", font_size=36).to_edge(DOWN)
        self.play(Write(formula_eq))
        self.wait(1)

        # Show equation rearrangement
        self.play(FadeOut(grid_formula), FadeOut(formula_text))
        eq_rearrange = MathTex("a \\times d - b - c = 0", font_size=36).to_edge(UP)
        eq_rearrange.shift(0.0 * RIGHT + 0.42 * UP)  # layout: separation vector
        self.play(Write(eq_rearrange))
        self.wait(1)

        rearranged = MathTex("a \\times d = b + c", font_size=36).next_to(eq_rearrange, DOWN)
        self.play(Write(rearranged))
        self.wait(1)

        # Show swapping b and c
        self.play(FadeOut(eq_rearrange), FadeOut(rearranged))

        grid_swap1 = Matrix([[2, 1], [3, 4]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        grid_swap1.to_corner(UL)
        self.play(Write(grid_swap1))
        self.wait(0.5)

        swap1_formula = MathTex("2 \\times 4 - 1 - 3 =", "4", font_size=36).next_to(grid_swap1, DOWN)
        self.play(Write(swap1_formula))
        self.wait(0.5)

        grid_swap2 = Matrix([[2, 3], [1, 4]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        grid_swap2.to_corner(UR)
        self.play(Write(grid_swap2))
        self.wait(0.5)

        swap2_formula = MathTex("2 \\times 4 - 3 - 1 =", "4", font_size=36).next_to(grid_swap2, DOWN)
        self.play(Write(swap2_formula))
        self.wait(1)

        # Final summary
        self.play(FadeOut(grid_swap1), FadeOut(swap1_formula), FadeOut(grid_swap2), FadeOut(swap2_formula))
        summary = Text("Swapping b and c keeps the vell.", font_size=30).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(1)

        self.play(FadeOut(summary))
        self.wait(0.5)
