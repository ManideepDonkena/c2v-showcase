from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Symmetry Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Show 4x2 and 2x4 rectangles with sorrel counts
        rect1 = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.3).move_to(LEFT * 2)
        rect2 = Rectangle(width=2, height=4, color=RED, fill_opacity=0.3).move_to(RIGHT * 2)

        w, h = 4, 2
        inside1 = (w - 1) * (h - 1)
        edge1 = 2 * (w + h)
        sorrel1 = inside1 - edge1

        inside2 = (h - 1) * (w - 1)
        edge2 = 2 * (h + w)
        sorrel2 = inside2 - edge2

        # Show first rectangle
        self.play(Create(rect1))
        self.wait(0.5)

        # Label and show counts
        label1 = Text(f"4×2", font_size=24).next_to(rect1, UP)
        self.play(Write(label1))
        self.wait(0.5)

        # Show inside points
        inside_text1 = MathTex(f"\\text{{Inside: }} {inside1}", font_size=24).to_edge(DOWN).shift(LEFT * 2)
        self.play(Write(inside_text1))
        self.wait(0.5)
        # Show edge points
        edge_text1 = MathTex(f"\\text{{Edge: }} {edge1}", font_size=24).next_to(inside_text1, DOWN)
        self.play(Write(edge_text1))
        self.wait(0.5)
        # Show sorrel count
        sorrel_text1 = MathTex(f"\\text{{Sorrel Count: }} {sorrel1}", font_size=24).next_to(edge_text1, DOWN)
        self.play(Write(sorrel_text1))
        self.wait(0.5)

        # Rotate to 2x4
        self.play(Transform(rect1, rect2), Transform(label1, Text("2×4", font_size=24).next_to(rect2, UP)))
        self.wait(0.5)

        # Show updated counts for second rectangle
        inside_text2 = MathTex(f"\\text{{Inside: }} {inside2}", font_size=24).to_edge(DOWN).shift(RIGHT * 2)
        self.play(Write(inside_text2))
        self.wait(0.5)

        edge_text2 = MathTex(f"\\text{{Edge: }} {edge2}", font_size=24).next_to(inside_text2, DOWN)
        self.play(Write(edge_text2))
        self.wait(0.5)

        sorrel_text2 = MathTex(f"\\text{{Sorrel Count: }} {sorrel2}", font_size=24).next_to(edge_text2, DOWN)
        self.play(Write(sorrel_text2))
        self.wait(0.5)

        # Highlight that both are equal
        highlight = SurroundingRectangle(VGroup(sorrel_text1, sorrel_text2), color=YELLOW, buff=0.1)
        self.play(Create(highlight))
        self.wait(1)

        # Show visual breakdown of edge points
        self.play(FadeOut(VGroup(rect1, rect2, label1, inside_text1, edge_text1, sorrel_text1,
                                 inside_text2, edge_text2, sorrel_text2, highlight)))

        # Show 2x3 grid
        grid23 = Rectangle(width=2, height=3, color=GREEN, fill_opacity=0.2).move_to(ORIGIN)
        self.play(Create(grid23))
        self.wait(0.5)

        label23 = Text("2×3", font_size=24).next_to(grid23, UP)
        self.play(Write(label23))
        self.wait(0.5)

        # Show inside and edge counts
        inside23 = (2 - 1) * (3 - 1)
        edge23 = 2 * (2 + 3)
        sorrel23 = inside23 - edge23

        inside_text23 = MathTex(f"\\text{{Inside: }} {inside23}", font_size=24).to_edge(DOWN).shift(LEFT * 2)
        self.play(Write(inside_text23))
        self.wait(0.5)

        edge_text23 = MathTex(f"\\text{{Edge: }} {edge23}", font_size=24).next_to(inside_text23, DOWN)
        self.play(Write(edge_text23))
        self.wait(0.5)

        # Show subtraction visually
        minus = MathTex("-", font_size=36).next_to(inside_text23, RIGHT)
        self.play(Write(minus))
        self.wait(0.5)

        result = MathTex(f"= {sorrel23}", font_size=36).next_to(minus, RIGHT)
        self.play(Write(result))
        self.wait(1)

        # Show 5x2 grid
        self.play(FadeOut(VGroup(grid23, label23, inside_text23, edge_text23, minus, result)))

        grid52 = Rectangle(width=5, height=2, color=PURPLE, fill_opacity=0.2).move_to(ORIGIN)
        self.play(Create(grid52))
        self.wait(0.5)

        label52 = Text("5×2", font_size=24).next_to(grid52, UP)
        self.play(Write(label52))
        self.wait(0.5)

        inside52 = (5 - 1) * (2 - 1)
        edge52 = 2 * (5 + 2)
        sorrel52 = inside52 - edge52

        inside_text52 = MathTex(f"\\text{{Inside: }} {inside52}", font_size=24).to_edge(DOWN).shift(LEFT * 2)
        self.play(Write(inside_text52))
        self.wait(0.5)

        edge_text52 = MathTex(f"\\text{{Edge: }} {edge52}", font_size=24).next_to(inside_text52, DOWN)
        self.play(Write(edge_text52))
        self.wait(0.5)

        minus52 = MathTex("-", font_size=36).next_to(inside_text52, RIGHT)
        self.play(Write(minus52))
        self.wait(0.5)

        result52 = MathTex(f"= {sorrel52}", font_size=36).next_to(minus52, RIGHT)
        self.play(Write(result52))
        self.wait(1)

        # Show 3x3 grid
        self.play(FadeOut(VGroup(grid52, label52, inside_text52, edge_text52, minus52, result52)))

        grid33 = Rectangle(width=3, height=3, color=YELLOW, fill_opacity=0.2).move_to(ORIGIN)
        self.play(Create(grid33))
        self.wait(0.5)

        label33 = Text("3×3", font_size=24).next_to(grid33, UP)
        self.play(Write(label33))
        self.wait(0.5)

        inside33 = (3 - 1) * (3 - 1)
        edge33 = 2 * (3 + 3)
        sorrel33 = inside33 - edge33

        inside_text33 = MathTex(f"\\text{{Inside: }} {inside33}", font_size=24).to_edge(DOWN).shift(LEFT * 2)
        self.play(Write(inside_text33))
        self.wait(0.5)

        edge_text33 = MathTex(f"\\text{{Edge: }} {edge33}", font_size=24).next_to(inside_text33, DOWN)
        self.play(Write(edge_text33))
        self.wait(0.5)

        minus33 = MathTex("-", font_size=36).next_to(inside_text33, RIGHT)
        self.play(Write(minus33))
        self.wait(0.5)

        result33 = MathTex(f"= {sorrel33}", font_size=36).next_to(minus33, RIGHT)
        self.play(Write(result33))
        self.wait(1)

        # Show final side-by-side comparison
        self.play(FadeOut(VGroup(grid33, label33, inside_text33, edge_text33, minus33, result33)))

        rect42 = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.3).move_to(LEFT * 2)
        rect24 = Rectangle(width=2, height=4, color=RED, fill_opacity=0.3).move_to(RIGHT * 2)

        label42 = Text("4×2", font_size=24).next_to(rect42, UP)
        label24 = Text("2×4", font_size=24).next_to(rect24, UP)

        self.play(Create(rect42), Create(rect24))
        self.play(Write(label42), Write(label24))
        self.wait(0.5)

        # Show inside and edge counts for both
        inside42 = (4 - 1) * (2 - 1)
        edge42 = 2 * (4 + 2)
        sorrel42 = inside42 - edge42

        inside24 = (2 - 1) * (4 - 1)
        edge24 = 2 * (2 + 4)
        sorrel24 = inside24 - edge24

        # Show inside and edge for first
        inside_text42 = MathTex(f"\\text{{Inside: }} {inside42}", font_size=20).to_edge(DOWN).shift(LEFT * 3)
        edge_text42 = MathTex(f"\\text{{Edge: }} {edge42}", font_size=20).next_to(inside_text42, DOWN)
        sorrel_text42 = MathTex(f"\\text{{Sorrel Count: }} {sorrel42}", font_size=20).next_to(edge_text42, DOWN)

        self.play(Write(inside_text42), Write(edge_text42), Write(sorrel_text42))
        self.wait(0.5)

        # Show inside and edge for second
        inside_text24 = MathTex(f"\\text{{Inside: }} {inside24}", font_size=20).to_edge(DOWN).shift(RIGHT * 3)
        edge_text24 = MathTex(f"\\text{{Edge: }} {edge24}", font_size=20).next_to(inside_text24, DOWN)
        sorrel_text24 = MathTex(f"\\text{{Sorrel Count: }} {sorrel24}", font_size=20).next_to(edge_text24, DOWN)

        self.play(Write(inside_text24), Write(edge_text24), Write(sorrel_text24))
        self.wait(1)

        # Final highlight
        final_highlight = SurroundingRectangle(VGroup(sorrel_text42, sorrel_text24), color=YELLOW, buff=0.1)
        self.play(Create(final_highlight))
        self.wait(1)

        # Show conclusion text
        self.play(FadeOut(VGroup(rect42, rect24, label42, label24, inside_text42, edge_text42, sorrel_text42,
                                 inside_text24, edge_text24, sorrel_text24, final_highlight)))

        conclusion = Text("Swapping width and height preserves the sorrel count.", font_size=24)
        self.play(Write(conclusion))
        self.wait(1)

        self.play(FadeOut(conclusion))
        self.wait(0.5)

        # End
        self.play(FadeOut(title))
