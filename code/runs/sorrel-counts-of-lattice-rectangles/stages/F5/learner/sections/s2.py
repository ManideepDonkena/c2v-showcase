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

        # Example explanation
        example_text = Text("For a 4 by 5 rectangle:", font_size=24)
        example_text.to_edge(LEFT).shift(DOWN * 2)
        self.play(Write(example_text))
        self.wait(0.5)

        # Show interior points calculation
        interior_calc = MathTex("3 \\times 4 = 12", font_size=24)
        interior_calc.next_to(example_text, DOWN)
        self.play(Write(interior_calc))
        self.wait(1)

        # Show edge points calculation
        edge_calc = MathTex("2 \\times (4 + 5) = 18", font_size=24)
        edge_calc.next_to(interior_calc, DOWN)
        self.play(Write(edge_calc))
        self.wait(1)

        # Show Sorrel Count
        sorrel_count = MathTex("12 - 18 = -6", font_size=24)
        sorrel_count.next_to(edge_calc, DOWN)
        self.play(Write(sorrel_count))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(title), FadeOut(rect), FadeOut(w_label), FadeOut(h_label),
                  FadeOut(interior_formula), FadeOut(edge_formula),
                  FadeOut(example_text), FadeOut(interior_calc), FadeOut(edge_calc), FadeOut(sorrel_count))
        self.wait(0.5)
