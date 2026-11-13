from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Worked Examples: Success vs Failure", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Left side: 24 is Glint
        num_24 = Text("24", font_size=40).to_edge(LEFT).shift(UP * 1.5)
        highlight_4 = SurroundingRectangle(num_24[1], color=YELLOW, buff=0.1)
        self.play(Write(num_24), Create(highlight_4))
        self.wait(0.5)
        eq_24 = MathTex("24 \\div 4 = 6", font_size=32).next_to(num_24, DOWN, buff=0.5)
        check = Tex("\\checkmark", color=GREEN, font_size=40).next_to(eq_24, LEFT)
        self.play(Write(eq_24), Write(check))
        self.wait(1)

        # Right side: 26 is not Glint
        num_26 = Text("26", font_size=40).to_edge(RIGHT).shift(UP * 1.5)
        highlight_6 = SurroundingRectangle(num_26[1], color=YELLOW, buff=0.1)
        self.play(Write(num_26), Create(highlight_6))
        self.wait(0.5)

        eq_26 = MathTex("26 \\div 6 = 4.33\\ldots", font_size=32).next_to(num_26, DOWN, buff=0.5)
        cross = Tex("✗", color=RED, font_size=40).next_to(eq_26, LEFT)
        self.play(Write(eq_26), Write(cross))
        self.wait(1)

        # Narration text
        narration1 = Text("24 is Glint", font_size=24).to_edge(BOTTOM).shift(UP * 0.5)
        narration2 = Text("26 is not Glint", font_size=24).next_to(narration1, RIGHT, buff=2)
        self.play(Write(narration1), Write(narration2))
        self.wait(1.5)

        # Clean up
        self.play(FadeOut(title), FadeOut(num_24), FadeOut(highlight_4), FadeOut(eq_24), FadeOut(check),
                  FadeOut(num_26), FadeOut(highlight_6), FadeOut(eq_26), FadeOut(cross),
                  FadeOut(narration1), FadeOut(narration2))
        self.wait(0.5)
