from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Reversal Property", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial dapple number 52
        dapple_52 = MathTex("52", color=GREEN).scale(2).move_to(UP * 1.5)
        dapple_label = Text("Dapple", font_size=24).next_to(dapple_52, DOWN)
        self.play(Write(dapple_52), Write(dapple_label))
        self.wait(1)
        # Split into digits
        digit5 = MathTex("5", color=GREEN).scale(1.5).move_to(LEFT * 0.6 + DOWN * 0.8)
        digit2 = MathTex("2", color=GREEN).scale(1.5).move_to(RIGHT * 0.6 + DOWN * 0.8)
        self.play(TransformFromCopy(dapple_52, digit5), Transform(dapple_label, Text("5", font_size=24).next_to(digit5, DOWN)))
        self.wait(0.5)
        self.play(TransformFromCopy(dapple_52, digit2), Transform(dapple_label, Text("2", font_size=24).next_to(digit2, DOWN)))
        self.wait(0.5)

        # Swap positions to form 25
        digits = VGroup(digit5, digit2)
        swapped = MathTex("25", color=RED).scale(2).move_to(digits.get_center())
        not_dapple_label = Text("Not Dapple", font_size=24).next_to(swapped, DOWN)
        arrow = Arrow(start=LEFT, end=RIGHT, color=WHITE).scale(0.5).next_to(digits, RIGHT, buff=0.6)
        reversal_text = Text("Reversal", font_size=24).next_to(arrow, UP)

        self.play(
            Transform(digit5, MathTex("2", color=RED).scale(1.5).move_to(digit5.get_center())),
            Transform(digit2, MathTex("5", color=RED).scale(1.5).move_to(digit2.get_center())),
            Write(arrow),
            Write(reversal_text),
            FadeOut(dapple_label)
        )
        self.wait(0.5)

        # Show 25 as not dapple
        self.play(
            ReplacementTransform(VGroup(digit5, digit2), swapped),
            Write(not_dapple_label)
        )
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(dapple_52),
            FadeOut(swapped),
            FadeOut(not_dapple_label),
            FadeOut(arrow),
            FadeOut(reversal_text)
        )
        self.wait(0.5)
