from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Calculating v(3) and v(4)", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial sequence
        seq = MathTex("1, 3")
        seq.scale(1.5)
        seq.to_corner(UL)
        self.play(Write(seq))
        self.wait(0.5)

        # Formula rule
        rule = Text("v(n) = v(n-1) + 2×v(n-2)", font_size=24)
        rule.next_to(seq, DOWN, buff=0.5)
        rule.shift(0.94 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(rule))
        self.wait(1)

        # v(3) calculation
        calc3 = MathTex("v(3) = 3 + 2 \\times 1 = 5")
        calc3.scale(1.2)
        calc3.next_to(rule, DOWN, buff=0.5)
        calc3.shift(0.86 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(calc3))
        self.wait(1)

        # Highlight result
        highlight3 = SurroundingRectangle(calc3, color=YELLOW, buff=0.2)
        highlight3.shift(0.2 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(highlight3))
        self.wait(1)
        self.play(FadeOut(highlight3))

        # v(4) calculation
        calc4 = MathTex("v(4) = 5 + 2 \\times 3 = 11")
        calc4.scale(1.2)
        calc4.next_to(calc3, DOWN, buff=0.5)
        self.play(Write(calc4))
        self.wait(1)

        # Highlight result
        highlight4 = SurroundingRectangle(calc4, color=YELLOW, buff=0.2)
        self.play(Create(highlight4))
        self.wait(1)
        self.play(FadeOut(highlight4))

        # Final sequence
        seq_full = MathTex("1, 3, 5, 11")
        seq_full.scale(1.5)
        seq_full.to_corner(UL)
        self.play(Transform(seq, seq_full))
        self.wait(1)

        # Rules summary
        rules = VGroup(
            Text("Rule 1: Every term is odd.", font_size=24),
            Text("Rule 2: Each term is about twice the one before.", font_size=24)
        )
        rules.arrange(DOWN, buff=0.3)
        rules.next_to(calc4, DOWN, buff=0.5)
        self.play(Write(rules))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(seq),
            FadeOut(rule),
            FadeOut(calc3),
            FadeOut(calc4),
            FadeOut(rules)
        )
        self.wait(0.5)
