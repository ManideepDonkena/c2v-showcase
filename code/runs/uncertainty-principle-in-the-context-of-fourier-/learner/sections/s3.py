from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Trade-off", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Split screen
        time_pulse = always_redraw(lambda: ParametricFunction(
            lambda t: [t, np.exp(-t**2 / 2), 0],
            t_range=[-2, 2],
            color=BLUE,
            stroke_width=3
        ))
        freq_spectrum = always_redraw(lambda: ParametricFunction(
            lambda w: [w, np.sinc(w/2)**2, 0],
            t_range=[-5, 5],
            color=RED,
            stroke_width=3
        ))

        # Slider for time pulse width
        slider = ValueTracker(1.0)
        def update_pulse(pulse):
            pulse.become(ParametricFunction(
                lambda t: [t, np.exp(-t**2 / (2*(slider.get_value())**2)), 0],
                t_range=[-3, 3],
                color=BLUE,
                stroke_width=3
            ))
        time_pulse.add_updater(update_pulse)

        def update_spectrum(spectrum):
            spectrum.become(ParametricFunction(
                lambda w: [w, np.sinc(w*slider.get_value()/2)**2, 0],
                t_range=[-10, 10],
                color=RED,
                stroke_width=3
            ))
        freq_spectrum.add_updater(update_spectrum)

        # Left and right screen
        left = VGroup(time_pulse).scale(0.5).to_edge(LEFT)
        right = VGroup(freq_spectrum).scale(0.5).to_edge(RIGHT)

        self.play(Create(left), Create(right))
        self.wait(1)

        # Show constant area under curves
        area_time = always_redraw(lambda: Polygon(
            [-3, 0, 0], [-3 + slider.get_value(), 0, 0],
            [-3 + slider.get_value(), np.exp(-slider.get_value()**2 / (2*2)), 0],
            [-3, np.exp(-slider.get_value()**2 / (2*2)), 0],
            color=BLUE, fill_opacity=0.3
        ))
        area_freq = always_redraw(lambda: Polygon(
            [-10, 0, 0], [-10 + 20/slider.get_value(), 0, 0],
            [-10 + 20/slider.get_value(), np.sinc(10*slider.get_value()/2)**2, 0],
            [-10, np.sinc(10*slider.get_value()/2)**2, 0],
            color=RED, fill_opacity=0.3
        ))

        self.play(Create(area_time), Create(area_freq))
        self.wait(1)

        # Show halving Δt and doubling Δω
        self.play(slider.animate.set_value(0.5), run_time=1)
        self.wait(0.5)
        text1 = Text("If Δt becomes 1/2, then Δω becomes 2", font_size=24).to_edge(DOWN)
        self.play(Write(text1))
        self.wait(1)
        self.play(FadeOut(text1))

        # Show limit as Δt → 0
        self.play(slider.animate.set_value(0.1), run_time=1)
        self.wait(0.5)

        # Numerical example: Δt = 2 ms, Δω = 100 Hz
        num_example = MathTex(r"\Delta t \cdot \Delta \omega = 2\,\text{ms} \times 100\,\text{Hz} = 0.2", font_size=30)
        num_example.to_edge(UP)
        self.play(Write(num_example))
        self.wait(1)
        self.play(FadeOut(num_example))

        # Show inverse proportionality: Δt × 4 → Δω ÷ 4
        self.play(slider.animate.set_value(4), run_time=1)
        self.wait(0.5)
        text2 = Text("Δt × 4 → Δω ÷ 4", font_size=24).to_edge(DOWN)
        self.play(Write(text2))
        self.wait(1)
        self.play(FadeOut(text2))

        # Gaussian vs exponential pulse
        gaussian = ParametricFunction(
            lambda t: [t, np.exp(-t**2 / 2), 0],
            t_range=[-3, 3],
            color=BLUE,
            stroke_width=3
        )
        exp_pulse = ParametricFunction(
            lambda t: [t, np.exp(-abs(t)), 0],
            t_range=[-3, 3],
            color=GREEN,
            stroke_width=3
        )

        gauss_spectrum = ParametricFunction(
            lambda w: [w, np.exp(-w**2 / 4), 0],
            t_range=[-5, 5],
            color=BLUE,
            stroke_width=3
        )
        exp_spectrum = ParametricFunction(
            lambda w: [w, 1/(1 + w**2), 0],
            t_range=[-5, 5],
            color=GREEN,
            stroke_width=3
        )

        self.play(FadeOut(left), FadeOut(right))
        self.wait(0.5)

        # Show comparison of area products
        comp_text = Text("Gaussian achieves minimum", font_size=24).to_edge(UP)
        self.play(Write(comp_text))
        self.wait(1)

        # Zero-padding demonstration
        self.play(FadeOut(comp_text))

        # Brick-wall filter example
        brick_filter = always_redraw(lambda: Rectangle(
            width=2, height=1, color=RED, fill_opacity=0.5
        ).move_to(ORIGIN))
        sinc_pulse = ParametricFunction(
            lambda t: [t, np.sinc(t), 0],
            t_range=[-10, 10],
            color=BLUE,
            stroke_width=3
        )
        self.play(Create(brick_filter), Create(sinc_pulse))
        self.wait(1)

        # Final inequality with 1/4π
        final_eq = MathTex(r"\Delta t \cdot \Delta \omega \geq \frac{1}{4\pi}", font_size=36)
        final_eq.to_edge(UP)
        self.play(Write(final_eq))
        self.wait(1)

        # End
        self.play(FadeOut(title), FadeOut(final_eq))
        self.wait(0.5)
