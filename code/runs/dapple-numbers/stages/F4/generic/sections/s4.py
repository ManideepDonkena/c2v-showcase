from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Reversal Property", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial dapple number 52
        num_52 = MathTex("52", color=GREEN).scale(2)
        num_52_label = Text("Dapple", font_size=24).next_to(num_52, DOWN)
        self.play(Write(num_52), Write(num_52_label))
        self.wait(1)

        # Split into digits
        digit_5 = MathTex("5", color=GREEN).scale(1.5)
        digit_2 = MathTex("2", color=GREEN).scale(1.5)
        group_digits = VGroup(digit_5, digit_2).arrange(RIGHT, buff=0.5)
        self.play(Transform(num_52, group_digits))
        self.wait(0.5)

        # Swap positions to make 25
        swapped_group = VGroup(digit_2.copy(), digit_5.copy()).arrange(RIGHT, buff=0.5)
        self.play(Transform(group_digits, swapped_group))
        self.wait(0.5)

        # Show result is not dapple
        num_25 = MathTex("25", color=RED).scale(2)
        num_25_label = Text("Not Dapple", font_size=24).next_to(num_25, DOWN)
        self.play(Transform(group_digits, num_25), Write(num_25_label))
        self.wait(1)

        # Arrow and text
        arrow = Arrow(start=UP, end=DOWN, color=YELLOW).scale(0.5).next_to(num_25, UP)
        reversal_text = Text("Reversal", font_size=24).next_to(arrow, UP)
        self.play(GrowArrow(arrow), Write(reversal_text))
        self.wait(1)

        # Narration key words
        key_words = Text("Reversal Property", font_size=24).to_edge(DOWN)
        self.play(Write(key_words))
        self.wait(1.5)

        # Clear screen and show explanation
        self.play(FadeOut(title), FadeOut(num_52_label), FadeOut(num_25_label),
                  FadeOut(arrow), FadeOut(reversal_text), FadeOut(key_words))

        # Show definition and example
        def_text = Text("A whole number is dapple when tens digit > units digit.", font_size=24)
        rule1 = Text("Rule 1: Every multiple of 10 from 10 to 90 is dapple.", font_size=24)
        example = Text("Example: 52 (5>2) → 25 (2<5)", font_size=24)

        def_text.to_edge(UP)
        rule1.next_to(def_text, DOWN)
        example.next_to(rule1, DOWN)

        self.play(Write(def_text))
        self.wait(0.5)
        self.play(Write(rule1))
        self.wait(0.5)
        self.play(Write(example))
        self.wait(2)

        # Fade out
        self.play(FadeOut(def_text), FadeOut(rule1), FadeOut(example))
        self.wait(0.5)
