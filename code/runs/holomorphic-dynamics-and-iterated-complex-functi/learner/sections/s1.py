from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Orbit of a Point", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Complex plane
        plane = NumberPlane(
            x_range=[-3.5, 3.5, 1],
            y_range=[-2, 2, 1],
            axis_config={"stroke_color": GREY_A},
            background_line_style={"stroke_color": GREY_D}
        )
        plane.scale(0.8)
        plane.shift(DOWN * 0.5)
        self.play(Create(plane))
        self.wait(0.5)

        # Fixed point z = 0
        origin_dot = Dot(point=ORIGIN, color=YELLOW)
        origin_label = MathTex("z = 0", font_size=24).next_to(origin_dot, UR, buff=0.1)
        self.play(FadeIn(origin_dot), Write(origin_label))
        self.wait(0.5)

        # Initial point z_0
        z0 = Dot(point=UP * 0.5, color=RED)
        z0_label = MathTex("z_0", font_size=24).next_to(z0, UR, buff=0.1).shift(UP * 0.2 + RIGHT * 0.1)
        self.play(FadeIn(z0), Write(z0_label))
        self.wait(0.5)

        # Function f(z) = z^2
        func_text = MathTex("f(z) = z^2", font_size=30).to_edge(UP).shift(DOWN * 0.7)
        self.play(Write(func_text))
        self.wait(0.5)

        # Show f(0) = 0
        calc = MathTex("f(0) = 0^2 = 0", font_size=30)
        calc.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(calc))
        self.wait(1)

        # Show orbit: z_0 -> z_1 -> z_2
        z1 = Dot(point=UP * 0.25, color=RED)
        z1_label = MathTex("z_1", font_size=24).next_to(z1, UR, buff=0.1)
        self.play(Transform(z0, z1), Transform(z0_label, z1_label))
        self.wait(0.5)

        z2 = Dot(point=UP * 0.125, color=RED)
        z2_label = MathTex("z_2", font_size=24).next_to(z2, UR, buff=0.1)
        self.play(Transform(z0, z2), Transform(z0_label, z2_label))
        self.wait(0.5)

        # Show convergence to fixed point
        self.play(
            z0.animate.move_to(ORIGIN),
            z0_label.animate.next_to(origin_dot, UR, buff=0.1)
        )
        self.wait(0.5)

        # Derivative at fixed point
        deriv_text = MathTex("f'(z) = 2z", font_size=30).to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(deriv_text))
        self.wait(0.5)

        multiplier = MathTex("f'(0) = 0", font_size=30).next_to(deriv_text, DOWN, buff=0.2)
        self.play(Write(multiplier))
        self.wait(1)

        # Label for attraction
        attract_label = Text("Stronger than standard attraction", font_size=24).next_to(multiplier, DOWN, buff=0.3).shift(UP * 0.31)
        self.play(Write(attract_label))
        self.wait(1.5)

        # Cleanup
        self.play(
            FadeOut(z0), FadeOut(z0_label), FadeOut(origin_dot),
            FadeOut(origin_label), FadeOut(func_text), FadeOut(calc),
            FadeOut(deriv_text), FadeOut(multiplier), FadeOut(attract_label),
            FadeOut(title), FadeOut(plane)
        )
        self.wait(0.5)
