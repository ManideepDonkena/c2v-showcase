from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Vell Formula", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid definition
        grid_def = MathTex(r"\text{Grid: } [[a, b], [c, d]]").scale(0.8)
        grid_def.next_to(title, DOWN, buff=0.3)
        self.play(Write(grid_def))
        self.wait(0.5)

        # Grid with labels
        a, b, c, d = 5, 2, 3, 1
        grid = Matrix([[a, b], [c, d]]).scale(0.8)
        grid.next_to(grid_def, DOWN, buff=0.5)
        # Set bracket style after creation
        grid[0][0].set_bracket_style("[]")
        self.play(Write(grid))
        self.wait(0.5)

        # Highlight a and d
        highlight_a = SurroundingRectangle(grid.get_mob_matrix()[0][0], color=YELLOW, buff=0.1)
        highlight_d = SurroundingRectangle(grid.get_mob_matrix()[1][1], color=YELLOW, buff=0.1)
        self.play(Create(highlight_a), Create(highlight_d))
        self.wait(0.5)

        # Cross out b and c
        cross_b = Cross(grid.get_mob_matrix()[0][1])
        cross_c = Cross(grid.get_mob_matrix()[1][0])
        self.play(Create(cross_b), Create(cross_c))
        self.wait(0.5)

        # Equation
        equation = MathTex(r"a \times d - b - c").scale(0.8)
        equation.next_to(grid, RIGHT, buff=1)
        self.play(Write(equation))
        self.wait(0.5)

        # Example 1: [[5, 2], [3, 1]]
        example1 = Matrix([[5, 2], [3, 1]]).scale(0.7)
        example1.next_to(grid, DOWN, buff=1.5)
        # Set bracket style after creation
        example1[0][0].set_bracket_style("[]")
        self.play(Write(example1))
        self.wait(0.5)

        # Highlight 5 and 1
        highlight_5 = SurroundingRectangle(example1.get_mob_matrix()[0][0], color=YELLOW, buff=0.1)
        highlight_1 = SurroundingRectangle(example1.get_mob_matrix()[1][1], color=YELLOW, buff=0.1)
        self.play(Create(highlight_5), Create(highlight_1))
        self.wait(0.5)

        # Multiply 5 and 1
        mult_result = MathTex(r"5 \times 1 = 5").scale(0.7).next_to(example1, RIGHT, buff=1)
        self.play(Write(mult_result))
        self.wait(0.5)

        # Subtract 2
        sub_2 = MathTex(r"5 - 2 = 3").scale(0.7).next_to(mult_result, DOWN, buff=0.3)
        self.play(Write(sub_2))
        self.wait(0.5)

        # Subtract 3
        final_result1 = MathTex(r"3 - 3 = 0").scale(0.7).next_to(sub_2, DOWN, buff=0.3)
        self.play(Write(final_result1))
        self.wait(0.5)

        # Example 2: [[10, 5], [2, 3]]
        example2 = Matrix([[10, 5], [2, 3]]).scale(0.7)
        example2.next_to(example1, DOWN, buff=1.5)
        # Set bracket style after creation
        example2[0][0].set_bracket_style("[]")
        self.play(Write(example2))
        self.wait(0.5)

        # Pulse 10 and 3
        pulse_10 = example2.get_mob_matrix()[0][0].animate.scale(1.2).set_color(YELLOW)
        pulse_3 = example2.get_mob_matrix()[1][1].animate.scale(1.2).set_color(YELLOW)
        self.play(pulse_10, pulse_3)
        self.wait(0.5)

        # Multiply 10 and 3
        mult_result2 = MathTex(r"10 \times 3 = 30").scale(0.7).next_to(example2, RIGHT, buff=1)
        self.play(Write(mult_result2))
        self.wait(0.5)

        # Subtract 5
        sub_5 = MathTex(r"30 - 5 = 25").scale(0.7).next_to(mult_result2, DOWN, buff=0.3)
        self.play(Write(sub_5))
        self.wait(0.5)

        # Subtract 2
        final_result2 = MathTex(r"25 - 2 = 23").scale(0.7).next_to(sub_5, DOWN, buff=0.3)
        self.play(Write(final_result2))
        self.wait(0.5)

        # Example 3: [[0, 5], [5, 0]]
        example3 = Matrix([[0, 5], [5, 0]]).scale(0.7)
        example3.next_to(example2, DOWN, buff=1.5)
        # Set bracket style after creation
        example3[0][0].set_bracket_style("[]")
        self.play(Write(example3))
        self.wait(0.5)

        # Pulse 0 and 0
        pulse_0 = example3.get_mob_matrix()[0][0].animate.scale(1.2).set_color(YELLOW)
        pulse_0_2 = example3.get_mob_matrix()[1][1].animate.scale(1.2).set_color(YELLOW)
        self.play(pulse_0, pulse_0_2)
        self.wait(0.5)

        # Multiply 0 and 0
        mult_result3 = MathTex(r"0 \times 0 = 0").scale(0.7).next_to(example3, RIGHT, buff=1)
        self.play(Write(mult_result3))
        self.wait(0.5)

        # Subtract 5
        sub_5_2 = MathTex(r"0 - 5 = -5").scale(0.7).next_to(mult_result3, DOWN, buff=0.3)
        self.play(Write(sub_5_2))
        self.wait(0.5)

        # Subtract 5 again
        final_result3 = MathTex(r"-5 - 5 = -10").scale(0.7).next_to(sub_5_2, DOWN, buff=0.3)
        self.play(Write(final_result3))
        self.wait(0.5)

        # Show that subtracting zero leaves unchanged
        zero_note = Text("Subtracting 0 leaves number unchanged", font_size=24).to_edge(DOWN)
        self.play(Write(zero_note))
        self.wait(1.0)
        self.play(FadeOut(zero_note))

        # Compare with full multiplication
        full_mult = MathTex(r"a \times b \times c \times d").scale(0.7)
        full_mult.next_to(final_result3, DOWN, buff=1)
        cross_full = Cross(full_mult)
        self.play(Write(full_mult), Create(cross_full))
        self.wait(0.5)

        # Show correct method
        correct_method = MathTex(r"a \times d - b - c").scale(0.7)
        correct_method.next_to(full_mult, DOWN, buff=0.3)
        self.play(Write(correct_method))
        self.wait(0.5)

        # Formula explanation
        formula_text = Text("The formula is a times d, then subtract b, and then subtract c.", font_size=24)
        formula_text.next_to(correct_method, DOWN, buff=0.3)
        self.play(Write(formula_text))
        self.wait(1.0)
        self.play(FadeOut(formula_text))

        # Equation rearrangement
        eq = MathTex(r"a \times d - b - c = 0").scale(0.7)
        eq.next_to(correct_method, DOWN, buff=0.3)
        self.play(Write(eq))
        self.wait(0.5)

        # Rearranged equation
        rearranged = MathTex(r"a \times d = b + c").scale(0.7).next_to(eq, DOWN, buff=0.3)
        self.play(Write(rearranged))
        self.wait(1.0)

        # Side-by-side grids with swapped middle numbers
        grid1 = Matrix([[2, 1], [3, 4]]).scale(0.6)
        grid2 = Matrix([[2, 2], [3, 4]]).scale(0.6)
        grid1.next_to(rearranged, DOWN, buff=1)
        grid2.next_to(grid1, RIGHT, buff=1)
        # Set bracket style after creation
        grid1[0][0].set_bracket_style("[]")
        grid2[0][0].set_bracket_style("[]")

        self.play(Write(grid1), Write(grid2))
        self.wait(0.5)

        # Show vell calculation for both
        vell1 = MathTex(r"2 \times 4 - 1 - 3 = 4").scale(0.6).next_to(grid1, DOWN, buff=0.3)
        vell2 = MathTex(r"2 \times 4 - 2 - 3 = 4").scale(0.6).next_to(grid2, DOWN, buff=0.3)

        self.play(Write(vell1), Write(vell2))
        self.wait(1.0)

        # Final summary
        summary = Text("The vell is defined as a×d - b - c", font_size=24).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(1.5)
        self.play(FadeOut(summary), FadeOut(title), FadeOut(grid_def), FadeOut(grid), 
                  FadeOut(highlight_a), FadeOut(highlight_d), FadeOut(cross_b), FadeOut(cross_c),
                  FadeOut(equation), FadeOut(example1), FadeOut(mult_result), FadeOut(sub_2),
                  FadeOut(final_result1), FadeOut(example2), FadeOut(mult_result2), FadeOut(sub_5),
                  FadeOut(final_result2), FadeOut(example3), FadeOut(mult_result3), FadeOut(sub_5_2),
                  FadeOut(final_result3), FadeOut(full_mult), FadeOut(cross_full), FadeOut(correct_method),
                  FadeOut(eq), FadeOut(rearranged), FadeOut(grid1), FadeOut(grid2), FadeOut(vell1), FadeOut(vell2))
