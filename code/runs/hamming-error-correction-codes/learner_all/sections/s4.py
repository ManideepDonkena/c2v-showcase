from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Correction and Recovery", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show bit flip correction
        original = "101"
        corrected = "101"
        codeword = Text(f"Original: {original}", font_size=24).to_corner(UL)
        self.play(Write(codeword))
        self.wait(0.5)

        # Highlight bit at index 2 (0-based)
        highlight = Rectangle(width=0.3, height=0.6, color=YELLOW).move_to(codeword[1].get_center())
        highlight.shift(-0.61 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(highlight))
        self.wait(0.5)

        # Flip the bit from 0 to 1
        self.play(Transform(codeword[1], Text("1", font_size=24).move_to(codeword[1].get_center())))
        self.wait(0.5)

        # Show green checkmark
        check = Tex(r"$\checkmark$").set_color(GREEN).scale(1.5).next_to(codeword, RIGHT)
        self.play(Write(check))
        self.wait(1)

        # Show limitation: two bit flips
        self.play(FadeOut(highlight), FadeOut(check), FadeOut(codeword))
        two_flip = Text("Two simultaneous flips:", font_size=24).to_corner(UL)
        self.play(Write(two_flip))
        self.wait(0.5)

        # Show codewords differing by 1 bit
        word1 = "1010"
        word2 = "1000"
        diff = Text(f"Word 1: {word1} vs Word 2: {word2}", font_size=24).next_to(two_flip, DOWN)
        self.play(Write(diff))
        self.wait(1)

        # Show codewords differing by 3 bits
        word3 = "1010"
        word4 = "0101"
        diff3 = Text(f"Word 3: {word3} vs Word 4: {word4}", font_size=24).next_to(diff, DOWN)
        self.play(Write(diff3))
        self.wait(1)

        # Show Hamming(7,4) structure
        self.play(FadeOut(two_flip), FadeOut(diff), FadeOut(diff3))
        hamming = Text("Hamming(7,4): 4 data bits + 3 parity bits", font_size=24).to_corner(UL)
        self.play(Write(hamming))
        self.wait(0.5)

        # Positions
        positions = [1, 2, 3, 4, 5, 6, 7]
        pos_labels = [Text(str(i), font_size=20) for i in positions]
        for i, label in enumerate(pos_labels):
            label.move_to(LEFT * 3 + DOWN * (i - 3))
        self.play(*[Write(label) for label in pos_labels])
        self.wait(0.5)

        # Parity bits at powers of two
        parity_positions = [1, 2, 4]
        parity_labels = [Text(f"P{i}", font_size=20).set_color(BLUE) for i in parity_positions]
        for i, label in enumerate(parity_labels):
            label.move_to(LEFT * 3 + DOWN * (parity_positions[i] - 4))
        self.play(*[Write(label) for label in parity_labels])
        self.wait(1)

        # Show binary weights
        self.play(FadeOut(hamming), *[FadeOut(label) for label in pos_labels + parity_labels])
        binary_weights = Text("Binary weights: 1, 2, 4", font_size=24).to_corner(UL)
        self.play(Write(binary_weights))
        self.wait(0.5)

        # Show rule
        rule = MathTex(r"2^r \geq k + r + 1").scale(1.2).next_to(binary_weights, DOWN)
        self.play(Write(rule))
        self.wait(0.5)

        # Show calculation for k=4
        calc = MathTex(r"2^3 = 8 \geq 4 + 3 + 1 = 8").scale(1.2).next_to(rule, DOWN)
        calc.shift(0.85 * RIGHT)  # layout: shift to frame
        self.play(Write(calc))
        self.wait(0.5)

        # Total length n = k + r
        total_length = MathTex(r"n = k + r = 4 + 3 = 7").scale(1.2).next_to(calc, DOWN)
        total_length.shift(0.77 * RIGHT)  # layout: shift to frame
        self.play(Write(total_length))
        self.wait(0.5)

        # Show overhead ratio
        self.play(FadeOut(binary_weights), FadeOut(rule), FadeOut(calc), FadeOut(total_length))
        overhead = MathTex(r"\frac{3}{7} \approx 42.86\%").scale(1.2).to_corner(UL)
        self.play(Write(overhead))
        self.wait(0.5)

        # Show syndrome mapping
        self.play(FadeOut(overhead))
        syndrome = Text("Syndrome maps to bit position:", font_size=24).to_corner(UL)
        syndrome.shift(0.0 * RIGHT + 0.48 * UP)  # layout: separation vector
        self.play(Write(syndrome))
        self.wait(0.5)

        # Visual mapping of syndrome bits
        s1, s2, s3 = 1, 0, 1
        syndrome_bits = Text(f"Syndrome: {s3}{s2}{s1}", font_size=24).next_to(syndrome, DOWN)
        self.play(Write(syndrome_bits))
        self.wait(0.5)

        # Show sum of positions
        sum_pos = MathTex(r"4 + 1 = 5").scale(1.2).next_to(syndrome_bits, DOWN)
        self.play(Write(sum_pos))
        self.wait(1)

        # Show two-bit error corrupting data
        self.play(FadeOut(syndrome), FadeOut(syndrome_bits), FadeOut(sum_pos))
        error = Text("Two-bit flip corrupts data:", font_size=24).to_corner(UL)
        error.shift(0.0 * RIGHT + 0.49 * UP)  # layout: separation vector
        self.play(Write(error))
        self.wait(0.5)

        # Show syndrome pointing to invalid bit
        invalid_syndrome = MathTex(r"Syndrome = 3 \Rightarrow \text{Invalid correction}").scale(1.2).next_to(error, DOWN)
        invalid_syndrome.shift(2.25 * RIGHT)  # layout: shift to frame
        self.play(Write(invalid_syndrome))
        self.wait(1)

        # Final summary
        self.play(FadeOut(error), FadeOut(invalid_syndrome))
        final = Text("Hamming codes correct single-bit errors only.", font_size=24).to_corner(UL)
        final.shift(0.0 * RIGHT + 0.48 * UP)  # layout: separation vector
        self.play(Write(final))
        self.wait(0.5)

        self.play(FadeOut(final), FadeOut(title))
