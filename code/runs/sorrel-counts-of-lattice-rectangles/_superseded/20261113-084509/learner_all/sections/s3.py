from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Symmetry Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial 4x2 rectangle
        w, h = 4, 2
        rect1 = Rectangle(width=w, height=h, color=BLUE, fill_opacity=0.3).move_to(ORIGIN)
        self.play(Create(rect1))
        self.wait(0.5)

        # Interior points (w-1) * (h-1)
        interior_count = MathTex(f"({w}-1) \times ({h}-1) = {int((w-1)*(h-1))}", font_size=24)
        interior_count.next_to(rect1, DOWN, buff=0.5)
        self.play(Write(interior_count))
        self.wait(0.5)

        # Edge points 2*(w+h)
        edge_count = MathTex(f"2({w}+{h}) = {2*(w+h)}", font_size=24)
        edge_count.next_to(interior_count, DOWN)
        self.play(Write(edge_count))
        self.wait(0.5)

        # Sorrel count
        sorrel1 = MathTex(f"{int((w-1)*(h-1))} - {2*(w+h)} = {-8}", font_size=24)
        sorrel1.next_to(edge_count, DOWN)
        self.play(Write(sorrel1))
        self.wait(0.5)

        # Rotate to 2x4
        rect2 = Rectangle(width=h, height=w, color=BLUE, fill_opacity=0.3).move_to(ORIGIN)
        self.play(Transform(rect1, rect2))
        self.wait(0.5)

        # Update counts for 2x4
        interior_count2 = MathTex(f"({h}-1) \\times ({w}-1) = {int((h-1)*(w-1))}", font_size=24)
        interior_count2.next_to(rect2, DOWN)
        self.play(ReplacementTransform(interior_count, interior_count2))
        self.wait(0.5)

        edge_count2 = MathTex(f"2({h}+{w}) = {2*(h+w)}", font_size=24)
        edge_count2.next_to(interior_count2, DOWN)
        self.play(ReplacementTransform(edge_count, edge_count2))
        self.wait(0.5)

        sorrel2 = MathTex(f"{int((h-1)*(w-1))} - {2*(h+w)} = {-8}", font_size=24)
        sorrel2.next_to(edge_count2, DOWN)
        self.play(ReplacementTransform(sorrel1, sorrel2))
        self.wait(0.5)

        # Show side-by-side rectangles
        rect_a = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.3).shift(LEFT*3)
        rect_b = Rectangle(width=2, height=4, color=BLUE, fill_opacity=0.3).shift(RIGHT*3)

        label_a = Text("4x2", font_size=24).next_to(rect_a, UP)
        label_b = Text("2x4", font_size=24).next_to(rect_b, UP)

        self.play(Create(rect_a), Create(rect_b), Write(label_a), Write(label_b))
        self.wait(0.5)

        # Show sorrel counts
        count_a = MathTex("\\text{Sorrel Count: } -6", font_size=24).next_to(rect_a, DOWN)
        count_b = MathTex("\\text{Sorrel Count: } -6", font_size=24).next_to(rect_b, DOWN)

        self.play(Write(count_a), Write(count_b))
        self.wait(1.0)

        # Highlight that they are equal
        highlight = SurroundingRectangle(VGroup(count_a, count_b), color=YELLOW, buff=0.1)
        self.play(Create(highlight))
        self.wait(1.0)

        # Final explanation text
        note = Text("Swapping width and height preserves the sorrel count", font_size=24).to_edge(DOWN)
        self.play(Write(note))
        self.wait(1.5)

        self.play(FadeOut(title, rect1, rect2, label_a, label_b, count_a, count_b, highlight, note, interior_count2, edge_count2, sorrel2))
