from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Quantum Connection", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Axes setup
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 1.2, 0.2],
            axis_config={"color": WHITE},
            tips=False,
        ).to_edge(UP).shift(DOWN)
        x_label = axes.get_x_axis_label("x").set_color(YELLOW)
        y_label = axes.get_y_axis_label(r"\psi(x)").set_color(YELLOW)
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # Add momentum axis
        axes2 = Axes(
            x_range=[-8, 8, 1],
            y_range=[0, 1.2, 0.2],
            axis_config={"color": WHITE},
            tips=False,
        ).scale(0.8).to_edge(DOWN).shift(3 * UP)
        k_label = axes2.get_x_axis_label("k").set_color(RED)
        y_label_k = axes2.get_y_axis_label(r"\tilde{\psi}(k)").set_color(RED)
        self.play(Create(axes2), Write(k_label), Write(y_label_k))
        self.wait(0.5)

        # Fourier transform of Gaussian
        gaussian1 = axes.plot(lambda x: np.exp(-x**2 / 2), color=BLUE)
        gaussian1_label = MathTex(r"\psi(x)", color=BLUE).next_to(gaussian1, UP, buff=0.2)
        self.play(Create(gaussian1), Write(gaussian1_label))
        self.wait(0.5)

        gaussian2 = axes2.plot(lambda k: np.exp(-k**2 / 2), color=RED)
        gaussian2_label = MathTex(r"\tilde{\psi}(k)", color=RED).next_to(gaussian2, UP, buff=0.2)
        self.play(Create(gaussian2), Write(gaussian2_label))
        self.wait(0.5)

        # Uncertainty inequality
        uncertainty = MathTex(r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}").to_edge(UP).shift(DOWN)
        self.play(Write(uncertainty))
        self.wait(1)

        # Demonstration: pulse width halved, spectrum width doubled
        self.play(FadeOut(gaussian1), FadeOut(gaussian2))

        # Time-domain pulse (narrower)
        narrow_pulse = axes.plot(lambda x: np.exp(-4 * x**2 / 2), color=BLUE)
        narrow_label = MathTex(r"\psi(x)", color=BLUE).next_to(narrow_pulse, UP, buff=0.2)
        self.play(Create(narrow_pulse), Write(narrow_label))
        self.wait(0.5)

        # Frequency-domain pulse (wider)
        wide_spectrum = axes2.plot(lambda k: np.exp(-k**2 / 8), color=RED)
        wide_label = MathTex(r"\tilde{\psi}(k)", color=RED).next_to(wide_spectrum, UP, buff=0.2)
        self.play(Create(wide_spectrum), Write(wide_label))
        self.wait(0.5)

        # Text: If Δt becomes 1/2, then Δω becomes 2
        text = Text("If Δt becomes 1/2, then Δω becomes 2", font_size=24).to_edge(DOWN)
        self.play(Write(text))
        self.wait(1.5)
        self.play(FadeOut(text))

        # Show limit: as Δt → 0, Δω → ∞
        self.play(FadeOut(narrow_pulse), FadeOut(wide_spectrum))
        narrowest = axes.plot(lambda x: np.exp(-16 * x**2 / 2), color=BLUE)
        widest = axes2.plot(lambda k: np.exp(-k**2 / 32), color=RED)
        self.play(Create(narrowest), Create(widest))
        self.wait(0.5)

        # Numerical example
        example_text = Text("Δt = 2 ms, Δω = 100 Hz → Product = 0.2", font_size=24).to_edge(DOWN)
        self.play(Write(example_text))
        self.wait(1.5)
        self.play(FadeOut(example_text))

        # Show inverse proportionality
        example2 = Text("If Δt × 4, then Δω ÷ 4", font_size=24).to_edge(DOWN)
        self.play(Write(example2))
        self.wait(1.5)
        self.play(FadeOut(example2))

        # Side-by-side comparison: Gaussian vs exponential
        self.play(FadeOut(narrowest), FadeOut(widest))

        exp_pulse = axes.plot(lambda x: np.exp(-x**2 / 2) * np.exp(-x**2 / 4), color=ORANGE)
        exp_label = MathTex(r"\text{Exponential}", color=ORANGE).next_to(exp_pulse, UP, buff=0.2)
        self.play(Create(exp_pulse), Write(exp_label))
        self.wait(0.5)

        # Show that Gaussian achieves minimum
        min_text = Text("Gaussian: minimum product", font_size=24).to_edge(DOWN)
        self.play(Write(min_text))
        self.wait(1.5)
        self.play(FadeOut(min_text))

        # Zero-padding demo
        self.play(FadeOut(exp_pulse), FadeOut(exp_label))

        # Show brick-wall filter → sinc function
        rect = axes.plot(lambda x: 1 if -0.5 <= x <= 0.5 else 0, color=GREEN)
        rect_label = MathTex(r"\text{Rectangular}").next_to(rect, UP, buff=0.2)
        self.play(Create(rect), Write(rect_label))
        self.wait(0.5)

        sinc = axes2.plot(lambda k: np.sin(k) / k, color=PURPLE)
        sinc_label = MathTex(r"\text{sinc}(k)").next_to(sinc, UP, buff=0.2)
        self.play(Create(sinc), Write(sinc_label))
        self.wait(1)

        # Show constant 1/4π
        const_text = MathTex(r"\Delta x \cdot \Delta p \geq \frac{1}{4\pi}").to_edge(UP).shift(DOWN)
        self.play(Transform(uncertainty, const_text))
        self.wait(1.5)

        # Dirac delta example
        self.play(FadeOut(rect), FadeOut(sinc), FadeOut(rect_label), FadeOut(sinc_label))

        delta = axes.plot(lambda x: 0 if x != 0 else 10, color=YELLOW)
        delta_label = MathTex(r"\delta(t)").next_to(delta, UP, buff=0.2)
        self.play(Create(delta), Write(delta_label))
        self.wait(0.5)

        # Fourier transform of delta
        flat_line = axes2.plot(lambda k: 1, color=WHITE)
        flat_label = MathTex(r"1").next_to(flat_line, UP, buff=0.2)
        self.play(Create(flat_line), Write(flat_label))
        self.wait(1)

        # Final summary
        final_text = Text("Quantum particles obey same math as waves", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)
        self.play(FadeOut(final_text))

        self.play(FadeOut(title), FadeOut(axes), FadeOut(axes2), FadeOut(uncertainty), FadeOut(delta), FadeOut(flat_line), FadeOut(delta_label), FadeOut(flat_label))
