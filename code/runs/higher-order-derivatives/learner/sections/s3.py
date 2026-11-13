from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Higher Order Derivatives: From Velocity to Jerk", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Axes
        axes = Axes(
            x_range=[-2, 4, 1],
            y_range=[-2, 4, 1],
            axis_config={"color": WHITE},
            tips=False,
        )
        axes.to_edge(DOWN)
        self.play(Create(axes))
        self.wait(0.5)

        # f''(t) - acceleration (green)
        acc_graph = axes.plot(lambda x: 0.5 * (x - 1)**2, color=GREEN)
        acc_label = MathTex("f''(t)", color=GREEN).next_to(acc_graph, UR)
        acc_label.shift(-0.33 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(acc_graph), Write(acc_label))
        self.wait(0.5)

        # f'''(t) - jerk (red)
        jerk_graph = axes.plot(lambda x: x - 1, color=RED)
        jerk_label = MathTex("f'''(t)", color=RED).next_to(jerk_graph, UR)
        jerk_graph.shift(0.0 * RIGHT + 0.65 * UP)  # layout: separation vector
        self.play(Create(jerk_graph), Write(jerk_label))
        self.wait(0.5)

        # Label 'Jerk'
        jerk_text = Text("Jerk", font_size=24).next_to(jerk_graph, DL)
        self.play(Write(jerk_text))
        self.wait(0.5)

        # Notation d^3y/dx^3
        notation = MathTex("\\frac{d^3 y}{dx^3}").scale(1.2).next_to(jerk_text, DOWN)
        self.play(Write(notation))
        self.wait(0.5)

        # Slider
        slider_dot = Dot(color=YELLOW).move_to(axes.c2p(0, 0))
        slider_line = always_redraw(
            lambda: Line(
                start=axes.c2p(slider_dot.get_x(), -3),
                end=axes.c2p(slider_dot.get_x(), 3),
                color=YELLOW
            )
        )
        self.play(Create(slider_line), Create(slider_dot))
        self.wait(0.5)

        # Animate slider along the x-axis
        self.play(slider_dot.animate.move_to(axes.c2p(1, 0)), run_time=1)
        self.wait(0.5)
        self.play(slider_dot.animate.move_to(axes.c2p(2, 0)), run_time=1)
        self.wait(0.5)

        # Show example: x^3 -> 6
        example_text = Text("Example: Differentiating x³ three times", font_size=24).to_edge(UP)
        self.play(ReplacementTransform(title, example_text))
        self.wait(0.5)

        # Show steps
        step1 = MathTex("x^3").scale(1.2).to_corner(UL)
        self.play(Write(step1))
        self.wait(0.5)

        step2 = MathTex("3x^2").scale(1.2).next_to(step1, DOWN)
        self.play(ReplacementTransform(step1, step2))
        self.wait(0.5)

        step3 = MathTex("6x").scale(1.2).next_to(step2, DOWN)
        self.play(ReplacementTransform(step2, step3))
        self.wait(0.5)

        step4 = MathTex("6").scale(1.2).next_to(step3, DOWN)
        self.play(ReplacementTransform(step3, step4))
        self.wait(0.5)

        # Fade out
        self.play(
            FadeOut(example_text),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3),
            FadeOut(step4),
            FadeOut(slider_line),
            FadeOut(slider_dot),
            FadeOut(notation),
            FadeOut(jerk_text),
            FadeOut(jerk_label),
            FadeOut(acc_label),
            FadeOut(acc_graph),
            FadeOut(jerk_graph),
            FadeOut(axes),
        )
        self.wait(0.5)
