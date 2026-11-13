from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Area Connection", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Squares
        a, b, c = 3, 4, 5
        square_a = Square(side_length=a, color=BLUE, fill_opacity=0.5).shift(2*LEFT + 1.5*DOWN)
        square_b = Square(side_length=b, color=GREEN, fill_opacity=0.5).shift(2*RIGHT + 1.5*DOWN)
        square_c = Square(side_length=c, color=RED, fill_opacity=0.5).shift(1.5*UP)

        # Labels
        label_a = MathTex("a = 3", font_size=24).next_to(square_a, DOWN)
        label_b = MathTex("b = 4", font_size=24).next_to(square_b, DOWN)
        label_c = MathTex("c = 5", font_size=24).next_to(square_c, UP)

        self.play(Create(square_a), Create(square_b), Create(square_c))
        label_c.shift(0.0 * RIGHT + -0.57 * UP)  # layout: separation vector
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(1)

        # Area labels
        area_a = MathTex("a^2 = 9", font_size=24).next_to(square_a, UP)
        area_b = MathTex("b^2 = 16", font_size=24).next_to(square_b, UP)
        area_c = MathTex("c^2 = 25", font_size=24).next_to(square_c, DOWN)

        self.play(Write(area_a), Write(area_b), Write(area_c))
        self.wait(1.5)

        # Liquid flow animation
        blue_sq = square_a.copy()
        green_sq = square_b.copy()

        self.play(
            FadeOut(label_a, label_b, label_c),
            FadeOut(area_a, area_b, area_c),
            Transform(blue_sq, square_c),
            Transform(green_sq, square_c),
            run_time=2
        )
        self.wait(1)

        # Show the sum check: 36 + 64 = 100
        a2, b2, c2 = 6, 8, 10
        square_a2 = Square(side_length=a2, color=BLUE, fill_opacity=0.5).shift(2*LEFT + 1.5*DOWN)
        square_b2 = Square(side_length=b2, color=GREEN, fill_opacity=0.5).shift(2*RIGHT + 1.5*DOWN)
        square_c2 = Square(side_length=c2, color=RED, fill_opacity=0.5).shift(1.5*UP)

        label_a2 = MathTex("a = 6", font_size=24).next_to(square_a2, DOWN)
        label_b2 = MathTex("b = 8", font_size=24).next_to(square_b2, DOWN)
        label_c2 = MathTex("c = 10", font_size=24).next_to(square_c2, UP)

        area_a2 = MathTex("a^2 = 36", font_size=24).next_to(square_a2, UP)
        area_b2 = MathTex("b^2 = 64", font_size=24).next_to(square_b2, UP)
        area_c2 = MathTex("c^2 = 100", font_size=24).next_to(square_c2, DOWN)

        self.play(
            FadeOut(blue_sq, green_sq),
            Create(square_a2), Create(square_b2), Create(square_c2),
            Write(label_a2), Write(label_b2), Write(label_c2),
            Write(area_a2), Write(area_b2), Write(area_c2)
        )
        self.wait(1.5)

        # Show sum
        sum_text = MathTex("36 + 64 = 100", font_size=30).to_edge(UP)
        self.play(Write(sum_text))
        self.wait(1.5)

        # Show error: adding lengths
        error_text = Text("Adding lengths ignores area!", font_size=24).to_edge(DOWN)
        self.play(Write(error_text))
        self.wait(1.5)

        # Show correct way
        correct_text = Text("Square first, then add.", font_size=24).next_to(error_text, UP)
        self.play(Write(correct_text))
        self.wait(1.5)

        self.play(
            FadeOut(sum_text, error_text, correct_text),
            FadeOut(square_a2, square_b2, square_c2),
            FadeOut(area_a2, area_b2, area_c2),
            FadeOut(title)
        )
        self.wait(0.5)
