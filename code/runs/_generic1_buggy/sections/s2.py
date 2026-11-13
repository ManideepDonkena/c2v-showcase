from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Pythagoras Theorem: Visual Proof", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Triangle
        triangle = Triangle().scale(2)
        triangle.shift(DOWN * 0.5)
        a = triangle.get_side_length(0)
        b = triangle.get_side_length(1)
        c = triangle.get_side_length(2)
        
        self.play(Create(triangle))
        self.wait(0.5)
        
        # Labels
        label_a = MathTex("a", font_size=24).next_to(triangle.get_vertices()[0], DOWN)
        label_b = MathTex("b", font_size=24).next_to(triangle.get_vertices()[1], LEFT)
        label_c = MathTex("c", font_size=24).next_to(triangle.get_vertices()[2], RIGHT)
        
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(0.5)

        # Square on side a (blue)
        square_a = Square(side_length=a, color=BLUE, fill_opacity=0.5)
        square_a.shift(triangle.get_vertices()[0] + DOWN * a/2 + LEFT * a/2)
        self.play(Create(square_a), run_time=1)
        self.wait(0.5)

        # Square on side b (green)
        square_b = Square(side_length=b, color=GREEN, fill_opacity=0.5)
        square_b.shift(triangle.get_vertices()[1] + DOWN * b/2 + RIGHT * b/2)
        self.play(Create(square_b), run_time=1)
        self.wait(0.5)

        # Square on side c (red)
        square_c = Square(side_length=c, color=RED, fill_opacity=0.5)
        square_c.shift(triangle.get_vertices()[2] + UP * c/2 + LEFT * c/2)
        self.play(Create(square_c), run_time=1)
        self.wait(0.5)

        # Text overlay
        text1 = Text("Imagine building a perfect square", font_size=24)
        text1.to_edge(DOWN)
        self.play(Write(text1))
        self.wait(1)

        text2 = Text("on each of the three sides.", font_size=24)
        text2.next_to(text1, DOWN)
        self.play(ReplacementTransform(text1, text2))
        self.wait(1)

        text3 = Text("The area depends on side length.", font_size=24)
        text3.next_to(text2, DOWN)
        self.play(ReplacementTransform(text2, text3))
        self.wait(1)

        text4 = Text("Compare small squares to largest.", font_size=24)
        text4.next_to(text3, DOWN)
        self.play(ReplacementTransform(text3, text4))
        self.wait(1)

        # Fade out
        self.play(FadeOut(title), FadeOut(triangle), FadeOut(label_a), FadeOut(label_b), 
                  FadeOut(label_c), FadeOut(square_a), FadeOut(square_b), FadeOut(square_c),
                  FadeOut(text4))
        self.wait(0.5)
