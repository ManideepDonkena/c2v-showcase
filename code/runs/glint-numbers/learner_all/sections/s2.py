from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Zero Exclusion Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 50, digit '0' turns red and shakes, X stamp
        num_50 = MathTex("50", font_size=40)
        num_50.move_to(ORIGIN)
        self.play(Write(num_50))
        self.wait(0.5)

        if len(num_50) > 1:
            zero = num_50[1]
            self.play(
                zero.animate.set_color(RED),
                zero.animate.shift(LEFT * 0.2).shift(RIGHT * 0.2).shift(LEFT * 0.2).shift(RIGHT * 0.2),
                run_time=0.8
            )
        self.wait(0.5)

        x_mark = Cross(stroke_width=12, scale_factor=2)
        x_mark.move_to(ORIGIN)
        self.play(FadeIn(x_mark))
        self.wait(0.5)

        rule_text = Text("Rule: Ending in 0 is NEVER Glint", font_size=24).next_to(x_mark, DOWN)
        self.play(Write(rule_text))
        self.wait(1.5)

        # Show 45 with '5' pulsing gold, equation and checkmark
        self.play(FadeOut(x_mark), FadeOut(rule_text))
        num_45 = MathTex("45", font_size=40)
        num_45.move_to(ORIGIN)
        num_45.shift(0.0 * RIGHT + 0.44 * UP)  # layout: separation vector
        self.play(Write(num_45))
        self.wait(0.5)

        if len(num_45) > 1:
            five = num_45[1]
            self.play(
                five.animate.set_color(GOLD),
                five.animate.scale(1.2).scale(1/1.2),
                run_time=1
            )
        self.wait(0.5)

        eq_45_div_5 = MathTex("45 \\div 5 = 9", font_size=30)
        eq_45_div_5.next_to(num_45, DOWN)
        eq_45_div_5.shift(0.0 * RIGHT + -0.34 * UP)  # layout: separation vector
        self.play(Write(eq_45_div_5))
        self.wait(0.5)

        checkmark = Tex(r"$\checkmark$", font_size=40, color=GREEN)
        checkmark.next_to(eq_45_div_5, RIGHT)
        self.play(FadeIn(checkmark))
        self.wait(1.5)

        # Show 30 with '0' red and shaking, X stamp
        self.play(FadeOut(num_45), FadeOut(eq_45_div_5), FadeOut(checkmark))
        num_30 = MathTex("30", font_size=40)
        num_30.move_to(ORIGIN)
        num_30.shift(0.0 * RIGHT + 0.44 * UP)  # layout: separation vector
        self.play(Write(num_30))
        self.wait(0.5)

        if len(num_30) > 1:
            zero_30 = num_30[1]
            self.play(
                zero_30.animate.set_color(RED),
                zero_30.animate.shift(LEFT * 0.2).shift(RIGHT * 0.2).shift(LEFT * 0.2).shift(RIGHT * 0.2),
                run_time=0.8
            )
        self.wait(0.5)

        x_mark_30 = Cross(stroke_width=12, scale_factor=2)
        x_mark_30.move_to(ORIGIN)
        self.play(FadeIn(x_mark_30))
        self.wait(0.5)

        text_30 = Text("Ending in 0 means it is NEVER a Glint number", font_size=24).next_to(x_mark_30, DOWN)
        self.play(Write(text_30))
        self.wait(1.5)

        # Show 10 with '0' red and shaking, text "Division by Zero is Impossible"
        self.play(FadeOut(x_mark_30), FadeOut(text_30))
        num_10 = MathTex("10", font_size=40)
        num_10.move_to(ORIGIN)
        self.play(Write(num_10))
        self.wait(0.5)

        if len(num_10) > 1:
            zero_10 = num_10[1]
            self.play(
                zero_10.animate.set_color(RED),
                zero_10.animate.shift(LEFT * 0.2).shift(RIGHT * 0.2).shift(LEFT * 0.2).shift(RIGHT * 0.2),
                run_time=0.8
            )
        self.wait(0.5)

        text_10 = Text("Division by Zero is Impossible", font_size=24).next_to(num_10, DOWN)
        self.play(Write(text_10))
        self.wait(1.5)

        # Show 31 with '1' pulsing green, checkmark
        self.play(FadeOut(num_10), FadeOut(text_10))
        num_31 = MathTex("31", font_size=40)
        num_31.move_to(ORIGIN)
        self.play(Write(num_31))
        self.wait(0.5)

        if len(num_31) > 1:
            one_31 = num_31[1]
            self.play(
                one_31.animate.set_color(GREEN),
                one_31.animate.scale(1.2).scale(1/1.2),
                run_time=1
            )
        self.wait(0.5)

        text_31 = Text("Ends in 1 = Always Glint", font_size=24).next_to(num_31, DOWN)
        self.play(Write(text_31))
        self.wait(1.5)

        # Show 27 with '7' pulsing green, equation and red X
        self.play(FadeOut(num_31), FadeOut(text_31))
        num_27 = MathTex("27", font_size=40)
        num_27.move_to(ORIGIN)
        self.play(Write(num_27))
        self.wait(0.5)

        if len(num_27) > 1:
            seven = num_27[1]
            self.play(
                seven.animate.set_color(GREEN),
                seven.animate.scale(1.2).scale(1/1.2),
                run_time=1
            )
        self.wait(0.5)

        eq_27_div_7 = MathTex("27 \\div 7 = 3.85...", font_size=30)
        eq_27_div_7.next_to(num_27, DOWN)
        self.play(Write(eq_27_div_7))
        self.wait(0.5)

        x_mark_27 = Cross(stroke_width=12, scale_factor=2)
        x_mark_27.next_to(eq_27_div_7, RIGHT)
        self.play(FadeIn(x_mark_27))
        self.wait(0.5)

        text_27 = Text("Ends in 7 is NOT always Glint", font_size=24).next_to(x_mark_27, RIGHT)
        self.play(Write(text_27))
        self.wait(1.5)

        # Show 22 with '2' pulsing, equation and checkmark
        self.play(FadeOut(num_27), FadeOut(eq_27_div_7), FadeOut(x_mark_27), FadeOut(text_27))
        num_22 = MathTex("22", font_size=40)
        num_22.move_to(ORIGIN)
        self.play(Write(num_22))
        self.wait(0.5)

        if len(num_22) > 1:
            two = num_22[1]
            self.play(
                two.animate.set_color(GREEN),
                two.animate.scale(1.2).scale(1/1.2),
                run_time=1
            )
        self.wait(0.5)

        eq_22_div_2 = MathTex("22 \\div 2 = 11", font_size=30)
        eq_22_div_2.next_to(num_22, DOWN)
        self.play(Write(eq_22_div_2))
        self.wait(0.5)

        checkmark_22 = Tex(r"$\checkmark$", font_size=40, color=GREEN)
        checkmark_22.next_to(eq_22_div_2, RIGHT)
        self.play(FadeIn(checkmark_22))
        self.wait(1.5)

        # Show 21 and 24 with last digits pulsing green and checkmarks
        self.play(FadeOut(num_22), FadeOut(eq_22_div_2), FadeOut(checkmark_22))
        num_21 = MathTex("21", font_size=40)
        num_21.to_edge(LEFT)
        self.play(Write(num_21))
        self.wait(0.5)

        if len(num_21) > 1:
            one_21 = num_21[1]
            self.play(
                one_21.animate.set_color(GREEN),
                one_21.animate.scale(1.2).scale(1/1.2),
                run_time=1
            )
        self.wait(0.5)

        checkmark_21 = Tex(r"$\checkmark$", font_size=40, color=GREEN)
        checkmark_21.next_to(num_21, RIGHT)
        self.play(FadeIn(checkmark_21))
        self.wait(0.5)

        num_24 = MathTex("24", font_size=40)
        num_24.to_edge(RIGHT)
        self.play(Write(num_24))
        self.wait(0.5)

        if len(num_24) > 1:
            four = num_24[1]
            self.play(
                four.animate.set_color(GREEN),
                four.animate.scale(1.2).scale(1/1.2),
                run_time=1
            )
        self.wait(0.5)

        checkmark_24 = Tex(r"$\checkmark$", font_size=40, color=GREEN)
        checkmark_24.next_to(num_24, RIGHT)
        self.play(FadeIn(checkmark_24))
        self.wait(1.5)

        # Show 26 ÷ 6 vs 24 ÷ 4
        self.play(FadeOut(num_21), FadeOut(checkmark_21), FadeOut(num_24), FadeOut(checkmark_24))
        eq_26_div_6 = MathTex("26 \\div 6 = 4.33...", font_size=30)
        eq_26_div_6.move_to(ORIGIN)
        self.play(Write(eq_26_div_6))
        self.wait(1.5)

        eq_24_div_4 = MathTex("24 \\div 4 = 6", font_size=30)
        eq_24_div_4.next_to(eq_26_div_6, DOWN)
        self.play(Write(eq_24_div_4))
        self.wait(1.5)

        # Final cleanup
        self.play(FadeOut(eq_26_div_6), FadeOut(eq_24_div_4))
        self.wait(0.5)
