from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Higher Order Derivatives: From Velocity to Jerk", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Start with f(t) = x^3
        func_text = MathTex("f(x) = x^3", font_size=40)
        func_text.to_corner(UL)
        func_text.shift(0.0 * RIGHT + -0.65 * UP)  # layout: separation vector
        self.play(Write(func_text))
        self.wait(1)

        # First derivative: 3x^2
        first_deriv = MathTex("\\frac{d}{dx}(x^3) = 3x^2", font_size=32)
        first_deriv.next_to(func_text, DOWN, buff=0.5)
        self.play(Write(first_deriv))
        self.wait(1)

        # Second derivative: 6x
        second_deriv = MathTex("\\frac{d}{dx}(3x^2) = 6x", font_size=32)
        second_deriv.next_to(first_deriv, DOWN, buff=0.5)
        self.play(Write(second_deriv))
        self.wait(1)

        # Third derivative: 6
        third_deriv = MathTex("\\frac{d}{dx}(6x) = 6", font_size=32)
        third_deriv.next_to(second_deriv, DOWN, buff=0.5)
        self.play(Write(third_deriv))
        self.wait(1)

        # Show that after n steps, we get a constant
        const_text = Text("After 3 steps: constant 6", font_size=24)
        const_text.next_to(third_deriv, DOWN, buff=0.5)
        const_text.shift(0.67 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(const_text))
        self.wait(1)

        # Fade out polynomial example
        self.play(FadeOut(func_text), FadeOut(first_deriv), FadeOut(second_deriv), FadeOut(third_deriv), FadeOut(const_text))

        # Show sine/cosine cycle
        sin_func = MathTex("\\sin(x)", font_size=40)
        sin_func.to_corner(UL)
        self.play(Write(sin_func))
        self.wait(0.5)

        cos_func = MathTex("\\cos(x)", font_size=32)
        cos_func.next_to(sin_func, DOWN, buff=0.5)
        self.play(Write(cos_func))
        self.wait(0.5)

        neg_sin = MathTex("-\\sin(x)", font_size=32)
        neg_sin.next_to(cos_func, DOWN, buff=0.5)
        self.play(Write(neg_sin))
        self.wait(0.5)

        neg_cos = MathTex("-\\cos(x)", font_size=32)
        neg_cos.next_to(neg_sin, DOWN, buff=0.5)
        self.play(Write(neg_cos))
        self.wait(0.5)

        back_to_sin = MathTex("\\sin(x)", font_size=32)
        back_to_sin.next_to(neg_cos, DOWN, buff=0.5)
        self.play(Write(back_to_sin))
        self.wait(1)

        # Fade out sine/cosine
        self.play(FadeOut(sin_func), FadeOut(cos_func), FadeOut(neg_sin), FadeOut(neg_cos), FadeOut(back_to_sin))

        # Show mixed partials example (x and y)
        mixed_text = Text("Mixed Partial Derivatives", font_size=36)
        mixed_text.to_edge(UP)
        mixed_text.shift(0.0 * RIGHT + -0.65 * UP)  # layout: separation vector
        self.play(Write(mixed_text))
        self.wait(0.5)

        # Show f(x,y) = x^2 * y
        func_xy = MathTex("f(x, y) = x^2 y", font_size=40)
        func_xy.to_corner(UL)
        self.play(Write(func_xy))
        self.wait(1)

        # First differentiate w.r.t. x then y
        diff_xy = MathTex("\\frac{\\partial^2 f}{\\partial y \\partial x} = 2x", font_size=32)
        diff_xy.next_to(func_xy, DOWN, buff=0.5)
        self.play(Write(diff_xy))
        self.wait(1)

        # First differentiate w.r.t. y then x
        diff_yx = MathTex("\\frac{\\partial^2 f}{\\partial x \\partial y} = 2x", font_size=32)
        diff_yx.next_to(diff_xy, DOWN, buff=0.5)
        self.play(Write(diff_yx))
        self.wait(1)

        # Show they are equal
        equal_text = Text("Equal if continuous!", font_size=24)
        equal_text.next_to(diff_yx, DOWN, buff=0.5)
        self.play(Write(equal_text))
        self.wait(1)

        # Fade out mixed partials
        self.play(FadeOut(func_xy), FadeOut(diff_xy), FadeOut(diff_yx), FadeOut(equal_text))

        # General formula
        general = MathTex("\\frac{d^n}{dx^n}", font_size=40)
        general.to_edge(UP)
        self.play(Write(general))
        self.wait(1)

        # Final text
        abstract = Text("Mathematical Abstraction", font_size=36)
        abstract.next_to(general, DOWN)
        self.play(Write(abstract))
        self.wait(1)

        self.play(FadeOut(general), FadeOut(abstract), FadeOut(title))
