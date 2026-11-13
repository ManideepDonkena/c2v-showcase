from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Algebraic Equivalence", font_size=36)
        title.to_edge(UP)
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

        # Vectors
        A = Vector([3, 1], color=YELLOW)
        B = Vector([2, 4], color=GREEN)
        A_label = MathTex("\\vec{A}", font_size=24).next_to(A.get_end(), UR)
        B_label = MathTex("\\vec{B}", font_size=24).next_to(B.get_end(), UR)

        # Labels for components
        Ax = MathTex("A_x = 3", font_size=24).to_edge(LEFT).shift(DOWN*2)
        Ay = MathTex("A_y = 1", font_size=24).next_to(Ax, DOWN)
        Bx = MathTex("B_x = 2", font_size=24).to_edge(RIGHT).shift(DOWN*2)
        By = MathTex("B_y = 4", font_size=24).next_to(Bx, DOWN)

        # Initial values
        B.shift(0.0 * RIGHT + -1.15 * UP)  # layout: separation vector
        B_label.shift(0.0 * RIGHT + -0.64 * UP)  # layout: separation vector
        self.play(Create(A), Create(B), Write(A_label), Write(B_label))
        self.wait(0.5)
        self.play(Write(Ax), Write(Ay), Write(Bx), Write(By))
        self.wait(0.5)

        # Compute initial dot product
        geo_result = MathTex("= 3.16 \\times 4.47 \\times 0.89 = 12", font_size=24)
        geo_result.next_to(geo_formula, DOWN)
        alg_result = MathTex("= 3 \\times 2 + 1 \\times 4 = 10", font_size=24)
        alg_result.next_to(alg_formula, DOWN)

        self.play(Write(geo_result), Write(alg_result))
        self.wait(1.5)

        # Rotate B
        def update_B_vector(mob, dt):
            mob.rotate(0.1 * dt, about_point=ORIGIN)
            # Update component labels
            new_Bx = mob.get_end()[0]
            new_By = mob.get_end()[1]
            Bx.become(MathTex(f"B_x = {new_Bx:.1f}", font_size=24).to_edge(RIGHT).shift(DOWN*2))
            By.become(MathTex(f"B_y = {new_By:.1f}", font_size=24).next_to(Bx, DOWN))

            # Update geometric result
            A_mag = A.get_length()
            B_mag = mob.get_length()
            theta = angle_of_vector(mob.get_end() - A.get_start())
            cos_theta = np.cos(theta)
            geo_val = A_mag * B_mag * cos_theta
            geo_result.become(MathTex(f"= {A_mag:.2f} \\times {B_mag:.2f} \\times {cos_theta:.2f} = {geo_val:.1f}", font_size=24).next_to(geo_formula, DOWN))

            # Update algebraic result
            alg_val = 3 * new_Bx + 1 * new_By
            alg_result.become(MathTex(f"= 3 \\times {new_Bx:.1f} + 1 \\times {new_By:.1f} = {alg_val:.1f}", font_size=24).next_to(alg_formula, DOWN))

        B.add_updater(update_B_vector)

        # Animate rotation
        self.play(Rotate(B, 2*PI, rate_func=linear, run_time=5))
        self.wait(0.5)

        # Final convergence message
        converge = Text("Both formulas converge to same value", font_size=24)
        converge.to_edge(DOWN)
        self.play(Write(converge))
        self.wait(1.5)

        # Clean up
        self.play(FadeOut(B), FadeOut(A), FadeOut(A_label), FadeOut(B_label),
                  FadeOut(Ax), FadeOut(Ay), FadeOut(Bx), FadeOut(By),
                  FadeOut(geo_result), FadeOut(alg_result), FadeOut(converge))
        self.wait(0.5)
