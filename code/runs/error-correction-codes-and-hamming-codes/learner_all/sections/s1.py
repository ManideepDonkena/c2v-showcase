from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Problem: Bit Flips", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial binary string
        original = MathTex("1011").scale(1.5).to_edge(LEFT)
        self.play(Write(original))
        self.wait(0.5)
        # Lightning bolt and bit flip
        lightning = always_redraw(lambda: Line(start=original[0][1].get_top(),
            end=original[0][1].get_bottom(),
            color=RED))
        bolt = always_redraw(lambda: Line(
            start=original[0][1].get_top(),
            end=original[0][1].get_bottom(),
            color=RED))
        self.play(Create(bolt))
        self.wait(0.2)
        self.play(Transform(original[0][1], MathTex("0").scale(1.5).move_to(original[0][1])))
        self.play(original.animate.shift(0.1 * UP + 0.1 * DOWN).shift(0.1 * LEFT + 0.1 * RIGHT))
        self.wait(0.5)
        self.play(FadeOut(bolt))

        # Narration text
        narration = Text("Noise causes unexpected bit flips", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        # Parity vs Hamming comparison
        parity_label = Text("Simple Parity", font_size=24).to_corner(UL)
        hamming_label = Text("Hamming Codes", font_size=24).to_corner(UR)
        self.play(Write(parity_label), Write(hamming_label))
        self.wait(0.5)

        parity_fail = Text("Detects odd errors only", font_size=20).next_to(parity_label, DOWN)
        hamming_fix = Text("Detects and corrects 1 error", font_size=20).next_to(hamming_label, DOWN)
        hamming_fix.shift(-0.19 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(parity_fail), Write(hamming_fix))
        self.wait(1.5)

        self.play(FadeOut(parity_label), FadeOut(hamming_label), FadeOut(parity_fail), FadeOut(hamming_fix))

        # Grid with positions
        grid = VGroup()
        for i in range(4):
            row = VGroup()
            for j in range(4):
                cell = Square(side_length=0.5, color=WHITE).move_to(np.array([j - 1.5, 1.5 - i, 0]))
                label = MathTex(str(i * 4 + j + 1)).scale(0.5).move_to(cell.get_center())
                row.add(VGroup(cell, label))
            grid.add(row)

        # Highlight powers of two
        positions = [1, 2, 4, 8]
        labels = []
        for pos in positions:
            i = (pos - 1) // 4
            j = (pos - 1) % 4
            cell = grid[i][j]
            label = MathTex(str(pos)).scale(0.6).move_to(cell.get_center())
            labels.append(label)
            self.play(Indicate(cell), Write(label))
            self.wait(0.3)

        # Show parity bits vs data bits
        self.play(FadeOut(*labels))
        parity_bits = [1, 2, 4]
        data_bits = [3, 5, 6, 7]

        p_labels = []
        d_labels = []

        for i in range(4):
            for j in range(4):
                pos = i * 4 + j + 1
                if pos in parity_bits:
                    cell = grid[i][j]
                    label = MathTex("P").scale(0.6).move_to(cell.get_center())
                    p_labels.append(label)
                    label.shift(0.31 * RIGHT + 0.0 * UP)  # layout: separation vector
                    self.play(Write(label))
                elif pos in data_bits:
                    cell = grid[i][j]
                    label = MathTex("D").scale(0.6).move_to(cell.get_center())
                    d_labels.append(label)
                    self.play(Write(label))
            self.wait(0.2)

        # Show guardians
        self.play(FadeOut(*p_labels), FadeOut(*d_labels))

        # Guardian circles (Venn diagram style)
        c1 = Circle(radius=1.5, color=GREEN).move_to(np.array([0, 0, 0]))
        c2 = Circle(radius=1.5, color=GREEN).move_to(np.array([1.5, 0, 0]))
        c4 = Circle(radius=1.5, color=GREEN).move_to(np.array([0, -1.5, 0]))

        c1.shift(0.2 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(c1), Create(c2), Create(c4))
        self.wait(0.5)

        # Show syndrome mapping
        syndrome = MathTex("S = 011").scale(1.2).to_edge(DOWN)
        self.play(Write(syndrome))
        self.wait(1.0)

        # Show error at position 3 (binary: 011)
        pos3 = Square(side_length=0.5, color=RED).move_to(np.array([0, -1.5, 0]))
        self.play(Write(pos3))
        self.wait(0.5)

        # Show single parity bit flip
        p2_flip = Circle(radius=1.5, color=RED).move_to(np.array([1.5, 0, 0]))
        self.play(Transform(c2, p2_flip))
        self.wait(0.5)

        # Final summary
        final_text = Text("Hamming codes detect and correct single errors", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(original), FadeOut(grid), FadeOut(c1), FadeOut(c2), FadeOut(c4),
                  FadeOut(syndrome), FadeOut(pos3), FadeOut(final_text))
