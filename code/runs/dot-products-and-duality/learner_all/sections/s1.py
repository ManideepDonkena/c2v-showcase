from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Geometric Definition", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Setup vectors A and B
        A = Arrow(start=ORIGIN, end=[3, 1, 0], color=BLUE)
        A_label = MathTex("A", font_size=24).next_to(A.get_end(), UR)
        B = Arrow(start=ORIGIN, end=[2, 4, 0], color=RED)
        B_label = MathTex("B", font_size=24).next_to(B.get_end(), UR)

        # Show initial vectors
        B.shift(0.0 * RIGHT + -0.82 * UP)  # layout: separation vector
        B_label.shift(0.0 * RIGHT + -0.35 * UP)  # layout: separation vector
        self.play(Create(A), Create(B), Write(A_label), Write(B_label))
        self.wait(1)

        # Highlight angle theta
        theta = Angle(A, B, radius=0.5, other_angle=False, color=GREEN)
        theta_label = MathTex(r"\theta", font_size=24).next_to(theta, UR)
        theta_label.shift(0.0 * RIGHT + 0.27 * UP)  # layout: separation vector
        self.play(Create(theta), Write(theta_label))
        self.wait(1)

        # Projection line
        proj_line = DashedLine(B.get_end(), A.get_projection(B.get_end()), color=YELLOW)
        proj_label = MathTex(r"\text{proj}_A(B)", font_size=24).next_to(proj_line, DOWN)
        self.play(Create(proj_line), Write(proj_label))
        self.wait(1)

        # Show scalar value
        mag_A = 3.16  # sqrt(3^2 + 1^2)
        mag_B = 4.47  # sqrt(2^2 + 4^2)
        theta_val = 56.31  # degrees
        cos_theta = np.cos(np.radians(theta_val))
        dot_result = mag_A * mag_B * cos_theta

        result_text = MathTex(f"{dot_result:.2f}", font_size=30).to_edge(DOWN)
        self.play(Write(result_text))
        self.wait(1)

        # Show signed length
        signed_length = Text("Signed length", font_size=24).next_to(result_text, UP)
        self.play(Write(signed_length))
        self.wait(1)
        self.play(FadeOut(signed_length))

        # Right angle case
        B_right = Arrow(start=ORIGIN, end=[-3, 0, 0], color=RED)
        self.play(Transform(B, B_right))
        self.wait(1)

        proj_line_right = DashedLine(B.get_end(), A.get_projection(B.get_end()), color=YELLOW)
        self.play(Create(proj_line_right))
        self.wait(1)

        # Show zero projection
        zero_text = Text("Projection = 0", font_size=24).next_to(proj_line_right, DOWN)
        self.play(Write(zero_text))
        self.wait(1.5)
        self.play(FadeOut(proj_line_right, zero_text))

        # Component-wise calculation
        calc_text = MathTex(r"(1)(-3) + (2)(4) = -3 + 8 = 5", font_size=24).to_edge(DOWN)
        self.play(Write(calc_text))
        self.wait(1.5)
        self.play(FadeOut(calc_text))

        # Show A=(3,1), B=(2,4) and swap
        A1 = Arrow(start=ORIGIN, end=[3, 1, 0], color=BLUE)
        B1 = Arrow(start=ORIGIN, end=[2, 4, 0], color=RED)
        self.play(Transform(A, A1), Transform(B, B1))
        self.wait(1)

        # Swap and show commutativity
        A_swap = Arrow(start=ORIGIN, end=[2, 4, 0], color=BLUE)
        B_swap = Arrow(start=ORIGIN, end=[3, 1, 0], color=RED)
        self.play(Transform(A, A_swap), Transform(B, B_swap))
        self.wait(1)

        commutative_text = Text("Commutative!", font_size=24).next_to(result_text, UP)
        self.play(Write(commutative_text))
        self.wait(1.5)
        self.play(FadeOut(commutative_text))

        # Unit vectors
        A_unit = Arrow(start=ORIGIN, end=[1, 0, 0], color=BLUE)
        B_unit = Arrow(start=ORIGIN, end=[0, 1, 0], color=RED)
        self.play(Transform(A, A_unit), Transform(B, B_unit))
        self.wait(1)

        # Show cosine relationship
        cos_text = MathTex(r"\cos(\theta)", font_size=24).next_to(result_text, UP)
        self.play(Write(cos_text))
        self.wait(1.5)
        self.play(FadeOut(cos_text))

        # Final scalar result
        final_result = MathTex("10", font_size=40).to_edge(DOWN)
        self.play(Transform(result_text, final_result))
        self.wait(1)

        # Show that dot product is scalar (not vector)
        scalar_text = Text("Scalar output", font_size=24).next_to(final_result, UP)
        self.play(Write(scalar_text))
        self.wait(1.5)
        self.play(FadeOut(scalar_text))

        # Perpendicular vectors
        A_perp = Arrow(start=ORIGIN, end=[1, 0, 0], color=BLUE)
        B_perp = Arrow(start=ORIGIN, end=[0, 1, 0], color=RED)
        self.play(Transform(A, A_perp), Transform(B, B_perp))
        self.wait(1)

        # Show zero dot product
        zero_dot = MathTex("a_x \cdot 0 + 0 \cdot b_y = 0", font_size=24).to_edge(DOWN)
        self.play(Write(zero_dot))
        self.wait(1.5)
        self.play(FadeOut(zero_dot))

        # Negative component example
        u = Arrow(start=ORIGIN, end=[1, -1, 0], color=RED)
        v = Arrow(start=ORIGIN, end=[2, 2, 0], color=BLUE)
        self.play(Transform(B, u), Transform(A, v))
        self.wait(1)

        neg_calc = MathTex(r"(1)(2) + (-1)(2) = 2 - 2 = 0", font_size=24).to_edge(DOWN)
        self.play(Write(neg_calc))
        self.wait(1.5)
        self.play(FadeOut(neg_calc))

        # Vectors A=(1,0), C=(2,0)
        A_func = Arrow(start=ORIGIN, end=[1, 0, 0], color=BLUE)
        C_func = Arrow(start=ORIGIN, end=[2, 0, 0], color=RED)
        self.play(Transform(A, A_func), Transform(B, C_func))
        self.wait(1)

        # Functional question
        func_question = Text("Do they produce different measurements?", font_size=24).to_edge(DOWN)
        self.play(Write(func_question))
        self.wait(1.5)
        self.play(FadeOut(func_question))

        # Level sets
        level_set_A = always_redraw(lambda: DashedLine([-7, 0, 0], [7, 0, 0], color=BLUE).set_opacity(0.5))
        level_set_C = always_redraw(lambda: DashedLine([-7, 0, 0], [7, 0, 0], color=RED).set_opacity(0.5).shift(0.5 * UP))
        self.play(Create(level_set_A), Create(level_set_C))
        self.wait(1)

        # Isomorphism conclusion
        iso_text = Text("Isomorphism!", font_size=24).to_edge(DOWN)
        self.play(Write(iso_text))
        self.wait(1.5)
        self.play(FadeOut(iso_text))

        # Show unique vector A' for functional L
        A_dash = Arrow(start=ORIGIN, end=[3, 1, 0], color=YELLOW)
        self.play(Transform(A, A_dash))
        self.wait(1)

        # Final statement
        final_statement = Text("Every functional corresponds to one vector.", font_size=24).to_edge(DOWN)
        self.play(Write(final_statement))
        self.wait(1.5)
        self.play(FadeOut(final_statement))

        self.play(FadeOut(title, A, B, A_label, B_label, theta, theta_label, proj_label))
