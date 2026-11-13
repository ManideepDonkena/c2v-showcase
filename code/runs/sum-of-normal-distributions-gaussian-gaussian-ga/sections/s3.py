from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Convolution Process", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Original Gaussian curves
        blue_graph = FunctionGraph(lambda x: 1/2 * np.exp(-0.5*(x-1)**2), color=BLUE, x_range=[-4, 4])
        red_graph = FunctionGraph(lambda x: 1/2 * np.exp(-0.5*(x+1)**2), color=RED, x_range=[-4, 4])
        
        # Semi-transparent
        blue_graph.set_opacity(0.5)
        red_graph.set_opacity(0.5)
        
        self.play(Create(blue_graph), Create(red_graph))
        self.wait(1)

        # Convolution process
        conv_text = Text("Convolution", font_size=24).to_edge(UP).shift(DOWN*0.5)
        self.play(Write(conv_text))
        self.wait(0.5)

        # Green convolution curve
        green_graph = FunctionGraph(
            lambda x: 0.5 * np.exp(-0.5*(x-1)**2) * 0.5 * np.exp(-0.5*(x+1)**2),
            color=GREEN,
            x_range=[-4, 4]
        )
        
        # Show convolution curve being drawn
        green_curve = always_redraw(
            lambda: ParametricFunction(
                lambda t: [t, 0.5 * np.exp(-0.5*(t-1)**2) * 0.5 * np.exp(-0.5*(t+1)**2), 0],
                t_range=[-4, 4],
                color=GREEN,
                stroke_width=3
            )
        )
        
        self.play(Create(green_curve))
        self.wait(1)

        # Fill area under convolution curve
        area = always_redraw(
            lambda: Polygon(
                *[
                    [x, 0.5 * np.exp(-0.5*(x-1)**2) * 0.5 * np.exp(-0.5*(x+1)**2), 0]
                    for x in np.linspace(-4, 4, 100)
                ] + [[4, 0, 0], [-4, 0, 0]],
                color=GREEN,
                fill_opacity=0.3
            )
        )
        
        self.play(Create(area))
        self.wait(2)

        # Final explanation text
        explanation = MathTex(r"\int f(x)g(x)dx", font_size=36)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(blue_graph),
            FadeOut(red_graph),
            FadeOut(green_curve),
            FadeOut(area),
            FadeOut(conv_text),
            FadeOut(explanation)
        )
        self.wait(0.5)
