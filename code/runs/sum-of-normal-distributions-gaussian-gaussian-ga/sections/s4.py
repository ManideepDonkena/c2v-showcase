from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Resulting Gaussian", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Original Gaussians
        mu1, sigma1 = 0, 1
        mu2, sigma2 = 2, 2
        # Create the two original curves
        blue_graph = ParametricFunction(
            lambda t: (t, np.exp(-0.5 * ((t - mu1) / sigma1)**2) / (sigma1 * np.sqrt(2 * PI)), 0),
            t_range=[-4, 4],
            color=BLUE,
            stroke_width=3
        )
        red_graph = ParametricFunction(
            lambda t: (t, np.exp(-0.5 * ((t - mu2) / sigma2)**2) / (sigma2 * np.sqrt(2 * PI)), 0),
            t_range=[-4, 4],
            color=RED,
            stroke_width=3
        )
        # Axes
        axes = Axes(
            x_range=[-7, 7, 1],
            y_range=[0, 0.5, 0.1],
            axis_config={"color": WHITE},
        )
        axes.to_edge(DOWN)
        self.play(Create(axes))
        self.play(Create(blue_graph), Create(red_graph))
        self.wait(1)

        # Fade out original curves
        self.play(FadeOut(blue_graph), FadeOut(red_graph))
        self.wait(0.5)

        # Resulting Gaussian
        mu_sum = mu1 + mu2
        sigma_sum_squared = sigma1**2 + sigma2**2
        sigma_sum = np.sqrt(sigma_sum_squared)
        
        green_graph = ParametricFunction(
            lambda t: (t, np.exp(-0.5 * ((t - mu_sum) / sigma_sum)**2) / (sigma_sum * np.sqrt(2 * PI)), 0),
            t_range=[-7, 7],
            color=GREEN,
            stroke_width=4
        )
        
        self.play(Create(green_graph))
        self.wait(1)

        # Labels for mean and variance
        mu_label = MathTex(r"\mu_{\text{new}} = 0 + 2 = 2", font_size=30)
        mu_label.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(mu_label))
        self.wait(1)

        sigma_label = MathTex(r"\sigma^2_{\text{new}} = 1 + 4 = 5", font_size=30)
        sigma_label.next_to(mu_label, DOWN)
        self.play(Write(sigma_label))
        self.wait(1.5)

        # Fade out labels
        self.play(FadeOut(mu_label), FadeOut(sigma_label))
        self.wait(0.5)

        # Final narration text
        final_text = Text("The result is another perfect Gaussian distribution.", font_size=24)
        final_text.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(final_text))
        self.wait(1)

        # Fade out title and final text
        self.play(FadeOut(title), FadeOut(final_text))
        self.wait(0.5)
