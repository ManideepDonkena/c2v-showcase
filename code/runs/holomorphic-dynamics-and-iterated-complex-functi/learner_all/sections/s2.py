from manim import *

class S2(Scene):
    def construct(self):
        title = Text("The Unit Circle Boundary", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Unit circle
        unit_circle = Circle(radius=1, color=BLUE)
        self.play(Create(unit_circle))
        self.wait(0.5)

        # Points inside and outside
        green_point = Dot(color=GREEN).move_to([0.5, 0, 0])
        red_point = Dot(color=RED).move_to([1.5, 0, 0])
        self.play(FadeIn(green_point), FadeIn(red_point))
        self.wait(0.5)

        # Labels
        inside_label = MathTex("|z_0| < 1", color=GREEN).next_to(green_point, DOWN)
        outside_label = MathTex("|z_0| > 1", color=RED).next_to(red_point, UP)
        inside_label.shift(0.0 * RIGHT + -0.82 * UP)  # layout: separation vector
        outside_label.shift(0.42 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(inside_label), Write(outside_label))
        self.wait(1)

        # Conformal property
        self.play(FadeOut(inside_label), FadeOut(outside_label))
        self.play(green_point.animate.move_to([0.3, 0, 0]), red_point.animate.move_to([2, 0, 0]))
        self.wait(0.5)

        # Critical point breakdown
        critical_point = Dot(color=YELLOW).move_to([1, 0, 0])
        self.play(FadeIn(critical_point))
        self.wait(0.5)
        self.play(critical_point.animate.move_to([0.9, 0.1, 0]))
        self.wait(0.5)

        # Derivative as scaling and rotation
        self.play(FadeOut(critical_point))
        circle = Circle(radius=0.2, color=BLUE).move_to([1, 0, 0])
        self.play(Create(circle))
        self.wait(0.5)
        ellipse = Ellipse(width=0.4, height=0.8, color=RED).move_to([1, 0, 0])
        self.play(Transform(circle, ellipse))
        self.wait(0.5)

        # Derivative value
        derivative_label = MathTex("f'(z) = 2z", "f'(1) = 2").to_edge(DOWN)
        self.play(Write(derivative_label))
        self.wait(1)

        # Conjugacy
        self.play(FadeOut(derivative_label), FadeOut(circle), FadeOut(ellipse))
        func_f = MathTex("f(z) = z^2")
        func_g = MathTex("g(w) = w^2 + c")
        func_f.next_to([0, 1.5, 0], DOWN)
        func_g.next_to([0, -1.5, 0], UP)
        func_f.shift(0.0 * RIGHT + 0.46 * UP)  # layout: separation vector
        self.play(Write(func_f), Write(func_g))
        self.wait(1)

        # Julia set connected vs disconnected
        self.play(FadeOut(func_f), FadeOut(func_g))
        julia_connected = Square(side_length=1, color=BLACK).move_to([-2, 0, 0])
        julia_disconnected = VGroup(*[Dot(color=BLACK).move_to([i*0.1, 0, 0]) for i in range(-5, 6)]).move_to([2, 0, 0])
        self.play(Create(julia_connected), Create(julia_disconnected))
        self.wait(1)

        # Fatou vs Julia
        self.play(FadeOut(julia_connected), FadeOut(julia_disconnected))
        fatou = Circle(radius=0.5, color=BLUE).move_to([-2, 0, 0])
        julia = DashedVMobject(Circle(radius=0.5, color=RED).move_to([2, 0, 0]))
        self.play(Create(fatou), Create(julia))
        self.wait(1)

        # Critical point escape
        self.play(FadeOut(fatou), FadeOut(julia))
        c = ValueTracker(-2)
        orbit_dot = always_redraw(lambda: Dot(color=RED).move_to([c.get_value(), 0, 0]))
        self.play(Create(orbit_dot))
        self.wait(0.5)
        self.play(c.animate.set_value(2), run_time=2)
        self.wait(1)

        # Fixed point
        self.play(FadeOut(orbit_dot))
        fixed_point = Dot(color=GREEN).move_to([0, 0, 0])
        self.play(Create(fixed_point))
        self.wait(0.5)
        multiplier_label = MathTex("f'(0) = 0").next_to(fixed_point, DOWN)
        self.play(Write(multiplier_label))
        self.wait(1)

        # Mandelbrot boundary
        self.play(FadeOut(multiplier_label), FadeOut(fixed_point))
        mandelbrot_boundary = VMobject().set_points_as_corners([*[[i/10, 0, 0] for i in range(-10, 11)], *[[1, i/10, 0] for i in range(10, -11, -1)]])
        self.play(Create(mandelbrot_boundary))
        self.wait(1)

        # Escape to infinity
        escape_dot = Dot(color=RED).move_to([0.5, 0, 0])
        self.play(Create(escape_dot))
        self.wait(0.5)
        self.play(escape_dot.animate.move_to([2.5, 0, 0]), run_time=1)
        self.wait(0.5)

        # Final summary
        self.play(FadeOut(mandelbrot_boundary), FadeOut(escape_dot))
        summary = Text("The boundary is fractal and infinitely complex", font_size=24).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(1)

        self.play(FadeOut(title), FadeOut(summary))
