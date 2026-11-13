from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Eigenvalue", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Vector v and Av
        v = Vector([2, 1], color=YELLOW)
        v_label = MathTex("\\vec{v}", font_size=24).next_to(v.get_end(), UR, buff=0.1)
        
        A = Matrix([[2, 1], [1, 2]])
        A.to_corner(UL)
        Av = Vector([5, 4], color=RED)
        Av_label = MathTex("A\\vec{v}", font_size=24).next_to(Av.get_end(), DR, buff=0.1)

        # Show v and Av
        self.play(Create(v), Write(v_label))
        self.wait(0.5)
        Av.shift(0.0 * RIGHT + -1.16 * UP)  # layout: separation vector
        self.play(Create(Av), Write(Av_label))
        self.wait(1)

        # Equation
        equation = MathTex("A\\vec{v} = \\lambda\\vec{v}", font_size=40)
        equation.to_edge(DOWN)
        self.play(Write(equation))
        self.wait(1)

        # Animate lambda value
        lambda_val = ValueTracker(2)
        lambda_text = always_redraw(
            lambda: MathTex("\\lambda = ", font_size=30).next_to(equation, LEFT, buff=0.5)
        )
        lambda_num = always_redraw(
            lambda: MathTex(str(lambda_val.get_value()), font_size=30).next_to(lambda_text, RIGHT, buff=0.1)
        )
        self.play(Write(lambda_text), Write(lambda_num))
        self.wait(0.5)

        # Show scaling effect
        self.play(lambda_val.animate.set_value(2.5), run_time=2)
        self.wait(1)

        # Direction and length explanation
        direction_text = Text("Same direction", font_size=24).to_edge(LEFT).shift(DOWN)
        length_text = Text("Length scaled by λ", font_size=24).to_edge(RIGHT).shift(DOWN)
        
        self.play(Write(direction_text))
        self.wait(1)
        length_text.shift(0.0 * RIGHT + -0.48 * UP)  # layout: separation vector
        self.play(Write(length_text))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(v), 
            FadeOut(Av), 
            FadeOut(v_label), 
            FadeOut(Av_label),
            FadeOut(equation),
            FadeOut(lambda_text),
            FadeOut(lambda_num),
            FadeOut(direction_text),
            FadeOut(length_text),
            FadeOut(title)
        )
        self.wait(0.5)
