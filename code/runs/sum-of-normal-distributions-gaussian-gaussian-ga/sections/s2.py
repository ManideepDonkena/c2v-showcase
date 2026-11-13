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
            y_range=[-3.9, 3.9, 1],
            axis_config={"color": WHITE},
        )
        axes.to_edge(DOWN)
        self.play(Create(axes))
        self.wait(0.5)

        # First curve
        self.play(Create(gaussian1), run_time=1)
        self.wait(0.5)

        # Second curve sliding in
        self.play(
            gaussian2.animate.shift(LEFT * 6),
            run_time=2
        )
        self.wait(1)

        # Show overlap
        self.play(
            gaussian2.animate.shift(RIGHT * 2),
            run_time=1
        )
        self.wait(1)

        # Text overlay
        text1 = Text("Independent", font_size=24).to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(text1))
        self.wait(1)
        
        self.play(FadeOut(text1))

        text2 = Text("Superposition", font_size=24).to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(text2))
        self.wait(1)
        
        self.play(FadeOut(text2))

        # Formula
        formula = MathTex("X \\sim N(0, 1)", "\\quad Y \\sim N(2, 4)", "\\quad X + Y \\sim N(2, 5)")
        formula.arrange(DOWN, buff=0.3)
        formula.to_edge(UP)
        formula.shift(0.0 * RIGHT + -0.53 * UP)  # layout: separation vector
        self.play(Write(formula))
        self.wait(2)

        # Fade out
        self.play(
            FadeOut(gaussian1),
            FadeOut(gaussian2),
            FadeOut(axes),
            FadeOut(title),
            FadeOut(formula)
        )
        self.wait(0.5)
