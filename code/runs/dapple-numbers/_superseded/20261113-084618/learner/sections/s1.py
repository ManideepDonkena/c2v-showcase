from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Condition", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 52 example
        tens_digit_5 = Text("5", font_size=64).set_color(WHITE)
        units_digit_2 = Text("2", font_size=64).set_color(WHITE)
        digits_52 = VGroup(tens_digit_5, units_digit_2).arrange(RIGHT, buff=0.3)
        self.play(Write(digits_52))
        self.wait(0.5)

        comparison_op = MathTex(">", color=WHITE, font_size=40)
        comparison_op.move_to(interpolate(tens_digit_5.get_center(), units_digit_2.get_center(), 0.5))
        self.play(Write(comparison_op))
        self.wait(0.5)

        # Make comparison green
        self.play(comparison_op.animate.set_color(GREEN))
        self.wait(0.5)

        # Pulse number 52 with golden glow
        pulse = Circle(radius=1.2, color=YELLOW, fill_opacity=0.3).move_to(digits_52)
        self.play(Create(pulse), run_time=0.5)
        self.play(FadeOut(pulse))
        self.wait(0.5)

        # Show "Tens > Units"
        tens_units = Text("Tens > Units", font_size=32).next_to(digits_52, DOWN)
        self.play(Write(tens_units))
        self.wait(1.0)

        # Fade out 52 and comparison
        self.play(FadeOut(digits_52), FadeOut(comparison_op), FadeOut(tens_units))

        # Show 10 example
        tens_digit_1 = Text("1", font_size=64).set_color(WHITE)
        units_digit_0 = Text("0", font_size=64).set_color(WHITE)
        digits_10 = VGroup(tens_digit_1, units_digit_0).arrange(RIGHT, buff=0.3)
        self.play(Write(digits_10))
        self.wait(0.5)

        # Highlight tens and units
        tens_digit_1_copy = tens_digit_1.copy().set_color(BLUE)
        units_digit_0_copy = units_digit_0.copy().set_color(RED)
        self.play(Transform(tens_digit_1, tens_digit_1_copy), Transform(units_digit_0, units_digit_0_copy))
        self.wait(0.5)

        # Show comparison 1 > 0
        comparison_10 = MathTex("1 > 0", color=GREEN, font_size=40)
        comparison_10.next_to(digits_10, DOWN)
        self.play(Write(comparison_10))
        self.wait(1.0)

        # Show 11 is not dapple
        self.play(FadeOut(digits_10), FadeOut(comparison_10))
        tens_digit_1 = Text("1", font_size=64).set_color(WHITE)
        units_digit_1 = Text("1", font_size=64).set_color(WHITE)
        digits_11 = VGroup(tens_digit_1, units_digit_1).arrange(RIGHT, buff=0.3)
        self.play(Write(digits_11))
        self.wait(0.5)

        comparison_11 = MathTex("1 = 1", color=RED, font_size=40)
        comparison_11.next_to(digits_11, DOWN)
        self.play(Write(comparison_11))
        self.wait(1.0)

        # Fade out 11
        self.play(FadeOut(digits_11), FadeOut(comparison_11))

        # Show one-digit number 7
        digit_7 = Text("7", font_size=64).set_color(WHITE)
        self.play(Write(digit_7))
        self.wait(0.5)

        # Show tens=0, units=7
        tens_digit_0 = Text("0", font_size=64).set_color(BLUE)
        units_digit_7 = Text("7", font_size=64).set_color(RED)
        digits_07 = VGroup(tens_digit_0, units_digit_7).arrange(RIGHT, buff=0.3)
        self.play(Transform(digit_7, digits_07))
        self.wait(0.5)

        comparison_07 = MathTex("0 > 7", color=RED, font_size=40)
        comparison_07.next_to(digits_07, DOWN)
        self.play(Write(comparison_07))
        self.wait(1.0)

        # Fade out 7
        self.play(FadeOut(digit_7), FadeOut(comparison_07))

        # Show 98 example
        tens_digit_9 = Text("9", font_size=64).set_color(WHITE)
        units_digit_8 = Text("8", font_size=64).set_color(WHITE)
        digits_98 = VGroup(tens_digit_9, units_digit_8).arrange(RIGHT, buff=0.3)
        self.play(Write(digits_98))
        self.wait(0.5)

        # Highlight tens and units
        tens_digit_9_copy = tens_digit_9.copy().set_color(BLUE)
        units_digit_8_copy = units_digit_8.copy().set_color(RED)
        self.play(Transform(tens_digit_9, tens_digit_9_copy), Transform(units_digit_8, units_digit_8_copy))
        self.wait(0.5)

        # Show comparison 9 > 8
        comparison_98 = MathTex("9 > 8", color=GREEN, font_size=40)
        comparison_98.next_to(digits_98, DOWN)
        self.play(Write(comparison_98))
        self.wait(1.0)

        # Show "Tens > Units"
        tens_units_2 = Text("Tens > Units", font_size=32).next_to(comparison_98, DOWN)
        self.play(Write(tens_units_2))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(digits_98), FadeOut(comparison_98), FadeOut(tens_units_2), FadeOut(title))
