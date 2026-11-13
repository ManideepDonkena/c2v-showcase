from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Absorbing Element (-1)", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First animation: -1 absorbs b
        neg_one = Circle(color=WHITE, fill_color=DARK_GRAY, fill_opacity=1, radius=1)
        neg_one_label = MathTex("-1", font_size=40).move_to(neg_one.get_center())
        b_circle = Circle(color=BLUE, fill_color=BLUE, fill_opacity=0.5, radius=1)
        b_label = MathTex("b", font_size=40).move_to(b_circle.get_center())

        neg_one.move_to(LEFT * 3)
        b_circle.move_to(RIGHT * 3)

        self.play(Create(neg_one), Write(neg_one_label))
        b_label.shift(0.0 * RIGHT + 0.43 * UP)  # layout: separation vector
        self.play(Create(b_circle), Write(b_label))
        self.wait(1)

        # Move -1 towards b
        self.play(neg_one.animate.shift(RIGHT * 3), run_time=1.5)
        self.wait(0.5)

        # Absorb effect
        self.play(FadeOut(b_circle), FadeOut(b_label), run_time=0.5)
        result = MathTex("=-1", font_size=40).next_to(neg_one, DOWN)
        self.play(Write(result))
        self.wait(1.5)

        # Clear screen
        self.play(FadeOut(neg_one), FadeOut(neg_one_label), FadeOut(result))
        self.wait(0.5)

        # Chain example: 3 ⊕ (-1) ⊕ 7
        text = Text("When chaining, we go left to right.", font_size=24).to_edge(UP)
        text.shift(0.0 * RIGHT + 0.49 * UP)  # layout: separation vector
        self.play(Write(text))
        self.wait(0.5)

        circle_3 = Circle(color=GREEN, fill_color=GREEN, fill_opacity=0.5, radius=0.6)
        label_3 = MathTex("3", font_size=24).move_to(circle_3.get_center())
        circle_neg1 = Circle(color=DARK_GRAY, fill_color=DARK_GRAY, fill_opacity=1, radius=0.6)
        label_neg1 = MathTex("-1", font_size=24).move_to(circle_neg1.get_center())
        circle_7 = Circle(color=YELLOW, fill_color=YELLOW, fill_opacity=0.5, radius=0.6)
        label_7 = MathTex("7", font_size=24).move_to(circle_7.get_center())

        group = VGroup(circle_3, label_3, circle_neg1, label_neg1, circle_7, label_7)
        group.arrange(RIGHT, buff=0.5)
        group.move_to(DOWN * 0.5)

        self.play(Create(circle_3), Write(label_3))
        self.play(Create(circle_neg1), Write(label_neg1))
        self.play(Create(circle_7), Write(label_7))
        self.wait(1)

        # First merge: 3 ⊕ (-1) = -1
        new_circle = Circle(color=DARK_GRAY, fill_color=DARK_GRAY, fill_opacity=1, radius=0.6)
        new_label = MathTex("-1", font_size=24).move_to(new_circle.get_center())
        self.play(
            Transform(circle_3, new_circle),
            Transform(label_3, new_label),
            FadeOut(circle_neg1),
            FadeOut(label_neg1),
            run_time=1
        )
        self.wait(0.5)

        # Second merge: (-1) ⊕ 7 = -1
        final_circle = Circle(color=DARK_GRAY, fill_color=DARK_GRAY, fill_opacity=1, radius=0.6)
        final_label = MathTex("-1", font_size=24).move_to(final_circle.get_center())
        self.play(
            Transform(circle_3, final_circle),
            Transform(label_3, final_label),
            FadeOut(circle_7),
            FadeOut(label_7),
            run_time=1
        )
        self.wait(1)

        # Final result text
        final_text = Text("Because -1 swallows everything it touches, the entire chain collapses to -1.", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(text), FadeOut(final_text))
        self.wait(0.5)
