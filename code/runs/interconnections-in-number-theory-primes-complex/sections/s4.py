from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Circle Constant", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial formula
        zeta_formula = MathTex(r"\zeta(2) = \sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}", font_size=40)
        self.play(Write(zeta_formula))
        self.wait(2)

        # Zoom in effect
        self.play(zeta_formula.animate.scale(0.7).to_corner(UL))
        self.wait(0.5)

        # Series visualization
        series_text = MathTex(r"1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \cdots", font_size=32)
        series_text.next_to(zeta_formula, DOWN, buff=0.5)
        self.play(Write(series_text))
        self.wait(1.5)

        # Circle expanding
        circle = Circle(color=BLUE, radius=0.5)
        circle.move_to(ORIGIN)
        self.play(Create(circle))
        self.wait(0.5)

        # Animate circle growing and shrinking
        self.play(
            circle.animate.scale(2),
            run_time=1.5
        )
        self.play(
            circle.animate.scale(0.5),
            run_time=1.5
        )

        # Show π²/6 appears
        pi_result = MathTex(r"\frac{\pi^2}{6}", font_size=32)
        pi_result.next_to(series_text, DOWN, buff=0.5)
        self.play(Write(pi_result))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(zeta_formula),
            FadeOut(series_text),
            FadeOut(circle),
            FadeOut(pi_result)
        )
        self.wait(0.5)
