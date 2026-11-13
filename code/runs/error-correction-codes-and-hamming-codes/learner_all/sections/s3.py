from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Mechanism: Syndrome Calculation", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid with bit positions
        grid = VGroup()
        for i in range(4):
            row = VGroup()
            for j in range(4):
                cell = Square(side_length=0.5, color=WHITE, fill_opacity=0)
                cell.move_to(np.array([j - 1.5, 1.5 - i, 0]))
                label = MathTex(str(i*4 + j + 1), font_size=20).move_to(cell.get_center())
                row.add(VGroup(cell, label))
            grid.add(row)
        grid.arrange_in_grid(rows=4, cols=4, buff=0.05)
        self.play(Write(grid))
        self.wait(0.5)

        # Highlight positions 1, 2, 4, 8
        pos_labels = [MathTex("1", font_size=24), MathTex("2", font_size=24), MathTex("4", font_size=24), MathTex("8", font_size=24)]
        for i, label in enumerate(pos_labels):
            label.move_to(grid[i][0].get_center())
            self.play(Write(label))
        self.wait(0.5)

        # Venn diagram of parity circles
        p1_circle = Circle(radius=1.2, color=GREEN, fill_opacity=0.2).move_to(np.array([-1, 0, 0]))
        p2_circle = Circle(radius=1.2, color=GREEN, fill_opacity=0.2).move_to(np.array([0, 1, 0]))
        p4_circle = Circle(radius=1.2, color=GREEN, fill_opacity=0.2).move_to(np.array([1, 0, 0]))

        p1_label = MathTex("P1", font_size=24).next_to(p1_circle, DOWN)
        p2_label = MathTex("P2", font_size=24).next_to(p2_circle, UP)
        p4_label = MathTex("P4", font_size=24).next_to(p4_circle, DOWN)

        self.play(Create(p1_circle), Create(p2_circle), Create(p4_circle))
        self.play(Write(p1_label), Write(p2_label), Write(p4_label))
        self.wait(0.5)

        # Data bits
        d1 = MathTex("D1", font_size=24).move_to(np.array([-1, 1, 0]))
        d2 = MathTex("D2", font_size=24).move_to(np.array([0, 0, 0]))
        d3 = MathTex("D3", font_size=24).move_to(np.array([1, 1, 0]))

        self.play(Write(d1), Write(d2), Write(d3))
        self.wait(0.5)

        # Simulate error in D2
        d2_copy = d2.copy()
        self.play(d2_copy.animate.set_color(RED))
        self.wait(0.5)

        # Show P1 and P4 fail, P2 passes
        p1_circle.set_color(RED)
        p4_circle.set_color(RED)
        p2_circle.set_color(GREEN)

        self.play(p1_circle.animate.set_fill(opacity=0.3), p4_circle.animate.set_fill(opacity=0.3))
        self.wait(0.5)

        # Show syndrome '101'
        syndrome = MathTex("101", font_size=32).to_edge(DOWN)
        self.play(Write(syndrome))
        self.wait(0.5)

        # Show mapping: P4=4, P2=2, P1=1
        mapping = VGroup(
            MathTex("P4 = 4", font_size=24),
            MathTex("P2 = 2", font_size=24),
            MathTex("P1 = 1", font_size=24)
        ).arrange(DOWN, buff=0.3).to_edge(LEFT)
        self.play(Write(mapping))
        self.wait(0.5)

        # Show syndrome calculation
        calc = MathTex("0 \\cdot 4 + 1 \\cdot 2 + 1 \\cdot 1 = 3", font_size=24).move_to(np.array([0, -2, 0]))
        self.play(Write(calc))
        self.wait(0.5)

        # Fade out all
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(p1_circle),
            FadeOut(p2_circle),
            FadeOut(p4_circle),
            FadeOut(p1_label),
            FadeOut(p2_label),
            FadeOut(p4_label),
            FadeOut(d1),
            FadeOut(d2),
            FadeOut(d3),
            FadeOut(syndrome),
            FadeOut(mapping),
            FadeOut(calc)
        )
        self.wait(0.5)

        # Show two codewords
        c1 = MathTex("000", font_size=32).to_edge(UP)
        c2 = MathTex("111", font_size=32).next_to(c1, DOWN, buff=0.5)
        self.play(Write(c1), Write(c2))
        self.wait(0.5)

        # Show distance of 3
        dist = MathTex("\\text{Distance} = 3", font_size=24).next_to(c2, RIGHT)
        self.play(Write(dist))
        self.wait(0.5)

        # Fade out
        self.play(
            FadeOut(c1),
            FadeOut(c2),
            FadeOut(dist)
        )
        self.wait(0.5)

        # Show two simultaneous flips
        flip1 = MathTex("D1 \\leftrightarrow D2", font_size=24).to_edge(DOWN)
        self.play(Write(flip1))
        self.wait(0.5)

        # Show ambiguous syndrome
        amb_syndrome = MathTex("Syndrome = 000", font_size=24).next_to(flip1, UP)
        self.play(Write(amb_syndrome))
        self.wait(0.5)

        # Fade out
        self.play(
            FadeOut(flip1),
            FadeOut(amb_syndrome)
        )
        self.wait(0.5)

        # Show parity bit flip
        p2_flip = MathTex("P2 \\leftrightarrow D3", font_size=24).to_edge(DOWN)
        self.play(Write(p2_flip))
        self.wait(0.5)

        # Show correct syndrome
        correct_syndrome = MathTex("Syndrome = 010", font_size=24).next_to(p2_flip, UP)
        self.play(Write(correct_syndrome))
        self.wait(0.5)

        # Fade out
        self.play(
            FadeOut(p2_flip),
            FadeOut(correct_syndrome)
        )
        self.wait(0.5)

        # Final message
        final = Text("Hamming codes detect and correct single-bit errors", font_size=24).to_edge(DOWN)
        self.play(Write(final))
        self.wait(1.5)

        self.play(FadeOut(final))
