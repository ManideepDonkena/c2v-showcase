from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Symmetry Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial 4x2 rectangle and sorrel count
        w, h = 4, 2
        rect1 = Rectangle(width=w, height=h, color=BLUE, fill_opacity=0.3).move_to(ORIGIN)
        inside1 = (w - 1) * (h - 1)
        edge1 = 2 * (w + h)
        sorrel1 = inside1 - edge1

        # Show 4x2 grid
        grid1 = VGroup()
        for i in range(h + 1):
            for j in range(w + 1):
                dot = Dot(point=[j, i, 0], color=RED, radius=0.05)
                grid1.add(dot)
        grid1.move_to(rect1.get_center())

        inside_text1 = MathTex(f"\\text{{Inside: }} {inside1}", font_size=24).next_to(rect1, DOWN)
        edge_text1 = MathTex(f"\\text{{Edge: }} {edge1}", font_size=24).next_to(inside_text1, DOWN)
        sorrel_text1 = MathTex(f"\\text{{Sorrel: }} {sorrel1}", font_size=24).next_to(edge_text1, DOWN)

        self.play(Create(rect1), FadeIn(grid1))
        self.wait(0.5)
        self.play(Write(inside_text1), Write(edge_text1), Write(sorrel_text1))
        self.wait(1)

        # Rotate to 2x4
        rect2 = Rectangle(width=h, height=w, color=BLUE, fill_opacity=0.3).move_to(ORIGIN)
        inside2 = (h - 1) * (w - 1)
        edge2 = 2 * (h + w)
        sorrel2 = inside2 - edge2

        self.play(Transform(rect1, rect2), Transform(grid1, VGroup()))
        self.wait(0.5)

        # Update text for rotated
        inside_text2 = MathTex(f"\\text{{Inside: }} {inside2}", font_size=24).next_to(rect2, DOWN)
        edge_text2 = MathTex(f"\\text{{Edge: }} {edge2}", font_size=24).next_to(inside_text2, DOWN)
        sorrel_text2 = MathTex(f"\\text{{Sorrel: }} {sorrel2}", font_size=24).next_to(edge_text2, DOWN)

        self.play(Transform(inside_text1, inside_text2), Transform(edge_text1, edge_text2), Transform(sorrel_text1, sorrel_text2))
        self.wait(1.5)

        # Show visual breakdown of edge points
        self.play(FadeOut(rect1, grid1, inside_text1, edge_text1, sorrel_text1))

        # Show 2x3 rectangle and calculation
        w2, h2 = 2, 3
        rect3 = Rectangle(width=w2, height=h2, color=BLUE, fill_opacity=0.3).move_to(LEFT * 3)
        grid3 = VGroup()
        for i in range(h2 + 1):
            for j in range(w2 + 1):
                dot = Dot(point=[j - 3, i, 0], color=RED, radius=0.05)
                grid3.add(dot)
        grid3.move_to(rect3.get_center())

        inside3 = (w2 - 1) * (h2 - 1)
        edge3 = 2 * (w2 + h2)
        sorrel3 = inside3 - edge3

        inside_text3 = MathTex(f"\\text{{Inside: }} {inside3}", font_size=24).next_to(rect3, DOWN)
        edge_text3 = MathTex(f"\\text{{Edge: }} {edge3}", font_size=24).next_to(inside_text3, DOWN)
        sorrel_text3 = MathTex(f"\\text{{Sorrel: }} {sorrel3}", font_size=24).next_to(edge_text3, DOWN)

        self.play(Create(rect3), FadeIn(grid3))
        self.wait(0.5)
        self.play(Write(inside_text3), Write(edge_text3), Write(sorrel_text3))
        self.wait(1)

        # Show 5x2 rectangle
        w4, h4 = 5, 2
        rect4 = Rectangle(width=w4, height=h4, color=BLUE, fill_opacity=0.3).move_to(RIGHT * 3)
        grid4 = VGroup()
        for i in range(h4 + 1):
            for j in range(w4 + 1):
                dot = Dot(point=[j + 3, i, 0], color=RED, radius=0.05)
                grid4.add(dot)
        grid4.move_to(rect4.get_center())

        inside4 = (w4 - 1) * (h4 - 1)
        edge4 = 2 * (w4 + h4)
        sorrel4 = inside4 - edge4

        inside_text4 = MathTex(f"\\text{{Inside: }} {inside4}", font_size=24).next_to(rect4, DOWN)
        edge_text4 = MathTex(f"\\text{{Edge: }} {edge4}", font_size=24).next_to(inside_text4, DOWN)
        sorrel_text4 = MathTex(f"\\text{{Sorrel: }} {sorrel4}", font_size=24).next_to(edge_text4, DOWN)

        self.play(Create(rect4), FadeIn(grid4))
        self.wait(0.5)
        self.play(Write(inside_text4), Write(edge_text4), Write(sorrel_text4))
        self.wait(1)

        # Show 3x3 grid
        w5, h5 = 3, 3
        rect5 = Rectangle(width=w5, height=h5, color=BLUE, fill_opacity=0.3).move_to(ORIGIN)
        grid5 = VGroup()
        for i in range(h5 + 1):
            for j in range(w5 + 1):
                dot = Dot(point=[j, i, 0], color=RED, radius=0.05)
                grid5.add(dot)
        grid5.move_to(rect5.get_center())

        inside5 = (w5 - 1) * (h5 - 1)
        edge5 = 2 * (w5 + h5)
        sorrel5 = inside5 - edge5

        inside_text5 = MathTex(f"\\text{{Inside: }} {inside5}", font_size=24).next_to(rect5, DOWN)
        edge_text5 = MathTex(f"\\text{{Edge: }} {edge5}", font_size=24).next_to(inside_text5, DOWN)
        sorrel_text5 = MathTex(f"\\text{{Sorrel: }} {sorrel5}", font_size=24).next_to(edge_text5, DOWN)

        self.play(FadeOut(rect3, grid3, inside_text3, edge_text3, sorrel_text3),
                  FadeOut(rect4, grid4, inside_text4, edge_text4, sorrel_text4))
        self.play(Create(rect5), FadeIn(grid5))
        self.wait(0.5)
        self.play(Write(inside_text5), Write(edge_text5), Write(sorrel_text5))
        self.wait(1)

        # Show side-by-side rectangles
        rect6 = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.3).move_to(LEFT * 2)
        rect7 = Rectangle(width=2, height=4, color=BLUE, fill_opacity=0.3).move_to(RIGHT * 2)

        grid6 = VGroup()
        for i in range(3):
            for j in range(5):
                dot = Dot(point=[j - 2, i, 0], color=RED, radius=0.05)
                grid6.add(dot)
        grid6.move_to(rect6.get_center())

        grid7 = VGroup()
        for i in range(5):
            for j in range(3):
                dot = Dot(point=[j + 2, i, 0], color=RED, radius=0.05)
                grid7.add(dot)
        grid7.move_to(rect7.get_center())

        label6 = Text("4x2", font_size=24).next_to(rect6, UP)
        label7 = Text("2x4", font_size=24).next_to(rect7, UP)

        self.play(FadeOut(rect5, grid5, inside_text5, edge_text5, sorrel_text5))
        self.play(Create(rect6), Create(rect7), FadeIn(grid6), FadeIn(grid7), Write(label6), Write(label7))
        self.wait(0.5)

        # Show final sorrel counts
        count1 = MathTex(f"\\text{{Sorrel: }} -6", font_size=24).next_to(rect6, DOWN)
        count2 = MathTex(f"\\text{{Sorrel: }} -6", font_size=24).next_to(rect7, DOWN)

        self.play(Write(count1), Write(count2))
        self.wait(1.5)

        # Show that swapping changes inside and edge but not final result
        self.play(FadeOut(rect6, rect7, grid6, grid7, label6, label7, count1, count2))

        # Show 4x2 vs 2x4 with inside and edge counts
        rect8 = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.3).move_to(LEFT * 2)
        rect9 = Rectangle(width=2, height=4, color=BLUE, fill_opacity=0.3).move_to(RIGHT * 2)

        label8 = Text("4x2", font_size=24).next_to(rect8, UP)
        label9 = Text("2x4", font_size=24).next_to(rect9, UP)

        inside8 = (4 - 1) * (2 - 1)
        edge8 = 2 * (4 + 2)
        sorrel8 = inside8 - edge8

        inside9 = (2 - 1) * (4 - 1)
        edge9 = 2 * (2 + 4)
        sorrel9 = inside9 - edge9

        self.play(Create(rect8), Create(rect9), Write(label8), Write(label9))
        self.wait(0.5)

        # Show inside and edge counts
        inside_text8 = MathTex(f"\\text{{Inside: }} {inside8}", font_size=24).next_to(rect8, DOWN)
        edge_text8 = MathTex(f"\\text{{Edge: }} {edge8}", font_size=24).next_to(inside_text8, DOWN)
        sorrel_text8 = MathTex(f"\\text{{Sorrel: }} {sorrel8}", font_size=24).next_to(edge_text8, DOWN)

        inside_text9 = MathTex(f"\\text{{Inside: }} {inside9}", font_size=24).next_to(rect9, DOWN)
        edge_text9 = MathTex(f"\\text{{Edge: }} {edge9}", font_size=24).next_to(inside_text9, DOWN)
        sorrel_text9 = MathTex(f"\\text{{Sorrel: }} {sorrel9}", font_size=24).next_to(edge_text9, DOWN)

        self.play(Write(inside_text8), Write(edge_text8), Write(sorrel_text8),
                  Write(inside_text9), Write(edge_text9), Write(sorrel_text9))
        self.wait(1.5)

        # Final statement
        final = Text("Swapping width and height preserves the sorrel count.", font_size=24).to_edge(DOWN)
        final.shift(0.0 * RIGHT + -0.32 * UP)  # layout: separation vector
        self.play(Write(final))
        self.wait(1)

        self.play(FadeOut(title, final))
