from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Basis Vectors", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid and basis vectors
        grid = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY}
        )
        self.play(Create(grid), run_time=1)
        self.wait(0.5)

        i_hat = Arrow(start=ORIGIN, end=(1, 0, 0), color=RED, stroke_width=6)
        j_hat = Arrow(start=ORIGIN, end=(0, 1, 0), color=BLUE, stroke_width=6)
        i_label = MathTex(r"\vec{i}", color=RED).next_to(i_hat.get_end(), UR, buff=0.2)
        j_label = MathTex(r"\vec{j}", color=BLUE).next_to(j_hat.get_end(), UR, buff=0.2)

        self.play(GrowArrow(i_hat), Write(i_label))
        self.play(GrowArrow(j_hat), Write(j_label))
        self.wait(1)

        # Pulsing grid lines
        pulse = always_redraw(lambda: grid.animate.set_opacity(0.3).set_stroke_width(1))
        self.play(pulse, run_time=2)
        self.wait(0.5)

        # Collapse both to same line
        i_new = Arrow(start=ORIGIN, end=(1, 0, 0), color=RED, stroke_width=6)
        j_new = Arrow(start=ORIGIN, end=(2, 0, 0), color=BLUE, stroke_width=6)
        self.play(Transform(j_hat, j_new), run_time=1.5)
        self.wait(1)

        # Show area collapses to zero
        area_text = Text("Area = 0", font_size=24).to_corner(UR)
        self.play(Write(area_text))
        self.wait(1.5)
        self.play(FadeOut(area_text))

        # Restore basis vectors
        self.play(Transform(j_hat, j_new), run_time=0.3)
        self.play(Transform(i_hat, i_new), run_time=0.3)
        self.wait(0.5)

        # Show linear combination and additivity
        u = Arrow(start=ORIGIN, end=(1, 2, 0), color=YELLOW, stroke_width=5)
        v = Arrow(start=(1, 2, 0), end=(2, 3, 0), color=PURPLE, stroke_width=5)
        w = Arrow(start=ORIGIN, end=(2, 3, 0), color=GREEN, stroke_width=5)
        self.play(GrowArrow(u), GrowArrow(v), GrowArrow(w))
        self.wait(1)

        # Show T(u + v) = T(u) + T(v)
        u_t = Arrow(start=ORIGIN, end=(1, 2, 0), color=YELLOW, stroke_width=5)
        v_t = Arrow(start=(1, 2, 0), end=(2, 3, 0), color=PURPLE, stroke_width=5)
        w_t = Arrow(start=ORIGIN, end=(2, 3, 0), color=GREEN, stroke_width=5)
        self.play(Transform(u, u_t), Transform(v, v_t), Transform(w, w_t))
        self.wait(1.5)

        # Collapse both to origin
        i_zero = Arrow(start=ORIGIN, end=(0, 0, 0), color=RED, stroke_width=6)
        j_zero = Arrow(start=ORIGIN, end=(0, 0, 0), color=BLUE, stroke_width=6)
        self.play(Transform(i_hat, i_zero), Transform(j_hat, j_zero))
        self.wait(1.5)

        # Show matrix [[0, 0], [0, 0]]
        matrix = MathTex(r"\begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}")
        matrix.to_corner(UL)
        self.play(Write(matrix))
        self.wait(1.5)
        self.play(FadeOut(matrix))

        # Shear transformation
        i_shear = Arrow(start=ORIGIN, end=(1, 1, 0), color=RED, stroke_width=6)
        j_shear = Arrow(start=ORIGIN, end=(0, 1, 0), color=BLUE, stroke_width=6)
        self.play(Transform(i_hat, i_shear), Transform(j_hat, j_shear))
        self.wait(1.5)

        # Show unit square area
        square = Square(side_length=1, color=GREY, fill_opacity=0.3).move_to(ORIGIN)
        self.play(FadeIn(square))
        self.wait(1)
        self.play(FadeOut(square))

        # Diagonal matrix example
        diag_matrix = MathTex(r"\begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}")
        diag_matrix.to_corner(UL)
        self.play(Write(diag_matrix))
        self.wait(1.5)
        self.play(FadeOut(diag_matrix))

        # Trace = sum of eigenvalues
        trace_matrix = MathTex(r"\begin{bmatrix} 1 & -1 \\ 1 & 4 \end{bmatrix}")
        trace_matrix.to_corner(UL)
        self.play(Write(trace_matrix))
        self.wait(1.5)
        self.play(FadeOut(trace_matrix))

        # Sequential transformations
        rotate = Matrix([[0, -1], [1, 0]])
        scale = Matrix([[2, 0], [0, 2]])
        combined = Matrix([[0, -2], [2, 0]])
        self.play(Write(rotate), Write(scale), Write(combined))
        self.wait(1.5)
        self.play(FadeOut(rotate), FadeOut(scale), FadeOut(combined))

        # Decompose vector
        vec = Arrow(start=ORIGIN, end=(3, 4, 0), color=WHITE, stroke_width=5)
        self.play(GrowArrow(vec))
        self.wait(1.5)

        # Show span of transformation
        self.play(FadeOut(vec))
        self.wait(0.5)

        # Eigenvalue example
        eigen_vec = Arrow(start=ORIGIN, end=(2, 0, 0), color=GREEN, stroke_width=5)
        self.play(GrowArrow(eigen_vec))
        self.wait(1.5)

        # Singular matrix mapping distinct inputs to same output
        v1 = Arrow(start=ORIGIN, end=(1, 0, 0), color=YELLOW, stroke_width=5)
        v2 = Arrow(start=ORIGIN, end=(2, 0, 0), color=PURPLE, stroke_width=5)
        self.play(GrowArrow(v1), GrowArrow(v2))
        self.wait(1.5)

        # Final transformation
        final_matrix = MathTex(r"\begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}")
        final_matrix.to_corner(UL)
        self.play(Write(final_matrix))
        self.wait(1.5)
        self.play(FadeOut(final_matrix))

        # End
        self.play(FadeOut(title), FadeOut(grid), FadeOut(i_hat), FadeOut(j_hat),
                  FadeOut(i_label), FadeOut(j_label))
        self.wait(0.5)
