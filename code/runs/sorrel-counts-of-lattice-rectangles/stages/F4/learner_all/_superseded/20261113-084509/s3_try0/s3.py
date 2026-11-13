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
        rect_label1 = MathTex(f"\\text{{4}} \\times \\text{{2}}", font_size=24).next_to(rect1, DOWN)
        inside_label1 = MathTex(f"\\text{{Inside: }} {inside_count}", font_size=24).next_to(rect_label1, DOWN)
        edge_label1 = MathTex(f"\\text{{Edges: }} {edge_count}", font_size=24).next_to(inside_label1, DOWN)
        sorrel_label1 = MathTex(f"\\text{{Sorrel: }} {sorrel1}", font_size=24).next_to(edge_label1, DOWN)

        self.play(Create(rect1), run_time=0.5)
        self.play(Write(rect_label1), run_time=0.5)
        self.play(Write(inside_label1), run_time=0.5)
        self.play(Write(edge_label1), run_time=0.5)
        self.play(Write(sorrel_label1), run_time=0.5)
        self.wait(1)

        # Rotate to 2x4
        rect2 = Rectangle(width=h, height=w, color=BLUE, fill_opacity=0.3).move_to(ORIGIN)
        inside_count2 = (h - 1) * (w - 1)
        edge_count2 = 2 * (h + w)
        sorrel2 = inside_count2 - edge_count2

        # Labels for rotated rectangle
        rect_label2 = MathTex(f"\\text{{2}} \\times \\text{{4}}", font_size=24).next_to(rect2, DOWN)
        inside_label2 = MathTex(f"\\text{{Inside: }} {inside_count2}", font_size=24).next_to(rect_label2, DOWN)
        edge_label2 = MathTex(f"\\text{{Edges: }} {edge_count2}", font_size=24).next_to(inside_label2, DOWN)
        sorrel_label2 = MathTex(f"\\text{{Sorrel: }} {sorrel2}", font_size=24).next_to(edge_label2, DOWN)

        # Adjust position to avoid overlap
        edge_label2.shift(DOWN * 0.22)
        inside_label2.shift(DOWN * 0.23)

        self.play(Transform(rect1, rect2), run_time=1.0)
        self.wait(0.5)

        # Update labels
        self.play(ReplacementTransform(rect_label1, rect_label2), run_time=0.5)
        self.play(ReplacementTransform(inside_label1, inside_label2), run_time=0.5)
        self.play(ReplacementTransform(edge_label1, edge_label2), run_time=0.5)
        self.play(ReplacementTransform(sorrel_label1, sorrel_label2), run_time=0.5)
        self.wait(1)

        # Show that sorrel counts are equal
        equal_text = Text("Sorrel count preserved!", font_size=24).set_color(GREEN).next_to(sorrel_label2, DOWN)
        equal_text.shift(UP * 0.49)  # Shift up to bring into frame

        self.play(Write(equal_text))
        self.wait(1.5)

        # Final explanation text
        final_text = Text("Swapping width and height preserves the sorrel count.", font_size=24).to_edge(DOWN)
        final_text.shift(UP * 0.33)  # Shift up to avoid overlap

        self.play(Write(final_text))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(rect1),
            FadeOut(rect_label2),
            FadeOut(inside_label2),
            FadeOut(edge_label2),
            FadeOut(sorrel_label2),
            FadeOut(equal_text),
            FadeOut(final_text),
            FadeOut(title)
        )
        self.wait(0.5)
