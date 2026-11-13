from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Holomorphicity and Conformality", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = always_redraw(lambda: NumberPlane(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            axis_config={"stroke_width": 1},
            background_line_style={"stroke_opacity": 0.5}
        ).scale(1.5).move_to(ORIGIN))

        # Function f(z) = z^2 + c
        def iterate_grid(grid, c=0.3, steps=1):
            # Simple animation of one step of z^2 + c
            return grid.animate.apply_complex_function(lambda z: z**2 + c)

        self.play(Create(grid))
        self.wait(0.5)

        # Show conformality
        self.play(iterate_grid(grid, c=0.3), run_time=1)
        self.wait(0.5)

        # Highlight critical point at z = 0 (where f'(z) = 2z = 0)
        critical_point = Dot(color=RED).move_to(ORIGIN)
        label_critical = MathTex("f'(z) = 2z = 0", font_size=24).next_to(critical_point, DOWN)
        self.play(FadeIn(critical_point), Write(label_critical))
        self.wait(1)

        # Zoom into critical point
        self.play(
            grid.animate.scale(5).move_to(ORIGIN),
            run_time=1
        )
        self.wait(0.5)

        # Show breakdown of conformality at critical point
        self.play(FadeOut(label_critical))
        label_broken = Text("Angles NOT Preserved", font_size=24).next_to(critical_point, DOWN)
        self.play(Write(label_broken))
        self.wait(1)

        # Fade out zoomed grid and return to normal
        self.play(
            FadeOut(grid),
            FadeOut(label_broken),
            FadeOut(critical_point),
            run_time=0.5
        )

        # Show derivative at z = 1
        fixed_point = Dot(color=YELLOW).move_to(UP)
        label_fixed = MathTex("z = 1", font_size=24).next_to(fixed_point, UP)
        self.play(FadeIn(fixed_point), Write(label_fixed))
        self.wait(0.5)

        # Show derivative f'(z) = 2z at z = 1
        derivative_value = MathTex("f'(1) = 2", font_size=30).next_to(fixed_point, DOWN)
        self.play(Write(derivative_value))
        self.wait(0.5)

        # Show mapping of circle to ellipse
        circle = Circle(radius=0.3, color=BLUE).move_to(UP)
        label_circle = MathTex("z", font_size=24).next_to(circle, UR)
        self.play(Create(circle), Write(label_circle))
        self.wait(0.5)

        # Apply f'(1) = 2 to circle
        ellipse = Ellipse(width=0.6, height=1.2, color=GREEN).move_to(UP)
        label_ellipse = MathTex("f'(1) \cdot z = 2z", font_size=24).next_to(ellipse, DOWN)
        self.play(Transform(circle, ellipse), Write(label_ellipse))
        self.wait(1)

        # Show repelling behavior
        repel_label = Text("Repelling Fixed Point", font_size=24).to_edge(DOWN)
        self.play(Write(repel_label))
        self.wait(1)

        # Conjugacy example
        self.play(FadeOut(derivative_value), FadeOut(label_fixed), FadeOut(circle), FadeOut(label_circle), FadeOut(ellipse), FadeOut(label_ellipse), FadeOut(repel_label))

        func_f = MathTex("f(z) = z^2", font_size=30).to_edge(UP)
        func_g = MathTex("g(w) = w^2 + c", font_size=30).next_to(func_f, DOWN)

        self.play(Write(func_f), Write(func_g))
        self.wait(1)

        # Conjugacy map h
        conjugate_map = MathTex("h: f \leftrightarrow g", font_size=24).to_edge(DOWN)
        self.play(Write(conjugate_map))
        self.wait(1)

        self.play(FadeOut(func_f), FadeOut(func_g), FadeOut(conjugate_map))

        # Final summary
        final_text = Text("Conjugacy preserves dynamics", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(FadeOut(final_text), FadeOut(title))
