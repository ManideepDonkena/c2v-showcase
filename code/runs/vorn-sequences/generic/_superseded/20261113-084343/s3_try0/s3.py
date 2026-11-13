from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Odd Number Property", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial terms
        terms = [1, 3, 5, 11]
        circles = []
        labels = []
        checkmarks = []
        odd_labels = []

        for i, term in enumerate(terms):
            # Circle
            circle = Circle(radius=0.4).move_to(LEFT * (3 - i*2))
            circle.set_fill(opacity=0.3)
            circle.set_stroke(width=3)
            circles.append(circle)

            # Number
            num = MathTex(str(term), font_size=36).move_to(circle.get_center())
            num.set_stroke(width=1)

            # Color
            colors = [RED, GREEN, BLUE, YELLOW]
            circle.set_fill(colors[i])
            circle.set_stroke(colors[i], width=3)
            # Checkmark
            check = Text("✓", font_size=40).next_to(circle, RIGHT)
            checkmarks.append(check)
            # Odd label
            odd_label = Text("Odd", font_size=24).next_to(check, RIGHT)
            odd_labels.append(odd_label)

            self.play(
                Create(circle),
                Write(num),
                run_time=0.5
            )
            self.wait(0.2)
            self.play(
                Write(check),
                Write(odd_label),
                run_time=0.3
            )
            self.wait(0.3)

        # Narration text
        narration = Text("Notice a key pattern:", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.0)

        # Fade out
        self.play(
            FadeOut(narration),
            *[FadeOut(c) for c in circles + [num] + checkmarks + odd_labels]
        )
        self.wait(0.5)

        # Final statement
        final = Text("Every term remains odd.", font_size=28).to_edge(DOWN)
        self.play(Write(final))
        self.wait(1.5)

        self.play(FadeOut(final))
        self.wait(0.5)
        self.play(FadeOut(title))
        self.wait(0.5)
