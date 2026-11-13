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

        # Labels
        label_a = MathTex("a", font_size=24).next_to(triangle.get_vertices()[0], DOWN)
        label_b = MathTex("b", font_size=24).next_to(triangle.get_vertices()[1], RIGHT)
        label_c = MathTex("c", font_size=24).next_to(triangle.get_vertices()[2], LEFT)
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(0.5)

        # Get side lengths using get_length
        a = triangle.get_side_length("AB")
        b = triangle.get_side_length("BC")
        c = triangle.get_side_length("AC")

        # Squares
        square_a = Square(side_length=a, color=BLUE, fill_opacity=0.5)
        square_a.shift(triangle.get_vertices()[0] + DOWN * a/2 + LEFT * a/2)
        square_b = Square(side_length=b, color=GREEN, fill_opacity=0.5)
        square_b.shift(triangle.get_vertices()[1] + UP * b/2 + RIGHT * b/2)
        square_c = Square(side_length=c, color=RED, fill_opacity=0.5)
        square_c.shift(triangle.get_vertices()[2] + DOWN * c/2 + LEFT * c/2)

        # Animate squares growing
        self.play(
            Create(square_a),
            run_time=1
        )
        self.wait(0.5)
        self.play(
            Create(square_b),
            run_time=1
        )
        self.wait(0.5)
        self.play(
            Create(square_c),
            run_time=1
        )
        self.wait(1)

        # Text overlay
        text1 = Text("Building squares", font_size=24).to_corner(UL)
        self.play(Write(text1))
        self.wait(1)
        self.play(FadeOut(text1))

        text2 = Text("Area depends on side length", font_size=24).to_corner(UL)
        self.play(Write(text2))
        self.wait(1)
        self.play(FadeOut(text2))

        text3 = Text("Compare small vs large square", font_size=24).to_corner(UL)
        self.play(Write(text3))
        self.wait(1)
        self.play(FadeOut(text3))

        # Final wait
        self.wait(1)

        self.play(
            FadeOut(title),
            FadeOut(triangle),
            FadeOut(label_a),
            FadeOut(label_b),
            FadeOut(label_c),
            FadeOut(square_a),
            FadeOut(square_b),
            FadeOut(square_c)
        )
