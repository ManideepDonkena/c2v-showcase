from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Algebraic Equivalence", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Left side: Geometric formula
        geo_formula = MathTex("|A||B|\\cos(\\theta)", font_size=40)
        geo_formula.to_corner(UL)
        self.play(Write(geo_formula))
        self.wait(0.5)

        # Right side: Algebraic formula
        alg_formula = MathTex("A_x B_x + A_y B_y", font_size=40)
        alg_formula.to_corner(UR)
        self.play(Write(alg_formula))
        self.wait(0.5)

        # Vectors A and B
        A = Vector([3, 1], color=YELLOW)
        B = Vector([2, 4], color=BLUE)
        A_label = MathTex("\\vec{A}=(3,1)", font_size=24).next_to(A.get_end(), UR)
        B_label = MathTex("\\vec{B}=(2,4)", font_size=24).next_to(B.get_end(), DR)

        B.shift(0.0 * RIGHT + -1.15 * UP)  # layout: separation vector
        self.play(Create(A), Create(B))
        self.play(Write(A_label), Write(B_label))
        self.wait(0.5)

        # Show component-wise multiplication and addition
        step1 = MathTex("3 \\times 2 + 1 \\times 4", font_size=30).to_edge(DOWN)
        step2 = MathTex("6 + 4 = 10", font_size=30).next_to(step1, DOWN)
        self.play(Write(step1))
        self.wait(0.5)
        self.play(Write(step2))
        self.wait(1)

        # Swap vectors
        swap_text = Text("Swapping A and B:", font_size=24).to_edge(LEFT).shift(DOWN)
        self.play(Write(swap_text))
        self.wait(0.5)

        step3 = MathTex("2 \\times 3 + 4 \\times 1", font_size=30).next_to(step2, DOWN)
        step4 = MathTex("6 + 4 = 10", font_size=30).next_to(step3, DOWN)
        self.play(Write(step3))
        self.wait(0.5)
        self.play(Write(step4))
        self.wait(1)

        # Highlight commutativity
        comm_text = Text("Commutative property ensures same result.", font_size=24).to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(comm_text))
        self.wait(1.5)

        # Clear previous content
        self.play(FadeOut(step1), FadeOut(step2), FadeOut(step3), FadeOut(step4), FadeOut(swap_text), FadeOut(comm_text))

        # Unit vectors rotating
        unit_A = Vector([1, 0], color=YELLOW)
        unit_B = Vector([0, 1], color=BLUE)
        unit_A_label = MathTex("\\vec{A}=(1,0)", font_size=24).next_to(unit_A.get_end(), UR)
        unit_B_label = MathTex("\\vec{B}=(0,1)", font_size=24).next_to(unit_B.get_end(), DR)

        self.play(Create(unit_A), Create(unit_B))
        self.play(Write(unit_A_label), Write(unit_B_label))
        self.wait(0.5)

        # Show dot product = cos(theta)
        dot_result = MathTex("0 \\times 0 + 1 \\times 1 = 1", font_size=30).to_edge(DOWN)
        self.play(Write(dot_result))
        self.wait(1)

        # Show that it equals cos(90°) = 0
        cos_text = Text("cos(90°) = 0", font_size=24).next_to(dot_result, DOWN).shift(DOWN * 0.5)
        self.play(Write(cos_text))
        self.wait(1.5)

        # Clear unit vectors
        self.play(FadeOut(unit_A), FadeOut(unit_B), FadeOut(unit_A_label), FadeOut(unit_B_label), FadeOut(dot_result), FadeOut(cos_text))

        # Show perpendicular vectors
        perp_A = Vector([3, 0], color=YELLOW)
        perp_B = Vector([0, 4], color=BLUE)
        perp_A_label = MathTex("\\vec{A}=(3,0)", font_size=24).next_to(perp_A.get_end(), UR)
        perp_B_label = MathTex("\\vec{B}=(0,4)", font_size=24).next_to(perp_B.get_end(), DR)

        self.play(Create(perp_A), Create(perp_B))
        self.play(Write(perp_A_label), Write(perp_B_label))
        self.wait(0.5)

        # Show dot product = 0
        zero_result = MathTex("3 \\times 0 + 0 \\times 4 = 0", font_size=30).to_edge(DOWN)
        self.play(Write(zero_result))
        self.wait(1.5)
        
        # Final scalar result
        final_scalar = MathTex("10", font_size=60).move_to(ORIGIN)
        self.play(Write(final_scalar))
        self.wait(1)

        # Final explanation
        scalar_text = Text("Dot product is a scalar (just one number)", font_size=24).next_to(final_scalar, DOWN).shift(DOWN * 0.5)
        self.play(Write(scalar_text))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(geo_formula), FadeOut(alg_formula), FadeOut(A), FadeOut(B), FadeOut(A_label), FadeOut(B_label), FadeOut(zero_result), FadeOut(final_scalar), FadeOut(scalar_text))
