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
        label_b = MathTex("b", font_size=24).next_to(triangle.get_vertices()[1], LEFT)
        label_c = MathTex("c", font_size=24).next_to(triangle.get_vertices()[2], RIGHT)
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(0.5)

        # Narration text
        narration = Text("Imagine building a perfect square on each of the three sides.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        # Squares
        a = triangle.get_side_length(triangle.get_vertices()[0] - triangle.get_vertices()[1])
        b = triangle.get_side_length(triangle.get_vertices()[1] - triangle.get_vertices()[2])
        c = triangle.get_side_length(triangle.get_vertices()[2] - triangle.get_vertices()[0])

        square_a = Square(side_length=a, color=BLUE, fill_opacity=0.5)
        square_a.move_to(triangle.get_vertices()[0])
        square_b = Square(side_length=b, color=GREEN, fill_opacity=0.5)
        square_b.move_to(triangle.get_vertices()[1])
        square_c = Square(side_length=c, color=RED, fill_opacity=0.5)
        square_c.move_to(triangle.get_vertices()[2])

        # Animate squares growing
        self.play(
            Create(square_a),
            Create(square_b),
            Create(square_c),
            run_time=2
        )
        self.wait(1)

        # Narration text 2
        narration2 = Text("The area of these squares depends on the length of the side they are built upon.", font_size=24)
        narration2.to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(2)
        self.play(FadeOut(narration2))

        # Narration text 3
        narration3 = Text("We will compare the size of the two smaller squares against the largest one.", font_size=24)
        narration3.to_edge(DOWN)
        self.play(Write(narration3))
        self.wait(2)
        self.play(FadeOut(narration3))

        # Show that it only works for right angle
        # Create a non-right triangle to demonstrate
        triangle2 = Triangle().scale(2).rotate(0.5)
        triangle2.shift(DOWN * 0.5)
        self.play(Transform(triangle, triangle2))
        self.wait(1)

        # Show squares on new triangle
        a2 = triangle2.get_side_length(triangle2.get_vertices()[0] - triangle2.get_vertices()[1])
        b2 = triangle2.get_side_length(triangle2.get_vertices()[1] - triangle2.get_vertices()[2])
        c2 = triangle2.get_side_length(triangle2.get_vertices()[2] - triangle2.get_vertices()[0])

        square_a2 = Square(side_length=a2, color=BLUE, fill_opacity=0.5)
        square_a2.move_to(triangle2.get_vertices()[0])
        square_b2 = Square(side_length=b2, color=GREEN, fill_opacity=0.5)
        square_b2.move_to(triangle2.get_vertices()[1])
        square_c2 = Square(side_length=c2, color=RED, fill_opacity=0.5)
        square_c2.move_to(triangle2.get_vertices()[2])

        self.play(
            Create(square_a2),
            Create(square_b2),
            Create(square_c2),
            run_time=1
        )
        self.wait(1)

        # Narration text 4
        narration4 = Text("If the angle is not 90 degrees, the squares on the legs do not perfectly fill the square on the third side.", font_size=24)
        narration4.to_edge(DOWN)
        self.play(Write(narration4))
        self.wait(3)
        self.play(FadeOut(narration4))

        # Fade out everything
        self.play(
            FadeOut(triangle),
            FadeOut(triangle2),
            FadeOut(square_a),
            FadeOut(square_b),
            FadeOut(square_c),
            FadeOut(square_a2),
            FadeOut(square_b2),
            FadeOut(square_c2),
            FadeOut(label_a),
            FadeOut(label_b),
            FadeOut(label_c),
            FadeOut(title)
        )
        self.wait(0.5)
