from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Duality Isomorphism", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Left: Functional L with contour lines
        functional_L = VGroup(
            Line([-6, -2, 0], [6, -2, 0], color=BLUE),
            Line([-6, 0, 0], [6, 0, 0], color=BLUE),
            Line([-6, 2, 0], [6, 2, 0], color=BLUE),
        ).set_stroke(width=2)
        L_label = Text("L", font_size=24).next_to(functional_L[1], UP)
        self.play(Create(functional_L), Write(L_label))
        self.wait(0.5)

        # Right: Vector A'
        A_prime = Arrow(start=[0, 0, 0], end=[3, 1, 0], color=RED, buff=0)
        A_label = Text("A'", font_size=24).next_to(A_prime.get_end(), UR)
        self.play(Create(A_prime), Write(A_label))
        self.wait(0.5)

        # Morphing animation
        morph_group = VGroup(functional_L, A_prime)
        self.play(
            Transform(functional_L[0], Line([-6, -2, 0], [6, -2, 0]).set_color(YELLOW)),
            Transform(functional_L[1], Line([-6, 0, 0], [6, 0, 0]).set_color(YELLOW)),
            Transform(functional_L[2], Line([-6, 2, 0], [6, 2, 0]).set_color(YELLOW)),
            run_time=1.5
        )
        self.wait(0.5)

        # Show L(B) = A' · B'
        eq = MathTex("L(B) = A' \\cdot B'", font_size=32).to_edge(DOWN)
        self.play(Write(eq))
        self.wait(1)

        # Scalar value from projection
        scalar_value = MathTex("||A|| \\cdot ||B|| \\cdot \\cos(\\theta)", font_size=24).next_to(eq, UP)
        self.play(Write(scalar_value))
        self.wait(0.5)

        # Signed length explanation
        signed_length = Text("Signed length of B's shadow on A", font_size=20).next_to(scalar_value, DOWN)
        self.play(Write(signed_length))
        self.wait(1)

        # Right angle example
        self.play(FadeOut(scalar_value), FadeOut(signed_length))

        right_angle_A = Arrow(start=[0, 0, 0], end=[3, 0, 0], color=GREEN)
        right_angle_B = Arrow(start=[0, 0, 0], end=[0, 2, 0], color=ORANGE)
        self.play(Create(right_angle_A), Create(right_angle_B))
        self.wait(0.5)

        # Projection is zero
        proj_zero = Text("Projection length = 0", font_size=24).next_to(right_angle_A, UR)
        self.play(Write(proj_zero))
        self.wait(1)

        # Concrete calculation: A=(3,1), B=(2,4)
        self.play(FadeOut(proj_zero), FadeOut(right_angle_A), FadeOut(right_angle_B))

        calc_text = Text("A = (3, 1), B = (2, 4)", font_size=24).to_edge(UP)
        self.play(Write(calc_text))
        self.wait(0.5)

        calc1 = MathTex("3 \\cdot 2 + 1 \\cdot 4 = 6 + 4 = 10", font_size=24).next_to(calc_text, DOWN)
        self.play(Write(calc1))
        self.wait(1)

        # Swap vectors
        swap_text = Text("Swap A and B:", font_size=24).next_to(calc1, DOWN)
        self.play(Write(swap_text))
        self.wait(0.5)

        calc2 = MathTex("2 \\cdot 3 + 4 \\cdot 1 = 6 + 4 = 10", font_size=24).next_to(swap_text, DOWN)
        self.play(Write(calc2))
        self.wait(1)

        # Commutativity
        commutative = Text("Commutative: order doesn't matter", font_size=24).next_to(calc2, DOWN)
        self.play(Write(commutative))
        self.wait(1.5)

        # Unit vectors
        self.play(FadeOut(calc1), FadeOut(calc2), FadeOut(swap_text), FadeOut(commutative))

        unit_A = Arrow(start=[0, 0, 0], end=[1, 0, 0], color=BLUE)
        unit_B = Arrow(start=[0, 0, 0], end=[0.64, 0.76, 0], color=ORANGE)
        self.play(Create(unit_A), Create(unit_B))
        self.wait(0.5)

        angle_label = MathTex("\\theta", font_size=24).next_to(unit_A, UR)
        self.play(Write(angle_label))
        self.wait(0.5)

        dot_product_unit = MathTex("1 \\cdot 1 \\cdot \\cos(\\theta) = \\cos(\\theta)", font_size=24).to_edge(DOWN)
        self.play(Write(dot_product_unit))
        self.wait(1.5)

        # Final scalar result
        final_scalar = MathTex("10", font_size=40).next_to(dot_product_unit, UP)
        self.play(Write(final_scalar))
        self.wait(1)

        # Zero dot product for perpendicular vectors
        self.play(FadeOut(final_scalar), FadeOut(dot_product_unit), FadeOut(angle_label))

        perp_A = Arrow(start=[0, 0, 0], end=[3, 0, 0], color=BLUE)
        perp_B = Arrow(start=[0, 0, 0], end=[0, 2, 0], color=ORANGE)
        self.play(Create(perp_A), Create(perp_B))
        self.wait(0.5)

        zero_dot = MathTex("3 \\cdot 0 + 0 \\cdot 2 = 0", font_size=24).next_to(perp_A, UR)
        self.play(Write(zero_dot))
        self.wait(1)

        # Component-wise calculation with negative
        self.play(FadeOut(zero_dot), FadeOut(perp_A), FadeOut(perp_B))

        u = Arrow(start=[0, 0, 0], end=[1, 0, 0], color=BLUE)
        v = Arrow(start=[0, 0, 0], end=[2, -2, 0], color=ORANGE)
        self.play(Create(u), Create(v))
        self.wait(0.5)

        neg_calc = MathTex("1 \\cdot 2 + 0 \\cdot (-2) = 2", font_size=24).next_to(u, UR)
        self.play(Write(neg_calc))
        self.wait(1)

        # Vector A and C
        self.play(FadeOut(neg_calc), FadeOut(u), FadeOut(v))

        A = Arrow(start=[0, 0, 0], end=[1, 0, 0], color=BLUE)
        C = Arrow(start=[0, 0, 0], end=[2, 0, 0], color=RED)
        self.play(Create(A), Create(C))
        self.wait(0.5)

        # Functional contours
        contour_A = VGroup(
            Line([-6, -1, 0], [6, -1, 0], color=BLUE),
            Line([-6, 0, 0], [6, 0, 0], color=BLUE),
            Line([-6, 1, 0], [6, 1, 0], color=BLUE),
        ).set_stroke(width=2)
        contour_C = VGroup(
            Line([-6, -2, 0], [6, -2, 0], color=RED),
            Line([-6, 0, 0], [6, 0, 0], color=RED),
            Line([-6, 2, 0], [6, 2, 0], color=RED),
        ).set_stroke(width=2)

        self.play(Transform(A, contour_A), Transform(C, contour_C))
        self.wait(1)
        # Isomorphism conclusion
        iso_text = Text("This defines an isomorphism", font_size=24).to_edge(DOWN)
        self.play(Write(iso_text))
        self.wait(1.5)

        self.play(FadeOut(iso_text), FadeOut(A), FadeOut(C), FadeOut(title))
        self.wait(0.5)
