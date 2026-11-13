from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Area Connection", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Squares
        square_a = Square(side_length=3, color=BLUE, fill_opacity=0.5)
        square_a.shift(2*LEFT + 1.5*DOWN)
        square_b = Square(side_length=4, color=GREEN, fill_opacity=0.5)
        square_b.shift(2*RIGHT + 1.5*DOWN)
        square_c = Square(side_length=5, color=RED, fill_opacity=0.5)
        square_c.shift(1.5*UP)

        # Labels
        label_a = MathTex("a = 3", font_size=24).next_to(square_a, DOWN)
        label_b = MathTex("b = 4", font_size=24).next_to(square_b, DOWN)
        label_c = MathTex("c = 5", font_size=24).next_to(square_c, UP)

        # Area labels
        area_a = MathTex("a^2 = 9", font_size=24).next_to(square_a, UP)
        area_b = MathTex("b^2 = 16", font_size=24).next_to(square_b, UP)
        area_c = MathTex("c^2 = 25", font_size=24).next_to(square_c, DOWN)

        # Show initial setup
        self.play(Create(square_a), Create(square_b), Create(square_c))
        label_c.shift(0.0 * RIGHT + -0.57 * UP)  # layout: separation vector
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.play(Write(area_a), Write(area_b), Write(area_c))
        self.wait(1)

        # Animation: liquid flow from a and b to c
        # Fade out labels and areas
        self.play(FadeOut(label_a, label_b, label_c, area_a, area_b, area_c))

        # Create moving shapes for liquid effect
        square_a_copy = square_a.copy()
        square_b_copy = square_b.copy()
        square_a_copy.set_fill(opacity=0.8)
        square_b_copy.set_fill(opacity=0.8)

        # Animate the flow
        self.play(
            square_a_copy.animate.move_to(square_c.get_center()),
            square_b_copy.animate.move_to(square_c.get_center()),
            run_time=2
        )

        # Show final area
        final_area = MathTex("9 + 16 = 25", font_size=30).move_to(square_c.get_center())
        self.play(Write(final_area))
        self.wait(2)

        # Clean up
        self.play(FadeOut(square_a_copy, square_b_copy, final_area, title))
        self.wait(0.5)
