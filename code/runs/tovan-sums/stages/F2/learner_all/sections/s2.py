from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Commutativity and Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Left scene: 0 ⊕ b -> b
        left_eq = MathTex("0 \\oplus b", font_size=40).to_corner(UL)
        self.play(Write(left_eq))
        self.wait(1)

        expand = MathTex("= 0 + b + (0 \\times b)", font_size=40).next_to(left_eq, DOWN, buff=0.5)
        expand.shift(0.71 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(expand))
        self.wait(1.5)

        step1 = MathTex("= 0 + b + 0", font_size=40).next_to(expand, DOWN, buff=0.5)
        self.play(Write(step1))
        self.wait(1.5)

        step2 = MathTex("= b", font_size=40).next_to(step1, DOWN, buff=0.5)
        self.play(Write(step2))
        self.wait(1.5)

        # Fade out left side
        self.play(FadeOut(VGroup(left_eq, expand, step1, step2)))

        # Right scene: 0 ⊕ b -> b (visual demonstration)
        right_eq = MathTex("0 \\oplus b", font_size=40).to_corner(UR)
        self.play(Write(right_eq))
        self.wait(1)

        zero_fade = right_eq[0][0].animate.set_fill(GRAY, opacity=0.5)
        self.play(zero_fade)
        self.wait(0.5)

        final = MathTex("= b", font_size=40).next_to(right_eq, DOWN, buff=0.5)
        self.play(Write(final))
        self.wait(1.5)

        # Fade out right side
        self.play(FadeOut(VGroup(right_eq, final)))

        # Show commutativity: a ⊕ b = b ⊕ a
        commutative = Text("Commutativity", font_size=24).to_edge(UP)
        self.play(Transform(title, commutative))
        self.wait(0.5)

        a_b = MathTex("a \\oplus b", font_size=40).to_corner(UL)
        b_a = MathTex("b \\oplus a", font_size=40).to_corner(UR)
        self.play(Write(a_b), Write(b_a))
        self.wait(1)

        eq_sign = MathTex("=", font_size=40).next_to(a_b, DOWN, buff=0.5)
        self.play(Write(eq_sign))
        self.wait(1)

        result_a_b = MathTex("a + b + ab", font_size=40).next_to(eq_sign, DOWN, buff=0.5)
        result_b_a = MathTex("b + a + ba", font_size=40).next_to(result_a_b, DOWN, buff=0.5)
        self.play(Write(result_a_b), Write(result_b_a))
        self.wait(1.5)

        self.play(FadeOut(VGroup(a_b, b_a, eq_sign, result_a_b, result_b_a)))

        # Associativity: nested structure
        assoc = Text("Associativity", font_size=24).to_edge(UP)
        self.play(Transform(title, assoc))
        self.wait(0.5)

        nested = MathTex("a \\oplus (b \\oplus c)", font_size=40).to_corner(UL)
        self.play(Write(nested))
        self.wait(1)

        highlight = SurroundingRectangle(nested[0][5:9], color=YELLOW, buff=0.1)
        highlight.shift(0.53 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(highlight))
        self.wait(1.5)

        inner = MathTex("b \\oplus c = b + c + bc", font_size=40).next_to(nested, DOWN, buff=0.5)
        inner.shift(0.29 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(inner))
        self.wait(1.5)

        example = MathTex("3 \\oplus 4 = 3 + 4 + 12 = 19", font_size=36).next_to(inner, DOWN, buff=0.5)
        self.play(Write(example))
        self.wait(1.5)

        outer = MathTex("2 \\oplus 19 = 2 + 19 + 38 = 60", font_size=36).next_to(example, DOWN, buff=0.5)
        self.play(Write(outer))
        self.wait(1.5)

        self.play(FadeOut(VGroup(nested, highlight, inner, example, outer)))

        # Compare with standard multiplication
        compare = Text("Tovan Sum vs Multiplication", font_size=24).to_edge(UP)
        self.play(Transform(title, compare))
        self.wait(0.5)

        two_three = MathTex("2 \\oplus 3 = 11", font_size=40).to_corner(UL)
        mult = MathTex("2 \\times 3 = 6", font_size=40).to_corner(UR)
        self.play(Write(two_three), Write(mult))
        self.wait(2)

        self.play(FadeOut(VGroup(two_three, mult)))

        # Demonstrate -1 swallows everything
        swallow = Text("The Swallowing Power of -1", font_size=24).to_edge(UP)
        self.play(Transform(title, swallow))
        self.wait(0.5)

        chain = VGroup(
            Circle().scale(0.3).set_fill(BLUE, opacity=0.5),
            Circle().scale(0.3).set_fill(BLUE, opacity=0.5),
            Circle().scale(0.3).set_fill(BLUE, opacity=0.5)
        ).arrange(RIGHT, buff=0.5).to_corner(UL)

        labels = [Text("4", font_size=24), Text("-1", font_size=24), Text("2", font_size=24)]
        for i, (c, l) in enumerate(zip(chain, labels)):
            l.next_to(c, DOWN)
            self.play(Create(c), Write(l))
            self.wait(0.5)

        # Evaluate 4 ⊕ -1
        step1 = MathTex("4 \\oplus (-1) = 4 + (-1) + (4)(-1) = 3 - 4 = -1", font_size=36).to_corner(DL)
        self.play(Write(step1))
        self.wait(2)

        # Now -1 ⊕ 2
        step2 = MathTex("(-1) \\oplus 2 = (-1) + 2 + (-1)(2) = 1 - 2 = -1", font_size=36).next_to(step1, DOWN, buff=0.5)
        self.play(Write(step2))
        self.wait(2)

        # Final result
        final_result = Text("All results are -1", font_size=36).to_corner(DR)
        self.play(Write(final_result))
        self.wait(2)

        self.play(FadeOut(VGroup(chain, *labels, step1, step2, final_result)))

        # End
        self.play(FadeOut(title))
        self.wait(0.5)
