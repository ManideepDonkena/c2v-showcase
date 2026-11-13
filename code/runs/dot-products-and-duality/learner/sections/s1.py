from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Geometric Definition", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Setup vectors
        A = Vector([3, 1], color=BLUE)
        B = Vector([2, 2], color=RED)
        origin = ORIGIN

        # Labels for vectors
        label_A = MathTex("\\vec{A}", color=BLUE).next_to(A.get_end(), UR, buff=0.2)
        label_B = MathTex("\\vec{B}", color=RED).next_to(B.get_end(), UR, buff=0.2)

        # Show initial setup
        self.play(Create(A), Create(B), Write(label_A), Write(label_B))
        self.wait(1)

        # Highlight angle theta
        theta = Angle(A, B, radius=0.5, other_angle=False, color=GREEN)
        theta_label = MathTex("\\theta", color=GREEN).next_to(theta, UR, buff=0.2)
        self.play(Create(theta), Write(theta_label))
        self.wait(1)

        # Projection line (dashed yellow)
        proj_line = DashedLine(B.get_end(), A.get_end() * (B.get_end()[0] / A.get_end()[0]), color=YELLOW)
        proj_label = MathTex("\\text{proj}_{\\vec{A}} \\vec{B}", color=YELLOW).next_to(proj_line, DOWN, buff=0.2)
        proj_label.shift(0.0 * RIGHT + -0.62 * UP)  # layout: separation vector
        self.play(Create(proj_line), Write(proj_label))
        self.wait(1)

        # Show scalar value
        mag_A = A.get_length()
        mag_B = B.get_length()
        theta_val = 30  # degrees
        cos_theta = np.cos(np.radians(theta_val))
        dot_product_value = mag_A * mag_B * cos_theta

        result_text = MathTex(
            "\\vec{A} \\cdot \\vec{B} =", 
            "{|\\vec{A}|} {|\\vec{B}|} \\cos(\\theta) =", 
            f"{dot_product_value:.2f}"
        ).to_edge(DOWN)
        self.play(Write(result_text))
        self.wait(1)

        # Show signed length explanation
        signed_text = Text("Signed length: positive if acute, negative if obtuse", font_size=24).next_to(result_text, UP)
        self.play(Write(signed_text))
        self.wait(1.5)

        # Clear and show 90-degree case
        self.play(FadeOut(proj_line), FadeOut(proj_label), FadeOut(theta), FadeOut(theta_label), FadeOut(signed_text))

        B_90 = Vector([1, -3], color=RED)
        label_B_90 = MathTex("\\vec{B}", color=RED).next_to(B_90.get_end(), UR, buff=0.2)
        self.play(Transform(B, B_90), Transform(label_B, label_B_90))
        self.wait(1)

        # Show projection is zero
        proj_line_90 = DashedLine(B_90.get_end(), A.get_end() * (B_90.get_end()[0] / A.get_end()[0]), color=YELLOW)
        self.play(Create(proj_line_90))
        self.wait(1)

        zero_text = Text("Projection length = 0", font_size=24).next_to(proj_line_90, DOWN)
        zero_text.shift(0.0 * RIGHT + -0.4 * UP)  # layout: separation vector
        self.play(Write(zero_text))
        self.wait(1.5)

        # Cleanup
        self.play(FadeOut(result_text), FadeOut(zero_text), FadeOut(proj_line_90), FadeOut(B), FadeOut(label_B), FadeOut(A), FadeOut(label_A), FadeOut(title))
        self.wait(0.5)
