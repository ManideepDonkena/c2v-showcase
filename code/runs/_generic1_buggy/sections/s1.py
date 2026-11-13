from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Pythagoras Theorem: Visual Proof", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Large right triangle
        triangle = Triangle().scale(2)
        triangle.shift(DOWN * 0.5)
        a_leg = triangle.get_side_length(0)
        b_leg = triangle.get_side_length(1)
        hypotenuse = triangle.get_side_length(2)

        # Labels for legs
        label_a = MathTex("a", font_size=30).next_to(triangle.get_vertices()[0], DOWN, buff=0.2)
        label_b = MathTex("b", font_size=30).next_to(triangle.get_vertices()[1], LEFT, buff=0.2)

        # Label for hypotenuse
        label_c = MathTex("c", font_size=30).next_to(triangle.get_vertices()[2], UP, buff=0.2)

        # Right angle marker
        right_angle = Square(side_length=0.3, color=WHITE).rotate(45 * DEGREES)
        right_angle.move_to(triangle.get_vertices()[0])

        # Initial triangle and labels
        self.play(Create(triangle))
        self.wait(0.5)
        self.play(Write(label_a), Write(label_b))
        self.wait(1)
        self.play(Write(label_c))
        self.wait(1)

        # Animate right angle marker
        self.play(FadeIn(right_angle))
        self.wait(1.5)

        # Narration text
        narration = Text("Every right-angled triangle has a special relationship between its three sides.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)

        # Clear narration and explain legs vs hypotenuse
        self.play(FadeOut(narration))
        self.wait(0.5)

        explanation = Text("The two shorter sides touching the right angle are called legs.", font_size=24)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)

        self.play(FadeOut(explanation))
        self.wait(0.5)

        explanation2 = Text("The longest side opposite the right angle is known as the hypotenuse.", font_size=24)
        explanation2.to_edge(DOWN)
        self.play(Write(explanation2))
        self.wait(2)

        self.play(FadeOut(explanation2))
        self.wait(0.5)

        # Final wait
        self.wait(1)
