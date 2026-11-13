from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Second Derivative: Acceleration", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Original function f(t) with tangent line
        axes = Axes(x_range=[-4, 4, 1], y_range=[-3, 3, 1], axis_config={"color": WHITE})
        axes.to_edge(DOWN)
        self.play(Create(axes))

        # Blue curve f(t)
        f_graph = axes.plot(lambda x: 0.5 * x**3 - x, color=BLUE)
        f_label = axes.get_graph_label(f_graph, "f(t)", x_val=2, direction=UP)
        self.play(Create(f_graph), Write(f_label))
        self.wait(1)
        
        # Tangent line at point
        tangent_line = axes.get_tangent_line(x=1, length=2, color=YELLOW)
        self.play(Create(tangent_line))
        self.wait(1)

        # Slope value of tangent line (approx 0.5)
        slope_text = MathTex("f'(1) = 0.5", font_size=24).next_to(tangent_line, UP)
        self.play(Write(slope_text))
        self.wait(1)

        # Fade out tangent and slope text
        self.play(FadeOut(tangent_line), FadeOut(slope_text))

        # Show second derivative curve f''(t) as green plot of slopes
        f2_graph = axes.plot(lambda x: 1.5 * x**2 - 1, color=GREEN)
        f2_label = axes.get_graph_label(f2_graph, "f''(t)", x_val=2, direction=UP)
        self.play(Create(f2_graph), Write(f2_label))
        self.wait(1)

        # Arrows showing relationship
        arrow_up = Arrow(axes.c2p(-2, 0.5), axes.c2p(-1, 1.5), color=RED, buff=0.1)
        arrow_down = Arrow(axes.c2p(0.5, 1.5), axes.c2p(1.5, 3.5), color=RED, buff=0.1)

        self.play(GrowArrow(arrow_up))
        self.wait(0.5)
        self.play(GrowArrow(arrow_down))
        self.wait(0.5)

        # Text explanation
        text1 = Text("If f'(t) increases → f''(t) > 0", font_size=24).to_edge(LEFT).shift(UP*2)
        text2 = Text("If f'(t) decreases → f''(t) < 0", font_size=24).next_to(text1, DOWN)

        self.play(Write(text1))
        self.wait(1)
        self.play(Write(text2))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(arrow_up), FadeOut(arrow_down))

        # Show concavity matching f''(t) sign
        def get_concave_up():
            return axes.plot(lambda x: 0.5 * x**3 - x, color=BLUE, stroke_width=6)

        def get_concave_down():
            return axes.plot(lambda x: 0.5 * x**3 - x, color=BLUE, stroke_width=6)

        concave_up = always_redraw(get_concave_up)
        concave_down = always_redraw(get_concave_down)

        self.play(ReplacementTransform(f_graph, concave_up))
        self.wait(1)

        # Final text
        final_text = Text("f''(t) measures acceleration", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(axes), FadeOut(f_graph), FadeOut(f2_graph), FadeOut(f_label), FadeOut(final_text))
