from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Non-Examples and Edge Cases", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 44
        num_44 = MathTex("44", font_size=40)
        num_44.shift(UP * 1)
        self.play(Write(num_44))
        self.wait(0.5)

        # Highlight both 4's
        highlight_44 = always_redraw(
            lambda: SurroundingRectangle(num_44, color=RED, buff=0.1)
        )
        self.play(Create(highlight_44))
        self.wait(0.5)

        # Add equals sign
        equals = MathTex("=", font_size=40)
        equals.next_to(num_44, RIGHT, buff=0.3)
        self.play(Write(equals))
        self.wait(0.5)

        # Label "Not Dapple"
        not_dapple_44 = Text("Not Dapple", font_size=24, color=RED)
        not_dapple_44.next_to(num_44, DOWN, buff=0.3)
        self.play(Write(not_dapple_44))
        self.wait(1)

        # Fade out 44 and equals
        self.play(FadeOut(num_44), FadeOut(equals), FadeOut(not_dapple_44), FadeOut(highlight_44))
        self.wait(0.5)

        # Show 25
        num_25 = MathTex("25", font_size=40)
        num_25.shift(UP * 1)
        self.play(Write(num_25))
        self.wait(0.5)

        # Highlight 2 and 5
        highlight_25 = always_redraw(
            lambda: SurroundingRectangle(num_25, color=RED, buff=0.1)
        )
        self.play(Create(highlight_25))
        self.wait(0.5)

        # Label "Not Dapple (2 < 5)"
        not_dapple_25 = Text("Not Dapple (2 < 5)", font_size=24, color=RED)
        not_dapple_25.next_to(num_25, DOWN, buff=0.3)
        self.play(Write(not_dapple_25))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(num_25),
            FadeOut(not_dapple_25),
            FadeOut(highlight_25),
            FadeOut(title)
        )
        self.wait(0.5)
