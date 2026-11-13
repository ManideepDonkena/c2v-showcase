from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Problem: Bit Flips", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Original string
        original = MathTex("101", font_size=40)
        original.to_edge(LEFT).shift(UP*1.5)
        self.play(Write(original))
        self.wait(0.5)

        # Lightning bolt (using fallback if SVG is not found)
        try:
            lightning = SVGMobject("assets/lightning.svg")
            lightning.set_fill(RED, opacity=0.8)
            lightning.set_stroke(RED, width=3)
            lightning.scale(0.2)
            lightning.next_to(original[1], DOWN, buff=0.3)
            self.play(FadeIn(lightning))
            self.wait(0.5)
        except:
            # Fallback: use a simple red square instead of SVG
            lightning = Square(side_length=0.2, fill_color=RED, fill_opacity=0.8, stroke_color=RED, stroke_width=3)
            lightning.next_to(original[1], DOWN, buff=0.3)
            self.play(FadeIn(lightning))
            self.wait(0.5)

        # Bit flip animation
        self.play(lightning.animate.shift(DOWN*0.5))
        self.wait(0.3)
        
        # Flip the middle bit
        corrupted = MathTex("100", font_size=40)
        corrupted.to_edge(LEFT).shift(UP*1.5)
        self.play(Transform(original, corrupted))
        self.wait(0.5)

        # Pulse effect on corrupted string
        pulse = original.copy()
        pulse.set_fill(RED)
        self.play(
            FadeIn(pulse),
            run_time=0.3
        )
        self.play(
            FadeOut(pulse),
            run_time=0.3
        )
        self.wait(0.5)

        # Narration text
        narration = Text("Bit flips cause data corruption", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        
        self.play(FadeOut(title), FadeOut(original), FadeOut(narration))
        self.wait(0.5)
