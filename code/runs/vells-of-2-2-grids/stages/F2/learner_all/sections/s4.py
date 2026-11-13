from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Rule: Swapping b and c", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid 1: [[5, 2], [3, 1]]
        grid1 = Matrix([[5, 2], [3, 1]], bracket_h_buff=0.4, bracket_v_buff=0.4)
        grid1.to_corner(UL)
        self.play(Write(grid1))
        self.wait(0.5)

        # Highlight 5 and 1
        highlight_5 = SurroundingRectangle(grid1.get_entries()[0], color=YELLOW, buff=0.1)
        highlight_1 = SurroundingRectangle(grid1.get_entries()[3], color=YELLOW, buff=0.1)
        self.play(Create(highlight_5), Create(highlight_1))
        self.wait(0.5)

        # Multiply 5 * 1 = 5
        mult_result = MathTex("5 \\times 1 = 5", font_size=24).next_to(grid1, DOWN)
        self.play(Write(mult_result))
        self.wait(0.5)

        # Subtract 2 from 5 to get 3
        sub_2 = MathTex("5 - 2 = 3", font_size=24).next_to(mult_result, DOWN)
        self.play(Write(sub_2))
        self.wait(0.5)

        # Subtract 3 from 3 to get 0
        sub_3 = MathTex("3 - 3 = 0", font_size=24).next_to(sub_2, DOWN)
        self.play(Write(sub_3))
        self.wait(0.5)

        # Final result: 0
        final_result = MathTex("\\text{Vell} = 0", font_size=30).next_to(sub_3, DOWN)
        self.play(Write(final_result))
        self.wait(1)

        # Grid 2: [[10, 5], [2, 3]]
        grid2 = Matrix([[10, 5], [2, 3]], bracket_h_buff=0.4, bracket_v_buff=0.4)
        grid2.to_corner(UR)
        self.play(Write(grid2))
        self.wait(0.5)

        # Pulse 10 and 3
        pulse_10 = grid2.get_entries()[0].animate.scale(1.2).set_color(YELLOW)
        pulse_3 = grid2.get_entries()[3].animate.scale(1.2).set_color(YELLOW)
        self.play(pulse_10, pulse_3)
        self.wait(0.5)

        # Multiply 10 * 3 = 30
        mult_result2 = MathTex("10 \\times 3 = 30", font_size=24).next_to(grid2, DOWN)
        self.play(Write(mult_result2))
        self.wait(0.5)

        # Subtract 5 from 30 to get 25
        sub_5 = MathTex("30 - 5 = 25", font_size=24).next_to(mult_result2, DOWN)
        self.play(Write(sub_5))
        self.wait(0.5)

        # Subtract 2 from 25 to get 23
        sub_2_2 = MathTex("25 - 2 = 23", font_size=24).next_to(sub_5, DOWN)
        self.play(Write(sub_2_2))
        self.wait(0.5)

        # Final result: 23
        final_result2 = MathTex("\\text{Vell} = 23", font_size=30).next_to(sub_2_2, DOWN)
        self.play(Write(final_result2))
        self.wait(1)

        # Grid 3: [[0, 5], [5, 0]]
        grid3 = Matrix([[0, 5], [5, 0]], bracket_h_buff=0.4, bracket_v_buff=0.4)
        grid3.to_corner(DL)
        self.play(Write(grid3))
        self.wait(0.5)

        # Pulse 0 and 0
        pulse_0 = grid3.get_entries()[0].animate.scale(1.2).set_color(YELLOW)
        pulse_0_2 = grid3.get_entries()[3].animate.scale(1.2).set_color(YELLOW)
        self.play(pulse_0, pulse_0_2)
        self.wait(0.5)

        # Multiply 0 * 0 = 0
        mult_result3 = MathTex("0 \\times 0 = 0", font_size=24).next_to(grid3, DOWN)
        self.play(Write(mult_result3))
        self.wait(0.5)

        # Subtract 5 from 0 to get -5
        sub_5_neg = MathTex("0 - 5 = -5", font_size=24).next_to(mult_result3, DOWN)
        self.play(Write(sub_5_neg))
        self.wait(0.5)

        # Subtract 5 from -5 to get -10
        sub_5_neg2 = MathTex("-5 - 5 = -10", font_size=24).next_to(sub_5_neg, DOWN)
        self.play(Write(sub_5_neg2))
        self.wait(0.5)

        # Final result: -10
        final_result3 = MathTex("\\text{Vell} = -10", font_size=30).next_to(sub_5_neg2, DOWN)
        self.play(Write(final_result3))
        self.wait(1)

        # Show subtraction of zero
        zero_text = Text("Subtracting zero leaves number unchanged", font_size=24).to_edge(DOWN)
        self.play(Write(zero_text))
        self.wait(1)
        self.play(FadeOut(zero_text))

        # Formula: a*d - b - c
        formula = MathTex("a \\times d - b - c", font_size=30).next_to(title, DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(1)

        # Show that swapping b and c doesn't change result
        grid_a = Matrix([["a", "b"], ["c", "d"]], bracket_h_buff=0.4, bracket_v_buff=0.4).to_corner(UL)
        grid_b = Matrix([["a", "c"], ["b", "d"]], bracket_h_buff=0.4, bracket_v_buff=0.4).to_corner(UR)

        self.play(Transform(grid1, grid_a))
        self.wait(0.5)

        # Show subtraction order
        sub_order = Text("Subtract b then c", font_size=24).next_to(grid_a, DOWN)
        self.play(Write(sub_order))
        self.wait(0.5)

        self.play(Transform(grid1, grid_b))
        self.wait(0.5)

        sub_order2 = Text("Subtract c then b", font_size=24).next_to(grid_b, DOWN)
        self.play(Write(sub_order2))
        self.wait(0.5)

        # Show equality
        equal = MathTex("a \\times d - b - c = a \\times d - c - b", font_size=24).next_to(sub_order2, DOWN)
        self.play(Write(equal))
        self.wait(1)

        # Show that both equal zero
        final_eq = MathTex("a \\times d = b + c", font_size=24).next_to(equal, DOWN)
        self.play(Write(final_eq))
        self.wait(1)

        # Show comparison with full multiplication
        wrong_formula = MathTex("a \\times b \\times c \\times d", font_size=24).set_color(RED).to_edge(DOWN)
        self.play(Write(wrong_formula))
        self.wait(0.5)

        correct_formula = MathTex("a \\times d - b - c", font_size=24).next_to(wrong_formula, UP)
        self.play(Write(correct_formula))
        self.wait(1)

        # Show checkmark
        check = Tex("\\checkmark").scale(2).set_color(GREEN).to_edge(DOWN)
        self.play(Write(check))
        self.wait(1)

        self.play(FadeOut(title, grid1, grid2, grid3, mult_result, sub_2, sub_3, final_result,
                          mult_result2, sub_5, sub_2_2, final_result2, mult_result3, sub_5_neg,
                          sub_5_neg2, final_result3, formula, sub_order, sub_order2, equal,
                          final_eq, wrong_formula, correct_formula, check))
