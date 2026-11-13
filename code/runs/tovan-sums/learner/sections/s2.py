from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Commutativity and Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Left scene: 0 ⊕ b
        left_eq = MathTex("0 \\oplus b", font_size=40)
        left_eq.to_corner(UL)
        self.play(Write(left_eq))
        self.wait(1)

        # Expand to 0 + b + (0 × b)
        expand = MathTex("= 0 + b + (0 \\times b)", font_size=40)
        expand.next_to(left_eq, DOWN, buff=0.5)
        expand.shift(0.71 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(expand))
        self.wait(1.5)

        # Show 0 + b = b
        step1 = MathTex("= 0 + b + 0", font_size=40)
        step1.next_to(left_eq, DOWN, buff=0.5)
        self.play(Transform(expand, step1))
        self.wait(1.5)

        # Show final result: b
        final = MathTex("= b", font_size=40)
        final.next_to(left_eq, DOWN, buff=0.5)
        self.play(Transform(expand, final))
        self.wait(2)

        # Add explanation text
        explain1 = Text("Adding zero contributes nothing...", font_size=24).to_edge(DOWN)
        self.play(Write(explain1))
        self.wait(2)
        self.play(FadeOut(explain1))

        # Right scene: a ⊕ b vs b ⊕ a
        right_eq = MathTex("a \\oplus b", font_size=40)
        right_eq.to_corner(UR)
        self.play(Write(right_eq))
        self.wait(1)

        # Show both sides equal
        commutative = MathTex("= b \\oplus a", font_size=40)
        commutative.next_to(right_eq, DOWN, buff=0.5)
        self.play(Write(commutative))
        self.wait(2)

        # Add explanation text
        explain2 = Text("Order does not matter", font_size=24).to_edge(DOWN)
        self.play(Write(explain2))
        self.wait(2)
        self.play(FadeOut(explain2))

        # Fade out everything
        self.play(
            FadeOut(left_eq),
            FadeOut(expand),
            FadeOut(right_eq),
            FadeOut(commutative),
            FadeOut(title)
        )
        self.wait(0.5)
