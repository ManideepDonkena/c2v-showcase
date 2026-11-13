from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Algebraic Equivalence", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Split screen
        left = Rectangle(height=6, width=4, color=BLUE, fill_opacity=0.1).to_edge(LEFT)
        right = Rectangle(height=6, width=4, color=GREEN, fill_opacity=0.1).to_edge(RIGHT)
        self.play(Create(left), Create(right))
        self.wait(0.5)

        # Left: Geometric formula
        geo_formula = MathTex("|A||B|\\cos(\\theta)", font_size=32).move_to(left.get_center())
        self.play(Write(geo_formula))
        self.wait(0.5)

        # Right: Algebraic formula
        alg_formula = MathTex("A_x B_x + A_y B_y", font_size=32).move_to(right.get_center())
        self.play(Write(alg_formula))
        self.wait(0.5)

        # Vectors A and B
        A = Vector([3, 1], color=YELLOW)
        B = Vector([2, 4], color=RED)
        A_label = MathTex("A=(3,1)", font_size=24).next_to(A.get_end(), UP)
        B_label = MathTex("B=(2,4)", font_size=24).next_to(B.get_end(), RIGHT)

        # Adjust positions to avoid overlap and keep within frame
        B.shift(0.0 * RIGHT + -1.15 * UP)  # layout: separation vector
        A_label.shift(-1.06 * RIGHT + 0.0 * UP)  # layout: separation vector
        B_label.shift(0.0 * RIGHT + -0.28 * UP)  # move label inside frame

        self.play(Create(A), Create(B), Write(A_label), Write(B_label))
        self.wait(0.5)

        # Show projection length
        proj_length = MathTex("|A||B|\\cos(\\theta) = 10", font_size=24).to_edge(DOWN)
        self.play(Write(proj_length))
        self.wait(0.5)

        # Show signed length explanation
        signed_length = Text("Signed length of B's shadow on A", font_size=20).next_to(proj_length, DOWN)
        signed_length.shift(0.0 * RIGHT + 0.18 * UP)  # move inside frame
        self.play(Write(signed_length))
        self.wait(1)

        # Show right angle case
        self.play(FadeOut(proj_length), FadeOut(signed_length))
        B_90 = Vector([1, -1], color=RED)
        self.play(Transform(B, B_90))
        proj_zero = MathTex("|A||B|\\cos(90^\\circ) = 0", font_size=24).to_edge(DOWN)
        self.play(Write(proj_zero))
        self.wait(1)

        # Show component-wise calculation
        self.play(FadeOut(proj_zero))
        calc_text = MathTex("3 \\cdot 2 + 1 \\cdot 4 = 6 + 4 = 10", font_size=24).to_edge(DOWN)
        self.play(Write(calc_text))
        self.wait(1)

        # Show commutativity
        commutative = Text("Commutative: A·B = B·A", font_size=24).next_to(calc_text, DOWN)
        self.play(Write(commutative))
        self.wait(1)

        # Unit vectors case
        self.play(FadeOut(calc_text), FadeOut(commutative))
        unit_A = Vector([1, 0], color=YELLOW)
        unit_B = Vector([0.6, 0.8], color=RED)
        angle = ArcBetweenPoints(unit_A.get_end(), unit_B.get_end(), radius=1.5, color=PURPLE)
        angle_label = MathTex("\\theta", font_size=24).next_to(angle, RIGHT)
        self.play(Create(unit_A), Create(unit_B), Create(angle), Write(angle_label))
        cos_theta = MathTex("\\cos(\\theta) = 0.6", font_size=24).to_edge(DOWN)
        self.play(Write(cos_theta))
        self.wait(1)

        # Final scalar result
        self.play(FadeOut(cos_theta), FadeOut(angle), FadeOut(angle_label))
        final_result = MathTex("A \\cdot B = 10", font_size=32).to_edge(DOWN)
        self.play(Write(final_result))
        self.wait(1)

        # Show zero dot product for perpendicular vectors
        self.play(FadeOut(final_result))
        perp_A = Vector([1, 0], color=YELLOW)
        perp_B = Vector([0, 1], color=RED)
        self.play(Create(perp_A), Create(perp_B))
        zero_dot = MathTex("1 \\cdot 0 + 0 \\cdot 1 = 0", font_size=24).to_edge(DOWN)
        self.play(Write(zero_dot))
        self.wait(1)

        # Negative component example
        self.play(FadeOut(zero_dot))
        neg_A = Vector([1, 0], color=YELLOW)
        neg_B = Vector([2, -2], color=RED)
        self.play(Create(neg_A), Create(neg_B))
        neg_calc = MathTex("1 \\cdot 2 + 0 \\cdot (-2) = 2", font_size=24).to_edge(DOWN)
        self.play(Write(neg_calc))
        self.wait(1)

        # Functional mapping
        self.play(FadeOut(neg_calc))
        A_func = Vector([1, 0], color=YELLOW)
        C_func = Vector([2, 0], color=GREEN)
        self.play(Create(A_func), Create(C_func))
        functional_text = Text("Functionals: different slopes", font_size=24).to_edge(DOWN)
        self.play(Write(functional_text))
        self.wait(1)

        # Isomorphism conclusion
        self.play(FadeOut(functional_text))
        iso_text = Text("One-to-one mapping defines isomorphism", font_size=24).to_edge(DOWN)
        self.play(Write(iso_text))
        self.wait(1.5)

        self.play(FadeOut(iso_text), FadeOut(A_func), FadeOut(C_func), FadeOut(left), FadeOut(right), FadeOut(title))
