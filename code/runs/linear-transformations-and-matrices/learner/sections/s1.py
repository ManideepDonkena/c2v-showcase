from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Basis Vectors", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Create coordinate system
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            axis_config={"stroke_color": GREY},
            tips=False
        )
        axes.scale(0.8)
        axes.shift(DOWN * 0.5)
        
        # Grid lines
        grid = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_opacity": 0.2},
            faded_line_ratio=1
        )
        
        # Add grid and axes
        self.play(Create(axes), run_time=1)
        self.play(Create(grid), run_time=1)
        
        # i-hat vector (red)
        i_hat = Arrow(ORIGIN, RIGHT, color=RED, buff=0)
        i_label = MathTex(r"\hat{i}", color=RED).next_to(i_hat.get_end(), UR, buff=0.1)
        
        # j-hat vector (blue)
        j_hat = Arrow(ORIGIN, UP, color=BLUE, buff=0)
        j_label = MathTex(r"\hat{j}", color=BLUE).next_to(j_hat.get_end(), UR, buff=0.1)
        
        # Show basis vectors
        self.play(GrowArrow(i_hat), Write(i_label), run_time=1)
        self.wait(0.5)
        self.play(GrowArrow(j_hat), Write(j_label), run_time=1)
        self.wait(1)
        
        # Pulsing grid effect
        def pulse_grid():
            return grid.animate.scale(1.02).set_opacity(0.3).scale(1/1.02).set_opacity(0.2)
        
        self.play(AnimationGroup(pulse_grid, run_time=4, rate_func=linear))
        
        # Narration text
        narration = Text("Before we transform anything...", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration), run_time=1)
        self.wait(1.5)
        
        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(grid),
            FadeOut(i_hat),
            FadeOut(j_hat),
            FadeOut(i_label),
            FadeOut(j_label),
            FadeOut(narration),
            run_time=1
        )
