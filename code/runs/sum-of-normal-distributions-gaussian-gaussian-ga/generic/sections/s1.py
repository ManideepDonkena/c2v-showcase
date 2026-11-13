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
        y_label = axes.get_y_axis_label("y")
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

        # Labels
        mu_label = MathTex(r"\mu = 0", font_size=30)
        mu_label.next_to(normal_curve.get_top(), UP, buff=0.2)
        sigma_label = MathTex(r"\sigma^2 = 1", font_size=30)
        sigma_label.next_to(normal_curve.point_from_proportion(0.7), RIGHT, buff=0.2)

        self.play(FadeIn(mu_label))
        self.wait(0.5)
        self.play(FadeIn(sigma_label))
        self.wait(0.5)

        # Pulse animation
        normal_curve.shift(-0.35 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(
            normal_curve.animate.scale(1.05, about_point=normal_curve.get_top()),
            rate_func=there_and_back,
            run_time=2
        )
        self.wait(0.5)

        # Narration text
        narration = Text("We begin with a standard normal distribution centered at zero.", font_size=24)
        narration.to_edge(UP)
        narration.shift(0.0 * RIGHT + 0.48 * UP)  # layout: separation vector
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        narration2 = Text("This bell curve is defined by its mean, which sets the center,", font_size=24)
        narration2.to_edge(UP)
        narration2.shift(0.0 * RIGHT + 0.48 * UP)  # layout: separation vector
        self.play(Write(narration2))
        self.wait(1.5)
        self.play(FadeOut(narration2))

        narration3 = Text("and its variance, which controls the spread.", font_size=24)
        narration3.to_edge(UP)
        narration3.shift(0.0 * RIGHT + 0.48 * UP)  # layout: separation vector
        self.play(Write(narration3))
        self.wait(1.5)
        self.play(FadeOut(narration3))

        # Final wait
        self.wait(1)
