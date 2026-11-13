from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Solution: Parity Bits", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial slots
        slots = VGroup(
            Rectangle(width=1, height=1).set_stroke(WHITE),
            Rectangle(width=1, height=1).set_stroke(WHITE),
            Rectangle(width=1, height=1).set_stroke(WHITE),
            Rectangle(width=1, height=1).set_stroke(WHITE)
        ).arrange(RIGHT, buff=0.2)
        
        labels = VGroup(
            Text("P1", font_size=24),
            Text("D1", font_size=24),
            Text("P2", font_size=24),
            Text("D2", font_size=24)
        ).arrange(RIGHT, buff=0.2).next_to(slots, DOWN, buff=0.2)

        self.play(Create(slots), Write(labels))
        self.wait(0.5)

        # Fill data bits
        d1 = Text("1", font_size=24).move_to(slots[1])
        d2 = Text("0", font_size=24).move_to(slots[3])
        self.play(Write(d1), Write(d2))
        self.wait(0.5)

        # Calculate parity bits
        p1 = Text("0", font_size=24).move_to(slots[0])
        p2 = Text("1", font_size=24).move_to(slots[2])
        self.play(Write(p1), Write(p2))
        self.wait(0.5)

        # Codeword
        codeword = Text("0101", font_size=30).next_to(slots, DOWN, buff=1)
        self.play(Write(codeword))
        self.wait(1)

        # Hamming(7,4) structure
        self.play(FadeOut(title), FadeOut(slots), FadeOut(labels), FadeOut(d1), FadeOut(d2), FadeOut(p1), FadeOut(p2), FadeOut(codeword))

        # Positions 1,2,4 with binary overlay
        positions = [1, 2, 4]
        pos_labels = VGroup(*[Text(str(pos), font_size=24) for pos in positions]).arrange(DOWN, buff=0.5).to_edge(LEFT)
        bin_labels = VGroup(*[Text(f"2^{i}", font_size=24) for i in range(3)]).arrange(DOWN, buff=0.5).next_to(pos_labels, RIGHT, buff=1)

        self.play(Write(pos_labels), Write(bin_labels))
        self.wait(1)

        # Show binary weights
        self.play(Indicate(pos_labels[0]), Indicate(bin_labels[0]))
        self.wait(0.5)
        self.play(Indicate(pos_labels[1]), Indicate(bin_labels[1]))
        self.wait(0.5)
        self.play(Indicate(pos_labels[2]), Indicate(bin_labels[2]))
        self.wait(1)

        # Hamming distance example
        self.play(FadeOut(pos_labels), FadeOut(bin_labels))

        codeword1 = "1010101"
        codeword2 = "1010111"

        c1 = Text(codeword1, font_size=24).to_edge(UP)
        c2 = Text(codeword2, font_size=24).next_to(c1, DOWN, buff=0.5)

        self.play(Write(c1), Write(c2))
        self.wait(1)

        # Show difference
        diff = VMobject()
        for i in range(len(codeword1)):
            if codeword1[i] != codeword2[i]:
                diff.add(Line(
                    start=c1[i].get_center() + UP * 0.2,
                    end=c2[i].get_center() + DOWN * 0.2,
                    color=RED
                ))
        diff.shift(0.41 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(diff))
        self.wait(1)

        # Show distance = 3
        dist_text = Text("Hamming Distance = 3", font_size=24).next_to(c2, DOWN, buff=0.5)
        self.play(Write(dist_text))
        self.wait(1)

        # Overhead ratio
        self.play(FadeOut(c1), FadeOut(c2), FadeOut(diff), FadeOut(dist_text))

        overhead = MathTex(r"\frac{3}{7}", font_size=40).to_edge(UP)
        self.play(Write(overhead))
        self.wait(1)

        # Formula
        formula = MathTex(r"2^r \geq k + r + 1", font_size=30).next_to(overhead, DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(1)

        # Show for k=4
        calc = MathTex(r"2^3 = 8 \geq 4 + 3 + 1 = 8", font_size=24).next_to(formula, DOWN, buff=0.5)
        self.play(Write(calc))
        self.wait(1)

        # Total length
        total_len = MathTex(r"n = k + r = 4 + 3 = 7", font_size=24).next_to(calc, DOWN, buff=0.5)
        self.play(Write(total_len))
        self.wait(1)

        self.play(FadeOut(overhead), FadeOut(formula), FadeOut(calc), FadeOut(total_len))
        self.wait(0.5)
