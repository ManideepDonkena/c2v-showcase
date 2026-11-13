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
        A_label = MathTex("\\vec{A}", font_size=24).next_to(A.get_end(), UR)
        B = Vector([2, 2], color=RED)
        B_label = MathTex("\\vec{B}", font_size=24).next_to(B.get_end(), UR)

        # Origin
        origin = Dot(color=WHITE)

        # Group vectors and labels
        self.play(Create(A), Create(B), Write(A_label), Write(B_label))
        self.wait(1)

        # Angle theta
        theta = Angle(A, B, radius=0.5, other_angle=False, color=GREEN)
        theta_label = MathTex("\\theta", font_size=24).next_to(theta, UR)

        self.play(Create(theta), Write(theta_label))
        self.wait(1.5)

        # Projection line
        proj_line = DashedLine(B.get_end(), A.get_end(), color=YELLOW)
        proj_label = MathTex("\\text{proj}_{\\vec{A}} \\vec{B}", font_size=24).next_to(proj_line, DOWN)

        self.play(Create(proj_line), Write(proj_label))
        self.wait(1.5)

        # Formula
        formula = MathTex(
            "\\vec{A} \\cdot \\vec{B} = |\\vec{A}| \\cdot \\text{proj}_{\\vec{A}} \\vec{B}",
            font_size=32
        )
        formula.to_edge(DOWN)
        self.play(Write(formula))
        self.wait(1.5)

        # Rotate B
        self.play(
            B.animate.rotate(-PI/4, about_point=ORIGIN),
            run_time=2
        )
        self.wait(0.5)

        # Update projection line and label
        self.play(
            proj_line.animate.become(DashedLine(B.get_end(), A.get_end(), color=YELLOW)),
            proj_label.animate.next_to(proj_line, DOWN)
        )
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(A), FadeOut(B),
            FadeOut(A_label), FadeOut(B_label),
            FadeOut(theta), FadeOut(theta_label),
            FadeOut(proj_line), FadeOut(proj_label),
            FadeOut(formula)
        )
        self.wait(0.5)
