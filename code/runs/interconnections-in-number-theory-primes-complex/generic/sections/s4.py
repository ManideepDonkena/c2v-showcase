from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Circle Constant", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial formula
        zeta_formula = MathTex(r"\zeta(2) = \sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}", font_size=36)
        zeta_formula.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(zeta_formula))
        self.wait(1)

        # Sum visualization
        sum_text = MathTex(r"1 + \frac{1}{4} + \frac{1}{9} + \cdots", font_size=32)
        sum_text.next_to(zeta_formula, DOWN, buff=0.5)
        self.play(Write(sum_text))
        self.wait(1)

        # Circle expanding and contracting
        circle = Circle(color=BLUE, radius=0.5).move_to(ORIGIN)
        self.play(Create(circle))
        self.wait(0.5)

        # Animate circle growth
        circle_grow = circle.animate.scale(2)
        self.play(circle_grow)
        self.wait(0.5)

        # Contract back to original size
        circle_shrink = circle.animate.scale(0.5)
        self.play(circle_shrink)
        self.wait(0.5)

        # Show area formula
        area_text = MathTex(r"\text{Area} = \pi r^2", font_size=32)
        area_text.next_to(sum_text, DOWN, buff=0.5)
        self.play(Write(area_text))
        self.wait(1)

        # Fade out old text
        self.play(FadeOut(sum_text), FadeOut(area_text))

        # Show final connection
        connect_text = Text("π, primes, and analysis are deeply intertwined", font_size=24)
        connect_text.next_to(zeta_formula, DOWN, buff=0.5)
        self.play(Write(connect_text))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(zeta_formula), FadeOut(circle), FadeOut(connect_text))
        self.wait(0.5)
