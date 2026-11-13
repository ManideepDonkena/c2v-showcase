from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Narrow Pulse", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Time Domain Graph (left)
        time_axis = NumberLine(x_range=[-4, 4, 1], include_numbers=True, color=BLUE)
        time_axis.to_edge(LEFT).shift(DOWN * 0.5)
        time_label = Text("Time", font_size=24).next_to(time_axis, DOWN)
        
        # Frequency Domain Graph (right)
        freq_axis = NumberLine(x_range=[-100, 100, 25], include_numbers=True, color=RED)
        freq_axis.to_edge(RIGHT).shift(DOWN * 0.5)
        freq_label = Text("Frequency", font_size=24).next_to(freq_axis, DOWN)

        # Gaussian pulse in time domain
        def gaussian(t, sigma=1):
            return np.exp(-t**2 / (2 * sigma**2))

        pulse = ParametricFunction(
            lambda t: [t, gaussian(t), 0],
            t_range=[-3, 3],
            color=YELLOW,
            stroke_width=4
        )

        # Fourier transform of Gaussian (also Gaussian)
        def fourier_gaussian(w, sigma=1):
            return np.exp(-sigma**2 * w**2 / 2)

        freq_pulse = ParametricFunction(
            lambda w: [w, fourier_gaussian(w), 0],
            t_range=[-50, 50],
            color=PURPLE,
            stroke_width=4
        )

        # Initial setup
        freq_axis.shift(187.18 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(time_axis), Create(freq_axis))
        self.play(Write(time_label), Write(freq_label))
        self.wait(0.5)

        # Show narrow pulse in time domain
        pulse_copy = pulse.copy()
        self.play(Create(pulse_copy))
        self.wait(1)

        # Show corresponding wide spectrum
        freq_pulse_copy = freq_pulse.copy()
        self.play(Create(freq_pulse_copy))
        self.wait(1)

        # Arrows connecting width
        arrow1 = Arrow(start=pulse_copy.get_left(), end=pulse_copy.get_right(), color=GREEN)
        arrow2 = Arrow(start=freq_pulse_copy.get_bottom(), end=freq_pulse_copy.get_top(), color=GREEN)
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.wait(1)

        # Narration text
        narration1 = Text("A sharp click contains a wide range of frequencies.", font_size=24).to_edge(DOWN)
        self.play(Write(narration1))
        self.wait(2)
        self.play(FadeOut(narration1))

        # Demonstrate constant area under curves
        area_text = Text("Area preserved", font_size=24).to_corner(UL)
        self.play(Write(area_text))
        self.wait(1)

        # Halve time width, double frequency width
        half_pulse = ParametricFunction(
            lambda t: [t, gaussian(t, sigma=0.5), 0],
            t_range=[-1.5, 1.5],
            color=YELLOW,
            stroke_width=4
        )
        self.play(Transform(pulse_copy, half_pulse))
        self.wait(0.5)

        double_freq = ParametricFunction(
            lambda w: [w, fourier_gaussian(w, sigma=0.5), 0],
            t_range=[-100, 100],
            color=PURPLE,
            stroke_width=4
        )
        self.play(Transform(freq_pulse_copy, double_freq))
        self.wait(0.5)

        ratio_text = Text("If Δt becomes 1/2, then Δω becomes 2", font_size=24).to_edge(DOWN)
        self.play(Write(ratio_text))
        self.wait(2)
        self.play(FadeOut(ratio_text))

        # Show limit case: Δt → 0, Δω → ∞
        narrow_pulse = ParametricFunction(
            lambda t: [t, gaussian(t, sigma=0.1), 0],
            t_range=[-0.5, 0.5],
            color=YELLOW,
            stroke_width=4
        )
        self.play(Transform(pulse_copy, narrow_pulse))
        self.wait(0.5)

        wide_freq = ParametricFunction(
            lambda w: [w, fourier_gaussian(w, sigma=0.1), 0],
            t_range=[-200, 200],
            color=PURPLE,
            stroke_width=4
        )
        self.play(Transform(freq_pulse_copy, wide_freq))
        self.wait(1)

        limit_text = Text("Δt → 0, Δω → ∞", font_size=24).to_edge(DOWN)
        self.play(Write(limit_text))
        self.wait(2)
        self.play(FadeOut(limit_text))

        # Numerical example: Δt * Δω = constant
        const_example = MathTex(r"\Delta t \cdot \Delta \omega = 2\,\text{ms} \times 100\,\text{Hz} = 0.2", font_size=30)
        const_example.to_edge(DOWN)
        self.play(Write(const_example))
        self.wait(2)
        self.play(FadeOut(const_example))

        # Show inverse proportionality
        inv_prop = MathTex(r"\Delta t \propto \frac{1}{\Delta \omega}", font_size=30)
        inv_prop.to_edge(DOWN)
        self.play(Write(inv_prop))
        self.wait(2)
        self.play(FadeOut(inv_prop))

        # Compare Gaussian vs Exponential
        exp_pulse = ParametricFunction(
            lambda t: [t, np.exp(-abs(t)), 0],
            t_range=[-3, 3],
            color=ORANGE,
            stroke_width=4
        )
        self.play(Transform(pulse_copy, exp_pulse))
        self.wait(1)

        exp_freq = ParametricFunction(
            lambda w: [w, 1 / (1 + w**2), 0],
            t_range=[-50, 50],
            color=PINK,
            stroke_width=4
        )
        self.play(Transform(freq_pulse_copy, exp_freq))
        self.wait(1)

        compare_text = Text("Gaussian achieves minimum", font_size=24).to_edge(DOWN)
        self.play(Write(compare_text))
        self.wait(2)
        self.play(FadeOut(compare_text))

        # Zero-padding demonstration
        pad_text = Text("Zero-padding does not narrow lobes", font_size=24).to_edge(DOWN)
        self.play(Write(pad_text))
        self.wait(2)
        self.play(FadeOut(pad_text))

        # Brick-wall filter → sinc function
        brick_wall = always_redraw(lambda: Line(start=[-50, 0, 0], end=[50, 0, 0], color=RED, stroke_width=4))
        self.play(Create(brick_wall))
        self.wait(1)

        sinc_func = ParametricFunction(
            lambda t: [t, np.sin(t) / t, 0],
            t_range=[-20, 20],
            color=BLUE,
            stroke_width=4
        )
        self.play(Transform(brick_wall, sinc_func))
        self.wait(1)

        filter_text = Text("Brick-wall → sinc", font_size=24).to_edge(DOWN)
        self.play(Write(filter_text))
        self.wait(2)
        self.play(FadeOut(filter_text))

        # Show constant 1/4π
        const_pi = MathTex(r"\frac{1}{4\pi}", font_size=30).to_corner(UR)
        self.play(Write(const_pi))
        self.wait(1)

        const_text = Text("Minimum product is 1/(4π)", font_size=24).to_edge(DOWN)
        self.play(Write(const_text))
        self.wait(2)
        self.play(FadeOut(const_text), FadeOut(const_pi))

        # Dirac delta
        dirac = always_redraw(lambda: Dot(point=[0, 0, 0], color=WHITE))
        self.play(Create(dirac))
        self.wait(1)

        freq_line = Line(start=[-50, 0, 0], end=[50, 0, 0], color=RED, stroke_width=4)
        self.play(Transform(dirac, freq_line))
        self.wait(1)

        dirac_text = Text("Dirac → constant", font_size=24).to_edge(DOWN)
        self.play(Write(dirac_text))
        self.wait(2)
        self.play(FadeOut(dirac_text))

        # Final cleanup
        self.play(FadeOut(title, time_axis, freq_axis, pulse_copy, freq_pulse_copy, arrow1, arrow2, dirac))
        self.wait(0.5)
