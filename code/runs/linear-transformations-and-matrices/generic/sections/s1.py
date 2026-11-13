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
        self.play(Create(axes), run_time=1)
        # Grid lines pulse animation
        grid = always_redraw(lambda: VGroup(*[Line(axes.c2p(-7, y), axes.c2p(7, y), color=GREY, stroke_width=1) for y in np.arange(-3.9, 4, 0.5)] + [Line(axes.c2p(x, -3.9), axes.c2p(x, 3.9), color=GREY, stroke_width=1) for x in np.arange(-7, 8, 0.5)]))
        self.add(grid)
        
        # i-hat vector
        i_hat = Arrow(ORIGIN, RIGHT, color=RED, buff=0)
        i_label = MathTex(r"\hat{i}", color=RED).next_to(i_hat.get_end(), UR, buff=0.1)
        
        # j-hat vector
        j_hat = Arrow(ORIGIN, UP, color=BLUE, buff=0)
        j_label = MathTex(r"\hat{j}", color=BLUE).next_to(j_hat.get_end(), UL, buff=0.1)
        
        # Show vectors
        self.play(GrowArrow(i_hat), Write(i_label), run_time=1)
        self.wait(0.5)
        self.play(GrowArrow(j_hat), Write(j_label), run_time=1)
        self.wait(0.5)

        # Narration text
        narration = Text("Before we transform anything...", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1)
        
        # Clear narration
        self.play(FadeOut(narration))
        
        # More explanation
        explanation = Text("In standard 2D space, every point is built from two fundamental directions:", font_size=24)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(1.5)
        
        # Show i and j directions clearly
        self.play(FadeOut(explanation))
        
        # Add labels for directions
        i_direction = Text("i-hat along x-axis", font_size=24).next_to(i_hat.get_end(), UR, buff=0.2)
        j_direction = Text("j-hat along y-axis", font_size=24).next_to(j_hat.get_end(), UL, buff=0.2)
        
        i_direction.shift(0.19 * RIGHT + 0.0 * UP)  # layout: separation vector
        j_direction.shift(-0.25 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(i_direction), Write(j_direction))
        self.wait(1.5)
        
        # Fade out
        self.play(FadeOut(i_direction), FadeOut(j_direction), FadeOut(i_hat), FadeOut(j_hat), FadeOut(i_label), FadeOut(j_label))
        self.wait(0.5)
        
        # Final title fade
        self.play(FadeOut(title))
        self.wait(0.5)
