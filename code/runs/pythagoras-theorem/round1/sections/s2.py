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
        
        self.play(Create(triangle))
        self.wait(0.5)
        
        # Get vertices
        v0, v1, v2 = triangle.get_vertices()
        
        # Labels
        label_a = MathTex("a").next_to(v0, DOWN, buff=0.2)
        label_b = MathTex("b").next_to(v1, RIGHT, buff=0.2)
        label_c = MathTex("c").next_to(v2, LEFT, buff=0.2)
        
        label_b.shift(0.0 * RIGHT + -0.33 * UP)  # layout: separation vector
        label_c.shift(0.0 * RIGHT + -0.26 * UP)  # layout: separation vector
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(0.5)

        # Square on side a (blue)
        a = np.linalg.norm(v1 - v0)
        square_a = Square(side_length=a, color=BLUE, fill_opacity=0.5)
        square_a.shift(v0 + DOWN * a/2 + LEFT * a/2)
        square_a.shift(-0.26 * RIGHT + 0.0 * UP)  # layout: separation vector
        square_a.shift(0.0 * RIGHT + 0.46 * UP)  # layout: separation vector
        self.play(Create(square_a), run_time=1)
        self.wait(0.5)

        # Square on side b (green)
        b = np.linalg.norm(v2 - v1)
        square_b = Square(side_length=b, color=GREEN, fill_opacity=0.5)
        square_b.shift(v1 + UP * b/2 + RIGHT * b/2)
        self.play(Create(square_b), run_time=1)
        self.wait(0.5)

        # Square on side c (red)
        c = np.linalg.norm(v0 - v2)
        square_c = Square(side_length=c, color=RED, fill_opacity=0.5)
        square_c.shift(v2 + UP * c/2 + LEFT * c/2)
        self.play(Create(square_c), run_time=1)
        self.wait(1)

        # Text overlay
        text1 = Text("Building squares", font_size=24).to_edge(UP).shift(DOWN*0.5)
        self.play(Write(text1))
        self.wait(1)
        
        text2 = Text("Area depends on side length", font_size=24).next_to(text1, DOWN)
        self.play(Write(text2))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(title), FadeOut(triangle), FadeOut(label_a), FadeOut(label_b), FadeOut(label_c),
                  FadeOut(square_a), FadeOut(square_b), FadeOut(square_c), FadeOut(text1), FadeOut(text2))
        self.wait(0.5)
