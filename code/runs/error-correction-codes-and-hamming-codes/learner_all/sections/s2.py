from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Solution: Parity Bits", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid positions with labels
        grid_labels = VGroup()
        for i in range(1, 9):
            label = MathTex(str(i), font_size=24).move_to(ORIGIN)
            label.shift((i - 1) * RIGHT * 0.8 + UP * 0.3)
            grid_labels.add(label)

        # Create slots
        slots = VGroup()
        for i in range(1, 9):
            rect = Rectangle(width=0.7, height=0.7, color=WHITE, fill_opacity=0)
            rect.move_to((i - 1) * RIGHT * 0.8)
            slots.add(rect)

        slots.shift(0.0 * RIGHT + -0.28 * UP)  # layout: separation vector
        self.play(Create(slots), Write(grid_labels))
        self.wait(0.5)

        # Label parity positions
        parity_positions = [1, 2, 4]
        for pos in parity_positions:
            label = MathTex("P_" + str(pos), font_size=24).move_to((pos - 1) * RIGHT * 0.8)
            self.play(Write(label))
            self.wait(0.3)

        # Data bits
        data_labels = VGroup()
        for i, pos in enumerate([3, 5, 7]):
            label = MathTex("D_" + str(i+1), font_size=24).move_to((pos - 1) * RIGHT * 0.8)
            data_labels.add(label)
            self.play(Write(label))
            self.wait(0.3)

        # Show parity bits as guardians
        guardian_circles = VGroup()
        for i, pos in enumerate(parity_positions):
            circle = Circle(radius=0.5, color=BLUE, fill_opacity=0.2).move_to((pos - 1) * RIGHT * 0.8)
            guardian_circles.add(circle)
            self.play(Create(circle))
            self.wait(0.3)

        # Show coverage
        coverage_text = Text("Coverage:", font_size=24).to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(coverage_text))
        self.wait(0.5)

        # Show parity bit coverage visually
        p1_coverage = [1, 3, 5, 7]
        p2_coverage = [2, 3, 6, 7]
        p4_coverage = [4, 5, 6, 7]

        self.play(Indicate(slots[p1_coverage[0]-1], color=GREEN), run_time=0.5)
        self.play(Indicate(slots[p1_coverage[1]-1], color=GREEN), run_time=0.5)
        self.play(Indicate(slots[p1_coverage[2]-1], color=GREEN), run_time=0.5)
        self.play(Indicate(slots[p1_coverage[3]-1], color=GREEN), run_time=0.5)

        self.wait(0.5)

        # Show two valid codewords
        codeword1 = "000"
        codeword2 = "111"

        cw1 = Text(f"Valid Codeword 1: {codeword1}", font_size=24).to_edge(DOWN).shift(UP * 0.5)
        cw2 = Text(f"Valid Codeword 2: {codeword2}", font_size=24).next_to(cw1, DOWN)

        self.play(Write(cw1))
        self.wait(0.5)
        self.play(Write(cw2))
        self.wait(0.5)

        # Show distance between codewords
        dist_text = Text("Distance = 3", font_size=24).next_to(cw2, DOWN)
        self.play(Write(dist_text))
        self.wait(0.5)

        # Show single vs double error
        single_error = Text("Single Error → Syndrome points to correct bit", font_size=24).to_edge(DOWN)
        double_error = Text("Double Error → Ambiguous syndrome", font_size=24).next_to(single_error, DOWN)

        self.play(Write(single_error))
        self.wait(1.0)
        self.play(Transform(single_error, double_error))
        self.wait(1.0)

        # Syndrome mapping
        syndrome_label = Text("Syndrome Mapping:", font_size=24).to_edge(DOWN)
        self.play(Write(syndrome_label))
        self.wait(0.5)

        # Show syndrome calculation
        calc_text = MathTex("S = P_4 \\cdot 4 + P_2 \\cdot 2 + P_1 \\cdot 1", font_size=30).next_to(syndrome_label, DOWN)
        self.play(Write(calc_text))
        self.wait(1.0)

        # Show error at D3 (syndrome = 3)
        error_pos = Text("Error at D3 → Syndrome = 011", font_size=24).next_to(calc_text, DOWN)
        self.play(Write(error_pos))
        self.wait(1.0)

        # Show parity bit flip
        p2_flip = Text("Flip P2 → Syndrome = 010 (position 2)", font_size=24).next_to(error_pos, DOWN)
        self.play(Write(p2_flip))
        self.wait(1.0)

        # Final summary
        final_text = Text("Hamming codes detect and correct single-bit errors", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.0)

        self.play(FadeOut(title, slots, grid_labels, guardian_circles, cw1, cw2, dist_text, single_error, double_error,
                          syndrome_label, calc_text, error_pos, p2_flip, final_text))
