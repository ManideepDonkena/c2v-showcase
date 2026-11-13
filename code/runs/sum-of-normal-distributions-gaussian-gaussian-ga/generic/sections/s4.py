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
        
        # Create the two original Gaussian curves
        gaussian1 = ParametricFunction(
            lambda t: np.array([t, np.exp(-0.5 * ((t - mu1)/sigma1)**2) / (sigma1 * np.sqrt(2 * PI)), 0]),
            t_range=[-4, 4],
            color=BLUE
        )
        gaussian2 = ParametricFunction(
            lambda t: np.array([t, np.exp(-0.5 * ((t - mu2)/sigma2)**2) / (sigma2 * np.sqrt(2 * PI)), 0]),
            t_range=[-4, 8],
            color=RED
        )

        # Add original curves to scene
        gaussian2.shift(-1.04 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(gaussian1), Create(gaussian2))
        self.wait(1)

        # Show the convolution result as a new Gaussian
        mu_sum = mu1 + mu2
        sigma_sum_squared = sigma1**2 + sigma2**2
        sigma_sum = np.sqrt(sigma_sum_squared)
        
        gaussian_sum = ParametricFunction(
            lambda t: np.array([t, np.exp(-0.5 * ((t - mu_sum)/sigma_sum)**2) / (sigma_sum * np.sqrt(2 * PI)), 0]),
            t_range=[-6, 10],
            color=GREEN,
            stroke_width=5
        )

        # Animate the solidification of the new Gaussian
        self.play(Transform(gaussian1, gaussian_sum), Transform(gaussian2, gaussian_sum))
        self.wait(1)

        # Fade out original curves
        self.play(FadeOut(gaussian1), FadeOut(gaussian2))
        self.wait(0.5)

        # Show labels for mean and variance
        mean_label = MathTex(r"\mu_{\text{new}} = 0 + 2 = 2", font_size=30)
        mean_label.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(mean_label))
        self.wait(1)

        var_label = MathTex(r"\sigma^2_{\text{new}} = 1 + 4 = 5", font_size=30)
        var_label.next_to(mean_label, DOWN)
        self.play(Write(var_label))
        self.wait(1.5)

        # Fade out labels
        self.play(FadeOut(mean_label), FadeOut(var_label))
        self.wait(0.5)

        # Show closure property text
        closure_text = Text("Gaussians are closed under addition", font_size=24)
        closure_text.to_edge(DOWN)
        self.play(Write(closure_text))
        self.wait(1.5)

        # Fade out title and closure text
        self.play(FadeOut(title), FadeOut(closure_text))
        self.wait(0.5)
