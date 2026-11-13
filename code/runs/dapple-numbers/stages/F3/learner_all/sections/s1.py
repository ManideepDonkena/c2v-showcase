from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Condition", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 5 and 2 side by side
        tens_digit = Integer(5, font_size=80).set_color(WHITE)
        units_digit = Integer(2, font_size=80).set_color(WHITE)
        tens_digit.next_to(ORIGIN, LEFT, buff=0.5)
        units_digit.next_to(ORIGIN, RIGHT, buff=0.5)
        self.play(Write(tens_digit), Write(units_digit))
        self.wait(0.5)

        # Show comparison operator
        compare = MathTex(">", font_size=60).set_color(WHITE)
        compare.move_to(tens_digit.get_center() + units_digit.get_center() / 2)
        self.play(Write(compare))
        self.wait(0.5)

        # Make comparison green
        self.play(compare.animate.set_color(GREEN))
        self.wait(0.5)

        # Show number 52 with golden glow
        number = MathTex("52", font_size=100)
        number.next_to(compare, DOWN, buff=1)
        self.play(Write(number))
        self.wait(0.5)

        # Golden pulse effect
        pulse = number.copy().set_color(YELLOW).set_opacity(0.3)
        number.shift(0.0 * RIGHT + 0.86 * UP)  # layout: separation vector
        self.play(
            FadeIn(pulse),
            run_time=0.5
        )
        self.play(
            FadeOut(pulse),
            run_time=0.5
        )
        self.wait(0.5)

        # Show "Tens > Units"
        condition = Text("Tens > Units", font_size=32).next_to(number, DOWN, buff=0.5)
        self.play(Write(condition))
        self.wait(1)

        # Narration: example 32
        self.play(FadeOut(compare), FadeOut(pulse), FadeOut(condition))

        tens_digit_2 = Integer(3, font_size=80).set_color(WHITE)
        units_digit_2 = Integer(2, font_size=80).set_color(WHITE)
        tens_digit_2.next_to(ORIGIN, LEFT, buff=0.5)
        units_digit_2.next_to(ORIGIN, RIGHT, buff=0.5)
        tens_digit_2.shift(-0.48 * RIGHT + 0.0 * UP)  # layout: separation vector
        units_digit_2.shift(0.48 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(tens_digit_2), Write(units_digit_2))
        self.wait(0.5)

        compare_2 = MathTex(">", font_size=60).set_color(WHITE)
        compare_2.move_to(tens_digit_2.get_center() + units_digit_2.get_center() / 2)
        self.play(Write(compare_2))
        self.wait(0.5)

        # Make comparison green
        self.play(compare_2.animate.set_color(GREEN))
        self.wait(0.5)

        number_2 = MathTex("32", font_size=100)
        number_2.next_to(compare_2, DOWN, buff=1)
        self.play(Write(number_2))
        self.wait(0.5)

        # Highlight digits
        tens_digit_2_copy = tens_digit_2.copy().set_color(GOLD)
        units_digit_2_copy = units_digit_2.copy().set_color(GOLD)
        self.play(
            tens_digit_2.animate.set_color(GOLD),
            units_digit_2.animate.set_color(GOLD)
        )
        self.wait(0.5)

        # Golden glow around 32
        pulse_2 = number_2.copy().set_color(YELLOW).set_opacity(0.3)
        self.play(
            FadeIn(pulse_2),
            run_time=0.5
        )
        self.play(
            FadeOut(pulse_2),
            run_time=0.5
        )
        self.wait(0.5)
        # Show checkmark or confirmation
        check = Text("✓", font_size=80).set_color(GREEN)
        check.next_to(number_2, DOWN, buff=0.5)
        self.play(Write(check))
        self.wait(1)

        # Fade out everything
        self.play(
            FadeOut(tens_digit),
            FadeOut(units_digit),
            FadeOut(compare),
            FadeOut(number),
            FadeOut(tens_digit_2),
            FadeOut(units_digit_2),
            FadeOut(compare_2),
            FadeOut(number_2),
            FadeOut(check),
            FadeOut(title)
        )
        self.wait(0.5)
