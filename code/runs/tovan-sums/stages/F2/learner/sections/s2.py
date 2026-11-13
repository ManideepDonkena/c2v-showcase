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

        # Right scene: a ⊕ b vs b ⊕ a
        right_eq = MathTex("a \\oplus b", font_size=40)
        right_eq.to_corner(UR)
        self.play(Write(right_eq))
        self.wait(1)

        # Show commutativity
        comm = MathTex("= b \\oplus a", font_size=40)
        comm.next_to(right_eq, DOWN, buff=0.5)
        self.play(Write(comm))
        self.wait(2)

        # Fade out everything except title
        self.play(
            FadeOut(left_eq),
            FadeOut(expand),
            FadeOut(right_eq),
            FadeOut(comm),
            FadeOut(title)
        )
        self.wait(0.5)

        # Show the key message
        msg = Text("Order does not matter: a ⊕ b = b ⊕ a", font_size=24).to_edge(UP)
        self.play(Write(msg))
        self.wait(1.5)

        msg2 = Text("Zero is neutral: 0 ⊕ b = b", font_size=24).to_edge(DOWN)
        self.play(Write(msg2))
        self.wait(2)

        # Final fade out
        self.play(
            FadeOut(msg),
            FadeOut(msg2)
        )
        self.wait(0.5)
