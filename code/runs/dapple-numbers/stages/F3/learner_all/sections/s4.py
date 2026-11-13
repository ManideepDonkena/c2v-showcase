from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Reversal Property", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 52 as Dapple
        num_52 = MathTex("52", color=GREEN).scale(1.5)
        label_52 = Text("Dapple", font_size=24).next_to(num_52, DOWN)
        self.play(Write(num_52), Write(label_52))
        self.wait(1)
        # Split 52 into digits
        digit_5 = MathTex("5")
        digit_2 = MathTex("2")
        self.play(Transform(num_52, VGroup(digit_5, digit_2)))
        self.wait(0.5)

        # Swap positions to make 25
        swapped = VGroup(digit_2.copy(), digit_5.copy())
        swapped.arrange(RIGHT, buff=0.3)
        swapped.move_to(num_52.get_center()).shift(UP * 0.58)
        self.play(Transform(VGroup(digit_5, digit_2), swapped))
        self.wait(0.5)
        # Change to 25 and label as Not Dapple
        num_25 = MathTex("25", color=RED).scale(1.5)
        label_25 = Text("Not Dapple", font_size=24).next_to(num_25, DOWN)
        self.play(Transform(swapped, num_25), Transform(label_52, label_25))
        self.wait(1)

        # Arrow from 52 to 25
        arrow = Arrow(start=num_52.get_left(), end=num_25.get_right(), buff=0.2)
        reversal_text = Text("Reversal", font_size=24).next_to(arrow, UP)
        self.play(GrowArrow(arrow), Write(reversal_text))
        self.wait(1.5)

        # Fade out previous content
        self.play(FadeOut(title), FadeOut(num_52), FadeOut(label_52), FadeOut(arrow), FadeOut(reversal_text))

        # Show 32 as example of dapple number
        num_32 = MathTex("32", color=GREEN).scale(1.5)
        label_32 = Text("Dapple", font_size=24).next_to(num_32, DOWN)
        self.play(Write(num_32), Write(label_32))
        self.wait(1)

        # Highlight tens and units digits
        tens_digit = SurroundingRectangle(MathTex("3"), color=YELLOW, buff=0.1)
        units_digit = SurroundingRectangle(MathTex("2"), color=YELLOW, buff=0.1)
        self.play(Create(tens_digit), Create(units_digit))
        self.wait(1)

        # Show condition 3 > 2
        condition = MathTex("3 > 2", color=GREEN).next_to(num_32, DOWN, buff=0.5)
        self.play(Write(condition))
        self.wait(1.5)

        # Glow around 32 to confirm it's dapple
        checkmark = always_redraw(lambda: Circle(color=GREEN, radius=0.4, stroke_width=8).move_to(num_32))
        self.play(Create(checkmark))
        self.wait(1)

        # Fade out everything
        self.play(FadeOut(num_32), FadeOut(label_32), FadeOut(tens_digit), FadeOut(units_digit),
                  FadeOut(condition), FadeOut(checkmark))
        self.wait(0.5)
