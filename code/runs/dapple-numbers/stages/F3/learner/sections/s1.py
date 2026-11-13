from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Condition", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 52 with comparison
        tens_digit_5 = Text("5", font_size=80).set_color(WHITE)
        units_digit_2 = Text("2", font_size=80).set_color(WHITE)
        comparison = MathTex(">", font_size=60).set_color(GREEN)

        tens_digit_5.next_to(ORIGIN, LEFT, buff=0.5)
        units_digit_2.next_to(ORIGIN, RIGHT, buff=0.5)
        comparison.move_to(ORIGIN)

        self.play(Write(tens_digit_5), Write(units_digit_2))
        self.wait(0.5)
        self.play(Write(comparison))
        self.wait(0.5)

        # Glow around 52
        number_group = VGroup(tens_digit_5, units_digit_2)
        glow = number_group.copy().set_color(YELLOW).set_opacity(0.8)
        glow.shift(0.63 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(glow), run_time=0.5)
        self.play(FadeOut(glow))
        # Show "Tens > Units"
        condition_text = Text("Tens > Units", font_size=32).next_to(number_group, DOWN, buff=0.5)
        self.play(Write(condition_text))
        self.wait(1)

        # Narration: example 32
        self.play(FadeOut(comparison), FadeOut(condition_text))

        tens_digit_3 = Text("3", font_size=80).set_color(WHITE)
        units_digit_2_again = Text("2", font_size=80).set_color(WHITE)
        comparison_32 = MathTex(">", font_size=60).set_color(GREEN)

        tens_digit_3.next_to(ORIGIN, LEFT, buff=0.5)
        units_digit_2_again.next_to(ORIGIN, RIGHT, buff=0.5)
        comparison_32.move_to(ORIGIN)

        self.play(Write(tens_digit_3), Write(units_digit_2_again))
        self.wait(0.5)
        self.play(Write(comparison_32))
        self.wait(1)

        # Confirm it's dapple with golden glow or checkmark
        number_group_32 = VGroup(tens_digit_3, units_digit_2_again)
        checkmark = Tex(r"$\checkmark$", font_size=60).set_color(YELLOW)  # Changed GOLDEN to YELLOW
        checkmark.next_to(number_group_32, DOWN, buff=0.5)

        self.play(Write(checkmark))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(number_group_32), FadeOut(comparison_32), FadeOut(checkmark))
        self.wait(0.5)
