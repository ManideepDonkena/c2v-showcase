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
        original.to_edge(UP, buff=1.5)
        
        # Error message with highlighted bit
        error = MathTex("100", font_size=40)
        error.shift(DOWN * 1.5)
        
        # Highlight bit at index 2 (0-indexed from left)
        highlight = Rectangle(height=0.6, width=0.6, color=YELLOW, fill_opacity=0.3)
        highlight.move_to(error[0].get_center() + RIGHT * 0.3)
        
        # Show original and error
        self.play(Write(original))
        self.play(Write(error))
        self.wait(0.5)
        
        # Highlight the bit that needs to be flipped
        highlight.shift(0.43 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(highlight))
        self.wait(1)
        
        # Flip the bit from 0 to 1
        self.play(Transform(error[0][2], MathTex("1", font_size=40).move_to(error[0][2].get_center())))
        self.wait(1)
        
        # Show final corrected message
        correct = MathTex("101", font_size=40)
        correct.move_to(error.get_center())
        # Green checkmark
        check = Text(
            "✓",
            font_size=60,
            color=GREEN
        )
        self.play(Transform(error, correct))
        self.play(Write(check))
        self.wait(1.5)
        
        # Narration text
        correction_text = Text("By flipping the identified bit", font_size=24)
        correction_text.to_edge(DOWN, buff=0.5)
        self.play(Write(correction_text))
        self.wait(1)
        
        self.play(FadeOut(correction_text))
        
        auto_correct = Text("Hamming codes allow us not just to detect, but to correct single-bit errors automatically.", font_size=24)
        auto_correct.to_edge(DOWN, buff=0.5)
        self.play(Write(auto_correct))
        self.wait(2)
        
        self.play(FadeOut(auto_correct), FadeOut(title), FadeOut(error), FadeOut(check), FadeOut(highlight))
        self.wait(0.5)
