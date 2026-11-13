from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Reversal Property", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 52 as dapple
        num_52 = MathTex("52", color=GREEN).scale(2)
        label_52 = Text("Dapple", font_size=24).next_to(num_52, DOWN)
        self.play(Write(num_52), Write(label_52))
        self.wait(1)

        # Split into digits
        digit_5 = MathTex("5", color=GREEN).scale(1.5).move_to(num_52.get_left())
        digit_2 = MathTex("2", color=GREEN).scale(1.5).move_to(num_52.get_right())
        self.play(Transform(num_52, digit_5), Transform(label_52, Text(" ", font_size=24)))
        self.wait(0.5)
        self.play(ReplacementTransform(digit_5, digit_2), ReplacementTransform(digit_2, digit_5))
        self.wait(0.5)

        # Form 25
        num_25 = MathTex("25", color=RED).scale(2)
        label_25 = Text("Not Dapple", font_size=24).next_to(num_25, DOWN)
        num_25.shift(0.3 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(num_25), Write(label_25))
        self.wait(1)

        # Arrow
        arrow = Arrow(start=num_52.get_center(), end=num_25.get_center(), color=YELLOW)
        arrow_label = Text("Reversal", font_size=24).next_to(arrow, UP)
        self.play(GrowArrow(arrow), Write(arrow_label))
        self.wait(1)

        # Fade out
        self.play(FadeOut(num_52), FadeOut(label_52), FadeOut(num_25), FadeOut(label_25), FadeOut(arrow), FadeOut(arrow_label))

        # Definition and examples
        def_text = Text("A whole number is dapple if its tens digit > units digit.", font_size=24).to_edge(UP)
        self.play(Write(def_text))
        self.wait(1)

        # Example 61 is dapple
        ex_61 = MathTex("61", color=GREEN).scale(1.5).shift(UP * 0.5)
        check_61 = Circle(color=GREEN, radius=0.3).move_to(ex_61.get_center())
        check_mark = Text("✓", color=GREEN, font_size=30).move_to(check_61.get_center())
        self.play(Write(ex_61))
        self.wait(0.5)
        self.play(Create(check_61), Write(check_mark))
        self.wait(1)

        # Example 16 is not dapple
        ex_16 = MathTex("16", color=RED).scale(1.5).shift(DOWN * 0.5)
        self.play(Write(ex_16))
        self.wait(0.5)
        self.play(FadeOut(check_61), FadeOut(check_mark))

        # Rule 2: Reversal of dapple is not dapple
        rule = Text("Reversing the two digits of a dapple number gives a non-dapple number.", font_size=24).to_edge(DOWN)
        self.play(Write(rule))
        self.wait(1)

        # Worked example: 52 -> 25
        ex_52 = MathTex("52", color=GREEN).scale(1.5).shift(UP * 0.5)
        ex_25 = MathTex("25", color=RED).scale(1.5).shift(DOWN * 0.5)
        self.play(Write(ex_52))
        self.wait(0.5)
        self.play(ReplacementTransform(ex_52, ex_25))
        self.wait(0.5)

        # 44 is not dapple
        ex_44 = MathTex("44", color=RED).scale(1.5).shift(DOWN * 1.5)
        self.play(Write(ex_44))
        self.wait(1)

        # Fade out
        self.play(FadeOut(def_text), FadeOut(rule), FadeOut(ex_52), FadeOut(ex_25), FadeOut(ex_44))
        self.wait(0.5)
