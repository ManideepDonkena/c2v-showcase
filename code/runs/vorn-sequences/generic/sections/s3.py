from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Odd Number Property", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial terms
        seq = [1, 3, 5, 11]
        circles = []
        labels = []
        checkmarks = []

        for i, num in enumerate(seq):
            circle = Circle(radius=0.4).set_color([BLUE, GREEN, YELLOW, RED][i])
            circle.shift((i - 1.5) * RIGHT)
            num_text = Integer(num, font_size=32).move_to(circle.get_center())
            label = Text("Odd", font_size=24).next_to(circle, DOWN)
            checkmark = Tex(r"$\checkmark$", font_size=32).next_to(label, RIGHT)

            circles.append(circle)
            labels.append(label)
            checkmarks.append(checkmark)

            self.play(Create(circle), Write(num_text))
            self.wait(0.3)
            checkmark.shift(-0.25 * RIGHT + 0.0 * UP)  # layout: separation vector
            self.play(Write(label), Write(checkmark))
            self.wait(0.5)

        # Formula
        formula = MathTex("v(n) = v(n-1) + 2 \\times v(n-2)", font_size=32).to_edge(DOWN)
        self.play(Write(formula))
        self.wait(1)

        # Rule explanation
        rule_text = Text("Every term is odd.", font_size=24).next_to(formula, UP, buff=0.5)
        self.play(Write(rule_text))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(circles[0]), FadeOut(circles[1]), FadeOut(circles[2]), FadeOut(circles[3]),
            FadeOut(labels[0]), FadeOut(labels[1]), FadeOut(labels[2]), FadeOut(labels[3]),
            FadeOut(checkmarks[0]), FadeOut(checkmarks[1]), FadeOut(checkmarks[2]), FadeOut(checkmarks[3]),
            FadeOut(formula),
            FadeOut(rule_text)
        )
        self.wait(0.5)
