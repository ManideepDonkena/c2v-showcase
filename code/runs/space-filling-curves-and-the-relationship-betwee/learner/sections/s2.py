from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Length Paradox", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Bounding box
        box = Square(side_length=1, color=WHITE)
        box.move_to(ORIGIN)
        self.play(Create(box))
        self.wait(0.5)

        # Initial curve (iteration 1)
        line1 = Line(start=LEFT*0.5, end=RIGHT*0.5, color=YELLOW)
        self.play(Create(line1))
        self.wait(0.5)

        # Labels for iteration 1
        label1 = MathTex("Iteration\\ 1: Length\\ 3", font_size=24)
        label1.next_to(box, DOWN, buff=0.3)
        self.play(Write(label1))
        self.wait(1)

        # First iteration - replace line with more complex curve
        self.play(FadeOut(line1))
        curve1 = VMobject()
        curve1.set_points_as_corners([
            LEFT*0.5, UP*0.25, RIGHT*0.5, DOWN*0.25, LEFT*0.5
        ])
        curve1.set_color(YELLOW)
        self.play(Create(curve1))
        self.wait(0.5)

        # Update label for iteration 2
        self.play(Transform(label1, MathTex("Iteration\\ 2: Length\\ 9", font_size=24)))
        self.wait(1)

        # Second iteration - even more complex curve
        self.play(FadeOut(curve1))
        curve2 = VMobject()
        curve2.set_points_as_corners([
            LEFT*0.5, UP*0.25, RIGHT*0.5, DOWN*0.25, 
            LEFT*0.5, UP*0.125, RIGHT*0.5, DOWN*0.125,
            LEFT*0.5, UP*0.25, RIGHT*0.5, DOWN*0.25
        ])
        curve2.set_color(YELLOW)
        self.play(Create(curve2))
        self.wait(0.5)

        # Update label for iteration 3
        self.play(Transform(label1, MathTex("Iteration\\ 3: Length\\ 27", font_size=24)))
        self.wait(1)

        # Third iteration - dense curve
        self.play(FadeOut(curve2))
        curve3 = VMobject()
        curve3.set_points_as_corners([
            LEFT*0.5, UP*0.25, RIGHT*0.5, DOWN*0.25,
            LEFT*0.5, UP*0.125, RIGHT*0.5, DOWN*0.125,
            LEFT*0.5, UP*0.0625, RIGHT*0.5, DOWN*0.0625,
            LEFT*0.5, UP*0.25, RIGHT*0.5, DOWN*0.25
        ])
        curve3.set_color(YELLOW)
        self.play(Create(curve3))
        self.wait(1)

        # Final dense curve - highlight it
        final_curve = VMobject()
        final_curve.set_points_as_corners([
            LEFT*0.5, UP*0.25, RIGHT*0.5, DOWN*0.25,
            LEFT*0.5, UP*0.125, RIGHT*0.5, DOWN*0.125,
            LEFT*0.5, UP*0.0625, RIGHT*0.5, DOWN*0.0625,
            LEFT*0.5, UP*0.03125, RIGHT*0.5, DOWN*0.03125,
            LEFT*0.5, UP*0.25, RIGHT*0.5, DOWN*0.25
        ])
        final_curve.set_color(YELLOW)
        self.play(FadeOut(curve3))
        self.play(Create(final_curve))
        self.wait(1)

        # Final label showing infinity
        self.play(Transform(label1, MathTex("Length\\ \\rightarrow\\ \\infty", font_size=24)))
        self.wait(1.5)

        # Paradox text
        paradox = Text("Notice the paradox:", font_size=24)
        paradox.to_edge(DOWN)
        self.play(Write(paradox))
        self.wait(1)

        # Explanation
        explanation = Text("as the curve fills the square, its total length explodes to infinity", font_size=20)
        explanation.next_to(paradox, DOWN, buff=0.2)
        self.play(Write(explanation))
        self.wait(2)

        # Final text
        final_text = Text("We have an object of infinite length trapped within a finite boundary", font_size=20)
        final_text.next_to(explanation, DOWN, buff=0.2)
        self.play(Write(final_text))
        self.wait(2)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(box),
            FadeOut(final_curve),
            FadeOut(label1),
            FadeOut(paradox),
            FadeOut(explanation),
            FadeOut(final_text)
        )
        self.wait(0.5)
