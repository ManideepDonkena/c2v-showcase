from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Verification and Growth", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Final word
        final_word = Text("XYYYXYX", font_size=40)
        final_word.next_to(title, DOWN, buff=0.5)
        self.play(Write(final_word))
        self.wait(1)

        # Length counter
        length_text = Text("Length: 7", font_size=32)
        length_text.next_to(final_word, DOWN, buff=0.5)
        self.play(Write(length_text))
        self.wait(1)

        # Arrow and text
        arrow = Arrow(start=UP, end=DOWN, color=YELLOW).next_to(length_text, DOWN, buff=0.5)
        growth_text = Text("Every rewrite makes the word longer", font_size=24)
        growth_text.next_to(arrow, DOWN, buff=0.2)
        self.play(GrowArrow(arrow), Write(growth_text))
        self.wait(1)

        # Checkmark
        checkmark = Tex(r"$\checkmark$").set_color(GREEN).scale(1.5)
        checkmark.next_to(growth_text, RIGHT, buff=0.3)
        self.play(Write(checkmark))
        self.wait(2)

        # Narration text
        narration = Text("We have successfully generated the second orbit word.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)

        self.play(FadeOut(narration))

        narration2 = Text("Notice that every rewrite strictly increases the length,", font_size=24)
        narration2.to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(1.5)

        self.play(FadeOut(narration2))

        narration3 = Text("ensuring the orbit word grows indefinitely.", font_size=24)
        narration3.to_edge(DOWN)
        self.play(Write(narration3))
        self.wait(2)

        self.play(FadeOut(title, final_word, length_text, arrow, growth_text, checkmark, narration3))
