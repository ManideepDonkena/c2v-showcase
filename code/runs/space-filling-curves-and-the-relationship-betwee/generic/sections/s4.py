from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Fractal Dimension and Conclusion", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial curve fading into square
        curve = Line(LEFT * 3, RIGHT * 3, color=BLUE, stroke_width=2)
        square = Square(side_length=6, color=YELLOW, fill_opacity=0.5)
        
        self.play(Create(curve))
        self.wait(0.5)
        self.play(Transform(curve, square))
        self.wait(1)

        # Dimension labels
        top_dim = MathTex("Topological\\ Dimension = 1", font_size=30)
        haus_dim = MathTex("Hausdorff\\ Dimension = 2", font_size=30)
        
        top_dim.to_edge(UP).shift(DOWN * 0.5)
        haus_dim.next_to(top_dim, DOWN)
        
        self.play(Write(top_dim))
        self.wait(0.5)
        self.play(Write(haus_dim))
        self.wait(1.5)

        # Fade out dimension labels
        self.play(FadeOut(top_dim), FadeOut(haus_dim))

        # Fractal dimension formula
        formula = MathTex("D = \\frac{\\log(N)}{\\log(1/r)}", font_size=40)
        self.play(Write(formula))
        self.wait(2)

        # Show scaling effect
        self.play(FadeOut(formula))

        # Final title
        final_title = Text("Infinity in Finite Space", font_size=36).to_edge(UP)
        final_title.shift(0.0 * RIGHT + -0.53 * UP)  # layout: separation vector
        self.play(Write(final_title))
        self.wait(1.5)

        # Narration text
        narration = Text("Space-filling curves reveal that dimension is not always an integer.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)
        
        self.play(FadeOut(narration))
        
        narration2 = Text("By analyzing how length scales with size, we see that these curves possess a fractal dimension of 2, perfectly bridging the gap between infinite mathematics and finite geometry.", font_size=24)
        narration2.to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(3)
        
        self.play(FadeOut(narration2), FadeOut(final_title))
        self.wait(0.5)
