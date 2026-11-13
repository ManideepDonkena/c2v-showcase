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
        numbers = []
        checkmarks = []
        labels = []

        for i, num in enumerate(seq):
            circle = Circle(radius=0.4).set_color([BLUE, GREEN, YELLOW, RED][i])
            number = MathTex(str(num), font_size=32)
            number.move_to(circle.get_center())
            circles.append(circle)
            numbers.append(number)

        # Arrange circles horizontally
        group = VGroup(*circles, *numbers).arrange(RIGHT, buff=0.8)
        group.to_edge(UP, buff=1.5)
        self.play(*[Create(c) for c in circles], *[Write(n) for n in numbers])
        self.wait(1)

        # Add checkmarks and labels
        for i, (circle, num) in enumerate(zip(circles, numbers)):
            check = Tex(r"\checkmark", font_size=40, color=GREEN).next_to(circle, DOWN)
            label = Text("Odd", font_size=24).next_to(check, DOWN)
            checkmarks.append(check)
            labels.append(label)
            self.play(Write(check), Write(label))
            self.wait(0.5)
        
        # Show rule explanation
        rule_text = Text("Rule: v(n) = v(n-1) + 2×v(n-2)", font_size=24).to_edge(DOWN)
        self.play(Write(rule_text))
        self.wait(1)

        # Example calculation
        calc = MathTex("v(3) = 3 + 2 \\times 1 = 5", font_size=30)
        calc.next_to(rule_text, UP, buff=0.5)
        self.play(Write(calc))
        self.wait(1.5)

        # Another example
        calc2 = MathTex("v(4) = 5 + 2 \\times 3 = 11", font_size=30)
        calc2.next_to(calc, DOWN, buff=0.5)
        calc2.shift(0.0 * RIGHT + -0.45 * UP)  # layout: separation vector
        self.play(Write(calc2))
        self.wait(1.5)

        # Fade out everything except title and sequence
        self.play(
            FadeOut(rule_text),
            FadeOut(calc),
            FadeOut(calc2),
            *[FadeOut(c) for c in checkmarks],
            *[FadeOut(l) for l in labels]
        )
        self.wait(0.5)

        # Final statement
        final = Text("Every term remains odd.", font_size=28).to_edge(DOWN)
        self.play(Write(final))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(group), FadeOut(final))
        self.wait(0.5)
