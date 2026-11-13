from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Chained Operations Example", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First example: 2 ⊕ 3
        eq1 = MathTex("2 \\oplus 3").scale(1.5)
        self.play(Write(eq1))
        self.wait(1)

        # Step 1: 2 + 3
        step1 = MathTex("2 + 3").scale(1.5).next_to(eq1, DOWN, buff=0.5)
        self.play(ReplacementTransform(eq1.copy(), step1))
        self.wait(1)

        # Step 2: add (2 × 3)
        step2 = MathTex("2 + 3 + (2 \\times 3)").scale(1.5).next_to(step1, DOWN, buff=0.5)
        self.play(ReplacementTransform(step1, step2))
        self.wait(1)

        # Step 3: resolve to 11
        step3 = MathTex("= 11").scale(1.5).next_to(step2, DOWN, buff=0.5)
        self.play(ReplacementTransform(step2, step3))
        self.wait(1.5)

        # Show 0 ⊕ b
        self.play(FadeOut(step3))
        eq2 = MathTex("0 \\oplus b").scale(1.5).to_edge(UP)
        self.play(Write(eq2))
        self.wait(0.5)

        step4 = MathTex("0 + b + (0 \\times b)").scale(1.5).next_to(eq2, DOWN, buff=0.5)
        self.play(Write(step4))
        self.wait(1)

        step5 = MathTex("= b + 0 = b").scale(1.5).next_to(step4, DOWN, buff=0.5)
        self.play(ReplacementTransform(step4, step5))
        self.wait(1.5)

        # Show nested: a ⊕ (b ⊕ c)
        self.play(FadeOut(eq2, step5))
        eq3 = MathTex("a \\oplus (b \\oplus c)").scale(1.5).to_edge(UP)
        self.play(Write(eq3))
        self.wait(0.5)

        # Highlight inner parentheses
        inner = SurroundingRectangle(MathTex("b \\oplus c"), color=YELLOW, buff=0.1)
        self.play(Create(inner))
        self.wait(1)

        # Compute b ⊕ c first (e.g., 3 ⊕ 4)
        step6 = MathTex("3 \\oplus 4 = 3 + 4 + 12 = 19").scale(1.5).next_to(eq3, DOWN, buff=0.5)
        self.play(Write(step6))
        self.wait(1)

        # Now compute a ⊕ (result)
        step7 = MathTex("2 \\oplus 19 = 2 + 19 + 38 = 60").scale(1.5).next_to(step6, DOWN, buff=0.5)
        self.play(ReplacementTransform(step6, step7))
        self.wait(1.5)

        # Compare with standard multiplication
        self.play(FadeOut(eq3, step7, inner))
        comp = MathTex("2 \\oplus 3 = 11 \\quad 2 \\times 3 = 6").scale(1.5).to_edge(UP)
        self.play(Write(comp))
        self.wait(1.5)

        # Show chain with -1
        self.play(FadeOut(comp))
        chain = VGroup(
            Circle().scale(0.4).set_color(BLUE),
            Text("4", font_size=24).move_to(Circle().scale(0.4).get_center()),
            Circle().scale(0.4).set_color(BLUE),
            Text("-1", font_size=24).move_to(Circle().scale(0.4).get_center()),
            Circle().scale(0.4).set_color(BLUE),
            Text("2", font_size=24).move_to(Circle().scale(0.4).get_center())
        ).arrange(RIGHT, buff=0.5).to_edge(DOWN)
        self.play(Create(chain))
        self.wait(1)

        # Show 4 ⊕ -1 = -1
        step8 = MathTex("4 \\oplus (-1) = 4 + (-1) + (4 \\times -1) = 3 - 4 = -1").scale(1.2).next_to(chain, UP, buff=0.5)
        self.play(Write(step8))
        self.wait(1.5)

        # Show -1 ⊕ 2 = -1
        step9 = MathTex("(-1) \\oplus 2 = -1 + 2 + (-1 \\times 2) = 1 - 2 = -1").scale(1.2).next_to(step8, DOWN, buff=0.5)
        self.play(ReplacementTransform(step8, step9))
        self.wait(1.5)

        # Final statement
        final = Text("The -1 element swallows everything after it.", font_size=24).to_edge(DOWN)
        self.play(Write(final))
        self.wait(1.5)

        self.play(FadeOut(title, chain, step9, final))
