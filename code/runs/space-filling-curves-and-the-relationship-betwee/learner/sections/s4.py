from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Fractal Dimension and Conclusion", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Fade out title
        self.play(FadeOut(title))

        # Show curve fading into square
        square = Square(side_length=4, color=BLUE, fill_opacity=0.5)
        curve = VMobject(color=RED)
        curve.set_points_as_corners([
            [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
            [0, 0, 0]
        ])
        self.play(Create(curve), run_time=1)
        self.wait(0.5)

        # Animate curve fading into square
        self.play(
            Transform(curve, square),
            run_time=2
        )
        self.wait(0.5)

        # Show dimensions text
        top_dim = Text("Topological Dimension = 1", font_size=24).to_edge(UP)
        haus_dim = Text("Hausdorff Dimension = 2", font_size=24).next_to(top_dim, DOWN)
        self.play(Write(top_dim), run_time=0.5)
        self.wait(0.5)
        self.play(Write(haus_dim), run_time=0.5)
        self.wait(1)

        # Fade out dimension text
        self.play(FadeOut(top_dim), FadeOut(haus_dim))

        # Show fractal dimension formula
        formula = MathTex("D = \\frac{\\log(N)}{\\log(1/r)}", font_size=40)
        self.play(Write(formula))
        self.wait(1.5)

        # Show scaling parameters for Hilbert curve
        self.play(FadeOut(formula))
        hilbert_text = Text("For the Hilbert curve:", font_size=24).to_edge(UP)
        self.play(Write(hilbert_text))
        self.wait(0.5)

        n_text = Text("N = 4 sub-segments", font_size=24).next_to(hilbert_text, DOWN)
        r_text = Text("r = 1/2 scaling factor", font_size=24).next_to(n_text, DOWN)
        self.play(Write(n_text), run_time=0.5)
        self.wait(0.5)
        self.play(Write(r_text), run_time=0.5)
        self.wait(1)

        # Show calculation
        calc = MathTex("\\frac{\\log(4)}{\\log(2)} = 2", font_size=30).to_edge(DOWN)
        self.play(Write(calc))
        self.wait(1.5)

        # Final text
        self.play(FadeOut(hilbert_text), FadeOut(n_text), FadeOut(r_text), FadeOut(calc))

        final_title = Text("Infinity in Finite Space", font_size=36).to_edge(UP)
        self.play(Write(final_title))
        self.wait(2)

        self.play(FadeOut(final_title))
