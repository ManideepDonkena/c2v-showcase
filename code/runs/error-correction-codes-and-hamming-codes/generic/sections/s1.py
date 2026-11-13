from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Problem: Bit Flips", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Original binary string
        original = MathTex("1011", font_size=40)
        original.to_edge(LEFT).shift(UP*1.5)
        self.play(Write(original))
        self.wait(0.5)

        # Lightning bolt (using a simple Manim primitive instead of SVG)
        lightning = RegularPolygon(n=3, color=RED, fill_opacity=1).scale(0.2)
        lightning.move_to(original.get_center() + RIGHT*1.5)
        self.play(FadeIn(lightning))
        self.wait(0.5)

        # Flip animation
        flipped = MathTex("0011", font_size=40)
        flipped.to_edge(LEFT).shift(UP*1.5)
        self.play(Transform(original, flipped))
        self.wait(0.5)

        # Shake effect
        self.play(original.animate.shift(RIGHT*0.1).shift(LEFT*0.2).shift(RIGHT*0.1))
        self.wait(0.5)

        # Narration text
        narration = Text("Noise causes bit flips", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)

        # Clean up
        self.play(FadeOut(title), FadeOut(lightning), FadeOut(original), FadeOut(narration))
        self.wait(0.5)
