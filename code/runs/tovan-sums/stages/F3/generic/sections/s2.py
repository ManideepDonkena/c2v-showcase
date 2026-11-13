from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Commutativity and Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Left scene: 0 ⊕ 7 → 7
        left_expr = MathTex("0 \\oplus 7", font_size=40)
        left_expr.shift(2 * LEFT + UP)
        self.play(Write(left_expr))
        self.wait(1)

        zero_fade = left_expr[0].copy()
        self.play(FadeOut(zero_fade), run_time=0.5)
        self.wait(0.5)

        result_left = MathTex("= 7", font_size=40).next_to(left_expr, RIGHT)
        self.play(Write(result_left))
        self.wait(1.5)

        # Right scene: 7 ⊕ 0 → 7
        right_expr = MathTex("7 \\oplus 0", font_size=40)
        right_expr.shift(2 * RIGHT + UP)
        self.play(Write(right_expr))
        self.wait(1)

        if len(right_expr) > 2:
            zero_fade_right = right_expr[2].copy()
            self.play(FadeOut(zero_fade_right), run_time=0.5)
        self.wait(0.5)

        result_right = MathTex("= 7", font_size=40).next_to(right_expr, RIGHT)
        self.play(Write(result_right))
        self.wait(1.5)

        # Show commutativity
        commutative_text = Text("a ⊕ b = b ⊕ a", font_size=24).to_edge(DOWN)
        self.play(Write(commutative_text))
        self.wait(1.5)

        # Show identity property
        identity_text = Text("0 is neutral: 0 ⊕ b = b", font_size=24).next_to(commutative_text, DOWN)
        self.play(Write(identity_text))
        self.wait(2)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(left_expr),
            FadeOut(result_left),
            FadeOut(right_expr),
            FadeOut(result_right),
            FadeOut(commutative_text),
            FadeOut(identity_text)
        )
        self.wait(0.5)
