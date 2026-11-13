from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Second Derivative: Acceleration", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Original function graph
        axes = Axes(x_range=[-4, 4, 1], y_range=[-2, 2, 1], axis_config={"color": WHITE})
        axes.to_edge(DOWN)
        self.play(Create(axes))

        # Blue curve f(t)
        f_graph = axes.plot(lambda x: 0.5 * x**3 - x, color=BLUE)
        f_label = axes.get_graph_label(f_graph, "f(t)", x_val=3, direction=UP)
        f_label.shift(0.33 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(f_graph), Write(f_label))
        self.wait(1)

        # Tangent line at point
        tangent_line = always_redraw(
            lambda: axes.get_secant_slope_group(
                x=1.5,
                graph=f_graph,
                dx=0.2,
                secant_line_color=YELLOW,
                secant_line_length=2
            )
        )
        self.play(Create(tangent_line))
        self.wait(1)

        # Slope value at point
        slope_value = always_redraw(
            lambda: DecimalNumber(axes.x_range[1], color=YELLOW, font_size=24)
            .move_to(axes.c2p(1.5, 0.5 * (1.5)**3 - 1.5))
        )
        self.play(Write(slope_value))
        self.wait(1)

        # Fade out tangent and slope
        self.play(FadeOut(tangent_line), FadeOut(slope_value))

        # Show second derivative curve f''(t)
        f2_graph = axes.plot(lambda x: 1.5 * x, color=GREEN)
        f2_label = axes.get_graph_label(f2_graph, "f''(t)", x_val=3, direction=UP)
        self.play(Create(f2_graph), Write(f2_label))
        self.wait(1)

        # Arrows showing relationship
        arrow_up = Arrow(axes.c2p(-2, 0.5), axes.c2p(-2, 2), color=RED, buff=0.1)
        arrow_down = Arrow(axes.c2p(2, -2), axes.c2p(2, -0.5), color=RED, buff=0.1)
        
        self.play(GrowArrow(arrow_up))
        self.wait(0.5)
        self.play(GrowArrow(arrow_down))
        self.wait(0.5)

        # Text explanation
        text1 = Text("When f'(t) increases", font_size=24).to_edge(LEFT).shift(UP*2)
        text2 = Text("f''(t) is positive", font_size=24).next_to(text1, DOWN)
        text3 = Text("When f'(t) decreases", font_size=24).next_to(text2, DOWN)
        text4 = Text("f''(t) is negative", font_size=24).next_to(text3, DOWN)

        self.play(Write(text1))
        self.wait(0.5)
        self.play(Write(text2))
        self.wait(0.5)
        self.play(Write(text3))
        self.wait(0.5)
        self.play(Write(text4))
        self.wait(1)

        # Fade out
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3), FadeOut(text4))
        self.wait(0.5)

        # Show concavity matching f''(t) sign
        concave_up = always_redraw(
            lambda: axes.plot(lambda x: 0.5 * x**3 - x, color=BLUE).set_color(BLUE)
        )
        concave_down = always_redraw(
            lambda: axes.plot(lambda x: 0.5 * x**3 - x, color=BLUE).set_color(BLUE)
        )

        # Show concavity
        self.play(ReplacementTransform(f_graph, concave_up))
        self.wait(1)

        # Final text
        final_text = Text("Second derivative measures acceleration", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(FadeOut(final_text), FadeOut(title))
