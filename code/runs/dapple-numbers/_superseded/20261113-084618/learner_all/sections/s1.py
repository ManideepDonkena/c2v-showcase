from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Condition", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Example: 52 is dapple
        tens_digit_5 = Tex("5", font_size=60).shift(LEFT * 1.5)
        units_digit_2 = Tex("2", font_size=60).shift(RIGHT * 1.5)
        comparison_op = always_redraw(lambda: Tex(">", font_size=40).move_to((tens_digit_5.get_center() + units_digit_2.get_center()) / 2))
        number_52 = VGroup(tens_digit_5, units_digit_2, comparison_op)
        self.play(Write(number_52))
        self.wait(0.5)
        self.play(Indicate(comparison_op, color=GREEN))
        self.wait(0.5)
        golden_pulse = always_redraw(lambda: number_52.copy().set_color(YELLOW).set_opacity(0.7))
        self.add(golden_pulse)
        self.wait(1)
        self.remove(golden_pulse)

        # Text below
        text_52 = Tex("Tens > Units", font_size=30).next_to(number_52, DOWN)
        self.play(Write(text_52))
        self.wait(1.5)

        # Show 77 is not dapple
        self.play(FadeOut(text_52))
        tens_digit_7 = Tex("7", font_size=60).shift(LEFT * 1.5)
        units_digit_7 = Tex("7", font_size=60).shift(RIGHT * 1.5)
        equal_op = always_redraw(lambda: Tex("=", font_size=40).move_to((tens_digit_7.get_center() + units_digit_7.get_center()) / 2))
        number_77 = VGroup(tens_digit_7, units_digit_7, equal_op)
        tens_digit_7.shift(0.41 * RIGHT + 0.0 * UP)  # layout: separation vector
        units_digit_7.shift(0.41 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(number_77))
        self.wait(0.5)
        self.play(Indicate(equal_op, color=RED))
        self.wait(0.5)
        self.play(number_77.animate.set_color(RED))
        not_dapple_text = Tex("Not Dapple (Tens = Units)", font_size=24).next_to(number_77, DOWN)
        self.play(Write(not_dapple_text))
        self.wait(1.5)

        # Show 44 is not dapple
        self.play(FadeOut(number_77, not_dapple_text))
        tens_digit_4 = Tex("4", font_size=60).shift(LEFT * 1.5)
        units_digit_4 = Tex("4", font_size=60).shift(RIGHT * 1.5)
        equal_op_2 = always_redraw(lambda: Tex("=", font_size=40).move_to((tens_digit_4.get_center() + units_digit_4.get_center()) / 2))
        number_44 = VGroup(tens_digit_4, units_digit_4, equal_op_2)
        tens_digit_4.shift(0.41 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(number_44))
        self.wait(0.5)
        self.play(Indicate(equal_op_2, color=RED))
        self.wait(0.5)
        self.play(number_44.animate.set_color(RED))
        not_dapple_text_2 = Tex("Not Dapple (Tens = Units)", font_size=24).next_to(number_44, DOWN)
        self.play(Write(not_dapple_text_2))
        self.wait(1.5)

        # Show 10 is dapple
        self.play(FadeOut(number_44, not_dapple_text_2))
        tens_digit_1 = Tex("1", font_size=60).shift(LEFT * 1.5)
        units_digit_0 = Tex("0", font_size=60).shift(RIGHT * 1.5)
        comparison_op_10 = always_redraw(lambda: Tex(">", font_size=40).move_to((tens_digit_1.get_center() + units_digit_0.get_center()) / 2))
        number_10 = VGroup(tens_digit_1, units_digit_0, comparison_op_10)
        self.play(Write(number_10))
        self.wait(0.5)
        self.play(Indicate(comparison_op_10, color=GREEN))
        self.wait(0.5)
        text_10 = Tex("1 > 0", font_size=24).next_to(number_10, DOWN)
        self.play(Write(text_10))
        self.wait(1.5)

        # Show 11 is not dapple
        self.play(FadeOut(number_10, text_10))
        tens_digit_1_1 = Tex("1", font_size=60).shift(LEFT * 1.5)
        units_digit_1_1 = Tex("1", font_size=60).shift(RIGHT * 1.5)
        equal_op_3 = always_redraw(lambda: Tex("=", font_size=40).move_to((tens_digit_1_1.get_center() + units_digit_1_1.get_center()) / 2))
        number_11 = VGroup(tens_digit_1_1, units_digit_1_1, equal_op_3)
        self.play(Write(number_11))
        self.wait(0.5)
        self.play(Indicate(equal_op_3, color=RED))
        self.wait(0.5)
        self.play(number_11.animate.set_color(RED))
        not_dapple_text_3 = Tex("Not Dapple", font_size=24).next_to(number_11, DOWN)
        self.play(Write(not_dapple_text_3))
        self.wait(1.5)

        # Show 7 is not dapple (one-digit number)
        self.play(FadeOut(number_11, not_dapple_text_3))
        single_digit = Tex("7", font_size=60).shift(LEFT * 0.5)
        tens_digit_0 = Tex("0", font_size=60).shift(LEFT * 1.5)
        units_digit_7 = Tex("7", font_size=60).shift(RIGHT * 1.5)
        comparison_op_07 = always_redraw(lambda: Tex(">", font_size=40).move_to((tens_digit_0.get_center() + units_digit_7.get_center()) / 2))
        number_07 = VGroup(tens_digit_0, units_digit_7, comparison_op_07)
        self.play(Write(single_digit))
        self.wait(0.5)
        self.play(Write(number_07))
        self.wait(0.5)
        self.play(Indicate(comparison_op_07, color=RED))
        self.wait(0.5)
        not_dapple_text_4 = Tex("Not Dapple (0 > 7 is false)", font_size=24).next_to(number_07, DOWN)
        self.play(Write(not_dapple_text_4))
        self.wait(1.5)

        # Show 98 is dapple
        self.play(FadeOut(single_digit, number_07, not_dapple_text_4))
        tens_digit_9 = Tex("9", font_size=60).shift(LEFT * 1.5)
        units_digit_8 = Tex("8", font_size=60).shift(RIGHT * 1.5)
        comparison_op_98 = always_redraw(lambda: Tex(">", font_size=40).move_to((tens_digit_9.get_center() + units_digit_8.get_center()) / 2))
        number_98 = VGroup(tens_digit_9, units_digit_8, comparison_op_98)
        self.play(Write(number_98))
        self.wait(0.5)
        self.play(Indicate(comparison_op_98, color=GREEN))
        self.wait(0.5)
        text_98 = Tex("Tens > Units", font_size=30).next_to(number_98, DOWN)
        self.play(Write(text_98))
        self.wait(1.5)

        # Show 0 is not dapple
        self.play(FadeOut(number_98, text_98))
        zero_digit = Tex("0", font_size=60).shift(LEFT * 0.5)
        self.play(Write(zero_digit))
        self.wait(0.5)
        not_dapple_zero = Tex("Not Dapple (no tens digit)", font_size=24).next_to(zero_digit, DOWN)
        self.play(Write(not_dapple_zero))
        self.wait(1.5)

        # End
        self.play(FadeOut(title, zero_digit, not_dapple_zero))
        self.wait(0.5)
