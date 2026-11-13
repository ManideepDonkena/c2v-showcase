from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Symmetry Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First pair: 4x2 and 2x4 rectangles with labels and sorrel counts
        rect1 = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.3).move_to(LEFT * 2)
        rect2 = Rectangle(width=2, height=4, color=RED, fill_opacity=0.3).move_to(RIGHT * 2)

        label1 = Text("4×2", font_size=24).next_to(rect1, DOWN)
        label2 = Text("2×4", font_size=24).next_to(rect2, DOWN)

        # Sorrel count calculation
        inside1 = (4 - 1) * (2 - 1)  # 3 * 1 = 3
        edge1 = 2 * (4 + 2)          # 2 * 6 = 12
        sorrel1 = inside1 - edge1     # 3 - 12 = -9

        inside2 = (2 - 1) * (4 - 1)  # 1 * 3 = 3
        edge2 = 2 * (2 + 4)          # 2 * 6 = 12
        sorrel2 = inside2 - edge2     # 3 - 12 = -9

        count1 = MathTex(f"\\text{{Inside: }} {inside1}, \\text{{ Edge: }} {edge1} \\Rightarrow \\text{{Sorrel Count: }} {sorrel1}", font_size=24).next_to(rect1, UP)
        count2 = MathTex(f"\\text{{Inside: }} {inside2}, \\text{{ Edge: }} {edge2} \\Rightarrow \\text{{Sorrel Count: }} {sorrel2}", font_size=24).next_to(rect2, UP)

        self.play(Create(rect1), Create(rect2), Write(label1), Write(label2))
        self.wait(0.5)
        self.play(Write(count1), Write(count2))
        self.wait(1)

        # Highlight that sorrel counts are equal
        highlight = SurroundingRectangle(VGroup(count1, count2), color=YELLOW, buff=0.1)
        self.play(Create(highlight))
        self.wait(1.5)
        self.play(FadeOut(highlight))

        # Show point breakdown side-by-side
        self.play(FadeOut(count1, count2))

        # Rebuild with detailed point counts
        inside1 = 3
        edge1 = 12
        inside2 = 3
        edge2 = 12

        points1 = MathTex(f"\text{{Inside: }} {inside1}, \text{{ Edge: }} {edge1} \Rightarrow \text{{Sorrel Count: }} -9", font_size=24).to_edge(UP)
        points2 = MathTex(f"\text{{Inside: }} {inside2}, \text{{ Edge: }} {edge2} \Rightarrow \text{{Sorrel Count: }} -9", font_size=24).to_edge(UP)

        points1.shift(0.0 * RIGHT + 0.38 * UP)  # layout: separation vector
        self.play(Write(points1))
        self.wait(0.5)
        points2.shift(0.0 * RIGHT + 0.76 * UP)  # layout: separation vector
        self.play(Write(points2))
        self.wait(1.5)

        # Show that swapping dimensions doesn't change final result
        note = Text("Swapping width and height preserves the sorrel count.", font_size=24).to_edge(DOWN)
        self.play(Write(note))
        self.wait(1.5)

        # Final explanation
        formula = MathTex("\\text{Sorrel Count} = (w-1)(h-1) - 2(w+h)", font_size=24).next_to(note, UP)
        self.play(Write(formula))
        self.wait(1.5)

        self.play(FadeOut(title, rect1, rect2, label1, label2, points1, points2, note, formula))
        self.wait(0.5)
