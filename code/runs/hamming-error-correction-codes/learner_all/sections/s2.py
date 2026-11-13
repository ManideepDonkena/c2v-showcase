from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Solution: Parity Bits", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial slots
        slots = VGroup(*[Rectangle(width=0.8, height=1).set_stroke(WHITE) for _ in range(4)])
        slots.arrange(RIGHT, buff=0.2)
        labels = VGroup(
            Text("P1", font_size=24),
            Text("D1", font_size=24),
            Text("P2", font_size=24),
            Text("D2", font_size=24)
        )
        for i, (slot, label) in enumerate(zip(slots, labels)):
            label.next_to(slot, UP)
            slot.shift(DOWN * 0.5)
            label.shift(DOWN * 0.5)

        self.play(Create(slots), Write(labels))
        self.wait(0.5)

        # Fill data bits
        d1 = Text("1", font_size=24).move_to(slots[1].get_center())
        d2 = Text("0", font_size=24).move_to(slots[3].get_center())
        self.play(Write(d1), Write(d2))
        self.wait(0.5)

        # Calculate parity bits
        p1 = Text("0", font_size=24).move_to(slots[0].get_center())
        p2 = Text("1", font_size=24).move_to(slots[2].get_center())
        self.play(Write(p1), Write(p2))
        self.wait(0.5)

        # Codeword
        codeword = "0101"
        cw_text = Text(codeword, font_size=30).next_to(slots, DOWN)
        self.play(Write(cw_text))
        self.wait(1)

        # Narration text
        narration = Text("Hamming codes insert parity bits at powers of two.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        # Show bit flip example
        error_codeword = "101"
        error_text = Text("Error: " + error_codeword, font_size=24).to_edge(DOWN)
        self.play(Write(error_text))
        self.wait(1.5)
        self.play(FadeOut(error_text))

        # Hamming(7,4) structure
        self.play(FadeOut(slots), FadeOut(labels), FadeOut(d1), FadeOut(d2), FadeOut(p1), FadeOut(p2), FadeOut(cw_text))
        self.wait(0.5)

        # Positions 1,2,4 for P1,P2,P4
        positions = [1, 2, 4]
        parity_positions = VGroup(*[Text(f"P{p}", font_size=24) for p in positions])
        parity_positions.arrange(RIGHT, buff=0.5)
        parity_positions.to_edge(UP)

        data_positions = [3, 5, 6, 7]
        data_positions_text = VGroup(*[Text(f"D{i}", font_size=24) for i in data_positions])
        data_positions_text.arrange(RIGHT, buff=0.5)
        data_positions_text.next_to(parity_positions, DOWN)

        parity_positions.shift(0.0 * RIGHT + 0.39 * UP)  # layout: separation vector
        self.play(Write(parity_positions), Write(data_positions_text))
        self.wait(1)

        # Formula
        formula = MathTex("2^r \\ge m + r + 1", font_size=30).next_to(parity_positions, DOWN)
        self.play(Write(formula))
        self.wait(1.5)
        self.play(FadeOut(formula))

        # Binary overlay
        binary_labels = VGroup(
            Text("1", font_size=24),
            Text("2", font_size=24),
            Text("4", font_size=24),
            Text("8", font_size=24)
        )
        binary_labels.arrange(RIGHT, buff=0.5)
        binary_labels.next_to(parity_positions, DOWN, buff=1)

        self.play(Write(binary_labels))
        self.wait(1.5)
        self.play(FadeOut(binary_labels))

        # Overhead ratio
        overhead = MathTex("\\frac{3}{7}", font_size=30).next_to(data_positions_text, DOWN)
        self.play(Write(overhead))
        self.wait(1.5)
        self.play(FadeOut(overhead))

        # Rule for r
        rule = MathTex("2^r \\ge k + r + 1", font_size=30).to_edge(DOWN)
        self.play(Write(rule))
        self.wait(1.5)
        self.play(FadeOut(rule))

        # Distance example
        word1 = "1010101"
        word2 = "1010111"
        w1 = Text(word1, font_size=24).to_edge(UP)
        w2 = Text(word2, font_size=24).next_to(w1, DOWN)
        self.play(Write(w1), Write(w2))
        self.wait(1.5)
        self.play(FadeOut(w1), FadeOut(w2))

        # Syndrome mapping
        syndrome = MathTex("101", font_size=30).to_edge(DOWN)
        self.play(Write(syndrome))
        self.wait(1.5)
        self.play(FadeOut(syndrome))

        # Two-bit error
        two_bit_error = Text("Two bits flip at positions 1 and 2.", font_size=24).to_edge(DOWN)
        self.play(Write(two_bit_error))
        self.wait(1.5)
        self.play(FadeOut(two_bit_error))

        self.play(FadeOut(title), FadeOut(parity_positions), FadeOut(data_positions_text))
