from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Glint Numbers", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 21 with '1' pulsing green and checkmark
        num_21 = MathTex("21", font_size=40)
        num_21.move_to(ORIGIN)
        last_digit_21 = num_21[-1].copy()
        last_digit_21.set_color(GREEN)
        self.play(Write(num_21))
        self.play(last_digit_21.animate.scale(1.5).set_color(GREEN).set_opacity(0.8), run_time=0.5)
        self.play(last_digit_21.animate.scale(1/1.5).set_color(WHITE).set_opacity(1), run_time=0.5)

        # Text below
        definition = Text("Glint Number: Last digit ≠ 0 AND Number ÷ Last Digit = Whole", font_size=24)
        definition.next_to(num_21, DOWN, buff=0.5)
        self.play(Write(definition))
        self.wait(0.5)

        # Checkmark
        check_21 = MathTex(r"\checkmark", font_size=40).next_to(num_21, RIGHT, buff=0.5)
        self.play(FadeIn(check_21))
        self.wait(0.5)

        # Narration text for 21
        narration_21 = Text("Every number ending in 1 is automatically a Glint number", font_size=20).to_edge(DOWN)
        # Show 45 with '5' pulsing gold and equation
        num_45 = MathTex("45", font_size=40).move_to(ORIGIN)
        last_digit_45 = num_45[-1].copy()
        last_digit_45.set_color(GOLD)
        self.play(Transform(num_21, num_45))
        self.play(last_digit_45.animate.scale(1.5).set_color(GOLD).set_opacity(0.8), run_time=0.5)
        self.play(last_digit_45.animate.scale(1/1.5).set_color(WHITE).set_opacity(1), run_time=0.5)

        equation_45 = MathTex("45 \\div 5 = 9", font_size=30).next_to(num_45, DOWN, buff=0.5)
        equation_45.shift(0.0 * RIGHT + 0.38 * UP)  # layout: separation vector
        self.play(Write(equation_45))
        self.wait(1.5)
        self.play(FadeOut(equation_45))
        self.play(Write(equation_45))
        check_45 = MathTex(r"\checkmark", font_size=40).next_to(equation_45, RIGHT, buff=0.5)
        self.play(FadeIn(check_45))
        self.wait(1.5)

        # Show 24 with '4' pulsing and equation
        num_24 = MathTex("24", font_size=40).move_to(ORIGIN)
        last_digit_24 = num_24[-1].copy()
        last_digit_24.set_color(GREEN)
        self.play(Transform(num_45, num_24))
        self.play(last_digit_24.animate.scale(1.5).set_color(GREEN).set_opacity(0.8), run_time=0.5)
        self.play(last_digit_24.animate.scale(1/1.5).set_color(WHITE).set_opacity(1), run_time=0.5)

        equation_24 = MathTex("24 \\div 4 = 6", font_size=30).next_to(num_24, DOWN, buff=0.5)
        equation_24.shift(0.0 * RIGHT + 0.37 * UP)  # layout: separation vector
        self.play(Write(equation_24))
        check_24 = MathTex(r"\checkmark", font_size=40).next_to(equation_24, RIGHT, buff=0.5)
        self.play(FadeIn(check_24))
        self.wait(1.5)

        # Show 22 with '2' pulsing and equation
        num_22 = MathTex("22", font_size=40).move_to(ORIGIN)
        last_digit_22 = num_22[-1].copy()
        last_digit_22.set_color(GREEN)
        self.play(Transform(num_24, num_22))
        self.play(last_digit_22.animate.scale(1.5).set_color(GREEN).set_opacity(0.8), run_time=0.5)
        self.play(last_digit_22.animate.scale(1/1.5).set_color(WHITE).set_opacity(1), run_time=0.5)

        equation_22 = MathTex("22 \\div 2 = 11", font_size=30).next_to(num_22, DOWN, buff=0.5)
        self.play(Write(equation_22))
        check_22 = MathTex(r"\checkmark", font_size=40).next_to(equation_22, RIGHT, buff=0.5)
        self.play(FadeIn(check_22))
        self.wait(1.5)

        # Show both 21 and 24 as Glint numbers
        num_21_copy = MathTex("21", font_size=40).move_to(LEFT * 2)
        last_digit_21_copy = num_21_copy[-1].copy()
        last_digit_21_copy.set_color(GREEN)
        check_21_copy = MathTex(r"\checkmark", font_size=40).next_to(num_21_copy, RIGHT, buff=0.5)

        num_24_copy = MathTex("24", font_size=40).move_to(RIGHT * 2)
        last_digit_24_copy = num_24_copy[-1].copy()
        last_digit_24_copy.set_color(GREEN)
        check_24_copy = MathTex(r"\checkmark", font_size=40).next_to(num_24_copy, RIGHT, buff=0.5)

        self.play(Transform(num_22, num_21_copy), Transform(equation_22, check_21_copy))
        self.play(Write(num_24_copy), Write(check_24_copy))
        self.wait(1.5)

        # Narration: both are Glint numbers
        narration_both = Text("Both 21 and 24 are Glint numbers", font_size=20).to_edge(DOWN)
        self.play(Write(narration_both))
        self.wait(1.5)
        self.play(FadeOut(narration_both))

        # Show 10 with '0' shaking red
        num_10 = MathTex("10", font_size=40).move_to(ORIGIN)
        last_digit_10 = num_10[-1].copy()
        last_digit_10.set_color(RED)
        self.play(Transform(num_24_copy, num_10))
        self.play(last_digit_10.animate.scale(1.5).set_color(RED).set_opacity(0.8), run_time=0.5)
        self.play(last_digit_10.animate.scale(1/1.5).set_color(WHITE).set_opacity(1), run_time=0.5)

        # Shake animation
        self.play(last_digit_10.animate.shift(LEFT * 0.1).shift(RIGHT * 0.1).shift(LEFT * 0.1).shift(RIGHT * 0.1), run_time=0.5)
        
        # Text: Division by Zero is Impossible
        zero_text = Text("Division by Zero is Impossible", font_size=24).next_to(num_10, DOWN, buff=0.5)
        self.play(Write(zero_text))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(num_10), FadeOut(last_digit_10), FadeOut(equation_22), FadeOut(check_22), FadeOut(zero_text))
        self.wait(0.5)
