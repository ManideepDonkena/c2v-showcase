from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Duality via Linear Functionals", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Vector A fixed
        A = Arrow(start=ORIGIN, end=[3, 1, 0], color=YELLOW)
        A_label = MathTex(r"\vec{A} = (3,1)", font_size=24).next_to(A.get_end(), UR)
        self.play(Create(A), Write(A_label))
        self.wait(0.5)

        # Grid of points
        grid = VGroup()
        for x in range(-6, 7):
            for y in range(-4, 5):
                grid.add(Dot([x, y, 0], color=GREY))
        grid.shift(0.0 * RIGHT + -0.23 * UP)  # layout: separation vector
        self.play(FadeIn(grid))
        self.wait(0.5)

        # Test vector B
        B = Arrow(start=ORIGIN, end=[2, 4, 0], color=GREEN)
        B_label = MathTex(r"\vec{B} = (2,4)", font_size=24).next_to(B.get_end(), DR)
        self.play(Create(B), Write(B_label))
        self.wait(0.5)

        # Dot product value
        dot_val = MathTex(r"\vec{A} \cdot \vec{B} = 3 \cdot 2 + 1 \cdot 4 = 10", font_size=24).to_edge(DOWN)
        self.play(Write(dot_val))
        self.wait(1)

        # Show projection length
        proj_arrow = Arrow(start=ORIGIN, end=[3, 1, 0], color=RED)
        proj_label = MathTex(r"\text{Signed length} = |\vec{A}| \cdot |\vec{B}| \cdot \cos(\theta)", font_size=24).next_to(proj_arrow, UR)
        self.play(Create(proj_arrow), Write(proj_label))
        self.wait(1)

        # Right angle case
        B_perp = Arrow(start=ORIGIN, end=[-1, 2, 0], color=GREEN)
        B_perp_label = MathTex(r"\vec{B} \perp \vec{A}", font_size=24).next_to(B_perp.get_end(), DL)
        self.play(Transform(B, B_perp), Write(B_perp_label))
        self.wait(0.5)

        # Dot product = 0
        zero_val = MathTex(r"\vec{A} \cdot \vec{B} = 0", font_size=24).to_edge(DOWN)
        self.play(Transform(dot_val, zero_val))
        self.wait(1)

        # Swap vectors A and B
        A_swap = Arrow(start=ORIGIN, end=[2, 4, 0], color=YELLOW)
        B_swap = Arrow(start=ORIGIN, end=[3, 1, 0], color=GREEN)
        swap_label = MathTex(r"\vec{B} \cdot \vec{A} = 2 \cdot 3 + 4 \cdot 1 = 10", font_size=24).to_edge(DOWN)
        self.play(Transform(A, A_swap), Transform(B, B_swap), Transform(dot_val, swap_label))
        self.wait(1)

        # Unit vectors rotating
        unit_A = Arrow(start=ORIGIN, end=[1, 0, 0], color=YELLOW)
        unit_B = Arrow(start=ORIGIN, end=[0.5, 0.866, 0], color=GREEN)
        angle_label = MathTex(r"\theta = 60^\circ", font_size=24).next_to(unit_B.get_end(), UR)
        self.play(Create(unit_A), Create(unit_B), Write(angle_label))
        self.wait(0.5)

        # Dot product = cos(theta)
        cos_val = MathTex(r"\vec{A} \cdot \vec{B} = \cos(60^\circ) = 0.5", font_size=24).to_edge(DOWN)
        self.play(Transform(dot_val, cos_val))
        self.wait(1)

        # Show scalar result
        scalar_result = MathTex(r"10", font_size=40).to_corner(DR)
        self.play(Write(scalar_result))
        self.wait(1)

        # Perpendicular vectors
        A_perp = Arrow(start=ORIGIN, end=[1, 0, 0], color=YELLOW)
        B_perp2 = Arrow(start=ORIGIN, end=[0, 1, 0], color=GREEN)
        self.play(Transform(A, A_perp), Transform(B, B_perp2))
        self.wait(0.5)

        # Dot product = 0 again
        zero_val2 = MathTex(r"\vec{A} \cdot \vec{B} = 1 \cdot 0 + 0 \cdot 1 = 0", font_size=24).to_edge(DOWN)
        self.play(Transform(dot_val, zero_val2))
        self.wait(1)

        # Component-wise calculation with negative
        neg_label = MathTex(r"u = (1, -1), v = (2, 2)", font_size=24).to_edge(UP)
        self.play(Write(neg_label))
        self.wait(0.5)

        neg_calc = MathTex(r"1 \cdot 2 + (-1) \cdot 2 = 2 - 2 = 0", font_size=24).to_edge(DOWN)
        self.play(Write(neg_calc))
        self.wait(1)

        # Different vectors A and C
        A_diff = Arrow(start=ORIGIN, end=[1, 0, 0], color=YELLOW)
        C_diff = Arrow(start=ORIGIN, end=[2, 0, 0], color=PURPLE)
        self.play(Transform(A, A_diff), Transform(B, C_diff))
        self.wait(0.5)

        # Functional contours
        contour1 = DashedLine(start=[-7, 0, 0], end=[7, 0, 0], color=YELLOW)
        contour2 = DashedLine(start=[-7, 0, 0], end=[7, 0, 0], color=PURPLE).shift(1 * UP)
        self.play(Create(contour1), Create(contour2))
        self.wait(0.5)

        # Isomorphism conclusion
        iso_text = Text("This defines an isomorphism.", font_size=24).to_edge(DOWN)
        self.play(Write(iso_text))
        self.wait(1)

        # Final vector A' from contours
        A_prime = Arrow(start=ORIGIN, end=[0.5, 0.5, 0], color=BLUE)
        self.play(Create(A_prime))
        self.wait(0.5)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(A),
            FadeOut(B),
            FadeOut(grid),
            FadeOut(proj_arrow),
            FadeOut(A_label),
            FadeOut(B_label),
            FadeOut(proj_label),
            FadeOut(dot_val),
            FadeOut(angle_label),
            FadeOut(cos_val),
            FadeOut(scalar_result),
            FadeOut(neg_label),
            FadeOut(neg_calc),
            FadeOut(contour1),
            FadeOut(contour2),
            FadeOut(iso_text),
            FadeOut(A_prime)
        )
        self.wait(0.5)
