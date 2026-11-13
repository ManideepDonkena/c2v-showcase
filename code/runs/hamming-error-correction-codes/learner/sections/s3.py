from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Detecting the Error", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Codeword: 0101
        codeword = MathTex("0101").scale(1.5).to_edge(LEFT).shift(UP * 1.5)
        self.play(Write(codeword))
        self.wait(0.5)

        # Show error at position 2 (middle bit flips)
        error_pos = 2
        error_dot = Dot().move_to(codeword[0][error_pos].get_center()).set_color(RED)
        error_dot.shift(0.0 * RIGHT + 0.49 * UP)  # layout: separation vector
        self.play(FadeIn(error_dot))
        self.wait(0.5)

        # Parity check groups
        parity_groups = VGroup(
            MathTex("P_1 = 0 \oplus 1 \oplus 1 = 0"),
            MathTex("P_2 = 1 \oplus 0 \oplus 1 = 0"),
            MathTex("P_3 = 0 \oplus 1 \oplus 0 = 1")
        ).arrange(DOWN, buff=0.4).scale(0.8).to_edge(RIGHT).shift(UP * 0.5)

        self.play(Write(parity_groups[0]))
        self.wait(0.5)
        self.play(Write(parity_groups[1]))
        self.wait(0.5)
        self.play(Write(parity_groups[2]))
        self.wait(0.5)

        # Syndrome
        syndrome = MathTex("S = 101").scale(1.5).next_to(codeword, DOWN, buff=0.8)
        syndrome.shift(0.21 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(syndrome))
        self.wait(0.5)

        # Show mapping of syndrome to bit position
        mapping = VGroup(
            MathTex("S_1 = 1 \Rightarrow \text{position } 1"),
            MathTex("S_2 = 0 \Rightarrow \text{position } 2"),
            MathTex("S_3 = 1 \Rightarrow \text{position } 4")
        ).arrange(DOWN, buff=0.4).scale(0.7).to_edge(RIGHT).shift(DOWN * 1.5)

        self.play(Write(mapping[0]))
        self.wait(0.5)
        self.play(Write(mapping[1]))
        self.wait(0.5)
        self.play(Write(mapping[2]))
        self.wait(0.5)

        # Sum to get position
        sum_text = MathTex("1 + 4 = 5").scale(0.8).next_to(mapping, DOWN, buff=0.3)
        self.play(Write(sum_text))
        self.wait(0.5)

        # Show two bits flipping: positions 1 and 2
        self.play(FadeOut(syndrome), FadeOut(mapping), FadeOut(sum_text), FadeOut(parity_groups))

        codeword2 = MathTex("0101").scale(1.5).to_edge(LEFT).shift(UP * 1.5)
        codeword2.shift(0.0 * RIGHT + 0.66 * UP)  # layout: separation vector
        self.play(Write(codeword2))
        self.wait(0.5)

        error_dots = VGroup(
            Dot().move_to(codeword2[0][0].get_center()).set_color(RED),
            Dot().move_to(codeword2[0][1].get_center()).set_color(RED)
        )
        self.play(FadeIn(error_dots))
        self.wait(0.5)

        # New syndrome
        new_syndrome = MathTex("S = 011").scale(1.5).next_to(codeword2, DOWN, buff=0.8)
        self.play(Write(new_syndrome))
        self.wait(0.5)

        # Show that this points to position 3 (non-existent)
        pos_text = MathTex("S = 011 \Rightarrow \text{position } 3").scale(0.8).next_to(new_syndrome, DOWN, buff=0.3)
        self.play(Write(pos_text))
        self.wait(0.5)

        # Show that this corrupts the codeword
        corrupted = MathTex("0001").scale(1.5).next_to(pos_text, DOWN, buff=0.3)
        self.play(Write(corrupted))
        self.wait(0.5)
        # Final explanation
        note = Text("System 'corrects' valid codeword into invalid one", font_size=24).to_edge(DOWN)
        self.play(Write(note))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(codeword), FadeOut(error_dot), FadeOut(parity_groups),
                  FadeOut(syndrome), FadeOut(mapping), FadeOut(sum_text),
                  FadeOut(new_syndrome), FadeOut(pos_text), FadeOut(corrupted), FadeOut(note))
        self.wait(0.5)
