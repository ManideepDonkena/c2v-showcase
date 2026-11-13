from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Odd Number Property", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial sequence
        seq = [1, 3, 5, 11]
        circles = []
        labels = []
        checkmarks = []

        for i, num in enumerate(seq):
            circle = Circle(radius=0.4).set_color([BLUE, GREEN, YELLOW, RED][i])
            text = MathTex(str(num), font_size=32)
            text.move_to(circle.get_center())
            circles.append(circle)
            labels.append(text)

        # Arrange circles horizontally
        group = VGroup(*circles, *labels).arrange(RIGHT, buff=1.0)
        group.to_edge(UP, buff=1.5)

        for i in range(len(seq)):
            self.play(Create(circles[i]), Write(labels[i]))
            self.wait(0.3)

        # Add checkmarks and 'Odd' labels
        for i in range(len(seq)):
            check = Tex(r"\checkmark", font_size=32).set_color(GREEN)  # Fixed: removed extra backslash
            odd_label = Text("Odd", font_size=24).next_to(check, RIGHT)
            checkmark_group = VGroup(check, odd_label).next_to(circles[i], DOWN)
            self.play(Write(checkmark_group))
            checkmarks.append(checkmark_group)
            self.wait(0.3)

        # Narration: "Notice a key pattern: every single term in a Vorn sequence remains odd."
        narration1 = Text("Every term is odd", font_size=24).to_edge(DOWN)
        self.play(Write(narration1))
        self.wait(1.5)
        self.play(FadeOut(narration1))

        # Show calculation: Odd + 2 × Odd
        calc1 = MathTex("Odd + 2 \\times Odd", font_size=32)
        calc1.to_edge(UP, buff=0.5)

        calc1.shift(0.0 * RIGHT + 0.41 * UP)  # layout: separation vector
        self.play(Write(calc1))
        self.wait(1.0)

        # Breakdown into Odd + Even
        calc2 = MathTex("Odd + Even", font_size=32)
        calc2.next_to(calc1, DOWN, buff=0.5)
        calc2.shift(0.0 * RIGHT + -0.3 * UP)  # layout: separation vector
        self.play(Write(calc2))
        self.wait(1.0)

        # Visual demonstration of Odd + Even = Odd
        odd_circle = Circle(radius=0.4).set_color(BLUE)
        even_circle = Circle(radius=0.4).set_color(YELLOW)
        result_circle = Circle(radius=0.4).set_color(GREEN)

        odd_text = MathTex("Odd", font_size=24).move_to(odd_circle.get_center())
        even_text = MathTex("Even", font_size=24).move_to(even_circle.get_center())
        result_text = MathTex("Odd", font_size=24).move_to(result_circle.get_center())

        calc_group = VGroup(odd_circle, even_circle, result_circle).arrange(RIGHT, buff=1.0)
        texts = VGroup(odd_text, even_text, result_text)

        calc_group.to_edge(DOWN, buff=1.0)
        even_text.shift(0.0 * RIGHT + 0.33 * UP)  # layout: separation vector
        self.play(
            Transform(calc1.copy(), odd_circle),
            Transform(calc2.copy(), even_circle),
            Write(result_circle),
            Write(texts)
        )
        self.wait(1.5)

        # Algebraic breakdown
        algebra = MathTex("Odd + 2 \\times Odd = Odd + Even = Odd", font_size=32)
        algebra.to_edge(DOWN, buff=0.5)
        self.play(Transform(calc2, algebra))
        self.wait(2.0)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(VGroup(*circles, *labels, *checkmarks)),
            FadeOut(calc1),
            FadeOut(calc2),
            FadeOut(calc_group),
            FadeOut(texts)
        )
        self.wait(0.5)
