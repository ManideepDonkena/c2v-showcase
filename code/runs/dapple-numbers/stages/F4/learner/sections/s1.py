from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Condition", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Digits 5 and 2
        tens_digit = Integer(5, font_size=80).shift(LEFT * 1.5)
        units_digit = Integer(2, font_size=80).shift(RIGHT * 1.5)
        self.play(Write(tens_digit), Write(units_digit))
        self.wait(0.5)

        # Greater than sign
        greater_than = MathTex(">", font_size=60).shift(DOWN * 0.2)
        self.play(Write(greater_than))
        self.wait(0.5)

        # Green checkmark around 52
        number_group = VGroup(tens_digit, units_digit)
        checkmark = VMobject().set_points_as_corners([ORIGIN, UP, RIGHT]).scale(0.5).set_color(GREEN).move_to(number_group.get_center())
        self.play(
            ApplyMethod(greater_than.set_color, GREEN),
            Create(checkmark),
            number_group.animate.set_fill(YELLOW, opacity=0.3).set_stroke(YELLOW, width=5)
        )
        self.wait(1)

        # Number 52 with golden glow
        number_text = MathTex("52", font_size=80).move_to(number_group.get_center())
        pulse = number_text.copy().set_fill(YELLOW, opacity=0.7).set_stroke(YELLOW, width=5)
        number_text.shift(0.0 * RIGHT + 0.72 * UP)  # layout: separation vector
        self.play(
            FadeOut(greater_than),
            ReplacementTransform(number_group, number_text),
            Create(pulse),
            run_time=0.5
        )
        self.wait(0.5)

        # "Tens > Units" text
        condition = Text("Tens > Units", font_size=32).next_to(number_text, DOWN)
        self.play(Write(condition))
        self.wait(1.5)

        # Fade out first example
        self.play(FadeOut(title), FadeOut(number_text), FadeOut(pulse), FadeOut(condition))

        # Second example: 61
        tens_digit_2 = Integer(6, font_size=80).shift(LEFT * 1.5)
        units_digit_2 = Integer(1, font_size=80).shift(RIGHT * 1.5)
        self.play(Write(tens_digit_2), Write(units_digit_2))
        self.wait(0.5)

        greater_than_2 = MathTex(">", font_size=60).shift(DOWN * 0.2)
        self.play(Write(greater_than_2))
        self.wait(0.5)

        # Use Checkmark from manim
        checkmark_2 = always_redraw(lambda: VMobject().set_points_as_corners([ORIGIN, UP, RIGHT]).scale(0.5).set_color(GREEN).move_to(VGroup(tens_digit_2, units_digit_2).get_center()))
        self.play(
            ApplyMethod(greater_than_2.set_color, GREEN),
            Create(checkmark_2)
        )
        self.wait(1)
        # Fade out second example
        self.play(FadeOut(tens_digit_2), FadeOut(units_digit_2), FadeOut(greater_than_2), FadeOut(checkmark_2))

        # Third example: 16 (not dapple)
        tens_digit_3 = Integer(1, font_size=80).shift(LEFT * 1.5)
        units_digit_3 = Integer(6, font_size=80).shift(RIGHT * 1.5)
        self.play(Write(tens_digit_3), Write(units_digit_3))
        self.wait(0.5)

        less_than = MathTex("<", font_size=60).shift(DOWN * 0.2)
        self.play(Write(less_than))
        self.wait(0.5)

        cross = Cross().scale(0.5).set_color(RED).move_to(VGroup(tens_digit_3, units_digit_3).get_center())
        self.play(
            ApplyMethod(less_than.set_color, RED),
            Create(cross)
        )
        self.wait(1.5)

        # Fade everything
        self.play(FadeOut(tens_digit_3), FadeOut(units_digit_3), FadeOut(less_than), FadeOut(cross))
