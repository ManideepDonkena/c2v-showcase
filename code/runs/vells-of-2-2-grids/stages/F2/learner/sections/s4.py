from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Rule: Swapping b and c", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grids with values
        a, b, c, d = 2, 1, 3, 4
        grid1 = Matrix([[a, b], [c, d]]).scale(0.8)
        grid2 = Matrix([[a, c], [b, d]]).scale(0.8)
        grid1.bracket_style = "[]"
        grid2.bracket_style = "[]"
        # Position grids side by side
        grid1.shift(LEFT * 2)
        grid2.shift(RIGHT * 2)

        # Labels
        label1 = Text("Grid 1", font_size=24).next_to(grid1, DOWN)
        label2 = Text("Grid 2", font_size=24).next_to(grid2, DOWN)

        self.play(Write(grid1), Write(label1))
        self.wait(0.5)
        self.play(Write(grid2), Write(label2))
        self.wait(0.5)

        # Vell formulas
        vell1 = MathTex("a \\times d - b - c", font_size=32).next_to(grid1, DOWN, buff=0.8)
        vell2 = MathTex("a \\times d - c - b", font_size=32).next_to(grid2, DOWN, buff=0.8)

        self.play(Write(vell1))
        self.wait(0.5)
        self.play(Write(vell2))
        self.wait(0.5)

        # Highlight subtraction order
        highlight1 = SurroundingRectangle(vell1[0][6:9], color=YELLOW, buff=0.1)  # -b -c
        highlight2 = SurroundingRectangle(vell2[0][6:9], color=YELLOW, buff=0.1)  # -c -b

        highlight1.shift(0.38 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(highlight1))
        self.wait(0.5)
        self.play(Transform(highlight1, highlight2))
        self.wait(0.5)
        self.play(FadeOut(highlight1))

        # Show that they are equal
        equal = MathTex("= 4", font_size=32).next_to(vell1, RIGHT, buff=0.5)
        self.play(Write(equal))
        self.wait(0.5)

        # Narration text
        narration = Text("Subtraction order does not change result", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.0)

        # Final checkmark
        check = Tex(r"$\checkmark$").scale(2).set_color(GREEN).next_to(equal, RIGHT, buff=0.5)
        self.play(Write(check))
        self.wait(1.0)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(grid1),
            FadeOut(grid2),
            FadeOut(label1),
            FadeOut(label2),
            FadeOut(vell1),
            FadeOut(vell2),
            FadeOut(equal),
            FadeOut(narration),
            FadeOut(check)
        )
        self.wait(0.5)
