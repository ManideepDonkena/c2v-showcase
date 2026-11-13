from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Correction and Recovery", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Original message
        original = MathTex("101", font_size=40)
        original.to_edge(UP).shift(DOWN*1.5)
        self.play(Write(original))
        self.wait(0.5)

        # Error string with highlighted bit
        error = MathTex("100", font_size=40)
        error.next_to(original, DOWN, buff=0.5)
        self.play(Write(error))
        self.wait(0.5)

        # Highlight bit at index 2
        highlight = Rectangle(height=0.6, width=0.6, color=YELLOW, fill_opacity=0.3)
        highlight.move_to(error[0][2])  # Bit at index 2 (0-based)
        highlight.shift(0.54 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(highlight))
        self.wait(0.5)

        # Flip the bit
        self.play(Transform(error[0][2], MathTex("1")))
        self.wait(0.5)

        # Show final corrected message
        corrected = MathTex("101", font_size=40)
        corrected.next_to(error, DOWN, buff=0.5)
        self.play(Write(corrected))
        self.wait(0.5)
        # Green checkmark
        check = Text("✓", color=GREEN, font_size=60)
        check.next_to(corrected, RIGHT, buff=0.5)
        self.play(Write(check))
        self.wait(0.5)

        # Narration text
        narration1 = Text("By flipping the identified bit", font_size=24)
        narration1.to_edge(LEFT).shift(UP*2)
        self.play(Write(narration1))
        self.wait(1)

        self.play(FadeOut(narration1))

        narration2 = Text("we restore the original data", font_size=24)
        narration2.to_edge(LEFT).shift(UP*2)
        self.play(Write(narration2))
        self.wait(1)

        self.play(FadeOut(narration2))

        narration3 = Text("Hamming codes allow us not just to detect", font_size=24)
        narration3.to_edge(LEFT).shift(UP*2)
        narration3.shift(0.0 * RIGHT + 0.32 * UP)  # layout: separation vector
        self.play(Write(narration3))
        self.wait(1)

        self.play(FadeOut(narration3))

        narration4 = Text("but to correct single-bit errors automatically", font_size=24)
        narration4.to_edge(LEFT).shift(UP*2)
        narration4.shift(0.0 * RIGHT + 0.32 * UP)  # layout: separation vector
        self.play(Write(narration4))
        self.wait(1)

        self.play(FadeOut(narration4))

        # Cleanup
        self.play(
            FadeOut(title),
            FadeOut(original),
            FadeOut(error),
            FadeOut(corrected),
            FadeOut(check),
            FadeOut(highlight)
        )
        self.wait(0.5)
