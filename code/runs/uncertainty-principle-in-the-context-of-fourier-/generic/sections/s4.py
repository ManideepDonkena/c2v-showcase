from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Quantum Connection", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial axes with labels
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 1.2, 0.2],
            axis_config={"stroke_color": WHITE},
            tips=False,
        )
        axes.to_edge(DOWN)
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("\\psi(x)")
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # Gaussian curve
        gaussian = axes.plot(lambda x: np.exp(-x**2 / 2), color=BLUE)
        gaussian_label = MathTex(r"\psi(x)", font_size=24).next_to(gaussian, UP)
        self.play(Create(gaussian), Write(gaussian_label))
        self.wait(0.5)

        # Change x to position
        self.play(
            Transform(x_label, axes.get_x_axis_label("x")),
            run_time=1
        )
        self.wait(0.5)

        # Add momentum axis (k)
        k_axes = Axes(
            x_range=[0, 3.5, 0.5],
            y_range=[0, 1.2, 0.2],
            axis_config={"stroke_color": WHITE},
            tips=False,
        )
        k_axes.to_edge(DOWN)
        k_label = k_axes.get_x_axis_label("k")
        k_y_label = k_axes.get_y_axis_label("\\Phi(k)")
        self.play(Create(k_axes), Write(k_label), Write(k_y_label))
        self.wait(0.5)

        # Transform to momentum space
        gaussian_k = k_axes.plot(lambda x: np.exp(-x**2 / 2), color=RED)
        gaussian_k_label = MathTex(r"\Phi(k)", font_size=24).next_to(gaussian_k, UP)
        self.play(Create(gaussian_k), Write(gaussian_k_label))
        self.wait(0.5)

        # Show uncertainty principle
        inequality = MathTex(r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}", font_size=32)
        inequality.to_edge(UP)
        self.play(Transform(title, inequality))
        self.wait(1)

        # Narration text - positioned above axes to avoid overlap
        narration1 = Text("In quantum mechanics", font_size=24).to_corner(UL)
        self.play(Write(narration1))
        self.wait(1.5)
        self.play(FadeOut(narration1))

        narration2 = Text("particles are described by wave functions", font_size=24).to_corner(UL)
        self.play(Write(narration2))
        self.wait(1.5)
        self.play(FadeOut(narration2))

        narration3 = Text("Just like sound waves", font_size=24).to_corner(UL)
        self.play(Write(narration3))
        self.wait(1.5)
        self.play(FadeOut(narration3))

        narration4 = Text("This is not a limitation of measurement", font_size=24).to_corner(UL)
        self.play(Write(narration4))
        self.wait(1.5)
        self.play(FadeOut(narration4))

        narration5 = Text("but a fundamental property of nature", font_size=24).to_corner(UL)
        self.play(Write(narration5))
        self.wait(1.5)
        self.play(FadeOut(narration5))

        # Final fade out
        self.play(
            FadeOut(axes),
            FadeOut(k_axes),
            FadeOut(gaussian),
            FadeOut(gaussian_k),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(k_label),
            FadeOut(k_y_label),
            FadeOut(gaussian_label),
            FadeOut(gaussian_k_label),
            FadeOut(title)
        )
        self.wait(0.5)
