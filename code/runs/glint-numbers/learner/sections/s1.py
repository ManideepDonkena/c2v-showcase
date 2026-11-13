from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Glint Numbers", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 21 with last digit pulsing and checkmark
        num_21 = MathTex("21", font_size=40)
        num_21.move_to(ORIGIN)
        last_digit_21 = num_21[-1].copy()
        last_digit_21.set_color(GREEN)
        self.play(Write(num_21))
        self.play(last_digit_21.animate.scale(1.5).set_color(GREEN).set_opacity(0.8))
        self.wait(0.5)

        # Definition text
        definition = Text("Glint Number: Last digit ≠ 0 AND Number ÷ Last Digit = Whole", font_size=24)
        definition.next_to(num_21, DOWN, buff=0.5)
        self.play(Write(definition))
        self.wait(0.5)

        # Checkmark
        check = Tex(r"$\checkmark$").set_color(GREEN).scale(1.5)
        check.next_to(num_21, RIGHT, buff=0.5)
        self.play(FadeIn(check))
        self.wait(1)

        # Narration: "For instance, every number ending in 1 is automatically a Glint number..."
        narration = Text("Ends in 1 = Always Glint", font_size=24)
        narration.next_to(definition, DOWN, buff=0.5)
        self.play(Write(narration))
        self.wait(1.5)

        # Fade out previous
        self.play(FadeOut(last_digit_21), FadeOut(check), FadeOut(narration))

        # Show 31 with '1' pulsing and text
        num_31 = MathTex("31", font_size=40)
        num_31.move_to(ORIGIN)
        last_digit_31 = num_31[-1].copy()
        last_digit_31.set_color(GREEN)
        num_31.shift(0.0 * RIGHT + 0.43 * UP)  # layout: separation vector
        self.play(Write(num_31))
        self.play(last_digit_31.animate.scale(1.5).set_color(GREEN).set_opacity(0.8))
        self.wait(0.5)

        narration2 = Text("Ends in 1 = Always Glint", font_size=24)
        narration2.next_to(num_31, DOWN, buff=0.5)
        self.play(Write(narration2))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(last_digit_31), FadeOut(narration2))

        # Show 27 with '7' pulsing and red X
        num_27 = MathTex("27", font_size=40)
        num_27.move_to(ORIGIN)
        last_digit_27 = num_27[-1].copy()
        last_digit_27.set_color(GREEN)
        num_27.shift(0.0 * RIGHT + 0.43 * UP)  # layout: separation vector
        num_27.shift(0.0 * RIGHT + 0.44 * UP)  # layout: separation vector
        self.play(Write(num_27))
        self.play(last_digit_27.animate.scale(1.5).set_color(GREEN).set_opacity(0.8))
        self.wait(0.5)

        # Equation and X
        eq_27 = MathTex("27 \\div 7 = 3.85...", font_size=24)
        eq_27.next_to(num_27, DOWN, buff=0.5)
        self.play(Write(eq_27))
        self.wait(0.5)

        x_mark = Tex(r"$\times$").set_color(RED).scale(1.5)
        x_mark.next_to(num_27, RIGHT, buff=0.5)
        self.play(FadeIn(x_mark))
        self.wait(1)

        # Narration: "Ends in 7 is NOT always Glint"
        narration3 = Text("Ends in 7 is NOT always Glint", font_size=24)
        narration3.next_to(eq_27, DOWN, buff=0.5)
        self.play(Write(narration3))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(last_digit_27), FadeOut(x_mark), FadeOut(eq_27), FadeOut(narration3))

        # Show 22 with last digit pulsing and checkmark
        num_22 = MathTex("22", font_size=40)
        num_22.move_to(ORIGIN)
        last_digit_22 = num_22[-1].copy()
        last_digit_22.set_color(GREEN)
        self.play(Write(num_22))
        self.play(last_digit_22.animate.scale(1.5).set_color(GREEN).set_opacity(0.8))
        self.wait(0.5)

        # Equation and checkmark
        eq_22 = MathTex("22 \\div 2 = 11", font_size=24)
        eq_22.next_to(num_22, DOWN, buff=0.5)
        self.play(Write(eq_22))
        self.wait(0.5)

        check_22 = Tex(r"$\checkmark$").set_color(GREEN).scale(1.5)
        check_22.next_to(num_22, RIGHT, buff=0.5)
        self.play(FadeIn(check_22))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(last_digit_22), FadeOut(eq_22), FadeOut(check_22))

        # Show 21 and 24 both with checkmarks
        num_21_final = MathTex("21", font_size=40)
        num_24_final = MathTex("24", font_size=40)
        num_21_final.to_edge(LEFT, buff=1)
        num_24_final.to_edge(RIGHT, buff=1)

        # Pulse 1 in 21
        last_digit_21_final = num_21_final[-1].copy()
        last_digit_21_final.set_color(GREEN)
        self.play(Write(num_21_final))
        self.play(last_digit_21_final.animate.scale(1.5).set_color(GREEN).set_opacity(0.8))

        # Pulse 4 in 24
        last_digit_24_final = num_24_final[-1].copy()
        last_digit_24_final.set_color(GREEN)
        self.play(Write(num_24_final))
        self.play(last_digit_24_final.animate.scale(1.5).set_color(GREEN).set_opacity(0.8))

        # Checkmarks
        check_21 = Tex(r"$\checkmark$").set_color(GREEN).scale(1.5)
        check_24 = Tex(r"$\checkmark$").set_color(GREEN).scale(1.5)
        check_21.next_to(num_21_final, RIGHT, buff=0.5)
        check_24.next_to(num_24_final, RIGHT, buff=0.5)

        self.play(FadeIn(check_21), FadeIn(check_24))
        self.wait(0.5)

        # Narration: "Both are Glint numbers to demonstrate that they can be odd or even"
        narration4 = Text("Both are Glint numbers", font_size=24)
        narration4.next_to(VGroup(num_21_final, num_24_final), DOWN, buff=0.5)
        self.play(Write(narration4))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(last_digit_21_final), FadeOut(last_digit_24_final), 
                  FadeOut(check_21), FadeOut(check_24), FadeOut(narration4))

        # Final title fade
        self.play(FadeOut(title))
        self.wait(0.5)
