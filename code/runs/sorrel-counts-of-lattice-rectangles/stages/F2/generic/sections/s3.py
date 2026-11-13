from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Symmetry Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial rectangle: 4x2
        w, h = 4, 2
        rect1 = Rectangle(width=w, height=h, color=BLUE, fill_opacity=0.3).move_to(ORIGIN)
        inside_count = (w - 1) * (h - 1)
        edge_count = 2 * (w + h)
        sorrel1 = inside_count - edge_count

        # Labels for initial rectangle
        rect_label1 = MathTex(f"w={w}, h={h}", font_size=24).next_to(rect1, DOWN)
        inside_label1 = MathTex(f"\text{{Inside}} = {inside_count}", font_size=24).next_to(rect_label1, DOWN)
        edge_label1 = MathTex(f"\text{{Edges}} = {edge_count}", font_size=24).next_to(inside_label1, DOWN)
        sorrel_label1 = MathTex(f"\text{{Sorrel}} = {inside_count} - {edge_count} = {sorrel1}", font_size=24).next_to(edge_label1, DOWN)

        self.play(Create(rect1), Write(rect_label1))
        self.wait(0.5)
        self.play(Write(inside_label1), Write(edge_label1), Write(sorrel_label1))
        self.wait(1)

        # Rotate to 2x4
        rect2 = Rectangle(width=h, height=w, color=BLUE, fill_opacity=0.3).move_to(ORIGIN)
        inside_count2 = (h - 1) * (w - 1)
        edge_count2 = 2 * (h + w)
        sorrel2 = inside_count2 - edge_count2

        # Update labels
        rect_label2 = MathTex(f"w={h}, h={w}", font_size=24).next_to(rect2, DOWN)
        inside_label2 = MathTex(f"\\text{{Inside}} = {inside_count2}", font_size=24).next_to(rect_label2, DOWN)
        edge_label2 = MathTex(f"\\text{{Edges}} = {edge_count2}", font_size=24).next_to(inside_label2, DOWN)
        sorrel_label2 = MathTex(f"\\text{{Sorrel}} = {inside_count2} - {edge_count2} = {sorrel2}", font_size=24).next_to(edge_label2, DOWN)

        self.play(Transform(rect1, rect2), Transform(rect_label1, rect_label2))
        self.wait(0.5)
        self.play(Transform(inside_label1, inside_label2), Transform(edge_label1, edge_label2), Transform(sorrel_label1, sorrel_label2))
        self.wait(1)

        # Show invariance
        invariant = Text("Sorrel count unchanged!", font_size=24).set_color(GREEN).next_to(sorrel_label1, DOWN)
        self.play(Write(invariant))
        self.wait(1.5)

        # Final explanation
        explanation = Text("Algebraic expression is symmetric in w and h", font_size=24).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)

        # Clean up
        self.play(FadeOut(title, rect1, rect_label1, inside_label1, edge_label1, sorrel_label1, invariant, explanation))
        self.wait(0.5)
