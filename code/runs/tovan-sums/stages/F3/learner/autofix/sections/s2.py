from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Commutativity and Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Left scene: 0 ⊕ 7
        left_expr = MathTex("0 \\oplus 7", font_size=40)
        left_expr.shift(2 * LEFT + 1.5 * UP)
        self.play(Write(left_expr))
        self.wait(1)

        zero_fade = left_expr[0][0]
        self.play(FadeOut(zero_fade))
        self.wait(0.5)

        left_result = MathTex("= 7", font_size=40).next_to(left_expr, RIGHT)
        self.play(Write(left_result))
        self.wait(1.5)

        # Right scene: 7 ⊕ 0
        right_expr = MathTex("7 \\oplus 0", font_size=40)
        right_expr.shift(2 * RIGHT + 1.5 * UP)
        self.play(Write(right_expr))
        self.wait(1)

        # Check if the index exists before accessing
        if len(right_expr[0]) > 3:
            zero_fade_right = right_expr[0][3]
            self.play(FadeOut(zero_fade_right))
            self.wait(0.5)
        else:
            self.wait(0.5)

        right_result = MathTex("= 7", font_size=40).next_to(right_expr, RIGHT)
        self.play(Write(right_result))
        self.wait(1.5)

        # Commutativity
        commutative_text = Text("a ⊕ b = b ⊕ a", font_size=24).to_edge(DOWN)
        self.play(Write(commutative_text))
        self.wait(1.5)

        # Fade out all
        self.play(
            FadeOut(left_expr),
            FadeOut(right_expr),
            FadeOut(left_result),
            FadeOut(right_result),
            FadeOut(commutative_text),
            FadeOut(title)
        )
        self.wait(0.5)
