from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Convolution Process", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Original functions
        x = np.linspace(-4, 4, 100)
        blue_func = lambda x: np.exp(-0.5 * (x - 1)**2) / np.sqrt(2 * np.pi)
        red_func = lambda x: np.exp(-0.5 * (x + 1)**2) / np.sqrt(2 * np.pi)
        
        blue_graph = ParametricFunction(
            lambda t: np.array([t, blue_func(t), 0]),
            t_range=[-4, 4],
            color=BLUE,
            stroke_width=3
        )
        red_graph = ParametricFunction(
            lambda t: np.array([t, red_func(t), 0]),
            t_range=[-4, 4],
            color=RED,
            stroke_width=3
        )
        
        # Semi-transparent
        blue_graph.set_opacity(0.5)
        red_graph.set_opacity(0.5)
        
        self.play(Create(blue_graph), Create(red_graph))
        self.wait(1)

        # Convolution integral visualization
        conv_text = Text("Convolution", font_size=24).to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(conv_text))
        self.wait(0.5)
        
        # Show convolution process
        green_func = lambda t: 0.5 * (blue_func(t-2) + blue_func(t-1) + blue_func(t) + blue_func(t+1))
        green_graph = ParametricFunction(
            lambda t: np.array([t, green_func(t), 0]),
            t_range=[-4, 4],
            color=GREEN,
            stroke_width=3
        )
        
        # Create area under convolution curve
        area = always_redraw(
            lambda: Polygon(
                *[np.array([x[i], 0, 0]) for i in range(len(x)) if x[i] <= 0.5],
                np.array([0.5, 0, 0]),
                np.array([0.5, green_func(0.5), 0]),
                color=GREEN,
                fill_opacity=0.3
            )
        )
        
        self.play(Create(green_graph), run_time=2)
        self.wait(1)
        
        # Show accumulation
        self.play(Create(area), run_time=2)
        self.wait(1.5)
        
        # Final explanation
        explanation = MathTex(r"\int_{-\infty}^{\infty} f(t)g(x-t)dt", font_size=30)
        explanation.next_to(title, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(2)
        
        # Clean up
        self.play(FadeOut(title), FadeOut(conv_text), FadeOut(blue_graph), 
                  FadeOut(red_graph), FadeOut(green_graph), FadeOut(area), FadeOut(explanation))
        self.wait(0.5)
