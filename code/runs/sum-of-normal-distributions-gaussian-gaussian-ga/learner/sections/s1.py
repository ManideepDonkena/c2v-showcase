from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The First Bell", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Axes
        axes = Axes(
            x_range=[-7, 7, 1],
            y_range=[-3.9, 3.9, 1],
            axis_config={"color": WHITE},
        )
        axes_labels = axes.get_axis_labels()
        axes_labels.shift(0.0 * RIGHT + -0.41 * UP)  # layout: separation vector
        self.play(Create(axes), Write(axes_labels))
        self.wait(0.5)

        # Standard normal curve
        normal_curve = axes.plot(
            lambda x: 1 / np.sqrt(2 * PI) * np.exp(-0.5 * x**2),
            color=BLUE,
            stroke_width=4,
        )
        self.play(Create(normal_curve))
        self.wait(0.5)

        # Labels for mean and variance
        mu_label = MathTex(r"\mu = 0", font_size=30).to_edge(UP).shift(DOWN * 0.5)
        sigma2_label = MathTex(r"\sigma^2 = 1", font_size=30).to_edge(UP).shift(DOWN * 1.0)
        
        mu_label.shift(-0.24 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(FadeIn(mu_label))
        self.wait(0.5)
        self.play(FadeIn(sigma2_label))
        self.wait(0.5)

        # Pulse animation
        normal_curve.shift(0.0 * RIGHT + 0.24 * UP)  # layout: separation vector
        self.play(
            normal_curve.animate.scale(1.05, about_point=axes.c2p(0, 0)),
            rate_func=there_and_back,
            run_time=2
        )
        self.wait(0.5)

        # Fade out labels
        self.play(FadeOut(mu_label), FadeOut(sigma2_label))
        self.wait(0.5)

        # Shift the curve by adding constant c
        c = 2
        shifted_curve = axes.plot(
            lambda x: 1 / np.sqrt(2 * PI) * np.exp(-0.5 * (x - c)**2),
            color=BLUE,
            stroke_width=4,
        )
        
        # Show shift
        self.play(Transform(normal_curve, shifted_curve))
        self.wait(0.5)

        # New labels for shifted curve
        new_mu_label = MathTex(r"\mu = 2", font_size=30).to_edge(UP).shift(DOWN * 0.5)
        self.play(FadeIn(new_mu_label))
        self.wait(0.5)

        # Narration text
        narration = Text("Adding a constant moves the center but does not stretch or compress the distribution, so the variance stays exactly the same.", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(3)

        self.play(FadeOut(narration), FadeOut(new_mu_label), FadeOut(title), FadeOut(axes), FadeOut(normal_curve))
        self.wait(0.5)
