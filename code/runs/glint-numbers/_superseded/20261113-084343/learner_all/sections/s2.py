from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Zero Exclusion Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 50, digit '0' turns red and shakes
        num_50 = MathTex("50", font_size=40)
        num_50.move_to(ORIGIN)
        self.play(Write(num_50))
        self.wait(0.5)

        if len(num_50) > 1:
            zero_digit = num_50[1]
            self.play(
                zero_digit.animate.set_color(RED).shift(LEFT * 0.2).shift(RIGHT * 0.2).shift(LEFT * 0.2).shift(RIGHT * 0.2),
                run_time=0.6
            )
        self.wait(0.5)

        # Large red X stamp
        cross = Cross(stroke_color=RED, stroke_width=12, scale_factor=2)
        cross.move_to(ORIGIN)
        self.play(GrowFromCenter(cross))
        self.wait(0.5)

        # Rule text
        rule_text = Text("Rule: Ending in 0 is NEVER Glint", font_size=24).next_to(cross, DOWN)
        self.play(Write(rule_text))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(num_50), FadeOut(cross), FadeOut(rule_text))

        # Show 45 with '5' pulsing gold and equation
        num_45 = MathTex("45", font_size=40)
        num_45.move_to(ORIGIN)
        self.play(Write(num_45))
        self.wait(0.5)

        if len(num_45) > 1:
            five_digit = num_45[1]
            self.play(five_digit.animate.set_color(GOLD).scale(1.2).scale(1/1.2), run_time=1)
        self.wait(0.5)

        eq_45 = MathTex("45 \\div 5 = 9", font_size=30).next_to(num_45, DOWN)
        check_45 = Tex("\\checkmark", color=GREEN, font_size=36).next_to(eq_45, RIGHT)
        self.play(Write(eq_45), Write(check_45))
        self.wait(1.5)

        # Show 24 with last digit '4' highlighted and equation
        self.play(FadeOut(num_45), FadeOut(eq_45), FadeOut(check_45))
        num_24 = MathTex("24", font_size=40)
        num_24.move_to(ORIGIN)
        self.play(Write(num_24))
        self.wait(0.5)

        if len(num_24) > 1:
            four_digit = num_24[1]
            self.play(four_digit.animate.set_color(YELLOW).scale(1.2).scale(1/1.2), run_time=1)
        self.wait(0.5)

        eq_24 = MathTex("24 \\div 4 = 6", font_size=30).next_to(num_24, DOWN)
        check_24 = Tex("\\checkmark", color=GREEN, font_size=36).next_to(eq_24, RIGHT)
        self.play(Write(eq_24), Write(check_24))
        self.wait(1.5)

        # Show 22 with last digit '2' pulsing and equation
        self.play(FadeOut(num_24), FadeOut(eq_24), FadeOut(check_24))
        num_22 = MathTex("22", font_size=40)
        num_22.move_to(ORIGIN)
        self.play(Write(num_22))
        self.wait(0.5)

        if len(num_22) > 1:
            two_digit = num_22[1]
            self.play(two_digit.animate.set_color(GREEN).scale(1.2).scale(1/1.2), run_time=1)
        self.wait(0.5)

        eq_22 = MathTex("22 \\div 2 = 11", font_size=30).next_to(num_22, DOWN)
        check_22 = Tex("\\checkmark", color=GREEN, font_size=36).next_to(eq_22, RIGHT)
        self.play(Write(eq_22), Write(check_22))
        self.wait(1.5)

        # Show 21 and 24 both with last digits pulsing and checkmarks
        self.play(FadeOut(num_22), FadeOut(eq_22), FadeOut(check_22))
        num_21 = MathTex("21", font_size=40)
        num_24_again = MathTex("24", font_size=40)
        num_21.next_to(ORIGIN, LEFT)
        num_24_again.next_to(ORIGIN, RIGHT)
        self.play(Write(num_21), Write(num_24_again))
        self.wait(0.5)

        if len(num_21) > 1 and len(num_24_again) > 1:
            one_digit = num_21[1]
            four_digit_again = num_24_again[1]
            self.play(
                one_digit.animate.set_color(GREEN).scale(1.2).scale(1/1.2),
                four_digit_again.animate.set_color(GREEN).scale(1.2).scale(1/1.2),
                run_time=1
            )
        self.wait(0.5)

        check_21 = Tex("\\checkmark", color=GREEN, font_size=36).next_to(num_21, DOWN)
        check_24_again = Tex("\\checkmark", color=GREEN, font_size=36).next_to(num_24_again, DOWN)
        self.play(Write(check_21), Write(check_24_again))
        self.wait(1.5)

        # Show 10 with '0' turning red and shaking + text
        self.play(FadeOut(num_21), FadeOut(num_24_again), FadeOut(check_21), FadeOut(check_24_again))
        num_10 = MathTex("10", font_size=40)
        num_10.move_to(ORIGIN)
        self.play(Write(num_10))
        self.wait(0.5)

        if len(num_10) > 1:
            zero_digit_10 = num_10[1]
            self.play(
                zero_digit_10.animate.set_color(RED).shift(LEFT * 0.2).shift(RIGHT * 0.2).shift(LEFT * 0.2).shift(RIGHT * 0.2),
                run_time=0.6
            )
        self.wait(0.5)

        div_text = Text("Division by Zero is Impossible", font_size=24).next_to(num_10, DOWN)
        self.play(Write(div_text))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(num_10), FadeOut(div_text), FadeOut(title))
        self.wait(0.5)
