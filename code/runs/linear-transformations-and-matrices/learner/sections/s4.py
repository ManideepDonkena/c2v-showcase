from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Matrix-Vector Multiplication", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial vector (2,1) in green
        point = Dot([2, 1, 0], color=GREEN)
        label = Tex("$(2,1)$", font_size=24).next_to(point, UR, buff=0.2)
        self.play(FadeIn(point), Write(label))
        self.wait(0.5)

        # Transformation matrix
        M = Matrix([[0, -1], [1, 0]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        v = Vector([2, 1], color=YELLOW)
        result = Vector([-1, 2], color=RED)
        eq = MathTex(r"\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \cdot \begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} -1 \\ 2 \end{bmatrix}", font_size=24)
        eq.to_edge(DOWN)

        self.play(Write(eq))
        self.wait(0.5)

        # Show linear combination breakdown
        col1 = Vector([0, 1], color=BLUE)
        col2 = Vector([-1, 0], color=PURPLE)
        scale1 = MathTex("2 \\cdot", font_size=24).next_to(col1, LEFT)
        scale2 = MathTex("1 \\cdot", font_size=24).next_to(col2, DOWN)

        self.play(Create(col1), Create(col2))
        self.play(Write(scale1), Write(scale2))
        self.wait(0.5)

        # Add scaled columns
        scaled_col1 = Vector([0, 2], color=BLUE)
        scaled_col2 = Vector([-1, 0], color=PURPLE)
        sum_vec = Vector([-1, 2], color=RED)
        self.play(Create(scaled_col1), Create(scaled_col2))
        self.play(Create(sum_vec))
        self.wait(0.5)

        # Fade out intermediate steps
        self.play(FadeOut(col1), FadeOut(col2), FadeOut(scale1), FadeOut(scale2),
                  FadeOut(scaled_col1), FadeOut(scaled_col2), FadeOut(sum_vec))

        # Sequential transformations example
        self.wait(0.5)
        text1 = Text("Sequential Transformations", font_size=24).to_edge(UP)
        self.play(Transform(title, text1))
        self.wait(0.5)

        # Rotate then scale
        rot = Matrix([[0, -1], [1, 0]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        scale = Matrix([[2, 0], [0, 2]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        combined = Matrix([[0, -2], [2, 0]], bracket_h_buff=0.2, bracket_v_buff=0.2)

        self.play(Write(rot), Write(scale), Write(combined))
        self.wait(1.0)

        # Show equivalence
        text2 = Text("Equivalent to single matrix multiplication", font_size=24).to_edge(DOWN)
        text2.shift(0.0 * RIGHT + -0.48 * UP)  # layout: separation vector
        self.play(Write(text2))
        self.wait(1.5)

        # Vector decomposition example
        self.play(FadeOut(rot), FadeOut(scale), FadeOut(combined), FadeOut(text2))

        text3 = Text("Vector Decomposition", font_size=24).to_edge(UP)
        self.play(Transform(title, text3))
        self.wait(0.5)

        # Show vector as linear combination of basis vectors
        ihat = Vector([1, 0], color=BLUE)
        jhat = Vector([0, 1], color=PURPLE)
        vec = Vector([3, 4], color=YELLOW)
        coeff1 = MathTex("3 \\cdot", font_size=24).next_to(ihat, UP)
        coeff2 = MathTex("4 \\cdot", font_size=24).next_to(jhat, RIGHT)

        self.play(Create(ihat), Create(jhat))
        coeff2.shift(-0.27 * RIGHT + 0.0 * UP)  # layout: separation vector
        coeff2.shift(0.17 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(coeff1), Write(coeff2))
        self.wait(0.5)

        # Apply transformation
        trans_i = Vector([0, 1], color=BLUE)
        trans_j = Vector([-1, 0], color=PURPLE)
        result_vec = Vector([-4, 3], color=RED)
        self.play(Create(trans_i), Create(trans_j))
        self.play(Create(result_vec))
        self.wait(0.5)

        # Fade out
        self.play(FadeOut(ihat), FadeOut(jhat), FadeOut(coeff1), FadeOut(coeff2),
                  FadeOut(trans_i), FadeOut(trans_j), FadeOut(result_vec))

        # Show multiple vectors and span
        text4 = Text("Column Space / Span", font_size=24).to_edge(UP)
        self.play(Transform(title, text4))
        self.wait(0.5)

        # Vectors [1,0], [0,1], [2,3]
        v1 = Vector([1, 0], color=YELLOW)
        v2 = Vector([0, 1], color=YELLOW)
        v3 = Vector([2, 3], color=YELLOW)
        self.play(Create(v1), Create(v2), Create(v3))
        self.wait(0.5)

        # Transformed versions
        t1 = Vector([0, 1], color=RED)
        t2 = Vector([-1, 0], color=RED)
        t3 = Vector([-3, 2], color=RED)
        self.play(Create(t1), Create(t2), Create(t3))
        self.wait(0.5)

        # Fade out
        self.play(FadeOut(v1), FadeOut(v2), FadeOut(v3),
                  FadeOut(t1), FadeOut(t2), FadeOut(t3))

        # Eigenvalue example
        text5 = Text("Eigenvalues", font_size=24).to_edge(UP)
        self.play(Transform(title, text5))
        self.wait(0.5)

        vec_eigen = Vector([2, 0], color=YELLOW)
        trans_eigen = Vector([0, 2], color=RED)
        self.play(Create(vec_eigen), Create(trans_eigen))
        self.wait(0.5)

        # Label eigenvalue
        label_eig = Text("Eigenvalue = 1", font_size=24).next_to(trans_eigen, UR)
        self.play(Write(label_eig))
        self.wait(1.0)

        # Singular matrix example
        self.play(FadeOut(vec_eigen), FadeOut(trans_eigen), FadeOut(label_eig))

        text6 = Text("Singular Matrix", font_size=24).to_edge(UP)
        self.play(Transform(title, text6))
        self.wait(0.5)

        # Singular matrix
        S = Matrix([[1, 0], [0, 0]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        v_a = Vector([1, 0], color=YELLOW)
        v_b = Vector([2, 0], color=YELLOW)
        self.play(Write(S))
        self.wait(0.5)

        # Both map to same point
        t_a = Vector([1, 0], color=RED)
        t_b = Vector([1, 0], color=RED)
        self.play(Create(v_a), Create(v_b))
        self.play(Create(t_a), Create(t_b))
        self.wait(1.0)

        # Final summary
        self.play(FadeOut(S), FadeOut(v_a), FadeOut(v_b), FadeOut(t_a), FadeOut(t_b))

        text7 = Text("Linear transformations preserve straight lines", font_size=24).to_edge(DOWN)
        self.play(Write(text7))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(text7))
