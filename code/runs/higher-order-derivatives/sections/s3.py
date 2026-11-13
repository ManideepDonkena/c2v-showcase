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
            x_range=[0, 10, 1],
            y_range=[-2, 4, 1],
            axis_config={"color": WHITE},
            tips=False,
        )
        axes.to_edge(DOWN)
        x_label = axes.get_x_axis_label("t")
        self.play(Create(axes), Write(x_label))
        self.wait(0.5)

        # f(t) = position
        f_t = axes.plot(lambda t: 0.1 * t**3 - 0.5 * t**2 + 2, color=BLUE)
        f_t_label = MathTex("f(t)", color=BLUE).next_to(f_t, UR)
        self.play(Create(f_t), Write(f_t_label))
        self.wait(0.5)

        # f'(t) = velocity
        f_prime = axes.plot(lambda t: 0.3 * t**2 - t, color=YELLOW)
        f_prime_label = MathTex("f'(t)", color=YELLOW).next_to(f_prime, UR)
        self.play(Create(f_prime), Write(f_prime_label))
        self.wait(0.5)

        # f''(t) = acceleration
        f_double_prime = axes.plot(lambda t: 0.6 * t - 1, color=GREEN)
        f_double_prime_label = MathTex("f''(t)", color=GREEN).next_to(f_double_prime, UR)
        self.play(Create(f_double_prime), Write(f_double_prime_label))
        self.wait(0.5)

        # f'''(t) = jerk
        f_triple_prime = axes.plot(lambda t: 0.6 * np.ones_like(t), color=RED)
        f_triple_prime_label = MathTex("f'''(t)", color=RED).next_to(f_triple_prime, UR)
        self.play(Create(f_triple_prime), Write(f_triple_prime_label))
        self.wait(0.5)

        # Highlight jerk
        jerk_text = Text("Jerk", font_size=24).set_color(RED).to_edge(LEFT).shift(UP*2)
        self.play(Write(jerk_text))
        self.wait(0.5)

        # Slider
        slider = ValueTracker(3)
        dot = always_redraw(
            lambda: Dot(
                point=axes.c2p(slider.get_value(), 0),
                color=WHITE,
                radius=0.1
            )
        )
        self.play(Create(dot))
        self.wait(0.5)

        # Show jerk spike when acceleration changes sharply
        self.play(slider.animate.set_value(5), run_time=2)
        self.wait(0.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(f_t),
            FadeOut(f_prime),
            FadeOut(f_double_prime),
            FadeOut(f_triple_prime),
            FadeOut(f_t_label),
            FadeOut(f_prime_label),
            FadeOut(f_double_prime_label),
            FadeOut(f_triple_prime_label),
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(dot),
            FadeOut(jerk_text)
        )
        self.wait(0.5)
