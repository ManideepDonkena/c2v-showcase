from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Commutativity and Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Left scene: 0 ⊕ 7
        left_expr = MathTex("0 \\oplus 7").scale(1.5).to_corner(UL)
        self.play(Write(left_expr))
        self.wait(1)

        zero = always_redraw(lambda: Circle(color=BLUE, radius=0.3).set_fill(BLUE, opacity=0.5))
        seven = always_redraw(lambda: Circle(color=GREEN, radius=0.3).set_fill(GREEN, opacity=0.5))
        zero_label = MathTex("0").scale(0.7).move_to(zero.get_center())
        seven_label = MathTex("7").scale(0.7).move_to(seven.get_center())

        self.play(Create(zero), Create(seven), Write(zero_label), Write(seven_label))
        self.wait(1)

        # Show 0 fading away
        self.play(FadeOut(zero), FadeOut(zero_label))
        self.wait(0.5)

        result = MathTex("7").scale(1.5).move_to(left_expr.get_center())
        self.play(Transform(left_expr, result))
        self.wait(1.5)

        # Right scene: 7 ⊕ 0
        right_expr = MathTex("7 \\oplus 0").scale(1.5).to_corner(UR)
        self.play(Write(right_expr))
        self.wait(1)

        seven_c = always_redraw(lambda: Circle(color=GREEN, radius=0.3).set_fill(GREEN, opacity=0.5))
        zero_c = always_redraw(lambda: Circle(color=BLUE, radius=0.3).set_fill(BLUE, opacity=0.5))
        seven_label_r = MathTex("7").scale(0.7).move_to(seven_c.get_center())
        zero_label_r = MathTex("0").scale(0.7).move_to(zero_c.get_center())

        self.play(Create(seven_c), Create(zero_c), Write(seven_label_r), Write(zero_label_r))
        self.wait(1)

        # Show 0 fading away
        self.play(FadeOut(zero_c), FadeOut(zero_label_r))
        self.wait(0.5)

        result2 = MathTex("7").scale(1.5).move_to(right_expr.get_center())
        self.play(Transform(right_expr, result2))
        self.wait(1.5)

        # Commutativity text
        comm_text = Text("a ⊕ b = b ⊕ a", font_size=24).to_edge(DOWN)
        self.play(Write(comm_text))
        self.wait(2)

        # Chain example: 4, -1, 2
        self.play(FadeOut(left_expr), FadeOut(right_expr), FadeOut(comm_text))

        chain = VGroup(
            Circle(color=RED, radius=0.3).set_fill(RED, opacity=0.5),
            Circle(color=ORANGE, radius=0.3).set_fill(ORANGE, opacity=0.5),
            Circle(color=YELLOW, radius=0.3).set_fill(YELLOW, opacity=0.5)
        ).arrange(RIGHT, buff=0.2)

        labels = VGroup(
            MathTex("4").scale(0.7).move_to(chain[0].get_center()),
            MathTex("-1").scale(0.7).move_to(chain[1].get_center()),
            MathTex("2").scale(0.7).move_to(chain[2].get_center())
        )

        self.play(Create(chain), Write(labels))
        self.wait(1)

        # Merge first two
        merged_1 = Circle(color=PURPLE, radius=0.3).set_fill(PURPLE, opacity=0.5)
        merged_label_1 = MathTex("-1").scale(0.7).move_to(merged_1.get_center())
        self.play(TransformFromCopy(VGroup(chain[0], chain[1]), merged_1), Write(merged_label_1))
        self.wait(1)

        # Move to third
        final_circle = Circle(color=PURPLE, radius=0.3).set_fill(PURPLE, opacity=0.5)
        final_label = MathTex("-1").scale(0.7).move_to(final_circle.get_center())
        self.play(TransformFromCopy(VGroup(merged_1, chain[2]), final_circle), Write(final_label))
        self.wait(1)

        # Explanation
        explain_text = Text("Because -1 swallows everything it touches", font_size=24).to_edge(DOWN)
        self.play(Write(explain_text))
        self.wait(2)

        # Formula expansion
        self.play(FadeOut(chain), FadeOut(labels), FadeOut(merged_1), FadeOut(merged_label_1),
                  FadeOut(final_circle), FadeOut(final_label), FadeOut(explain_text))

        formula = MathTex("(-1) + 5 + ((-1) \\times 5)").scale(1.2).to_edge(UP)
        self.play(Write(formula))
        self.wait(1)

        step1 = MathTex("= -1 + 5 + (-5)").scale(1.2).next_to(formula, DOWN, buff=0.3)
        self.play(Write(step1))
        self.wait(1)

        step2 = MathTex("= -1 + (5 - 5)").scale(1.2).next_to(step1, DOWN, buff=0.3)
        self.play(Write(step2))
        self.wait(1)

        step3 = MathTex("= -1").scale(1.2).next_to(step2, DOWN, buff=0.3)
        self.play(Write(step3))
        self.wait(1.5)

        # Parentheses example
        self.play(FadeOut(formula), FadeOut(step1), FadeOut(step2), FadeOut(step3))

        paren_expr = MathTex("a \\oplus (b \\oplus c)").scale(1.2).to_edge(UP)
        self.play(Write(paren_expr))
        self.wait(1)

        # Highlight inner parentheses
        highlight = SurroundingRectangle(paren_expr[3:6], color=YELLOW, buff=0.1)
        self.play(Create(highlight))
        self.wait(1)

        # Explanation
        paren_text = Text("Solve inside first", font_size=24).to_edge(DOWN)
        self.play(Write(paren_text))
        self.wait(2)

        self.play(FadeOut(paren_expr), FadeOut(highlight), FadeOut(paren_text))
        self.wait(0.5)

        # Final summary
        final_title = Text("Summary", font_size=36).to_edge(UP)
        self.play(Write(final_title))
        self.wait(0.5)

        rules = VGroup(
            Text("1. Commutativity: a ⊕ b = b ⊕ a", font_size=24),
            Text("2. Neutral element: 0 ⊕ b = b", font_size=24),
            Text("3. Absorbing element: (-1) ⊕ b = -1", font_size=24),
            Text("4. Chain left to right", font_size=24)
        ).arrange(DOWN, buff=0.3).scale(0.8).to_edge(LEFT)

        self.play(Write(rules))
        self.wait(2)

        self.play(FadeOut(final_title), FadeOut(rules))
        self.wait(0.5)
