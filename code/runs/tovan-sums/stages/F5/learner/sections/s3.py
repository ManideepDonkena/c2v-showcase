from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Absorbing Element (-1)", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial circles
        minus_one = Circle(radius=1.2, color=BLUE, fill_color=BLUE, fill_opacity=0.8)
        minus_one_label = MathTex(r"-1", font_size=40).move_to(minus_one.get_center())
        b = Circle(radius=1.2, color=RED, fill_color=RED, fill_opacity=0.8)
        b_label = MathTex(r"b", font_size=40).move_to(b.get_center())

        # Position circles
        minus_one.to_edge(LEFT, buff=2)
        b.to_edge(RIGHT, buff=2)

        self.play(Create(minus_one), Write(minus_one_label))
        b_label.shift(0.0 * RIGHT + 0.43 * UP)  # layout: separation vector
        self.play(Create(b), Write(b_label))
        self.wait(1)

        # Move -1 towards b
        self.play(minus_one.animate.move_to((minus_one.get_center() + b.get_center()) / 2), run_time=1.5)
        self.wait(0.5)

        # Collision effect: b disappears, -1 stays
        self.play(FadeOut(b), FadeOut(b_label))
        self.wait(0.5)

        # Show result
        result_text = MathTex(r"(-1) \oplus b = -1", font_size=32).to_edge(DOWN)
        self.play(Write(result_text))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(minus_one), FadeOut(minus_one_label), FadeOut(result_text))
        self.wait(0.5)

        # New chain animation
        # Create three circles labeled '3', '(-1)', and '7'
        circle3 = Circle(radius=0.6, color=GREEN, fill_color=GREEN, fill_opacity=0.8)
        label3 = MathTex(r"3", font_size=24).move_to(circle3.get_center())
        circle_neg1 = Circle(radius=0.6, color=YELLOW, fill_color=YELLOW, fill_opacity=0.8)
        label_neg1 = MathTex(r"(-1)", font_size=24).move_to(circle_neg1.get_center())
        circle7 = Circle(radius=0.6, color=PURPLE, fill_color=PURPLE, fill_opacity=0.8)
        label7 = MathTex(r"7", font_size=24).move_to(circle7.get_center())

        # Arrange horizontally
        circle3.to_edge(LEFT, buff=1.5)
        circle_neg1.next_to(circle3, RIGHT, buff=1)
        circle7.next_to(circle_neg1, RIGHT, buff=1)

        self.play(Create(circle3), Write(label3))
        label_neg1.shift(0.0 * RIGHT + 0.36 * UP)  # layout: separation vector
        self.play(Create(circle_neg1), Write(label_neg1))
        circle7.shift(-0.19 * RIGHT + 0.0 * UP)  # layout: separation vector
        label7.shift(0.26 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(circle7), Write(label7))
        self.wait(0.5)

        # Say "When chaining, we go left to right."
        self.play(Write(Text("When chaining, we go left to right.", font_size=24).to_edge(DOWN)))
        self.wait(1.5)
        self.play(FadeOut(Text("When chaining, we go left to right.", font_size=24).to_edge(DOWN)))

        # Merge first two circles
        merged_circle = Circle(radius=0.6, color=DARK_BROWN, fill_color=DARK_BROWN, fill_opacity=0.8)
        merged_label = MathTex(r"-1", font_size=24).move_to(merged_circle.get_center())
        self.play(
            ReplacementTransform(circle3, merged_circle),
            Transform(label3, merged_label),
            FadeOut(circle_neg1),
            FadeOut(label_neg1)
        )
        self.wait(0.5)

        # Move merged circle to merge with third
        self.play(merged_circle.animate.move_to((merged_circle.get_center() + circle7.get_center()) / 2))
        self.wait(0.5)

        # Final merge
        final_circle = Circle(radius=0.6, color=DARK_BROWN, fill_color=DARK_BROWN, fill_opacity=0.8)
        final_label = MathTex(r"-1", font_size=24).move_to(final_circle.get_center())
        self.play(
            ReplacementTransform(merged_circle, final_circle),
            ReplacementTransform(merged_label, final_label),
            FadeOut(circle7),
            FadeOut(label7)
        )
        self.wait(0.5)

        # Say "Because -1 swallows everything it touches, the entire chain collapses to -1."
        self.play(Write(Text("Because -1 swallows everything it touches, the entire chain collapses to -1.", font_size=24).to_edge(DOWN)))
        self.wait(2)
        self.play(FadeOut(Text("Because -1 swallows everything it touches, the entire chain collapses to -1.", font_size=24).to_edge(DOWN)))

        # Fade out final circle
        self.play(FadeOut(final_circle), FadeOut(final_label))
        self.wait(0.5)
