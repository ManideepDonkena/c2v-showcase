from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Formula for w × h Rectangles", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial rectangle
        w, h = 4, 3
        rect = Rectangle(width=w, height=h, color=BLUE, fill_opacity=0.3).move_to(ORIGIN)
        w_label = MathTex("w", font_size=24).next_to(rect, DOWN)
        h_label = MathTex("h", font_size=24).next_to(rect, RIGHT)

        self.play(Create(rect), Write(w_label), Write(h_label))
        self.wait(1)

        # Interior points formula
        interior_formula = MathTex("(w-1) \\times (h-1)", font_size=30)
        interior_formula.to_edge(UP).shift(UP * 0.5)
        self.play(Write(interior_formula))
        self.wait(1)

        # Edge points formula
        edge_formula = MathTex("2 \\times (w + h)", font_size=30)
        edge_formula.to_edge(DOWN).shift(DOWN * 0.5)
        self.play(Write(edge_formula))
        self.wait(1)

        # Combine into final sorrel count
        final_formula = MathTex("(w-1)(h-1) - 2(w+h)", font_size=30)
        final_formula.move_to(ORIGIN)
        self.play(Transform(interior_formula, final_formula))
        self.wait(1.5)

        # Explanation of the formula
        explanation = Text("This counts all interior points, then subtracts edge points.", font_size=24)
        explanation.to_edge(DOWN).shift(DOWN * 0.5)
        explanation.shift(0.0 * RIGHT + 0.46 * UP)  # layout: separation vector
        self.play(Write(explanation))
        self.wait(2)

        # Fade out
        self.play(FadeOut(title), FadeOut(rect), FadeOut(w_label), FadeOut(h_label),
                  FadeOut(interior_formula), FadeOut(edge_formula), FadeOut(explanation))
        self.wait(0.5)
