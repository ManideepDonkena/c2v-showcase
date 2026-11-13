from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Defining the Contour", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Draw simple closed curve
        curve = ParametricFunction(
            lambda t: np.array([
                3 * np.cos(t) + 0.5 * np.cos(3*t),
                2 * np.sin(t) + 0.5 * np.sin(3*t),
                0
            ]),
            t_range=[0, TAU],
            color=WHITE,
            stroke_width=3
        )
        # Animate drawing the curve
        self.play(Create(curve), run_time=3)
        self.wait(1)

        # Label
        label = Text("Simple Closed Curve", font_size=24).next_to(curve, UP)
        arrow = Arrow(label.get_bottom(), curve.get_top(), buff=0.1)
        self.play(Write(label), GrowArrow(arrow))
        self.wait(1)

        # Narration text
        narration = Text("We begin with a simple closed curve", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)

        # Clear narration and add more explanation
        self.play(FadeOut(narration))
        narration2 = Text("a continuous loop that doesn't cross itself", font_size=24).to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(1.5)

        # Clear and fade out
        self.play(FadeOut(label), FadeOut(arrow), FadeOut(curve), FadeOut(narration2), FadeOut(title))
        self.wait(0.5)
