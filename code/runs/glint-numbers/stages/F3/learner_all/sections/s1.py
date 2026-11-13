from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Glint Numbers", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 21 as example of Glint number
        num_21 = Integer(21, font_size=40).move_to(ORIGIN)
        last_digit_21 = num_21[-1]
        self.play(Write(num_21))
        self.wait(0.5)

        # Pulse last digit '1' green
        self.play(last_digit_21.animate.set_color(GREEN).scale(1.2), run_time=0.5)
        self.play(last_digit_21.animate.scale(1/1.2).set_color(WHITE), run_time=0.5)

        # Fade rest of number slightly
        num_21_copy = num_21.copy().set_opacity(0.5)
        self.play(Transform(num_21, num_21_copy))

        # Definition text
        definition = MathTex(r"\text{Glint Number: Last digit} \neq 0 \text{ AND } \frac{\text{Number}}{\text{Last Digit}} = \text{Whole}", font_size=24)
        definition.next_to(num_21, DOWN, buff=0.5)
        self.play(Write(definition))
        self.wait(1)

        # Checkmark
        check = Tex(r"$\checkmark$").set_color(GREEN).scale(1.5)
        check.next_to(num_21, RIGHT, buff=0.5)
        self.play(FadeIn(check))
        self.wait(1.5)

        # Narration: "Ending in 0 is NEVER Glint"
        num_10 = Integer(10, font_size=40).move_to(ORIGIN)
        last_digit_10 = num_10[-1]
        self.play(ReplacementTransform(num_21, num_10))
        self.wait(0.5)

        # Shake and turn red
        self.play(last_digit_10.animate.set_color(RED).scale(1.3), run_time=0.2)
        self.play(last_digit_10.animate.scale(1/1.3).set_color(WHITE), run_time=0.2)
        self.play(last_digit_10.animate.set_color(RED), run_time=0.2)
        self.wait(0.5)

        # X mark
        x_mark = Tex(r"$\times$").set_color(RED).scale(2)
        x_mark.next_to(num_10, RIGHT, buff=0.7)  # Increased buffer to avoid overlap
        x_mark.shift(0.44 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(FadeIn(x_mark))
        self.wait(1.5)

        # Narration: "Every number ending in 1 is automatically a Glint number"
        self.play(FadeOut(num_10), FadeOut(x_mark), FadeOut(definition), FadeOut(check))

        # Show 22 and its division
        num_22 = Integer(22, font_size=40).move_to(ORIGIN)
        last_digit_22 = num_22[-1]
        self.play(Write(num_22))
        self.wait(0.5)

        # Pulse last digit '2'
        self.play(last_digit_22.animate.set_color(GREEN).scale(1.2), run_time=0.5)
        self.play(last_digit_22.animate.scale(1/1.2).set_color(WHITE), run_time=0.5)

        # Equation
        equation = MathTex("22 \\div 2 = 11", font_size=30)
        equation.next_to(num_22, DOWN, buff=0.5)
        self.play(Write(equation))
        self.wait(1)

        # Green checkmark
        check2 = Tex(r"$\checkmark$").set_color(GREEN).scale(1.5)
        check2.next_to(equation, RIGHT, buff=0.5)
        self.play(FadeIn(check2))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(num_22), FadeOut(equation), FadeOut(check2), FadeOut(title))
