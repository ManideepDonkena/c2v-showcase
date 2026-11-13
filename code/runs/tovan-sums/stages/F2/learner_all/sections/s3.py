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

        self.play(neg_one.animate.move_to([-3, 0, 0]), b_circle.animate.move_to([3, 0, 0]))
        self.wait(1)
        self.play(b_circle.animate.scale(0.001), FadeOut(b_label))
        self.wait(0.5)

        result_text = MathTex(r"\text{Result} = -1", font_size=32).next_to(neg_one, DOWN)
        self.play(Write(result_text))
        self.wait(1.5)

        # Part 2: 0 ⊕ b = b
        self.play(FadeOut(title), FadeOut(result_text))
        zero = Circle(radius=1, color=YELLOW, fill_color=YELLOW, fill_opacity=0.8)
        zero_label = MathTex(r"0", font_size=40).move_to(zero.get_center())
        b2 = Circle(radius=1, color=BLUE, fill_color=BLUE, fill_opacity=0.8)
        b2_label = MathTex(r"b", font_size=40).move_to(b2.get_center())

        zero_label.shift(0.0 * RIGHT + 0.43 * UP)  # layout: separation vector
        self.play(Create(zero), Write(zero_label))
        self.wait(0.5)
        self.play(Create(b2), Write(b2_label))
        self.wait(0.5)

        eq1 = MathTex(r"0 \oplus b =", font_size=32).next_to(zero, DOWN)
        eq2 = MathTex(r"0 + b + (0 \times b) =", font_size=32).next_to(eq1, DOWN)
        eq3 = MathTex(r"b", font_size=32).next_to(eq2, RIGHT)

        self.play(Write(eq1))
        self.wait(0.5)
        self.play(Write(eq2))
        self.wait(1)
        self.play(Write(eq3))
        self.wait(1.5)

        # Part 3: Nested structure
        self.play(FadeOut(zero), FadeOut(b2), FadeOut(zero_label), FadeOut(b2_label),
                  FadeOut(eq1), FadeOut(eq2), FadeOut(eq3))

        a = Circle(radius=0.7, color=GREEN, fill_color=GREEN, fill_opacity=0.8)
        a_label = MathTex(r"a", font_size=32).move_to(a.get_center())
        b3 = Circle(radius=0.7, color=BLUE, fill_color=BLUE, fill_opacity=0.8)
        b3_label = MathTex(r"b", font_size=32).move_to(b3.get_center())
        c = Circle(radius=0.7, color=PURPLE, fill_color=PURPLE, fill_opacity=0.8)
        c_label = MathTex(r"c", font_size=32).move_to(c.get_center())

        self.play(Create(a), Write(a_label))
        self.wait(0.5)
        self.play(Create(b3), Write(b3_label))
        self.wait(0.5)
        self.play(Create(c), Write(c_label))
        self.wait(0.5)

        expr = MathTex(r"a \oplus (b \oplus c)", font_size=32).to_edge(UP)
        self.play(Write(expr))
        self.wait(1)

        # Highlight inner parentheses
        self.play(a.animate.shift(LEFT * 2), b3.animate.shift(LEFT * 0.5), c.animate.shift(RIGHT * 0.5))
        self.wait(1)

        # Show intermediate result
        step1 = MathTex(r"b \oplus c =", font_size=24).to_edge(DOWN)
        step2 = MathTex(r"3 \oplus 4 = 19", font_size=24).next_to(step1, RIGHT)
        self.play(Write(step1))
        self.wait(0.5)
        self.play(Write(step2))
        self.wait(1)

        # Show outer operation
        step3 = MathTex(r"a \oplus 19 =", font_size=24).next_to(step1, DOWN)
        step4 = MathTex(r"2 \oplus 19 = 2 + 19 + 38 = 60", font_size=24).next_to(step3, RIGHT)
        self.play(Write(step3))
        self.wait(0.5)
        self.play(Write(step4))
        self.wait(1.5)

        # Part 4: Comparison with standard multiplication
        self.play(FadeOut(expr), FadeOut(step1), FadeOut(step2), FadeOut(step3), FadeOut(step4),
                  a.animate.shift(RIGHT * 2), b3.animate.shift(RIGHT * 0.5), c.animate.shift(LEFT * 0.5))

        two = Circle(radius=0.7, color=GREEN, fill_color=GREEN, fill_opacity=0.8)
        two_label = MathTex(r"2", font_size=32).move_to(two.get_center())
        three = Circle(radius=0.7, color=BLUE, fill_color=BLUE, fill_opacity=0.8)
        three_label = MathTex(r"3", font_size=32).move_to(three.get_center())

        self.play(Create(two), Write(two_label))
        self.wait(0.5)
        self.play(Create(three), Write(three_label))
        self.wait(0.5)

        eq_tovan = MathTex(r"2 \oplus 3 =", font_size=32).to_edge(UP)
        result_tovan = MathTex(r"11", font_size=32).next_to(eq_tovan, RIGHT)
        eq_mult = MathTex(r"2 \times 3 =", font_size=32).next_to(eq_tovan, DOWN)
        result_mult = MathTex(r"6", font_size=32).next_to(eq_mult, RIGHT)

        self.play(Write(eq_tovan))
        self.wait(0.5)
        self.play(Write(result_tovan))
        self.wait(1)
        self.play(Write(eq_mult))
        self.wait(0.5)
        self.play(Write(result_mult))
        self.wait(1.5)

        # Part 5: Chain absorption
        self.play(FadeOut(eq_tovan), FadeOut(result_tovan), FadeOut(eq_mult), FadeOut(result_mult),
                  two.animate.shift(LEFT * 2), three.animate.shift(RIGHT * 2))

        four = Circle(radius=0.7, color=GREEN, fill_color=GREEN, fill_opacity=0.8)
        four_label = MathTex(r"4", font_size=32).move_to(four.get_center())
        neg_one2 = Circle(radius=0.7, color=RED, fill_color=RED, fill_opacity=0.8)
        neg_one2_label = MathTex(r"-1", font_size=32).move_to(neg_one2.get_center())
        two2 = Circle(radius=0.7, color=BLUE, fill_color=BLUE, fill_opacity=0.8)
        two2_label = MathTex(r"2", font_size=32).move_to(two2.get_center())

        self.play(Create(four), Write(four_label))
        self.wait(0.5)
        self.play(Create(neg_one2), Write(neg_one2_label))
        self.wait(0.5)
        self.play(Create(two2), Write(two2_label))
        self.wait(0.5)

        chain = MathTex(r"(4 \oplus -1) \oplus 2", font_size=32).to_edge(UP)
        self.play(Write(chain))
        self.wait(1)

        # First step
        step_a = MathTex(r"4 \oplus -1 =", font_size=24).to_edge(DOWN)
        step_b = MathTex(r"-1", font_size=24).next_to(step_a, RIGHT)
        self.play(Write(step_a))
        self.wait(0.5)
        self.play(Write(step_b))
        self.wait(1)

        # Second step
        step_c = MathTex(r"(-1) \oplus 2 =", font_size=24).next_to(step_a, DOWN)
        step_d = MathTex(r"-1", font_size=24).next_to(step_c, RIGHT)
        self.play(Write(step_c))
        self.wait(0.5)
        self.play(Write(step_d))
        self.wait(1.5)

        # Final message
        final_msg = Text("The absorbing power of -1 is contagious!", font_size=24).to_edge(DOWN)
        self.play(Write(final_msg))
        self.wait(1.5)

        self.play(FadeOut(chain), FadeOut(step_a), FadeOut(step_b), FadeOut(step_c), FadeOut(step_d),
                  FadeOut(final_msg), FadeOut(four), FadeOut(neg_one2), FadeOut(two2),
                  FadeOut(four_label), FadeOut(neg_one2_label), FadeOut(two2_label))
