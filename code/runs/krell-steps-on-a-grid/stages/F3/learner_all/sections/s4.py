from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Double Step Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(x_range=[-7, 7], y_range=[-4, 4], color=LIGHT_GREY)
        grid.set_opacity(0.5)
        self.play(Create(grid))
        self.wait(0.5)

        # Point A at (0, 0)
        A = Dot([0, 0, 0], color=YELLOW)
        label_A = MathTex("(0, 0)", font_size=24).next_to(A, DOWN)
        self.play(FadeIn(A), Write(label_A))
        self.wait(0.5)

        # Step 1: (0, 0) -> (0, 1)
        arrow1 = Arrow(start=A.get_center(), end=[0, 1, 0], color=BLUE, buff=0)
        label_step1 = MathTex("Step\ 1", font_size=24).next_to(arrow1, UP)
        self.play(GrowArrow(arrow1), Write(label_step1))
        self.wait(0.5)

        # Intermediate point B1
        B1 = Dot([0, 1, 0], color=YELLOW)
        label_B1 = MathTex("(0, 1)", font_size=24).next_to(B1, UP)
        label_B1.shift(0.0 * RIGHT + 0.29 * UP)  # layout: separation vector
        self.play(FadeIn(B1), Write(label_B1))
        self.wait(0.5)

        # Step 2: (0, 1) -> (1, 1)
        arrow2 = Arrow(start=B1.get_center(), end=[1, 1, 0], color=BLUE, buff=0)
        label_step2 = MathTex("Step\ 2", font_size=24).next_to(arrow2, UP)
        label_step2.shift(0.0 * RIGHT + 0.25 * UP)  # layout: separation vector
        label_step2.shift(0.24 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow2), Write(label_step2))
        self.wait(0.5)

        # Final point B
        B = Dot([1, 1, 0], color=YELLOW)
        label_B = MathTex("(1, 1)", font_size=24).next_to(B, UP)
        self.play(FadeIn(B), Write(label_B))
        self.wait(0.5)

        # Dashed arrow from A to B (net result)
        dashed_arrow = DashedLine(start=A.get_center(), end=B.get_center(), color=GREEN)
        label_net = MathTex("(+1, +1)", font_size=24).next_to(dashed_arrow, RIGHT)
        self.play(Create(dashed_arrow), Write(label_net))
        self.wait(1)

        # Narration text
        narration1 = Text("Two consecutive Krell steps have a powerful simplification.", font_size=24).to_edge(DOWN)
        self.play(Write(narration1))
        self.wait(1.5)
        self.play(FadeOut(narration1))

        # Specific numeric example
        narration2 = Text("Let's apply the rule to (0, 0).", font_size=24).to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(1.5)
        self.play(FadeOut(narration2))

        # Step-by-step explanation
        step1_text = Text("First, swap to get (0, 0), then add 1 to the second number to land on (0, 1).", font_size=24).to_edge(DOWN)
        self.play(Write(step1_text))
        self.wait(2)
        self.play(FadeOut(step1_text))

        step2_text = Text("Now take that result (0, 1) and step again: swap to get (1, 0), then add 1 to the second number to land on (1, 1).", font_size=24).to_edge(DOWN)
        self.play(Write(step2_text))
        self.wait(2.5)
        self.play(FadeOut(step2_text))

        # Third step from (1, 2) to (2, 3)
        C = Dot([1, 2, 0], color=YELLOW)
        label_C = MathTex("(1, 2)", font_size=24).next_to(C, UP)
        self.play(FadeIn(C), Write(label_C))
        self.wait(0.5)

        arrow3 = Arrow(start=C.get_center(), end=[2, 3, 0], color=BLUE, buff=0)
        label_step3 = MathTex("Step\ 3", font_size=24).next_to(arrow3, UP)
        self.play(GrowArrow(arrow3), Write(label_step3))
        self.wait(0.5)

        D = Dot([2, 3, 0], color=YELLOW)
        label_D = MathTex("(2, 3)", font_size=24).next_to(D, UP)
        self.play(FadeIn(D), Write(label_D))
        self.wait(1)

        # Final narration
        final_narration = Text("Two Krell steps move (x, y) to (x + 1, y + 1).", font_size=24).to_edge(DOWN)
        self.play(Write(final_narration))
        self.wait(1.5)
        self.play(FadeOut(final_narration))

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(grid),
            FadeOut(A),
            FadeOut(label_A),
            FadeOut(arrow1),
            FadeOut(label_step1),
            FadeOut(B1),
            FadeOut(label_B1),
            FadeOut(arrow2),
            FadeOut(label_step2),
            FadeOut(B),
            FadeOut(label_B),
            FadeOut(dashed_arrow),
            FadeOut(label_net),
            FadeOut(C),
            FadeOut(label_C),
            FadeOut(arrow3),
            FadeOut(label_step3),
            FadeOut(D),
            FadeOut(label_D)
        )
        self.wait(0.5)
