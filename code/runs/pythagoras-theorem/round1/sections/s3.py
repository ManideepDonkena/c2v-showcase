from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Area Connection", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Squares a, b, c
        square_a = Square(side_length=3, color=BLUE, fill_opacity=0.5).shift(2*LEFT + 1*DOWN)
        square_b = Square(side_length=4, color=GREEN, fill_opacity=0.5).shift(2*RIGHT + 1*DOWN)
        square_c = Square(side_length=5, color=RED, fill_opacity=0.5).shift(1*UP)

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
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.play(Write(area_a), Write(area_b), Write(area_c))
        self.wait(1)

        # Show area equality
        eq_text = MathTex("9 + 16 = 25", font_size=30).move_to(UP * 1.5)
        self.play(Write(eq_text))
        self.wait(1)

        # Fade out labels and areas
        self.play(FadeOut(label_a), FadeOut(label_b), FadeOut(label_c),
                  FadeOut(area_a), FadeOut(area_b), FadeOut(area_c))

        # Show sqrt operation
        sqrt_eq = MathTex("\sqrt{25} = 5", font_size=30).move_to(UP * 1.5)
        self.play(Transform(eq_text, sqrt_eq))
        self.wait(1)

        # Show irrational example: 1^2 + 1^2 = 2 -> c = sqrt(2)
        self.play(FadeOut(eq_text))

        square_a2 = Square(side_length=1, color=BLUE, fill_opacity=0.5).shift(3*LEFT + 1*DOWN)
        square_b2 = Square(side_length=1, color=GREEN, fill_opacity=0.5).shift(3*RIGHT + 1*DOWN)
        square_c2 = Square(side_length=1.414, color=RED, fill_opacity=0.5).shift(1*UP)

        label_a2 = MathTex("a = 1", font_size=24).next_to(square_a2, DOWN)
        label_b2 = MathTex("b = 1", font_size=24).next_to(square_b2, DOWN)
        label_c2 = MathTex("c =\\sqrt{2} \\approx 1.41", font_size=24).next_to(square_c2, UP)

        area_a2 = MathTex("a^2 = 1", font_size=24).next_to(square_a2, UP)
        area_b2 = MathTex("b^2 = 1", font_size=24).next_to(square_b2, UP)
        area_c2 = MathTex("c^2 = 2", font_size=24).next_to(square_c2, DOWN)

        self.play(Create(square_a2), Create(square_b2), Create(square_c2))
        self.play(Write(label_a2), Write(label_b2), Write(label_c2))
        self.play(Write(area_a2), Write(area_b2), Write(area_c2))
        self.wait(1)

        # Fade out
        self.play(FadeOut(square_a2), FadeOut(square_b2), FadeOut(square_c2),
                  FadeOut(label_a2), FadeOut(label_b2), FadeOut(label_c2),
                  FadeOut(area_a2), FadeOut(area_b2), FadeOut(area_c2))

        # Show large numbers: 9^2 + 12^2 = 225 -> c = 15
        self.play(FadeOut(eq_text))
        square_a3 = Square(side_length=9, color=BLUE, fill_opacity=0.5).shift(3*LEFT + 1*DOWN)
        square_b3 = Square(side_length=12, color=GREEN, fill_opacity=0.5).shift(3*RIGHT + 1*DOWN)
        square_c3 = Square(side_length=15, color=RED, fill_opacity=0.5).shift(1*UP)

        label_a3 = MathTex("a = 9", font_size=24).next_to(square_a3, DOWN)
        label_b3 = MathTex("b = 12", font_size=24).next_to(square_b3, DOWN)
        label_c3 = MathTex("c = 15", font_size=24).next_to(square_c3, UP)

        area_a3 = MathTex("a^2 = 81", font_size=24).next_to(square_a3, UP)
        area_b3 = MathTex("b^2 = 144", font_size=24).next_to(square_b3, UP)
        area_c3 = MathTex("c^2 = 225", font_size=24).next_to(square_c3, DOWN)

        self.play(Create(square_a3), Create(square_b3), Create(square_c3))
        self.play(Write(label_a3), Write(label_b3), Write(label_c3))
        self.play(Write(area_a3), Write(area_b3), Write(area_c3))

        sum_text = MathTex("81 + 144 = 225", font_size=30).move_to(UP * 1.5)
        self.play(Write(sum_text))
        sqrt_text = MathTex("\sqrt{225} = 15", font_size=30).move_to(UP * 1.5)
        self.play(Transform(sum_text, sqrt_text))
        self.wait(1)

        # Show another large example: 5^2 + 12^2 = 169 -> c = 13
        self.play(FadeOut(square_a3), FadeOut(square_b3), FadeOut(square_c3),
                  FadeOut(label_a3), FadeOut(label_b3), FadeOut(label_c3),
                  FadeOut(area_a3), FadeOut(area_b3), FadeOut(area_c3),
                  FadeOut(sum_text))

        square_a4 = Square(side_length=5, color=BLUE, fill_opacity=0.5).shift(3*LEFT + 1*DOWN)
        square_b4 = Square(side_length=12, color=GREEN, fill_opacity=0.5).shift(3*RIGHT + 1*DOWN)
        square_c4 = Square(side_length=13, color=RED, fill_opacity=0.5).shift(1*UP)

        label_a4 = MathTex("a = 5", font_size=24).next_to(square_a4, DOWN)
        label_b4 = MathTex("b = 12", font_size=24).next_to(square_b4, DOWN)
        label_c4 = MathTex("c = 13", font_size=24).next_to(square_c4, UP)

        area_a4 = MathTex("a^2 = 25", font_size=24).next_to(square_a4, UP)
        area_b4 = MathTex("b^2 = 144", font_size=24).next_to(square_b4, UP)
        area_c4 = MathTex("c^2 = 169", font_size=24).next_to(square_c4, DOWN)

        self.play(Create(square_a4), Create(square_b4), Create(square_c4))
        self.play(Write(label_a4), Write(label_b4), Write(label_c4))
        self.play(Write(area_a4), Write(area_b4), Write(area_c4))

        sum_text2 = MathTex("25 + 144 = 169", font_size=30).move_to(UP * 1.5)
        self.play(Write(sum_text2))
        sqrt_text2 = MathTex("\sqrt{169} = 13", font_size=30).move_to(UP * 1.5)
        self.play(Transform(sum_text2, sqrt_text2))
        self.wait(1)

        # Show incorrect method: a + b vs correct method
        self.play(FadeOut(square_a4), FadeOut(square_b4), FadeOut(square_c4),
                  FadeOut(label_a4), FadeOut(label_b4), FadeOut(label_c4),
                  FadeOut(area_a4), FadeOut(area_b4), FadeOut(area_c4),
                  FadeOut(sum_text2))

        wrong_sum = MathTex("a + b = 3 + 4 = 7", font_size=30).move_to(UP * 1.5)
        correct_sum = MathTex("a^2 + b^2 = 9 + 16 = 25 \Rightarrow c = 5", font_size=30).move_to(UP * 1.5)

        self.play(Write(wrong_sum))
        self.wait(1)
        self.play(Transform(wrong_sum, correct_sum))
        self.wait(1)

        # Show final large example: 9^2 + 40^2 = 1681 -> c = 41
        self.play(FadeOut(wrong_sum))

        square_a5 = Square(side_length=9, color=BLUE, fill_opacity=0.5).shift(3*LEFT + 1*DOWN)
        square_b5 = Square(side_length=40, color=GREEN, fill_opacity=0.5).shift(3*RIGHT + 1*DOWN)
        square_c5 = Square(side_length=41, color=RED, fill_opacity=0.5).shift(1*UP)

        label_a5 = MathTex("a = 9", font_size=24).next_to(square_a5, DOWN)
        label_b5 = MathTex("b = 40", font_size=24).next_to(square_b5, DOWN)
        label_c5 = MathTex("c = 41", font_size=24).next_to(square_c5, UP)

        area_a5 = MathTex("a^2 = 81", font_size=24).next_to(square_a5, UP)
        area_b5 = MathTex("b^2 = 1600", font_size=24).next_to(square_b5, UP)
        area_c5 = MathTex("c^2 = 1681", font_size=24).next_to(square_c5, DOWN)

        self.play(Create(square_a5), Create(square_b5), Create(square_c5))
        self.play(Write(label_a5), Write(label_b5), Write(label_c5))
        self.play(Write(area_a5), Write(area_b5), Write(area_c5))

        sum_text3 = MathTex("81 + 1600 = 1681", font_size=30).move_to(UP * 1.5)
        self.play(Write(sum_text3))
        sqrt_text3 = MathTex("\sqrt{1681} = 41", font_size=30).move_to(UP * 1.5)
        self.play(Transform(sum_text3, sqrt_text3))
        self.wait(1)

        # Show last example: 15^2 + 8^2 = 289 -> c = 17
        self.play(FadeOut(square_a5), FadeOut(square_b5), FadeOut(square_c5),
                  FadeOut(label_a5), FadeOut(label_b5), FadeOut(label_c5),
                  FadeOut(area_a5), FadeOut(area_b5), FadeOut(area_c5),
                  FadeOut(sum_text3))

        square_a6 = Square(side_length=15, color=BLUE, fill_opacity=0.5).shift(3*LEFT + 1*DOWN)
        square_b6 = Square(side_length=8, color=GREEN, fill_opacity=0.5).shift(3*RIGHT + 1*DOWN)
        square_c6 = Square(side_length=17, color=RED, fill_opacity=0.5).shift(1*UP)

        label_a6 = MathTex("a = 15", font_size=24).next_to(square_a6, DOWN)
        label_b6 = MathTex("b = 8", font_size=24).next_to(square_b6, DOWN)
        label_c6 = MathTex("c = 17", font_size=24).next_to(square_c6, UP)

        area_a6 = MathTex("a^2 = 225", font_size=24).next_to(square_a6, UP)
        area_b6 = MathTex("b^2 = 64", font_size=24).next_to(square_b6, UP)
        area_c6 = MathTex("c^2 = 289", font_size=24).next_to(square_c6, DOWN)

        self.play(Create(square_a6), Create(square_b6), Create(square_c6))
        self.play(Write(label_a6), Write(label_b6), Write(label_c6))
        self.play(Write(area_a6), Write(area_b6), Write(area_c6))

        sum_text4 = MathTex("225 + 64 = 289", font_size=30).move_to(UP * 1.5)
        self.play(Write(sum_text4))
        sqrt_text4 = MathTex("\sqrt{289} = 17", font_size=30).move_to(UP * 1.5)
        self.play(Transform(sum_text4, sqrt_text4))
        self.wait(1)

        # Final fade out
        self.play(FadeOut(square_a6), FadeOut(square_b6), FadeOut(square_c6),
                  FadeOut(label_a6), FadeOut(label_b6), FadeOut(label_c6),
                  FadeOut(area_a6), FadeOut(area_b6), FadeOut(area_c6),
                  FadeOut(sum_text4))
        self.wait(0.5)
