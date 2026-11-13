from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Peano Curve Construction", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial line
        initial_line = Line(LEFT * 3, RIGHT * 3, color=WHITE)
        self.play(Create(initial_line))
        self.wait(1)

        # First iteration: U shape
        u_shape = VGroup(
            Line(LEFT * 3, UP * 1.5, color=WHITE),
            Line(UP * 1.5, RIGHT * 3, color=WHITE),
            Line(RIGHT * 3, UP * 1.5, color=WHITE),
            Line(UP * 1.5, LEFT * 3, color=WHITE)
        )
        self.play(Transform(initial_line, u_shape))
        self.wait(1)

        # Second iteration
        u_shape2 = VGroup(
            Line(LEFT * 3, UP * 0.75, color=WHITE),
            Line(UP * 0.75, LEFT * 1.5, color=WHITE),
            Line(LEFT * 1.5, UP * 0.75, color=WHITE),
            Line(UP * 0.75, RIGHT * 1.5, color=WHITE),
            Line(RIGHT * 1.5, UP * 0.75, color=WHITE),
            Line(UP * 0.75, RIGHT * 3, color=WHITE),
            Line(RIGHT * 3, UP * 0.75, color=WHITE),
            Line(UP * 0.75, LEFT * 3, color=WHITE)
        )
        self.play(Transform(initial_line, u_shape2))
        self.wait(1)

        # Third iteration
        u_shape3 = VGroup(
            Line(LEFT * 3, UP * 0.375, color=WHITE),
            Line(UP * 0.375, LEFT * 2.25, color=WHITE),
            Line(LEFT * 2.25, UP * 0.375, color=WHITE),
            Line(UP * 0.375, LEFT * 1.5, color=WHITE),
            Line(LEFT * 1.5, UP * 0.375, color=WHITE),
            Line(UP * 0.375, RIGHT * 1.5, color=WHITE),
            Line(RIGHT * 1.5, UP * 0.375, color=WHITE),
            Line(UP * 0.375, RIGHT * 2.25, color=WHITE),
            Line(RIGHT * 2.25, UP * 0.375, color=WHITE),
            Line(UP * 0.375, RIGHT * 3, color=WHITE),
            Line(RIGHT * 3, UP * 0.375, color=WHITE),
            Line(UP * 0.375, LEFT * 3, color=WHITE)
        )
        self.play(Transform(initial_line, u_shape3))
        self.wait(1)

        # Key words
        words = Text("Infinite recursion", font_size=24).to_edge(DOWN)
        self.play(Write(words))
        self.wait(1.5)
        self.play(FadeOut(words))

        words2 = Text("Dense coverage", font_size=24).to_edge(DOWN)
        self.play(Write(words2))
        self.wait(1.5)
        self.play(FadeOut(words2))

        # Final fade
        self.play(FadeOut(initial_line), FadeOut(title))
        self.wait(0.5)
