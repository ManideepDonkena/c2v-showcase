from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Condition", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First example: 52
        tens_digit_52 = Text("5", font_size=60).set_color(WHITE)
        units_digit_52 = Text("2", font_size=60).set_color(WHITE)
        tens_units_52 = VGroup(tens_digit_52, units_digit_52).arrange(RIGHT, buff=0.3)
        self.play(Write(tens_units_52))
        self.wait(0.5)

        comparison_52 = MathTex(">", color=WHITE, font_size=40)
        comparison_52.next_to(tens_digit_52, buff=0.2)
        comparison_52.shift(0.1 * RIGHT)  # Adjusted to avoid overlap
        comparison_52.shift(-0.4 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(comparison_52))
        self.wait(0.5)

        comparison_52.generate_target()
        comparison_52.target.set_color(GREEN)
        self.play(MoveToTarget(comparison_52))
        self.wait(0.5)

        number_52 = Text("52", font_size=60).set_color(YELLOW)
        number_52.next_to(tens_units_52, DOWN, buff=0.5)
        self.play(Write(number_52))
        self.wait(0.5)

        pulse = number_52.copy().set_color(GOLD).animate.scale(1.1)
        self.play(pulse)
        self.play(pulse.scale(1/1.1))
        self.wait(0.5)
        condition_text_52 = Text("Tens > Units", font_size=30).next_to(number_52, DOWN)
        self.play(Write(condition_text_52))
        self.wait(1)

        # Second example: 32
        self.play(FadeOut(tens_units_52), FadeOut(comparison_52), FadeOut(number_52), FadeOut(condition_text_52))
        tens_digit_32 = Text("3", font_size=60).set_color(WHITE)
        units_digit_32 = Text("2", font_size=60).set_color(WHITE)
        tens_units_32 = VGroup(tens_digit_32, units_digit_32).arrange(RIGHT, buff=0.3)
        self.play(Write(tens_units_32))
        self.wait(0.5)

        comparison_32 = MathTex(">", color=WHITE, font_size=40)
        comparison_32.next_to(tens_digit_32, buff=0.2)
        self.play(Write(comparison_32))
        self.wait(0.5)

        comparison_32.generate_target()
        comparison_32.target.set_color(GREEN)
        self.play(MoveToTarget(comparison_32))
        self.wait(0.5)

        condition_text_32 = Text("Tens > Units", font_size=30).next_to(tens_units_32, DOWN)
        self.play(Write(condition_text_32))
        self.wait(1)

        # Third example: 10
        self.play(FadeOut(tens_units_32), FadeOut(comparison_32), FadeOut(condition_text_32))
        tens_digit_10 = Text("1", font_size=60).set_color(WHITE)
        units_digit_10 = Text("0", font_size=60).set_color(WHITE)
        tens_units_10 = VGroup(tens_digit_10, units_digit_10).arrange(RIGHT, buff=0.3)
        self.play(Write(tens_units_10))
        self.wait(0.5)

        comparison_10 = MathTex(">", color=WHITE, font_size=40)
        comparison_10.next_to(tens_digit_10, buff=0.2)
        comparison_10.shift(0.1 * RIGHT)  # Adjusted to avoid overlap
        self.play(Write(comparison_10))
        self.wait(0.5)

        comparison_10.generate_target()
        comparison_10.target.set_color(GREEN)
        self.play(MoveToTarget(comparison_10))
        self.wait(0.5)

        text_10 = Text("1 > 0", font_size=30).next_to(tens_units_10, DOWN)
        self.play(Write(text_10))
        self.wait(1)

        # Show 11 is not dapple
        self.play(FadeOut(tens_units_10), FadeOut(comparison_10), FadeOut(text_10))
        tens_digit_11 = Text("1", font_size=60).set_color(WHITE)
        units_digit_11 = Text("1", font_size=60).set_color(WHITE)
        tens_units_11 = VGroup(tens_digit_11, units_digit_11).arrange(RIGHT, buff=0.3)
        self.play(Write(tens_units_11))
        self.wait(0.5)

        comparison_11 = MathTex("=", color=WHITE, font_size=40)
        comparison_11.next_to(tens_digit_11, buff=0.2)
        self.play(Write(comparison_11))
        self.wait(0.5)

        comparison_11.generate_target()
        comparison_11.target.set_color(RED)
        self.play(MoveToTarget(comparison_11))
        self.wait(0.5)

        text_11 = Text("Not Dapple", font_size=30).next_to(tens_units_11, DOWN)
        self.play(Write(text_11))
        self.wait(1)

        # Fourth example: 83
        self.play(FadeOut(tens_units_11), FadeOut(comparison_11), FadeOut(text_11))
        tens_digit_83 = Text("8", font_size=60).set_color(WHITE)
        units_digit_83 = Text("3", font_size=60).set_color(WHITE)
        tens_units_83 = VGroup(tens_digit_83, units_digit_83).arrange(RIGHT, buff=0.3)
        self.play(Write(tens_units_83))
        self.wait(0.5)

        comparison_83 = MathTex(">", color=WHITE, font_size=40)
        comparison_83.next_to(tens_digit_83, buff=0.2)
        comparison_83.shift(0.1 * RIGHT)  # Adjusted to avoid overlap
        self.play(Write(comparison_83))
        self.wait(0.5)

        comparison_83.generate_target()
        comparison_83.target.set_color(GREEN)
        self.play(MoveToTarget(comparison_83))
        self.wait(0.5)

        condition_text_83 = Text("Tens > Units", font_size=30).next_to(tens_units_83, DOWN)
        self.play(Write(condition_text_83))
        self.wait(1)

        # Fifth example: 7 (one-digit)
        self.play(FadeOut(tens_units_83), FadeOut(comparison_83), FadeOut(condition_text_83))
        digit_7 = Text("7", font_size=60).set_color(WHITE)
        self.play(Write(digit_7))
        self.wait(0.5)

        tens_digit_7 = Text("0", font_size=60).set_color(WHITE)
        units_digit_7 = Text("7", font_size=60).set_color(WHITE)
        tens_units_7 = VGroup(tens_digit_7, units_digit_7).arrange(RIGHT, buff=0.3)
        self.play(Write(tens_units_7))
        self.wait(0.5)

        comparison_7 = MathTex(">", color=WHITE, font_size=40)
        comparison_7.next_to(tens_digit_7, buff=0.2)
        comparison_7.shift(0.1 * RIGHT)  # Adjusted to avoid overlap
        self.play(Write(comparison_7))
        self.wait(0.5)

        comparison_7.generate_target()
        comparison_7.target.set_color(RED)
        self.play(MoveToTarget(comparison_7))
        self.wait(0.5)

        text_7 = Text("0 > 7 is False", font_size=30).next_to(tens_units_7, DOWN)
        self.play(Write(text_7))
        self.wait(1)

        # Sixth example: 98
        self.play(FadeOut(digit_7), FadeOut(tens_units_7), FadeOut(comparison_7), FadeOut(text_7))
        tens_digit_98 = Text("9", font_size=60).set_color(WHITE)
        units_digit_98 = Text("8", font_size=60).set_color(WHITE)
        tens_units_98 = VGroup(tens_digit_98, units_digit_98).arrange(RIGHT, buff=0.3)
        self.play(Write(tens_units_98))
        self.wait(0.5)

        comparison_98 = MathTex(">", color=WHITE, font_size=40)
        comparison_98.next_to(tens_digit_98, buff=0.2)
        comparison_98.shift(0.1 * RIGHT)  # Adjusted to avoid overlap
        self.play(Write(comparison_98))
        self.wait(0.5)

        comparison_98.generate_target()
        comparison_98.target.set_color(GREEN)
        self.play(MoveToTarget(comparison_98))
        self.wait(0.5)

        condition_text_98 = Text("Tens > Units", font_size=30).next_to(tens_units_98, DOWN)
        self.play(Write(condition_text_98))
        self.wait(1)

        # Seventh example: 50
        self.play(FadeOut(tens_units_98), FadeOut(comparison_98), FadeOut(condition_text_98))
        tens_digit_50 = Text("5", font_size=60).set_color(WHITE)
        units_digit_50 = Text("0", font_size=60).set_color(WHITE)
        tens_units_50 = VGroup(tens_digit_50, units_digit_50).arrange(RIGHT, buff=0.3)
        self.play(Write(tens_units_50))
        self.wait(0.5)

        comparison_50 = MathTex(">", color=WHITE, font_size=40)
        comparison_50.next_to(tens_digit_50, buff=0.2)
        comparison_50.shift(0.1 * RIGHT)  # Adjusted to avoid overlap
        self.play(Write(comparison_50))
        self.wait(0.5)

        comparison_50.generate_target()
        comparison_50.target.set_color(GREEN)
        self.play(MoveToTarget(comparison_50))
        self.wait(0.5)

        text_50 = Text("5 > 0", font_size=30).next_to(tens_units_50, DOWN)
        self.play(Write(text_50))
        self.wait(1)

        # Final cleanup
        self.play(FadeOut(tens_units_50), FadeOut(comparison_50), FadeOut(text_50), FadeOut(title))
        self.wait(0.5)
