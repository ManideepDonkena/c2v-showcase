from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Chained Operations Example", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial expression: 2 ⊕ 3
        expr1 = MathTex("2 \\oplus 3", font_size=40)
        self.play(Write(expr1))
        self.wait(1)

        # Step 1: Expand to 2 + 3
        expr2 = MathTex("2 + 3", font_size=40)
        expr2.next_to(expr1, RIGHT, buff=0.5)
        self.play(ReplacementTransform(expr1, expr2))
        self.wait(1)

        # Step 2: Add (2 × 3)
        expr3 = MathTex("+ (2 \\times 3)", font_size=40)
        expr3.next_to(expr2, RIGHT, buff=0.5)
        self.play(Write(expr3))
        self.wait(1)

        # Step 3: Resolve to 11
        expr4 = MathTex("= 11", font_size=40)
        expr4.next_to(expr3, RIGHT, buff=0.5)
        self.play(Write(expr4))
        self.wait(2)

        # Narration text
        narration = Text("Left to right", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1)
        self.play(FadeOut(narration))

        # Add explanation
        explanation = Text("This shows how chained operations are evaluated left to right.", font_size=24).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(explanation))

        # Fade out everything
        self.play(FadeOut(expr1), FadeOut(expr2), FadeOut(expr3), FadeOut(expr4), FadeOut(title))
        self.wait(0.5)
