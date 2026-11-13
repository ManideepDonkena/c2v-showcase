from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Mechanism: Syndrome Calculation", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Venn Diagram for Hamming Code (P1, P2, P4 over D1-D4)
        p1_circle = Circle(radius=1.2, color=GREEN, fill_opacity=0.3).shift(LEFT * 1.5 + UP * 0.5)
        p2_circle = Circle(radius=1.2, color=GREEN, fill_opacity=0.3).shift(RIGHT * 1.5 + UP * 0.5)
        p4_circle = Circle(radius=1.2, color=GREEN, fill_opacity=0.3).shift(UP * -1.5)
        p1_label = Text("P1", font_size=24).next_to(p1_circle, UP)
        p2_label = Text("P2", font_size=24).next_to(p2_circle, UP)
        p4_label = Text("P4", font_size=24).next_to(p4_circle, DOWN)

        d1 = Text("D1", font_size=20).next_to(p1_circle, LEFT)
        d2 = Text("D2", font_size=20).next_to(p2_circle, LEFT)
        d3 = Text("D3", font_size=20).next_to(p4_circle, RIGHT)
        d4 = Text("D4", font_size=20).next_to(p1_circle, RIGHT).shift(RIGHT * 0.39)  # Adjusted to avoid overlap

        self.play(Create(p1_circle), Create(p2_circle), Create(p4_circle))
        self.play(Write(p1_label), Write(p2_label), Write(p4_label))
        self.play(Write(d1), Write(d2), Write(d3), Write(d4))
        self.wait(1)

        # Simulate error in D2
        d2_error = d2.copy().set_color(RED)
        self.play(Transform(d2, d2_error))
        p1_circle.set_color(RED)
        p4_circle.set_color(RED)
        p2_circle.set_color(GREEN)
        self.wait(1)

        # Show syndrome '101'
        syndrome = MathTex("101", font_size=36).to_edge(DOWN)
        self.play(Write(syndrome))
        self.wait(1)

        # Show mapping: P4=4, P2=2, P1=1
        mapping = MathTex("P4 = 4, \quad P2 = 2, \quad P1 = 1", font_size=24).to_edge(DOWN).shift(UP * 0.5)
        self.play(Transform(syndrome, mapping))
        self.wait(1)

        # Show syndrome calculation: 0*4 + 1*2 + 1*1 = 3
        calc = MathTex("0 \\cdot 4 + 1 \\cdot 2 + 1 \\cdot 1 = 3", font_size=24).to_edge(DOWN).shift(UP * 1)
        self.play(Transform(syndrome, calc))
        self.wait(1.5)

        # Show two valid codewords with distance 3
        codeword1 = MathTex("000", font_size=30).shift(LEFT * 3 + UP * 1)
        codeword2 = MathTex("111", font_size=30).shift(RIGHT * 3 + UP * 1)
        self.play(Write(codeword1), Write(codeword2))
        self.wait(1)

        # Show distance explanation
        dist_text = Text("Distance = 3", font_size=24).next_to(codeword1, DOWN).shift(LEFT * 0.79 + UP * 0.36)  # Adjusted to avoid overlap
        self.play(Write(dist_text))
        self.wait(1.5)

        # Show two simultaneous bit flips (D1 and D2) leading to a wrong syndrome
        d1_flip = d1.copy().set_color(YELLOW)
        d2_flip = d2.copy().set_color(YELLOW)
        self.play(Transform(d1, d1_flip), Transform(d2, d2_flip))
        p1_circle.set_color(GREEN)
        p2_circle.set_color(GREEN)
        p4_circle.set_color(RED)
        self.wait(1)

        # Show syndrome '010' (points to D3) - ambiguous
        ambiguous_syndrome = MathTex("010", font_size=36).to_edge(DOWN)
        self.play(Transform(syndrome, ambiguous_syndrome))
        self.wait(1.5)

        # Show single parity flip (P2 flipped)
        p2_circle.set_color(RED)
        self.wait(1)

        # Show syndrome '010' again
        self.play(Transform(syndrome, MathTex("010", font_size=36).to_edge(DOWN)))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(p1_circle), FadeOut(p2_circle), FadeOut(p4_circle),
                  FadeOut(p1_label), FadeOut(p2_label), FadeOut(p4_label),
                  FadeOut(d1), FadeOut(d2), FadeOut(d3), FadeOut(d4),
                  FadeOut(syndrome), FadeOut(dist_text), FadeOut(codeword1), FadeOut(codeword2))
        self.wait(0.5)
