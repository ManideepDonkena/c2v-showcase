from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Scaling Invariance", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial mirthful triangle: sides 4, 5, 6
        a, b, c = 4, 5, 6
        scale_factor = 2
        triangle1 = Triangle().scale(0.5).shift(LEFT * 2)
        triangle1.set_stroke(color=GREEN, width=3)
        triangle1_label = MathTex("4", "5", "6").arrange(DOWN, buff=0.2).next_to(triangle1, DOWN)
        self.play(Create(triangle1), Write(triangle1_label))
        self.wait(1)

        # Scale up to 8, 10, 12
        triangle2 = Triangle().scale(1.0).shift(RIGHT * 2)
        triangle2.set_stroke(color=GREEN, width=3)
        triangle2_label = MathTex("8", "10", "12").arrange(DOWN, buff=0.2).next_to(triangle2, DOWN)
        self.play(ReplacementTransform(triangle1, triangle2), ReplacementTransform(triangle1_label, triangle2_label))
        self.wait(1)
        # Text: Scaling preserves mirth
        text = Text("Scaling preserves mirth", font_size=24).to_edge(DOWN)
        self.play(Write(text))
        self.wait(1.5)

        # Scale down to 2, 2.5, 3
        triangle3 = Triangle().scale(0.25).shift(LEFT * 2)
        triangle3.set_stroke(color=GREEN, width=3)
        triangle3_label = MathTex("2", "2.5", "3").arrange(DOWN, buff=0.2).next_to(triangle3, DOWN)
        self.play(ReplacementTransform(triangle2, triangle3), ReplacementTransform(triangle2_label, triangle3_label))
        self.wait(1)

        # Fade out scaling text
        self.play(FadeOut(text))

        # Show check for triangle with sides 5, 7, 8
        triangle4 = Triangle().scale(0.6).shift(UP * 1.5)
        triangle4.set_stroke(color=BLUE, width=3)
        triangle4_label = MathTex("5", "7", "8").arrange(DOWN, buff=0.2).next_to(triangle4, DOWN)
        self.play(Create(triangle4), Write(triangle4_label))
        self.wait(1)

        # Ask: Is twice the longest side at most three times the shortest?
        question = Text("Is twice the longest side at most three times the shortest?", font_size=24).to_edge(DOWN)
        self.play(Write(question))
        self.wait(1.5)

        # Show calculation
        calc = MathTex("2 \\times 8 \\leq 3 \\times 5").scale(1.2).to_edge(UP)
        calc.shift(0.0 * RIGHT + -0.65 * UP)  # layout: separation vector
        self.play(Write(calc))
        self.wait(1.5)

        # Resolve: 16 <= 15
        result = MathTex("16 \\leq 15").scale(1.2).next_to(calc, DOWN, buff=0.3)
        self.play(Write(result))
        self.wait(1.5)

        # Red X or pulse to indicate failure
        cross = Cross(result)
        self.play(Create(cross))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(triangle1), FadeOut(triangle2), FadeOut(triangle3), FadeOut(triangle4),
                  FadeOut(triangle1_label), FadeOut(triangle2_label), FadeOut(triangle3_label), FadeOut(triangle4_label),
                  FadeOut(calc), FadeOut(result), FadeOut(cross), FadeOut(question), FadeOut(title))
        self.wait(0.5)
