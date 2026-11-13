from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Second Bell", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First Gaussian: N(0, 1)
        x = np.linspace(-7, 7, 100)
        y1 = np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)
        graph1 = ParametricFunction(
            lambda t: np.array([t, y1[np.argmin(np.abs(x - t))], 0]),
            t_range=[-7, 7],
            color=BLUE
        )
        graph1.shift(2 * DOWN)
        self.play(Create(graph1), run_time=1)

        # Second Gaussian: N(2, 4) - wider and shifted
        y2 = np.exp(-(x - 2)**2 / 8) / (2 * np.sqrt(2 * np.pi))
        graph2 = ParametricFunction(
            lambda t: np.array([t, y2[np.argmin(np.abs(x - t))], 0]),
            t_range=[-7, 7],
            color=RED
        )
        graph2.shift(2 * DOWN)
        self.play(Create(graph2), run_time=1)

        # Show overlap
        self.wait(1)

        # Text: introduce second variable
        text1 = Text("Now introduce a second independent normal variable", font_size=24)
        text1.to_edge(DOWN)
        self.play(Write(text1))
        self.wait(2)
        self.play(FadeOut(text1))

        # Show sum of two independent Gaussians
        y_sum = y1 + y2
        graph_sum = ParametricFunction(
            lambda t: np.array([t, y_sum[np.argmin(np.abs(x - t))], 0]),
            t_range=[-7, 7],
            color=YELLOW
        )
        graph_sum.shift(2 * DOWN)
        self.play(Create(graph_sum), run_time=1)

        # Text: sum behavior
        text2 = Text("When we consider the sum of these two independent variables", font_size=24)
        text2.to_edge(DOWN)
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(text2))

        # Show perfectly correlated case: Y = X
        y_correlated = 2 * y1
        graph_correlated = ParametricFunction(
            lambda t: np.array([t, y_correlated[np.argmin(np.abs(x - t))], 0]),
            t_range=[-7, 7],
            color=GREEN
        )
        graph_correlated.shift(2 * DOWN)
        self.play(Transform(graph_sum, graph_correlated), run_time=1)

        # Text: correlated case
        text3 = Text("If Y = X, sum is scaled version of one curve", font_size=24)
        text3.to_edge(DOWN)
        self.play(Write(text3))
        self.wait(2)
        self.play(FadeOut(text3))

        # Contrast with independent case
        self.play(Transform(graph_correlated, graph_sum), run_time=1)

        # Text: independence required
        text4 = Text("Independence is required for variance addition rule", font_size=24)
        text4.to_edge(DOWN)
        self.play(Write(text4))
        self.wait(2)
        self.play(FadeOut(text4))

        # Fade out all
        self.play(
            FadeOut(graph1),
            FadeOut(graph2),
            FadeOut(graph_sum),
            FadeOut(title),
            run_time=1
        )
