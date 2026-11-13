from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Detecting the Error", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Codeword with error
        codeword = "0101"
        bits = [Text(b, font_size=24) for b in codeword]
        bits_group = VGroup(*bits).arrange(RIGHT, buff=0.3).move_to(ORIGIN)
        self.play(Write(bits_group))
        self.wait(0.5)

        # Flip middle bit
        error_bit = bits[1].copy()
        self.play(Transform(error_bit, Text("1", font_size=24).set_color(RED)), run_time=0.5)
        self.wait(0.5)

        # Parity checks
        parity_checks = [Text("1", font_size=24), Text("0", font_size=24), Text("1", font_size=24)]
        parity_group = VGroup(*parity_checks).arrange(RIGHT, buff=0.5).next_to(bits_group, DOWN, buff=0.5)
        self.play(Write(parity_group))
        self.wait(0.5)

        # Syndrome
        syndrome = Text("Syndrome: 101", font_size=24).next_to(parity_group, DOWN, buff=0.5)
        self.play(Write(syndrome))
        self.wait(0.5)

        # Syndrome to position mapping
        pos_text = Text("Position 2 (binary 10)", font_size=24).next_to(syndrome, DOWN, buff=0.5)
        self.play(Write(pos_text))
        self.wait(0.5)

        # Show Hamming(7,4) structure
        self.play(FadeOut(title, bits_group, parity_group, syndrome, pos_text))

        # Positions and parity bits
        positions = [Text(str(i), font_size=24) for i in range(1, 8)]
        positions_group = VGroup(*positions).arrange(RIGHT, buff=0.3).move_to(ORIGIN)
        self.play(Write(positions_group))
        self.wait(0.5)

        # Parity bit labels
        p1 = Text("P1", font_size=24).move_to(positions[0].get_center())
        p2 = Text("P2", font_size=24).move_to(positions[1].get_center())
        p4 = Text("P4", font_size=24).move_to(positions[3].get_center())
        p4.shift(0.37 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(p1), Write(p2), Write(p4))
        self.wait(0.5)
        # Binary weights overlay
        binary_weights = [Text("1", font_size=24), Text("2", font_size=24), Text("4", font_size=24)]
        weights_group = VGroup(*binary_weights).arrange(RIGHT, buff=0.3).next_to(positions_group, DOWN, buff=0.5)
        self.play(Write(weights_group))
        self.wait(0.5)

        # Formula
        formula = MathTex("2^r \\ge m + r + 1", font_size=30).next_to(weights_group, DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(0.5)

        # Show k=4, r=3
        calc = MathTex("2^3 = 8 \\ge 4 + 3 + 1 = 8", font_size=24).next_to(formula, DOWN, buff=0.5)
        self.play(Write(calc))
        self.wait(0.5)

        # Total length
        total_length = MathTex("n = k + r = 4 + 3 = 7", font_size=24).next_to(calc, DOWN, buff=0.5)
        self.play(Write(total_length))
        self.wait(0.5)

        # Hamming distance example
        self.play(FadeOut(positions_group, p1, p2, p4, weights_group, formula, calc, total_length))

        codeword1 = "1011001"
        codeword2 = "1011010"
        c1 = [Text(b, font_size=24) for b in codeword1]
        c2 = [Text(b, font_size=24) for b in codeword2]
        c1_group = VGroup(*c1).arrange(RIGHT, buff=0.3).move_to(ORIGIN)
        c2_group = VGroup(*c2).arrange(RIGHT, buff=0.3).next_to(c1_group, DOWN, buff=0.5)

        self.play(Write(c1_group), Write(c2_group))
        self.wait(0.5)

        # Distance 3
        dist_text = Text("Hamming distance = 3", font_size=24).next_to(c2_group, DOWN, buff=0.5)
        self.play(Write(dist_text))
        self.wait(0.5)

        # Single flip
        self.play(FadeOut(c1_group, c2_group, dist_text))

        # Show two bits flipping
        codeword_orig = "1011001"
        flipped = [Text(b, font_size=24) for b in codeword_orig]
        flipped_group = VGroup(*flipped).arrange(RIGHT, buff=0.3).move_to(ORIGIN)
        self.play(Write(flipped_group))
        self.wait(0.5)

        # Flip bits 1 and 2
        self.play(Transform(flipped[0], Text("0", font_size=24).set_color(RED)),
                  Transform(flipped[1], Text("1", font_size=24).set_color(RED)))
        self.wait(0.5)

        # Syndrome points to invalid position or zero
        bad_syndrome = Text("Syndrome: 011 (position 3)", font_size=24).next_to(flipped_group, DOWN, buff=0.5)
        self.play(Write(bad_syndrome))
        self.wait(0.5)

        # Final cleanup
        self.play(FadeOut(flipped_group, bad_syndrome))
        self.wait(0.5)
