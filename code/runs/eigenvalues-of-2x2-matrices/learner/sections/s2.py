from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Eigenvalue", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial vector v and Av = λv
        v = Vector([1, 0], color=BLUE)
        v_label = MathTex(r"\vec{v}", font_size=24).next_to(v.get_end(), UR, buff=0.1)
        A = Matrix([[3, 0], [0, 1]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        A_label = MathTex(r"A", font_size=24).next_to(A, DOWN, buff=0.2)
        Av = Vector([3, 0], color=RED)
        Av_label = MathTex(r"A\vec{v}", font_size=24).next_to(Av.get_end(), UR, buff=0.1)

        # Show A and v
        self.play(Write(A), Write(A_label))
        self.wait(0.5)
        self.play(Write(v), Write(v_label))
        self.wait(0.5)

        # Show Av = λv
        equation = MathTex(r"A\vec{v} = \lambda\vec{v}", font_size=40).to_edge(UP, buff=0.5)
        equation.shift(0.0 * RIGHT + 0.45 * UP)  # layout: separation vector
        self.play(Write(equation))
        self.wait(1)

        # Animate λ = 3
        lambda_val = ValueTracker(3)
        lambda_text = always_redraw(
            lambda: MathTex(r"\lambda = ", font_size=32).next_to(equation, RIGHT, buff=0.2)
            .add(MathTex(str(lambda_val.get_value()), font_size=32).next_to(equation, RIGHT, buff=0.2))
        )
        self.play(Write(lambda_text))
        self.wait(1)

        # Show Av = 3v
        Av.shift(0.0 * RIGHT + -0.22 * UP)  # layout: separation vector
        self.play(Write(Av), Write(Av_label))
        self.wait(1)

        # Compare lengths
        v_line = Line(v.get_start(), v.get_end(), color=BLUE, stroke_width=5)
        Av_line = Line(Av.get_start(), Av.get_end(), color=RED, stroke_width=5)
        v_length = MathTex(r"|\vec{v}|", font_size=24).next_to(v_line, DOWN, buff=0.1)
        Av_length = MathTex(r"|A\vec{v}|", font_size=24).next_to(Av_line, DOWN, buff=0.1)

        self.play(Write(v_line), Write(v_length))
        self.wait(0.5)
        self.play(Write(Av_line), Write(Av_length))
        self.wait(1)

        # Fade out
        self.play(FadeOut(v_line), FadeOut(Av_line), FadeOut(v_length), FadeOut(Av_length))

        # Show inverse relationship: A⁻¹v = (1/λ)v
        self.play(FadeOut(lambda_text))
        self.wait(0.5)

        inv_equation = MathTex(r"A^{-1}\vec{v} = \frac{1}{\lambda}\vec{v}", font_size=32).to_edge(DOWN, buff=0.5)
        self.play(Write(inv_equation))
        self.wait(1.5)

        # Show that A * [1, 0] = [3, 0]
        self.play(FadeOut(inv_equation))
        self.wait(0.5)

        calc_text = Text("Example: ", font_size=24).to_edge(LEFT, buff=0.5).shift(UP)
        calc_vec = MathTex(r"\begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 3 \\ 0 \end{bmatrix}", font_size=24)
        calc_vec.next_to(calc_text, DOWN, buff=0.2)

        self.play(Write(calc_text), Write(calc_vec))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(calc_text), FadeOut(calc_vec))
        self.wait(0.5)

        # Final fade out
        self.play(FadeOut(title), FadeOut(v), FadeOut(v_label), FadeOut(A), FadeOut(A_label), FadeOut(Av), FadeOut(Av_label))
        self.wait(0.5)
