from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Mechanism: Syndrome Calculation", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Venn diagram circles
        p1 = Circle(radius=2, color=GREEN, fill_opacity=0.3).shift(LEFT * 1.5)
        p2 = Circle(radius=2, color=GREEN, fill_opacity=0.3).shift(UP * 1.5)
        p4 = Circle(radius=2, color=GREEN, fill_opacity=0.3).shift(RIGHT * 1.5)
        
        # Labels
        p1_label = Text("P1", font_size=24).next_to(p1, DOWN)
        p2_label = Text("P2", font_size=24).next_to(p2, UP)
        p4_label = Text("P4", font_size=24).next_to(p4, DOWN)
        
        # Data bits
        d1, d2, d3, d4, d5, d6, d7 = [Text(f"D{i}", font_size=24) for i in range(1, 8)]
        d_positions = [
            LEFT * 3 + UP * 0.5,
            LEFT * 1.5 + UP * 0.5,
            RIGHT * 0.5 + UP * 0.5,
            LEFT * 3 + DOWN * 0.5,
            LEFT * 1.5 + DOWN * 0.5,
            RIGHT * 0.5 + DOWN * 0.5,
            RIGHT * 2 + DOWN * 0.5
        ]
        data_bits = VGroup(*[d.move_to(pos) for d, pos in zip([d1, d2, d3, d4, d5, d6, d7], d_positions)])
        
        # Draw everything
        p2.shift(0.0 * RIGHT + -0.65 * UP)  # layout: separation vector
        self.play(Create(p1), Create(p2), Create(p4))
        self.play(Write(p1_label), Write(p2_label), Write(p4_label))
        d3.shift(0.35 * RIGHT + 0.0 * UP)  # layout: separation vector
        d6.shift(0.35 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(data_bits))
        self.wait(1)

        # Simulate error in D2
        d2_copy = d2.copy()
        self.play(d2_copy.animate.set_color(RED), run_time=0.5)
        self.wait(0.5)

        # Show failing parity checks
        p1_fail = Text("FAIL", font_size=24, color=RED).next_to(p1, DOWN)
        p2_pass = Text("PASS", font_size=24, color=GREEN).next_to(p2, UP)
        p4_fail = Text("FAIL", font_size=24, color=RED).next_to(p4, DOWN)
        
        self.play(Write(p1_fail), Write(p2_pass), Write(p4_fail))
        self.wait(1.5)

        # Show syndrome calculation
        self.play(FadeOut(p1_fail, p2_pass, p4_fail))
        self.wait(0.5)
        
        syndrome_text = Text("Syndrome:", font_size=30).to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(syndrome_text))
        self.wait(0.5)

        # Binary result
        binary_result = MathTex("101", font_size=40).next_to(syndrome_text, DOWN)
        self.play(Write(binary_result))
        self.wait(1)

        # Highlight position 5
        pos5_label = Text("Position 5", font_size=24).next_to(binary_result, DOWN)
        self.play(Write(pos5_label))
        self.wait(1.5)

        # Final explanation
        explanation = Text("Points to error location", font_size=24).next_to(pos5_label, DOWN)
        self.play(Write(explanation))
        self.wait(2)

        self.play(FadeOut(title, p1, p2, p4, p1_label, p2_label, p4_label, data_bits, binary_result, pos5_label, explanation))
        self.wait(0.5)
