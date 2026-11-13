from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Wide Pulse", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Time domain Gaussian pulse (wide)
        time_pulse = FunctionGraph(
            lambda x: np.exp(-x**2 / 2),
            x_range=[-3, 3],
            color=BLUE,
            stroke_width=3
        ).shift(DOWN * 1.5)
        time_label = Text("Time Domain", font_size=24).next_to(time_pulse, UP)
        self.play(Create(time_pulse), Write(time_label))
        self.wait(0.5)

        # Frequency domain (narrow)
        freq_pulse = FunctionGraph(
            lambda x: np.exp(-x**2 / 2),
            x_range=[-3, 3],
            color=RED,
            stroke_width=3
        ).shift(UP * 1.5)
        freq_label = Text("Frequency Domain", font_size=24).next_to(freq_pulse, UP)
        self.play(Create(freq_pulse), Write(freq_label))
        self.wait(0.5)

        # Narration text
        narration = Text("A sustained tone has precise pitch.", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        # Area constancy demonstration
        area_text = MathTex(r"\text{Area} = \text{constant}", font_size=30).to_corner(UL)
        self.play(Write(area_text))
        self.wait(1)

        # Pulse width halved, spectrum width doubled
        pulse_half = FunctionGraph(
            lambda x: np.exp(-x**2 / 0.5),
            x_range=[-1.5, 1.5],
            color=BLUE,
            stroke_width=3
        ).shift(DOWN * 1.5)
        spec_double = FunctionGraph(
            lambda x: np.exp(-x**2 / 0.5),
            x_range=[-6, 6],
            color=RED,
            stroke_width=3
        ).shift(UP * 1.5)

        self.play(Transform(time_pulse, pulse_half), Transform(freq_pulse, spec_double))
        self.wait(1)

        # Text: If Δt becomes 1/2, then Δω becomes 2
        ratio_text = Text("If Δt → 1/2, then Δω → 2", font_size=24).to_edge(DOWN)
        self.play(Write(ratio_text))
        self.wait(1.5)
        self.play(FadeOut(ratio_text))

        # As Δt → 0, Δω → ∞
        limit_text = Text("As Δt → 0, Δω → ∞", font_size=24).to_edge(DOWN)
        self.play(Write(limit_text))
        self.wait(1.5)
        self.play(FadeOut(limit_text))

        # Numerical example: Δt × Δω = constant
        const_example = MathTex(r"\Delta t \cdot \Delta \omega = 2 \times 100 = 0.2", font_size=30).to_corner(UL)
        self.play(Transform(area_text, const_example))
        self.wait(1.5)

        # Inverse proportionality: Δt × 4 → Δω ÷ 4
        inverse_text = MathTex(r"\text{If } \Delta t \times 4, \text{ then } \Delta \omega \div 4", font_size=24).to_edge(DOWN)
        self.play(Write(inverse_text))
        self.wait(1.5)
        self.play(FadeOut(inverse_text))

        # Side-by-side comparison: Gaussian vs exponential
        gaussian_pulse = FunctionGraph(
            lambda x: np.exp(-x**2 / 2),
            x_range=[-3, 3],
            color=BLUE,
            stroke_width=3
        ).shift(DOWN * 1.5)
        exp_pulse = FunctionGraph(
            lambda x: np.exp(-abs(x)),
            x_range=[-3, 3],
            color=GREEN,
            stroke_width=3
        ).shift(DOWN * 1.5)

        self.play(Transform(time_pulse, gaussian_pulse))
        self.wait(0.5)
        self.play(Transform(time_pulse, exp_pulse))
        self.wait(0.5)

        comparison_text = Text("Gaussian: minimum product", font_size=24).to_edge(DOWN)
        self.play(Write(comparison_text))
        self.wait(1.5)
        self.play(FadeOut(comparison_text))

        # Zero-padding demonstration
        pad_text = Text("Zero-padding does not narrow lobes", font_size=24).to_edge(DOWN)
        self.play(Write(pad_text))
        self.wait(1.5)
        self.play(FadeOut(pad_text))

        # Brick-wall filter → sinc function
        brick_wall = always_redraw(lambda: Rectangle(width=0.5, height=3, color=RED).shift(UP * 1.5).shift(DOWN * 0.4))
        sinc_func = FunctionGraph(
            lambda x: np.sinc(x),
            x_range=[-6, 6],
            color=BLUE,
            stroke_width=3
        ).shift(DOWN * 1.5)
        self.play(Create(brick_wall), Create(sinc_func))
        self.wait(1.5)

        # Show constant 1/4π
        const_pi = MathTex(r"\frac{1}{4\pi}", font_size=40).to_corner(UR)
        self.play(Write(const_pi))
        self.wait(1.5)

        # Dirac delta → constant spectrum
        delta_pulse = always_redraw(lambda: Line(start=[0, -2, 0], end=[0, 2, 0], color=BLUE))
        const_spectrum = always_redraw(lambda: Line(start=[-3, 0, 0], end=[3, 0, 0], color=RED))
        self.play(Transform(time_pulse, delta_pulse), Transform(freq_pulse, const_spectrum))
        self.wait(1.5)

        # Final summary
        final_text = Text("Uncertainty Principle: Δt·Δω ≥ 1/4π", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)

        self.play(FadeOut(title, time_pulse, freq_pulse, area_text, const_pi, final_text))
