from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Inscribed Square Problem: A Topological Journey", font_size=24)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Create the simple closed curve
        curve = ParametricFunction(
            lambda t: np.array([
                3 * np.cos(t) + 0.5 * np.cos(3 * t),
                1.5 * np.sin(t) + 0.5 * np.sin(3 * t),
                0
            ]),
            t_range=[0, TAU],
            color=WHITE,
            stroke_width=3
        )
        
        # Animate drawing the curve
        draw_curve = DrawBorderThenFill(curve, run_time=3)
        self.play(draw_curve)
        self.wait(1)

        # Label for the curve
        label = Text("Simple Closed Curve", font_size=24)
        label.next_to(curve, UP, buff=0.3)
        arrow = Arrow(label.get_bottom(), curve.get_top(), buff=0.1, color=YELLOW)
        
        self.play(Write(label), GrowArrow(arrow))
        self.wait(1)

        # Narration text
        narration = Text("We begin with a simple closed curve", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        
        self.play(FadeOut(narration))
        self.wait(0.5)
        
        narration2 = Text("- a continuous loop that doesn't cross itself", font_size=24)
        narration2.to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(1.5)
        
        self.play(FadeOut(narration2))
        self.wait(0.5)
        
        narration3 = Text("This boundary represents the perimeter of any convex shape", font_size=24)
        narration3.to_edge(DOWN)
        self.play(Write(narration3))
        self.wait(1.5)
        
        self.play(FadeOut(narration3))
        self.wait(0.5)
        
        narration4 = Text("setting the stage for our topological inquiry", font_size=24)
        narration4.to_edge(DOWN)
        self.play(Write(narration4))
        self.wait(1.5)
        
        self.play(FadeOut(narration4), FadeOut(title), FadeOut(curve), FadeOut(label), FadeOut(arrow))
        self.wait(0.5)
