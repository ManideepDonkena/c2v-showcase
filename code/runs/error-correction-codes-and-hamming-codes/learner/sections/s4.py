from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Correction: Flipping Back", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Original binary string with highlighted bit
        binary_string = "0011"
        bits = [Text(bit, font_size=40) for bit in binary_string]
        bits_group = VGroup(*bits).arrange(RIGHT, buff=0.3)
        bits_group.move_to(ORIGIN)

        # Position labels
        positions = [Text(str(i), font_size=24) for i in range(1, 5)]
        pos_group = VGroup(*positions).arrange(RIGHT, buff=0.3)
        pos_group.next_to(bits_group, DOWN, buff=0.2)

        # Highlight position 5 (which is actually position 4 in 0-indexed)
        highlight = Rectangle(width=0.4, height=0.7, color=RED, fill_opacity=0.3)
        highlight.move_to(bits_group[3])  # Position 4 (0-indexed)

        # Label for position 5
        pos_label = Text("5", font_size=24)
        pos_label.next_to(bits_group[3], DOWN, buff=0.1)

        self.play(Write(bits_group), Write(pos_group))
        self.wait(0.5)
        self.play(Create(highlight), Write(pos_label))
        self.wait(1)

        # Flip the bit from 0 to 1
        arrow = Arrow(start=bits_group[3].get_bottom(), end=bits_group[3].get_top(), 
                      color=YELLOW, buff=0.1)
        self.play(GrowArrow(arrow))
        self.wait(0.5)

        # Change the bit
        self.play(Transform(bits_group[3], Text("1", font_size=40).move_to(bits_group[3])))
        self.wait(1)

        # Show corrected message
        corrected = Text("CORRECTED", font_size=60, color=GREEN)
        corrected.move_to(ORIGIN)
        self.play(FadeIn(corrected))
        self.wait(2)

        # Narration text
        narration1 = Text("Hamming codes can detect and correct single-bit errors.", font_size=24)
        narration1.to_edge(DOWN)
        self.play(Write(narration1))
        self.wait(2)
        self.play(FadeOut(narration1))

        narration2 = Text("In this case, we flipped the erroneous bit back to its correct value.", font_size=24)
        narration2.to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(2)
        self.play(FadeOut(narration2))

        narration3 = Text("This is the power of Hamming codes: detecting and correcting single-bit errors automatically.", font_size=24)
        narration3.to_edge(DOWN)
        self.play(Write(narration3))
        self.wait(2)
        self.play(FadeOut(narration3), FadeOut(corrected), FadeOut(arrow), 
                  FadeOut(highlight), FadeOut(pos_label), FadeOut(title))
