from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Formula for w × h Rectangles", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial rectangle
        w, h = 4, 3
        rect = Rectangle(width=w, height=h, color=BLUE, fill_opacity=0.2).move_to(ORIGIN)
        w_label = MathTex("w", font_size=24).next_to(rect, DOWN)
        h_label = MathTex("h", font_size=24).next_to(rect, RIGHT)

        self.play(Create(rect), Write(w_label), Write(h_label))
        self.wait(1)

        # Interior points formula
        interior_formula = MathTex("(w-1) \\times (h-1)", font_size=30)
        interior_formula.to_edge(UP, buff=0.5)
        interior_formula.shift(0.0 * RIGHT + 0.46 * UP)  # layout: separation vector
        self.play(Write(interior_formula))
        self.wait(1)

        # Edge points formula
        edge_formula = MathTex("2 \\times (w + h)", font_size=30)
        edge_formula.to_edge(DOWN, buff=0.5)
        self.play(Write(edge_formula))
        self.wait(1)

        # Combine into final formula
        final_formula = MathTex("(w-1)(h-1) - 2(w+h)", font_size=30)
        final_formula.move_to(ORIGIN)
        self.play(Transform(interior_formula, final_formula))
        self.wait(1.5)

        # Show visual breakdown of edge points
        self.play(FadeOut(interior_formula, edge_formula))

        # Show 2x3 grid example
        w2, h2 = 2, 3
        rect2 = Rectangle(width=w2, height=h2, color=BLUE, fill_opacity=0.2).move_to(ORIGIN)
        self.play(Create(rect2))
        self.wait(0.5)

        # Show interior points count for 2x3
        interior_count = MathTex("(2-1) \\times (3-1) = 2", font_size=24)
        interior_count.to_edge(UP, buff=0.5)
        interior_count.shift(0.0 * RIGHT + 0.4 * UP)  # layout: separation vector
        self.play(Write(interior_count))
        self.wait(1)

        # Show edge points count for 2x3
        edge_count = MathTex("2 \\times (2 + 3) = 10", font_size=24)
        edge_count.to_edge(DOWN, buff=0.5)
        self.play(Write(edge_count))
        self.wait(1)

        # Show subtraction: 2 - 10 = -8
        result = MathTex("2 - 10 = -8", font_size=30).move_to(ORIGIN)
        self.play(Transform(interior_count, result))
        self.wait(1.5)

        # Fade out 2x3 example
        self.play(FadeOut(rect2, interior_count, edge_count))

        # Show 5x2 grid example
        w3, h3 = 5, 2
        rect3 = Rectangle(width=w3, height=h3, color=BLUE, fill_opacity=0.2).move_to(ORIGIN)
        self.play(Create(rect3))
        self.wait(0.5)

        # Interior points for 5x2
        interior_count2 = MathTex("(5-1) \\times (2-1) = 4", font_size=24)
        interior_count2.to_edge(UP, buff=0.5)
        interior_count2.shift(0.0 * RIGHT + 0.4 * UP)  # layout: separation vector
        self.play(Write(interior_count2))
        self.wait(1)

        # Edge points for 5x2
        edge_count2 = MathTex("2 \\times (5 + 2) = 14", font_size=24)
        edge_count2.to_edge(DOWN, buff=0.5)
        self.play(Write(edge_count2))
        self.wait(1)

        # Show final result: 4 - 14 = -10
        result2 = MathTex("4 - 14 = -10", font_size=30).move_to(ORIGIN)
        self.play(Transform(interior_count2, result2))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(rect3, interior_count2, edge_count2, title))
        self.wait(0.5)
