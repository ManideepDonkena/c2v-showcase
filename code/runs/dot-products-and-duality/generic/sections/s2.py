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
        
        # Right side: Algebraic formula
        alg_formula = MathTex("A_x B_x + A_y B_y", font_size=40)
        alg_formula.to_corner(UR)

        # Initial vectors
        A = Vector([3, 1], color=YELLOW)
        B = Vector([2, 4], color=GREEN)
        
        # Labels for vectors
        A_label = MathTex("\\vec{A}", font_size=24).next_to(A.get_end(), UR)
        B_label = MathTex("\\vec{B}", font_size=24).next_to(B.get_end(), UR)

        # Components of A and B
        Ax = MathTex("A_x = 3", font_size=24).to_edge(LEFT).shift(DOWN*2)
        Ay = MathTex("A_y = 1", font_size=24).next_to(Ax, DOWN)
        Bx = MathTex("B_x = 2", font_size=24).to_edge(RIGHT).shift(DOWN*2)
        By = MathTex("B_y = 4", font_size=24).next_to(Bx, DOWN)

        # Initial values
        self.play(Write(geo_formula), Write(alg_formula))
        self.wait(0.5)
        
        B.shift(0.0 * RIGHT + -1.15 * UP)  # layout: separation vector
        B_label.shift(0.0 * RIGHT + -0.64 * UP)  # layout: separation vector
        self.play(
            Create(A),
            Create(B),
            Write(A_label),
            Write(B_label),
            Write(Ax),
            Write(Ay),
            Write(Bx),
            Write(By)
        )
        self.wait(1)

        # Animation loop
        for i in range(5):
            # Rotate B
            new_B = B.copy().rotate(PI/4, about_point=ORIGIN)
            
            # Update components
            new_Bx = MathTex("B_x = " + f"{new_B.get_end()[0]:.2f}", font_size=24).to_edge(RIGHT).shift(DOWN*2)
            new_By = MathTex("B_y = " + f"{new_B.get_end()[1]:.2f}", font_size=24).next_to(new_Bx, DOWN)
            
            # Update formulas
            angle = np.arccos(
                (A.get_end()[0]*new_B.get_end()[0] + A.get_end()[1]*new_B.get_end()[1]) /
                (np.linalg.norm(A.get_end()) * np.linalg.norm(new_B.get_end()))
            )
            geo_result = np.linalg.norm(A.get_end()) * np.linalg.norm(new_B.get_end()) * np.cos(angle)
            alg_result = A.get_end()[0]*new_B.get_end()[0] + A.get_end()[1]*new_B.get_end()[1]
            
            geo_text = MathTex(f"= {geo_result:.2f}", font_size=24).next_to(geo_formula, RIGHT)
            alg_text = MathTex(f"= {alg_result:.2f}", font_size=24).next_to(alg_formula, RIGHT)

            # Animate
            self.play(
                Transform(B, new_B),
                Transform(Bx, new_Bx),
                Transform(By, new_By),
                FadeOut(geo_text),
                FadeOut(alg_text),
                run_time=1.5
            )
            
            # Show results
            self.play(
                Write(geo_text),
                Write(alg_text),
                run_time=0.5
            )
            self.wait(0.5)

        # Final statement
        final_text = Text("These definitions are identical!", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)
        
        self.play(
            FadeOut(title),
            FadeOut(geo_formula),
            FadeOut(alg_formula),
            FadeOut(A),
            FadeOut(B),
            FadeOut(A_label),
            FadeOut(B_label),
            FadeOut(Ax),
            FadeOut(Ay),
            FadeOut(Bx),
            FadeOut(By),
            FadeOut(geo_text),
            FadeOut(alg_text),
            FadeOut(final_text)
        )
