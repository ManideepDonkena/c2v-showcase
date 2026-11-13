from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The First Bell", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        # Axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            axis_config={'include_tip': False},
        )
        axes.to_edge(DOWN)
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("f(x)")
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # Standard normal curve
        normal_curve = axes.plot(
            lambda x: 1 / np.sqrt(2 * PI) * np.exp(-0.5 * x**2),
            color=BLUE,
            stroke_width=4,
        )
        self.play(Create(normal_curve))
        self.wait(0.5)

        # Pulse animation
        normal_curve.shift(-0.35 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(
            normal_curve.animate.scale(1.05, about_point=axes.c2p(0, 0.4)),
            run_time=1,
        )
        self.play(
            normal_curve.animate.scale(1/1.05, about_point=axes.c2p(0, 0.4)),
            run_time=1,
        )
        self.wait(0.5)

        # Mean label
        mu_label = MathTex(r"\mu = 0", font_size=30)
        mu_label.next_to(axes.c2p(0, 0.4), UP)
        self.play(FadeIn(mu_label))
        self.wait(1)

        # Variance label
        sigma_label = MathTex(r"\sigma^2 = 1", font_size=30)
        sigma_label.next_to(axes.c2p(0, 0.1), DOWN)
        self.play(FadeIn(sigma_label))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(normal_curve),
            FadeOut(mu_label),
            FadeOut(sigma_label),
        )
        self.wait(0.5)
