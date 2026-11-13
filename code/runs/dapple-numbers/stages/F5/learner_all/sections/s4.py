from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Reversal Property", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial dapple number 52
        dapple_52 = MathTex("52", color=GREEN).scale(2)
        dapple_label = Text("Dapple", font_size=24).next_to(dapple_52, DOWN)
        self.play(Write(dapple_52), Write(dapple_label))
        self.wait(1)
        # Split into digits
        digit5 = MathTex("5", color=GREEN).scale(1.5)
        digit2 = MathTex("2", color=GREEN).scale(1.5)
        self.play(Transform(dapple_52, digit5), Transform(dapple_label, Text("5", font_size=24).next_to(digit5, DOWN)))
        self.wait(0.5)
        self.play(Transform(dapple_52, digit2), Transform(dapple_label, Text("2", font_size=24).next_to(digit2, DOWN)))
        self.wait(0.5)

        # Swap positions to form 25
        swapped = MathTex("25", color=RED).scale(2)
        not_dapple_label = Text("Not Dapple", font_size=24).next_to(swapped, DOWN)
        arrow = Arrow(start=LEFT, end=RIGHT, color=WHITE).scale(0.5).next_to(dapple_52, UP)
        reversal_text = Text("Reversal", font_size=24).next_to(arrow, UP)

        self.play(
            Transform(digit5, MathTex("2", color=RED).scale(1.5)),
            Transform(digit2, MathTex("5", color=RED).scale(1.5)),
            Write(arrow),
            Write(reversal_text)
        )
        self.wait(0.5)

        # Show 25 as not dapple
        self.play(
            ReplacementTransform(VGroup(digit5, digit2), swapped),
            Write(not_dapple_label)
        )
        self.wait(1.5)

        # Add explanation text
        explanation = Text("A whole number is 'dapple' if its tens digit is strictly greater than its units digit.", font_size=20).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(1.5)

        # Example: 61 is dapple with green checkmark
        example_61 = MathTex("61", color=GREEN).scale(1.5).next_to(explanation, UP, buff=0.5)
        checkmark = Circle(color=GREEN, radius=0.3).next_to(example_61, LEFT)
        checkmark.add(Cross(checkmark))
        self.play(Write(example_61), Write(checkmark))
        self.wait(1.5)

        # Example: 16 is not dapple
        example_16 = MathTex("16", color=RED).scale(1.5).next_to(example_61, DOWN, buff=0.5)
        self.play(Write(example_16))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(dapple_52),
            FadeOut(dapple_label),
            FadeOut(swapped),
            FadeOut(not_dapple_label),
            FadeOut(arrow),
            FadeOut(reversal_text),
            FadeOut(explanation),
            FadeOut(example_61),
            FadeOut(checkmark),
            FadeOut(example_16)
        )
        self.wait(0.5)
