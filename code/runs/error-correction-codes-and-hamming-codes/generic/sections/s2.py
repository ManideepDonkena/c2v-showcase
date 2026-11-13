from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Solution: Parity Bits", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Bit positions
        positions = [1, 2, 3, 4, 5, 6]
        bit_labels = ["P1", "D1", "P2", "D2", "P4", "D3"]
        bits = VGroup()
        for i, (pos, label) in enumerate(zip(positions, bit_labels)):
            bit = Rectangle(width=0.8, height=0.8)
            bit.move_to(LEFT * 2.5 + RIGHT * pos * 0.6)
            label_obj = Text(label, font_size=24)
            label_obj.next_to(bit, DOWN, buff=0.1)
            bits.add(VGroup(bit, label_obj))
        
        self.play(*[Write(bit) for bit in bits])
        self.wait(1)

        # Highlight coverage
        p1_cover = [1, 3, 5]
        p2_cover = [2, 3, 6]
        p4_cover = [4, 5, 6]
        
        # P1 coverage
        p1_highlight = VGroup()
        for pos in p1_cover:
            bit = bits[pos-1][0]
            highlight = bit.copy().set_fill(GREEN, opacity=0.5)
            p1_highlight.add(highlight)
        self.play(AnimationGroup(*[FadeIn(h) for h in p1_highlight], run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(p1_highlight))

        # P2 coverage
        p2_highlight = VGroup()
        for pos in p2_cover:
            bit = bits[pos-1][0]
            highlight = bit.copy().set_fill(GREEN, opacity=0.5)
            p2_highlight.add(highlight)
        self.play(AnimationGroup(*[FadeIn(h) for h in p2_highlight], run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(p2_highlight))

        # P4 coverage
        p4_highlight = VGroup()
        for pos in p4_cover:
            bit = bits[pos-1][0]
            highlight = bit.copy().set_fill(GREEN, opacity=0.5)
            p4_highlight.add(highlight)
        self.play(AnimationGroup(*[FadeIn(h) for h in p4_highlight], run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(p4_highlight))

        # Explanation text
        explanation = Text("Parity bits check groups of data", font_size=24)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(1)

        # Fade out
        self.play(FadeOut(title, bits, explanation))
        self.wait(0.5)
