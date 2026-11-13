from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Fractal Dimension and Conclusion", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial curve fading into square
        curve = Line(LEFT * 3.5 + DOWN * 1.5, RIGHT * 3.5 + UP * 1.5, color=WHITE, stroke_width=2)
        square = Square(side_length=7, color=BLUE, fill_opacity=0.5)
        
        self.play(Create(curve), run_time=1)
        self.wait(0.5)
        self.play(Transform(curve, square), run_time=1)
        self.wait(0.5)

        # Topological dimension text
        top_dim = Text("Topological Dimension = 1", font_size=24).to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(top_dim))
        self.wait(0.5)

        # Hausdorff dimension text
        haus_dim = Text("Hausdorff Dimension = 2", font_size=24).next_to(top_dim, DOWN)
        self.play(Write(haus_dim))
        self.wait(1)

        # Fade out previous text
        self.play(FadeOut(top_dim), FadeOut(haus_dim))

        # Fractal dimension formula
        formula = MathTex("D = \\frac{\\log(N)}{\\log(1/r)}", font_size=40)
        self.play(Write(formula))
        self.wait(1.5)

        # Show scaling effect with animation
        r = ValueTracker(0.5)
        N = always_redraw(lambda: DecimalNumber(2**r.get_value(), num_decimal_places=0, font_size=30).to_edge(LEFT))
        
        self.play(r.animate.set_value(2), run_time=1.5)
        self.wait(0.5)
        self.play(r.animate.set_value(4), run_time=1.5)
        self.wait(0.5)

        # Final title
        final_title = Text("Infinity in Finite Space", font_size=36).to_edge(UP)
        self.play(Transform(title, final_title))
        self.wait(1)

        # Clean up
        self.play(FadeOut(formula), FadeOut(curve), FadeOut(title))
        self.wait(0.5)
