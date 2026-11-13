from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Symmetry Rule", font_size=36).to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # Initial rectangle: 4x2
        w, h = 4, 2
        rect_4x2 = Rectangle(width=w, height=h, color=BLUE, fill_opacity=0.3).move_to(ORIGIN)
        inside_count = (w - 1) * (h - 1)
        edge_count = 2 * (w + h)
        sorrel_count = inside_count - edge_count

        # Labels for 4x2
        inside_label_4x2 = MathTex(f"\\text{{Inside: }} {inside_count}").next_to(rect_4x2, DOWN, buff=0.3)
        edge_label_4x2 = MathTex(f"\\text{{Edges: }} {edge_count}").next_to(inside_label_4x2, DOWN, buff=0.3)
        sorrel_label_4x2 = MathTex(f"\\text{{Sorrel count: }} {sorrel_count}").next_to(edge_label_4x2, DOWN, buff=0.3)

        self.play(Create(rect_4x2), run_time=0.5)
        self.play(Write(inside_label_4x2), Write(edge_label_4x2), Write(sorrel_label_4x2))
        self.wait(1)

        # Rotate to 2x4
        rect_2x4 = Rectangle(width=h, height=w, color=BLUE, fill_opacity=0.3).move_to(ORIGIN)
        inside_count_rot = (h - 1) * (w - 1)
        edge_count_rot = 2 * (h + w)
        sorrel_count_rot = inside_count_rot - edge_count_rot

        # Labels for 2x4
        inside_label_2x4 = MathTex(f"\\text{{Inside: }} {inside_count_rot}").next_to(rect_2x4, DOWN, buff=0.3)
        edge_label_2x4 = MathTex(f"\\text{{Edges: }} {edge_count_rot}").next_to(inside_label_2x4, DOWN, buff=0.3)
        sorrel_label_2x4 = MathTex(f"\\text{{Sorrel count: }} {sorrel_count_rot}").next_to(edge_label_2x4, DOWN, buff=0.3)

        self.play(Transform(rect_4x2, rect_2x4), run_time=1)
        self.play(ReplacementTransform(inside_label_4x2, inside_label_2x4),
                  ReplacementTransform(edge_label_4x2, edge_label_2x4),
                  ReplacementTransform(sorrel_label_4x2, sorrel_label_2x4))
        self.wait(1.5)

        # Show invariance
        invariant_text = Text("Sorrel count is preserved!", font_size=24).to_edge(DOWN, buff=0.3)
        self.play(Write(invariant_text))
        self.wait(1.5)

        # Add explanation about Sorrel Count definition and example
        explanation = Text(
            "The Sorrel Count is defined as the number of interior grid points\n"
            "minus the number of edge grid points for a w by h rectangle,\n"
            "calculated via the formula (w-1)(h-1) - 2(w+h).\n\n"
            "A key principle is that small rectangles yield negative counts\n"
            "because the edge term dominates the interior term.\n\n"
            "For instance, consider a 4 by 5 rectangle:\n"
            "it has (4-1)×(5-1) = 12 interior points and 2×(4+5) = 18 edge points.\n"
            "The Sorrel Count is 12 - 18 = -6, demonstrating that the count\n"
            "is negative for this dimension.",
            font_size=20,
            line_spacing=1.2
        ).to_edge(DOWN, buff=1.0)

        self.play(FadeOut(invariant_text))
        self.wait(0.5)
        self.play(Write(explanation))
        self.wait(4)

        # Fade out
        self.play(FadeOut(rect_4x2), FadeOut(inside_label_2x4), FadeOut(edge_label_2x4),
                  FadeOut(sorrel_label_2x4), FadeOut(explanation), FadeOut(title))
        self.wait(0.5)
