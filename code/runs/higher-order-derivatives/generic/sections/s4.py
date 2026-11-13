from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Higher Order Derivatives: From Velocity to Jerk", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial function f(t)
        f_t = MathTex("f(t)", font_size=40)
        f_t.to_corner(UL)
        self.play(Write(f_t))
        self.wait(0.5)

        # Arrow and derivative
        arrow1 = Arrow(start=f_t.get_right(), end=f_t.get_right() + RIGHT * 2, buff=0.1)
        ddt1 = MathTex(r"\frac{d}{dt}", font_size=30).next_to(arrow1, UP)
        arrow1.shift(0.0 * RIGHT + 0.53 * UP)  # layout: separation vector
        ddt1.shift(0.0 * RIGHT + -0.86 * UP)  # layout: separation vector
        ddt1.shift(0.0 * RIGHT + -0.65 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow1), Write(ddt1))
        self.wait(0.5)

        # First derivative f'(t)
        f_prime_t = MathTex("f'(t)", font_size=40).next_to(arrow1.get_end(), RIGHT * 2)
        self.play(Write(f_prime_t))
        self.wait(0.5)

        # Second arrow and second derivative
        arrow2 = Arrow(start=f_prime_t.get_right(), end=f_prime_t.get_right() + RIGHT * 2, buff=0.1)
        ddt2 = MathTex(r"\frac{d}{dt}", font_size=30).next_to(arrow2, UP)
        self.play(GrowArrow(arrow2), Write(ddt2))
        self.wait(0.5)

        # Second derivative f''(t)
        f_double_prime_t = MathTex("f''(t)", font_size=40).next_to(arrow2.get_end(), RIGHT * 2)
        self.play(Write(f_double_prime_t))
        self.wait(0.5)

        # Third arrow and third derivative
        arrow3 = Arrow(start=f_double_prime_t.get_right(), end=f_double_prime_t.get_right() + RIGHT * 2, buff=0.1)
        ddt3 = MathTex(r"\frac{d}{dt}", font_size=30).next_to(arrow3, UP)
        self.play(GrowArrow(arrow3), Write(ddt3))
        self.wait(0.5)

        # Third derivative f'''(t)
        f_triple_prime_t = MathTex("f'''(t)", font_size=40).next_to(arrow3.get_end(), RIGHT * 2)
        self.play(Write(f_triple_prime_t))
        self.wait(0.5)

        # Fourth arrow and dashed curve for f^(4)(t)
        arrow4 = Arrow(start=f_triple_prime_t.get_right(), end=f_triple_prime_t.get_right() + RIGHT * 2, buff=0.1)
        ddt4 = MathTex(r"\frac{d}{dt}", font_size=30).next_to(arrow4, UP)
        self.play(GrowArrow(arrow4), Write(ddt4))
        self.wait(0.5)

        # Dashed curve for f^(4)(t)
        f_fourth_t = MathTex("f^{(4)}(t)", font_size=40).next_to(arrow4.get_end(), RIGHT * 2)
        f_fourth_t.set_color(GRAY)
        self.play(Write(f_fourth_t))
        self.wait(0.5)

        # Fade out arrows and labels
        self.play(FadeOut(arrow1), FadeOut(ddt1), FadeOut(arrow2), FadeOut(ddt2),
                  FadeOut(arrow3), FadeOut(ddt3), FadeOut(arrow4), FadeOut(ddt4))
        self.wait(0.5)

        # General formula
        general_formula = MathTex(r"\frac{d^n}{dx^n}", font_size=40).move_to(ORIGIN)
        self.play(Transform(f_fourth_t, general_formula))
        self.wait(1)

        # Text: Mathematical Abstraction
        abstraction_text = Text("Mathematical Abstraction", font_size=30)
        abstraction_text.next_to(general_formula, DOWN)
        self.play(Write(abstraction_text))
        self.wait(2)

        # Narration text
        narration1 = Text("We can continue this process indefinitely.", font_size=24)
        narration1.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(narration1))
        self.wait(1.5)
        self.play(FadeOut(narration1))

        narration2 = Text("Each higher-order derivative describes how the previous rate of change is evolving.", font_size=24)
        narration2.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(narration2))
        self.wait(2)
        self.play(FadeOut(narration2))

        narration3 = Text("While physical interpretations become abstract, the mathematical pattern remains consistent.", font_size=24)
        narration3.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(narration3))
        self.wait(2)
        self.play(FadeOut(narration3))

        # Final fade out
        self.play(FadeOut(title), FadeOut(f_t), FadeOut(f_prime_t), FadeOut(f_double_prime_t),
                  FadeOut(f_triple_prime_t), FadeOut(f_fourth_t), FadeOut(abstraction_text))
        self.wait(0.5)
