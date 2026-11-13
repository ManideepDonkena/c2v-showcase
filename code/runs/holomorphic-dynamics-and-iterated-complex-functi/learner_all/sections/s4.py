from manim import *

class S4(Scene):
    def construct(self):
        title = Text("Holomorphicity and Conformality", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = always_redraw(lambda: NumberPlane(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            axis_config={"stroke_width": 1},
            background_line_style={"stroke_opacity": 0.5}
        ))
        self.play(Create(grid))
        self.wait(0.5)

        # Show conformality
        grid_copy = grid.copy()
        self.play(Transform(grid, grid_copy), run_time=1)
        self.wait(0.5)

        # Critical point demonstration
        critical_point = Dot(color=YELLOW).move_to(ORIGIN)
        self.play(FadeIn(critical_point))
        self.wait(0.5)

        # Zoom in on critical point
        self.play(
            grid.animate.scale(4).move_to(ORIGIN),
            run_time=1
        )
        self.wait(0.5)

        # Show breakdown at critical point
        self.play(FadeOut(critical_point))
        self.wait(0.5)

        # Derivative as scaling and rotation
        circle = Circle(radius=0.2, color=BLUE).move_to(UP * 0.5)
        self.play(Create(circle))
        self.wait(0.5)

        # Show derivative at z=1
        deriv_text = MathTex("f'(z) = 2z", font_size=30).to_edge(DOWN)
        self.play(Write(deriv_text))
        self.wait(0.5)

        # Show multiplier value
        mult_val = MathTex("f'(1) = 2", font_size=30).next_to(deriv_text, DOWN)
        mult_val.shift(0.0 * RIGHT + 0.23 * UP)  # layout: separation vector
        self.play(Write(mult_val))
        self.wait(0.5)

        # Conjugacy example
        self.play(FadeOut(deriv_text), FadeOut(mult_val))

        func_f = MathTex("f(z) = z^2", font_size=30).to_edge(LEFT)
        func_g = MathTex("g(w) = w^2 + c", font_size=30).to_edge(RIGHT)

        self.play(Write(func_f), Write(func_g))
        self.wait(0.5)

        # Julia set connected vs disconnected
        self.play(FadeOut(func_f), FadeOut(func_g))

        # Mandelbrot set boundary
        mandelbrot_boundary = VMobject(color=RED).set_points_as_corners([
            [0, 0, 0],
            [1, 0.5, 0],
            [1.5, 0, 0],
            [1, -0.5, 0],
            [0, 0, 0]
        ])
        self.play(Create(mandelbrot_boundary))
        self.wait(0.5)

        # Show fractal boundary
        self.play(FadeOut(mandelbrot_boundary))

        # Escape to infinity
        escape_dot = Dot(color=RED).move_to(LEFT * 3)
        self.play(FadeIn(escape_dot))
        self.wait(0.5)

        # Orbit convergence
        orbit_converge = always_redraw(lambda: Dot(color=GREEN).move_to(UP * 0.2))
        self.play(Transform(escape_dot, orbit_converge))
        self.wait(0.5)

        # Fixed point at z=0
        fixed_point = MathTex("f(0) = 0^2 = 0", font_size=30).to_edge(DOWN)
        self.play(Write(fixed_point))
        self.wait(0.5)

        # Show multiplier at fixed point z=0
        mult_zero = MathTex("f'(0) = 0", font_size=30).next_to(fixed_point, DOWN)
        mult_zero.shift(0.0 * RIGHT + 0.23 * UP)  # layout: separation vector
        self.play(Write(mult_zero))
        self.wait(0.5)

        self.play(FadeOut(title), FadeOut(grid), FadeOut(escape_dot), FadeOut(fixed_point), FadeOut(mult_zero))
        self.wait(0.5)
