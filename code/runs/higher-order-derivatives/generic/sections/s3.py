from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Third Derivative: Jerk", font_size=36)
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

        # f(t) - position
        f_t = axes.plot(lambda t: 0.1 * t**3 - 0.5 * t**2 + 2, color=BLUE)
        f_t_label = MathTex("f(t)", color=BLUE).next_to(f_t, UR)
        self.play(Create(f_t), Write(f_t_label))
        self.wait(0.5)

        # f'(t) - velocity
        f_prime = axes.plot(lambda t: 0.3 * t**2 - t, color=YELLOW)
        f_prime_label = MathTex("f'(t)", color=YELLOW).next_to(f_prime, UR)
        self.play(Create(f_prime), Write(f_prime_label))
        self.wait(0.5)

        # f''(t) - acceleration
        f_double_prime = axes.plot(lambda t: 0.6 * t - 1, color=GREEN)
        f_double_prime_label = MathTex("f''(t)", color=GREEN).next_to(f_double_prime, UR)
        self.play(Create(f_double_prime), Write(f_double_prime_label))
        self.wait(0.5)

        # f'''(t) - jerk
        f_triple_prime = axes.plot(lambda t: 0.6 * np.ones_like(t), color=RED)
        f_triple_prime_label = MathTex("f'''(t)", color=RED).next_to(f_triple_prime, UR)
        self.play(Create(f_triple_prime), Write(f_triple_prime_label))
        self.wait(0.5)

        # Highlight jerk
        jerk_text = Text("Jerk", font_size=24).set_color(RED).to_edge(LEFT).shift(UP*2)
        self.play(Write(jerk_text))
        self.wait(0.5)

        # Slider
        slider = ValueTracker(2)
        slider_dot = always_redraw(
            lambda: Dot(axes.c2p(slider.get_value(), 0), color=WHITE)
        )
        self.play(Create(slider_dot))
        self.wait(0.5)

        # Animate slider
        self.play(slider.animate.set_value(5), run_time=3)
        self.wait(1)

        # Show spike in jerk when acceleration changes rapidly
        self.play(slider.animate.set_value(7), run_time=2)
        self.wait(1)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(f_t),
            FadeOut(f_prime),
            FadeOut(f_double_prime),
            FadeOut(f_triple_prime),
            FadeOut(f_t_label),
            FadeOut(f_prime_label),
            FadeOut(f_double_prime_label),
            FadeOut(f_triple_prime_label),
            FadeOut(slider_dot),
            FadeOut(jerk_text)
        )
        self.wait(0.5)

        # Final text
        final_text = Text("But acceleration doesn't change smoothly in real life.", font_size=24)
        final_text.to_edge(UP)
        self.play(Write(final_text))
        self.wait(1)

        final_text2 = Text("The third derivative, known as jerk, measures how abruptly acceleration changes.", font_size=24)
        final_text2.next_to(final_text, DOWN)
        self.play(Write(final_text2))
        self.wait(1)

        final_text3 = Text("High jerk means a sudden, jarring shift in force.", font_size=24)
        final_text3.next_to(final_text2, DOWN)
        self.play(Write(final_text3))
        self.wait(1)

        self.play(FadeOut(final_text), FadeOut(final_text2), FadeOut(final_text3))
        self.wait(0.5)
