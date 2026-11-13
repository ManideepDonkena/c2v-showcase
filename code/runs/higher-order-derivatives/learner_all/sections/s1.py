from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The First Derivative: Rate of Change", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Position curve f(t)
        axes = Axes(
            x_range=[-2, 6, 1],
            y_range=[-2, 4, 1],
            axis_config={"color": WHITE},
            tips=False,
        )
        axes.to_edge(DOWN)
        f_t = axes.plot(lambda x: 0.5*(x-2)**2 + 1, color=BLUE)
        f_t_label = MathTex("f(t)", color=BLUE).next_to(f_t, UR)
        
        self.play(Create(axes), run_time=1)
        self.play(Create(f_t), Write(f_t_label), run_time=1.5)
        self.wait(0.5)

        # Tangent line and point
        moving_point = always_redraw(
            lambda: Dot(color=YELLOW).move_to(f_t.point_from_proportion(0.3))
        )
        
        def get_tangent_line():
            # Get the point on the curve
            point = f_t.point_from_proportion(0.3)
            # Compute derivative manually (f'(x) = x - 2)
            dx = 0.3
            slope = dx - 2
            # Create a line with slope and passing through point
            line = Line(
                point + 0.5 * UP,
                point + 0.5 * DOWN,
                color=GREEN
            )
            line.rotate(slope, about_point=point)
            return line

        tangent_line = always_redraw(lambda: get_tangent_line())

        self.play(Create(moving_point), Create(tangent_line), run_time=1)
        self.wait(0.5)

        # Moving point along the curve
        self.play(
            MoveAlongPath(moving_point, f_t, rate_func=linear, run_time=3),
            Rotate(tangent_line, angle=PI/2, about_point=moving_point.get_center(), run_time=3),
            run_time=3
        )
        self.wait(0.5)

        # Show derivative label
        slope_label = always_redraw(
            lambda: MathTex("f'(t)", color=GREEN).move_to(axes.c2p(4, 2))
        )
        self.play(Write(slope_label), run_time=0.5)
        self.wait(1)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(f_t),
            FadeOut(f_t_label),
            FadeOut(moving_point),
            FadeOut(tangent_line),
            FadeOut(slope_label),
            FadeOut(axes),
            run_time=0.5
        )
        self.wait(0.5)
