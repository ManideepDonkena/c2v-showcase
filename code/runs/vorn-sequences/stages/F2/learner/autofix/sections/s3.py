from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Odd Number Property", font_size=36).to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # Initial terms
        seq = [1, 3, 5, 11]
        circles = []
        labels = []
        checkmarks = []

        # Create colored circles with numbers
        for i, num in enumerate(seq):
            circle = Circle(radius=0.4, color=[RED, GREEN, BLUE, YELLOW][i]).set_fill(opacity=0.3)
            number = Tex(str(num), font_size=28)  # Use Tex instead of MathTex
            number.move_to(circle.get_center())
            circles.append(VGroup(circle, number))

        # Arrange circles horizontally
        seq_group = VGroup(*circles).arrange(RIGHT, buff=0.8).move_to(DOWN * 0.5)

        # Animate appearance of sequence
        self.play(Create(seq_group), run_time=1)
        self.wait(0.5)

        # Add checkmarks and labels
        for i, circle in enumerate(circles):
            check = Tex(r"\checkmark", font_size=36, color=GREEN).next_to(circle, RIGHT, buff=0.3)  # Fixed LaTeX syntax
            odd_label = Text("Odd", font_size=24).next_to(check, RIGHT, buff=0.3)
            self.play(Write(check), run_time=0.5)
            odd_label.shift(0.0 * RIGHT + 0.38 * UP)  # layout: separation vector
            odd_label.shift(0.0 * RIGHT + 0.3 * UP)  # layout: separation vector
            self.play(Write(odd_label), run_time=0.5)
            checkmarks.append(check)
            labels.append(odd_label)
        
        # Narration text
        narration = Text("Notice a key pattern: every single term in a Vorn sequence remains odd.", font_size=24).to_edge(DOWN, buff=0.3)
        self.play(Write(narration), run_time=1)
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(narration), FadeOut(title))
        self.wait(0.5)
