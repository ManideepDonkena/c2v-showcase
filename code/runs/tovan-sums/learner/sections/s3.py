from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Absorbing Element (-1)", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial circles: '4', '-1', '2'
        circle4 = Circle(radius=0.7, color=BLUE, fill_color=BLUE, fill_opacity=0.5).move_to(LEFT * 2)
        text4 = MathTex("4", font_size=30).move_to(circle4.get_center())
        
        circle_neg1 = Circle(radius=0.7, color=RED, fill_color=RED, fill_opacity=0.5).move_to(ORIGIN)
        text_neg1 = MathTex("-1", font_size=30).move_to(circle_neg1.get_center())

        circle2 = Circle(radius=0.7, color=GREEN, fill_color=GREEN, fill_opacity=0.5).move_to(RIGHT * 2)
        text2 = MathTex("2", font_size=30).move_to(circle2.get_center())

        # Show initial chain
        self.play(Create(circle4), Write(text4))
        self.play(Create(circle_neg1), Write(text_neg1))
        self.play(Create(circle2), Write(text2))
        self.wait(1)

        # Label the operation
        op_label = MathTex("4 \\oplus -1", font_size=30).next_to(circle4, DOWN)
        self.play(Write(op_label))
        self.wait(1)

        # Show result of 4 ⊕ -1 = -1
        self.play(
            circle4.animate.shift(LEFT * 2),
            text4.animate.shift(LEFT * 2),
            run_time=0.5
        )
        self.wait(0.5)

        # Simulate absorption: -1 swallows '4'
        self.play(
            FadeOut(circle4),
            FadeOut(text4),
            run_time=0.3
        )

        # Show result is now just -1
        result_neg1 = MathTex("-1", font_size=30).move_to(LEFT * 2)
        self.play(Write(result_neg1))
        self.wait(0.5)

        # Now show (-1 ⊕ 2) = -1
        op_label2 = MathTex("-1 \\oplus 2", font_size=30).next_to(circle_neg1, DOWN)
        self.play(Write(op_label2))
        self.wait(1)

        # Move '2' toward '-1'
        self.play(
            circle2.animate.shift(RIGHT * 2),
            text2.animate.shift(RIGHT * 2),
            run_time=0.5
        )
        self.wait(0.5)

        # Simulate absorption: -1 swallows '2'
        self.play(
            FadeOut(circle2),
            FadeOut(text2),
            run_time=0.3
        )

        # Final result is still -1
        final_result = MathTex("-1", font_size=30).move_to(RIGHT * 2)
        self.play(Write(final_result))
        self.wait(1)

        # Narration text: "The number negative one acts as an absorbing element"
        absorb_text = Text("The number negative one acts as an absorbing element.", font_size=24).to_edge(DOWN)
        self.play(Write(absorb_text))
        self.wait(2)

        # Narration text: "Regardless of the other operand's value, if it is combined with -1, the result is always -1."
        rule_text = Text("Regardless of the other operand's value, if it is combined with -1, the result is always -1.", font_size=24).to_edge(DOWN)
        self.play(ReplacementTransform(absorb_text, rule_text))
        self.wait(3)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(op_label),
            FadeOut(op_label2),
            FadeOut(result_neg1),
            FadeOut(final_result),
            FadeOut(rule_text)
        )
        self.wait(0.5)
