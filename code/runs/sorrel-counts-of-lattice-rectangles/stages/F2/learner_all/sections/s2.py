from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Formula for w × h Rectangles", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial rectangle and formulas
        w, h = 4, 3
        rect = Rectangle(width=w, height=h, color=BLUE, fill_opacity=0.3)
        rect.move_to(ORIGIN)
        w_label = MathTex("w", font_size=24).next_to(rect, DOWN)
        h_label = MathTex("h", font_size=24).next_to(rect, RIGHT)

        self.play(Create(rect), Write(w_label), Write(h_label))
        self.wait(0.5)

        # Interior count formula
        interior_formula = MathTex("(w-1) \\times (h-1)", font_size=32)
        interior_formula.to_edge(UP).shift(UP * 0.5)
        self.play(Write(interior_formula))
        self.wait(0.5)

        # Edge count formula
        edge_formula = MathTex("2 \\times (w + h)", font_size=32)
        edge_formula.to_edge(DOWN).shift(DOWN * 0.5)
        self.play(Write(edge_formula))
        self.wait(0.5)

        # Show the full expression
        full_expr = MathTex("(w-1)(h-1) - 2(w+h)", font_size=32)
        full_expr.move_to(ORIGIN)
        self.play(Transform(interior_formula, full_expr))
        self.wait(1)

        # Breakdown of edge points
        self.play(FadeOut(interior_formula), FadeOut(edge_formula))

        # Show grid breakdown
        grid = VGroup()
        for i in range(h + 1):
            for j in range(w + 1):
                grid.add(Dot([j, i, 0], color=RED, radius=0.05))
        grid.move_to(ORIGIN)
        self.play(Create(grid))
        self.wait(0.5)

        # Highlight edges
        top_edge = Line([0, h, 0], [w, h, 0])
        bottom_edge = Line([0, 0, 0], [w, 0, 0])
        left_edge = Line([0, 0, 0], [0, h, 0])
        right_edge = Line([w, 0, 0], [w, h, 0])

        self.play(Create(top_edge), Create(bottom_edge), Create(left_edge), Create(right_edge))
        self.wait(0.5)

        # Show corner count
        corner_count = MathTex("4 \\text{ corners counted twice}", font_size=24)
        corner_count.next_to(rect, DOWN)
        corner_count.shift(0.0 * RIGHT + -0.26 * UP)  # layout: separation vector
        self.play(Write(corner_count))
        self.wait(1)

        self.play(FadeOut(top_edge), FadeOut(bottom_edge), FadeOut(left_edge), FadeOut(right_edge))

        # Example 2x3 rectangle
        self.play(FadeOut(grid), FadeOut(corner_count))
        w, h = 2, 3
        rect2 = Rectangle(width=w, height=h, color=BLUE, fill_opacity=0.3)
        rect2.move_to(ORIGIN)
        self.play(Create(rect2))
        self.wait(0.5)

        # Interior points: (w-1)(h-1) = 1*2 = 2
        interior_count = MathTex("(2-1)(3-1) = 2", font_size=24).to_edge(UP)
        interior_count.shift(0.0 * RIGHT + 0.4 * UP)  # layout: separation vector
        self.play(Write(interior_count))
        self.wait(0.5)

        # Edge points: 2(w+h) = 2(2+3) = 10
        edge_count = MathTex("2(2+3) = 10", font_size=24).to_edge(DOWN)
        self.play(Write(edge_count))
        self.wait(0.5)

        # Subtract: 2 - 10 = -8
        result = MathTex("2 - 10 = -8", font_size=32).move_to(ORIGIN)
        self.play(Transform(interior_count, result))
        self.wait(1)

        # Example 5x2 rectangle
        self.play(FadeOut(rect2), FadeOut(interior_count), FadeOut(edge_count))
        w, h = 5, 2
        rect3 = Rectangle(width=w, height=h, color=BLUE, fill_opacity=0.3)
        rect3.move_to(ORIGIN)
        self.play(Create(rect3))
        self.wait(0.5)

        # Interior points: (w-1)(h-1) = 4*1 = 4
        interior_count2 = MathTex("(5-1)(2-1) = 4", font_size=24).to_edge(UP)
        interior_count2.shift(0.0 * RIGHT + 0.4 * UP)  # layout: separation vector
        self.play(Write(interior_count2))
        self.wait(0.5)

        # Edge points: 2(w+h) = 2(5+2) = 14
        edge_count2 = MathTex("2(5+2) = 14", font_size=24).to_edge(DOWN)
        self.play(Write(edge_count2))
        self.wait(0.5)

        # Subtract: 4 - 14 = -10
        result2 = MathTex("4 - 14 = -10", font_size=32).move_to(ORIGIN)
        self.play(Transform(interior_count2, result2))
        self.wait(1)

        # Example 3x3 square
        self.play(FadeOut(rect3), FadeOut(interior_count2), FadeOut(edge_count2))
        w, h = 3, 3
        rect4 = Rectangle(width=w, height=h, color=BLUE, fill_opacity=0.3)
        rect4.move_to(ORIGIN)
        self.play(Create(rect4))
        self.wait(0.5)

        # Interior points: (w-1)(h-1) = 2*2 = 4
        interior_count3 = MathTex("(3-1)(3-1) = 4", font_size=24).to_edge(UP)
        self.play(Write(interior_count3))
        self.wait(0.5)

        # Edge points: 2(w+h) = 2(3+3) = 12
        edge_count3 = MathTex("2(3+3) = 12", font_size=24).to_edge(DOWN)
        self.play(Write(edge_count3))
        self.wait(0.5)

        # Subtract: 4 - 12 = -8
        result3 = MathTex("4 - 12 = -8", font_size=32).move_to(ORIGIN)
        self.play(Transform(interior_count3, result3))
        self.wait(1)

        # Side-by-side rectangles with same sorrel count
        self.play(FadeOut(rect4), FadeOut(interior_count3), FadeOut(edge_count3))

        rect5 = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.3)
        rect6 = Rectangle(width=2, height=4, color=BLUE, fill_opacity=0.3)

        rect5.move_to(LEFT * 2)
        rect6.move_to(RIGHT * 2)

        self.play(Create(rect5), Create(rect6))
        self.wait(0.5)

        # Labels
        label1 = MathTex("4 \\times 2", font_size=24).next_to(rect5, DOWN)
        label2 = MathTex("2 \\times 4", font_size=24).next_to(rect6, DOWN)
        self.play(Write(label1), Write(label2))
        self.wait(0.5)

        # Sorrel count for both
        count1 = MathTex("(3)(1) - 2(6) = 3 - 12 = -9", font_size=24).to_edge(UP)
        count2 = MathTex("(1)(3) - 2(6) = 3 - 12 = -9", font_size=24).to_edge(DOWN)
        self.play(Write(count1), Write(count2))
        self.wait(1)

        # Final result
        final = MathTex("Sorrel Count = -8", font_size=32).move_to(ORIGIN)
        self.play(Transform(count1, final))
        self.wait(1)

        self.play(FadeOut(rect5), FadeOut(rect6), FadeOut(label1), FadeOut(label2), FadeOut(count1), FadeOut(count2), FadeOut(title))
