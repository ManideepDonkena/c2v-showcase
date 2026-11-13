from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Geometric Definition", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Vectors A and B
        A = Vector([3, 1], color=BLUE)
        A_label = MathTex("\\vec{A}", color=BLUE).next_to(A.get_end(), UR, buff=0.2)
        
        B = Vector([2, 2], color=RED)
        B_label = MathTex("\\vec{B}", color=RED).next_to(B.get_end(), UR, buff=0.2)

        # Origin
        origin = Dot(color=WHITE)

        # Group A and labels
        A_group = VGroup(A, A_label)

        # Show initial vectors
        self.play(Create(A), Write(A_label))
        self.wait(0.5)
        self.play(Create(B), Write(B_label))
        self.wait(1)

        # Angle theta
        theta = Angle(A, B, radius=0.6, other_angle=False, color=GREEN)
        theta_label = MathTex("\\theta", color=GREEN).scale(0.8).next_to(theta.get_center(), UR, buff=0.2)

        self.play(Create(theta), Write(theta_label))
        self.wait(1)

        # Projection line
        proj_line = DashedLine(B.get_end(), A.get_end(), color=YELLOW)
        proj_label = MathTex("\\text{proj}_{\\vec{A}}\\vec{B}", color=YELLOW).next_to(proj_line, DOWN, buff=0.2)

        proj_label.shift(0.0 * RIGHT + -0.95 * UP)  # layout: separation vector
        self.play(Create(proj_line), Write(proj_label))
        self.wait(1.5)

        # Rotate B
        B_copy = B.copy()
        B_label_copy = B_label.copy()

        self.play(
            Rotate(B_copy, angle=PI/2, about_point=ORIGIN),
            run_time=2
        )
        self.wait(0.5)

        # Update projection
        self.play(
            FadeOut(proj_line),
            FadeOut(proj_label)
        )

        proj_line_new = DashedLine(B_copy.get_end(), A.get_end(), color=YELLOW)
        proj_label_new = MathTex("\\text{proj}_{\\vec{A}}\\vec{B}", color=YELLOW).next_to(proj_line_new, DOWN, buff=0.2)

        proj_label_new.shift(0.0 * RIGHT + -0.95 * UP)  # layout: separation vector
        self.play(Create(proj_line_new), Write(proj_label_new))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(A_group),
            FadeOut(B_copy),
            FadeOut(B_label_copy),
            FadeOut(theta),
            FadeOut(theta_label),
            FadeOut(proj_line_new),
            FadeOut(proj_label_new)
        )
        self.wait(0.5)
