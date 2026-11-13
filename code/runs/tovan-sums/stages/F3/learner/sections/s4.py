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
        expr3 = MathTex("+ (2 \\times 3)", font_size=40)
        expr3.next_to(expr2, RIGHT, buff=0.5)
        self.play(Write(expr3))
        self.wait(1)

        # Step 3: Resolve to 11
        expr4 = MathTex("= 11", font_size=40)
        expr4.next_to(expr3, RIGHT, buff=0.5)
        self.play(Write(expr4))
        self.wait(1.5)

        # Fade out the chain
        self.play(FadeOut(VGroup(expr1, expr2, expr3, expr4)))

        # Show nested structure: a ⊕ (b ⊕ c)
        nested = MathTex("a \\oplus (b \\oplus c)", font_size=40).to_edge(UP)
        nested.shift(0.0 * RIGHT + -0.65 * UP)  # layout: separation vector
        self.play(Write(nested))
        self.wait(1)

        # Highlight inner group (b ⊕ c)
        inner_group = SurroundingRectangle(MathTex("b \\oplus c", font_size=40), color=YELLOW, buff=0.2)
        self.play(Create(inner_group))
        self.wait(1.5)

        # Say the rule
        rule_text = Text("When parentheses exist, you must solve the inside group before applying the outside operation, just like standard order of operations.", font_size=24)
        rule_text.to_edge(DOWN)
        self.play(Write(rule_text))
        self.wait(3)

        # Fade out everything
        self.play(FadeOut(VGroup(nested, inner_group, rule_text)))
        self.wait(0.5)
