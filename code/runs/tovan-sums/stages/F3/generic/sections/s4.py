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
        self.play(Transform(expr1, expr2))
        self.wait(1)

        # Step 2: Add (2 × 3)
        expr3 = MathTex("2 + 3 + (2 \\times 3)", font_size=40)
        expr3.next_to(expr1, RIGHT, buff=0.5)
        self.play(Transform(expr1, expr3))
        self.wait(1)

        # Step 3: Resolve to 11
        expr4 = MathTex("= 11", font_size=40)
        expr4.next_to(expr1, RIGHT, buff=0.5)
        self.play(Transform(expr1, expr4))
        self.wait(1.5)

        # Narration text
        narration = Text("When chaining operations, we always work from left to right.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)

        self.play(FadeOut(narration))

        # Clarify the definition
        clarify = Text("Definition: a ⊕ b = a + b + a×b", font_size=24)
        clarify.to_edge(DOWN)
        self.play(Write(clarify))
        self.wait(2)

        self.play(FadeOut(clarify))

        # Show rules
        rule1 = Text("1. Order does not matter: a ⊕ b = b ⊕ a", font_size=24)
        rule2 = Text("2. 0 is neutral: 0 ⊕ b = b", font_size=24)
        rule3 = Text("3. -1 swallows everything: (-1) ⊕ b = -1", font_size=24)
        rule4 = Text("4. Chain is worked left to right", font_size=24)

        rules = VGroup(rule1, rule2, rule3, rule4).arrange(DOWN, buff=0.3).to_edge(LEFT)
        self.play(Write(rules))
        self.wait(3)

        self.play(FadeOut(rules))
        self.play(FadeOut(title), FadeOut(expr1))
