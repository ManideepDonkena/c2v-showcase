from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Pythagoras Theorem: Visual Proof", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Triangle
        triangle = Polygon(
            [0, 0, 0], [3, 0, 0], [0, 4, 0],
            color=WHITE, fill_opacity=0.2
        )
        triangle.shift(LEFT * 1.5 + DOWN * 0.5)
        triangle.shift(0.0 * RIGHT + -0.65 * UP)  # layout: separation vector
        self.play(Create(triangle))
        self.wait(0.5)

        # Labels for sides
        a_label = MathTex("a", font_size=30).next_to(triangle.get_vertices()[0], DOWN)
        b_label = MathTex("b", font_size=30).next_to(triangle.get_vertices()[1], DOWN)
        c_label = MathTex("c", font_size=30).next_to(triangle.get_vertices()[2], LEFT)

        self.play(Write(a_label), Write(b_label), Write(c_label))
        self.wait(0.5)

        # Text prompt
        prompt = Text("Imagine building a perfect square on each of the three sides.", font_size=24)
        prompt.to_edge(DOWN)
        self.play(Write(prompt))
        self.wait(1.5)

        # Fade out prompt
        self.play(FadeOut(prompt))

        # Square on side 'a'
        square_a = Square(side_length=3, color=BLUE, fill_opacity=0.5)
        square_a.move_to(triangle.get_vertices()[0])
        square_a.shift(LEFT * 1.5 + DOWN * 0.5)
        square_a.shift(-0.22 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(square_a), run_time=1.5)
        self.wait(0.5)

        # Square on side 'b'
        square_b = Square(side_length=4, color=GREEN, fill_opacity=0.5)
        square_b.move_to(triangle.get_vertices()[1])
        square_b.shift(LEFT * 1.5 + DOWN * 0.5)
        self.play(Create(square_b), run_time=1.5)
        self.wait(0.5)

        # Square on side 'c'
        square_c = Square(side_length=5, color=RED, fill_opacity=0.5)
        square_c.move_to(triangle.get_vertices()[2])
        square_c.shift(LEFT * 1.5 + DOWN * 0.5)
        square_c.shift(0.0 * RIGHT + -2.0 * UP)  # layout: separation vector
        self.play(Create(square_c), run_time=1.5)
        self.wait(0.5)

        # Text explanation
        explanation = Text("The area of these squares depends on the length of the side they are built upon.", font_size=24)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)

        # Fade out explanation
        self.play(FadeOut(explanation))

        # Final text
        final_text = Text("We will compare the size of the two smaller squares against the largest one.", font_size=24)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(triangle), FadeOut(a_label), FadeOut(b_label), FadeOut(c_label),
                  FadeOut(square_a), FadeOut(square_b), FadeOut(square_c), FadeOut(final_text))
