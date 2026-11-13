from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Second Bell", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First Gaussian curve (blue)
        gaussian1 = FunctionGraph(
            lambda x: 1/2 * np.exp(-0.5 * (x - 0)**2),
            x_range=[-4, 4],
            color=BLUE
        )
        gaussian1.shift(UP * 0.5)
        
        # Second Gaussian curve (red) - initially off-screen
        gaussian2 = FunctionGraph(
            lambda x: 1/4 * np.exp(-0.5 * (x - 2)**2),
            x_range=[-4, 6],
            color=RED
        )
        gaussian2.shift(UP * 0.5)
        
        # Axes
        axes = Axes(
            x_range=[-7, 7, 1],
            y_range=[0, 1, 0.2],
            axis_config={"color": WHITE},
        )
        axes.to_edge(DOWN)
        axes_labels = axes.get_axis_labels()
        
        # Initial setup
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(gaussian1))
        self.wait(1)
        
        # Slide in second curve
        self.play(
            gaussian2.animate.shift(LEFT * 6),
            run_time=3
        )
        self.wait(1)
        
        # Show labels for means and variances
        mean1_label = MathTex(r"\mu_1 = 0", font_size=24).next_to(gaussian1, DOWN)
        var1_label = MathTex(r"\sigma_1^2 = 1", font_size=24).next_to(mean1_label, DOWN)
        
        mean2_label = MathTex(r"\mu_2 = 2", font_size=24).next_to(gaussian2, DOWN)
        var2_label = MathTex(r"\sigma_2^2 = 4", font_size=24).next_to(mean2_label, DOWN)
        
        self.play(Write(mean1_label), Write(var1_label))
        self.wait(0.5)
        self.play(Write(mean2_label), Write(var2_label))
        self.wait(1.5)
        
        # Show convolution
        convolution = FunctionGraph(
            lambda x: 1/2 * np.exp(-0.5 * (x - 0)**2) + 1/4 * np.exp(-0.5 * (x - 2)**2),
            x_range=[-7, 7],
            color=YELLOW
        )
        convolution.shift(UP * 0.5)
        
        # Text overlay
        text1 = Text("Independent", font_size=24).to_corner(UL)
        text2 = Text("Superposition", font_size=24).next_to(text1, DOWN)
        
        self.play(FadeOut(mean1_label), FadeOut(var1_label), 
                  FadeOut(mean2_label), FadeOut(var2_label))
        self.wait(0.5)
        
        text2.shift(0.0 * RIGHT + 0.24 * UP)  # layout: separation vector
        self.play(Write(text1), Write(text2))
        self.wait(1)
        
        # Show convolution
        self.play(Create(convolution), run_time=2)
        self.wait(1.5)
        
        # Final text
        final_text = Text("Sum of independent normal variables", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)
        
        self.play(FadeOut(title), FadeOut(axes), FadeOut(gaussian1), 
                  FadeOut(gaussian2), FadeOut(convolution), FadeOut(text1), 
                  FadeOut(text2), FadeOut(final_text))
        self.wait(0.5)
