from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Absorbing Element (-1)", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Part 1: -1 absorbs everything
        neg_one = Circle(radius=1, color=RED, fill_color=RED, fill_opacity=0.8)
        neg_one_label = MathTex(r"-1", font_size=40).move_to(neg_one.get_center())
        b_circle = Circle(radius=1, color=BLUE, fill_color=BLUE, fill_opacity=0.8)
        b_label = MathTex(r"b", font_size=40).move_to(b_circle.get_center())

        self.play(Create(neg_one), Write(neg_one_label))
        self.wait(0.5)
        b_label.shift(0.0 * RIGHT + 0.43 * UP)  # layout: separation vector
        self.play(Create(b_circle), Write(b_label))
        self.wait(0.5)

        self.play(neg_one.animate.shift(RIGHT * 2), b_circle.animate.shift(LEFT * 2))
        self.wait(0.5)

        # Show absorption
        self.play(FadeOut(b_circle), FadeOut(b_label))
        result = MathTex(r"-1", font_size=40).move_to(neg_one.get_center())
        self.play(Write(result))
        self.wait(1)

        # Narration text
        narration1 = Text("The number negative one acts as an absorbing element.", font_size=24)
        narration1.to_edge(DOWN)
        self.play(Write(narration1))
        self.wait(2)
        self.play(FadeOut(narration1))

        # Part 2: 0 ⊕ b = b
        eq1 = MathTex(r"0 \oplus b", font_size=36)
        eq2 = MathTex(r"= 0 + b + (0 \times b)", font_size=36)
        eq3 = MathTex(r"= 0 + b + 0", font_size=36)
        eq4 = MathTex(r"= b", font_size=36)

        eq1.to_edge(UP, buff=0.5)
        eq1.shift(0.0 * RIGHT + 0.44 * UP)  # layout: separation vector
        self.play(Write(eq1))
        self.wait(0.5)
        self.play(Transform(eq1, eq2))
        self.wait(0.5)
        self.play(Transform(eq1, eq3))
        self.wait(0.5)
        self.play(Transform(eq1, eq4))
        self.wait(1)

        narration2 = Text("Adding zero contributes nothing to the sum or product, so the original number b remains exactly as it was.", font_size=24)
        narration2.to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(2)
        self.play(FadeOut(narration2), FadeOut(eq1))

        # Part 3: Nested structure
        nested = MathTex(r"a \oplus (b \oplus c)", font_size=36)
        nested.to_edge(UP, buff=0.5)
        self.play(Write(nested))
        self.wait(1)

        narration3 = Text("When you see parentheses, solve the inside part first.", font_size=24)
        narration3.to_edge(DOWN)
        self.play(Write(narration3))
        self.wait(2)
        self.play(FadeOut(narration3))

        # Show calculation: 3 ⊕ 4 = 19
        calc1 = MathTex(r"3 \oplus 4", font_size=36)
        calc2 = MathTex(r"= 3 + 4 + (3 \times 4)", font_size=36)
        calc3 = MathTex(r"= 3 + 4 + 12", font_size=36)
        calc4 = MathTex(r"= 19", font_size=36)

        calc1.to_edge(UP, buff=0.5)
        self.play(Transform(nested, calc1))
        self.wait(0.5)
        self.play(Transform(calc1, calc2))
        self.wait(0.5)
        self.play(Transform(calc1, calc3))
        self.wait(0.5)
        self.play(Transform(calc1, calc4))
        self.wait(1)

        # Next step: 2 ⊕ 19
        next_step = MathTex(r"2 \oplus 19", font_size=36)
        next_step.next_to(calc1, DOWN, buff=0.5)
        self.play(Write(next_step))
        self.wait(1)

        # Part 4: Comparison with standard multiplication
        comp1 = MathTex(r"2 \oplus 3 = 11", font_size=36)
        comp2 = MathTex(r"2 \times 3 = 6", font_size=36)
        comp1.to_edge(UP, buff=0.5)
        comp2.next_to(comp1, DOWN, buff=0.5)

        self.play(Transform(calc1, comp1), Write(comp2))
        self.wait(1.5)
        self.play(FadeOut(comp1), FadeOut(comp2))

        # Part 5: Chain with -1 absorbing
        chain = VGroup(
            Circle(radius=0.5, color=GREEN).move_to(LEFT * 2),
            Circle(radius=0.5, color=RED).move_to(ORIGIN),
            Circle(radius=0.5, color=BLUE).move_to(RIGHT * 2)
        )
        chain_labels = VGroup(
            MathTex(r"4", font_size=24).move_to(chain[0].get_center()),
            MathTex(r"-1", font_size=24).move_to(chain[1].get_center()),
            MathTex(r"2", font_size=24).move_to(chain[2].get_center())
        )
        self.play(Create(chain), Write(chain_labels))
        self.wait(1)

        # Show (4 ⊕ -1) = -1
        step1 = MathTex(r"(4 \oplus -1)", font_size=36)
        step1.to_edge(UP, buff=0.5)
        self.play(Write(step1))
        self.wait(0.5)

        result1 = MathTex(r"= 4 + (-1) + (4 \times -1)", font_size=36)
        result1.next_to(step1, DOWN, buff=0.5)
        self.play(Write(result1))
        self.wait(0.5)

        result2 = MathTex(r"= 4 - 1 - 4", font_size=36)
        result2.next_to(result1, DOWN, buff=0.5)
        self.play(Transform(result1, result2))
        self.wait(0.5)

        final_result = MathTex(r"= -1", font_size=36)
        final_result.next_to(result2, DOWN, buff=0.5)
        self.play(Write(final_result))
        self.wait(1)

        # Show (-1 ⊕ 2) = -1
        step2 = MathTex(r"(-1 \oplus 2)", font_size=36)
        step2.to_edge(UP, buff=0.5)
        self.play(Transform(step1, step2))
        self.wait(0.5)

        result3 = MathTex(r"= -1 + 2 + (-1 \times 2)", font_size=36)
        result3.next_to(step1, DOWN, buff=0.5)
        self.play(Write(result3))
        self.wait(0.5)

        result4 = MathTex(r"= -1 + 2 - 2", font_size=36)
        result4.next_to(result3, DOWN, buff=0.5)
        self.play(Transform(result3, result4))
        self.wait(0.5)

        final_result2 = MathTex(r"= -1", font_size=36)
        final_result2.next_to(result4, DOWN, buff=0.5)
        self.play(Write(final_result2))
        self.wait(1.5)

        # Final narration
        final_narration = Text("The absorbing power of -1 is contagious.", font_size=24)
        final_narration.to_edge(DOWN)
        self.play(Write(final_narration))
        self.wait(2)
        self.play(FadeOut(final_narration))

        # Cleanup
        self.play(FadeOut(title), FadeOut(chain), FadeOut(chain_labels), FadeOut(step1), FadeOut(result1), FadeOut(result3), FadeOut(final_result), FadeOut(final_result2))
