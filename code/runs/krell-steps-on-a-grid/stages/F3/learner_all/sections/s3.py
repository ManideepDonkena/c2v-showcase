from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Staircase Path from Origin", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(x_range=[-7, 7], y_range=[-4, 4], faded_line_ratio=1)
        grid.set_opacity(0.5)
        self.play(Create(grid))
        self.wait(0.5)

        # Initial point (0, 0)
        origin = Dot([0, 0, 0], color=YELLOW)
        origin_label = MathTex("(0, 0)", font_size=24).next_to(origin, DOWN, buff=0.2)
        self.play(FadeIn(origin), Write(origin_label))
        self.wait(1)

        # Step 1: (0, 0) -> (0, 1)
        step1 = MathTex("Krell\\ step:\\ (0, 0) \\to (0, 1)", font_size=24).to_edge(DOWN)
        self.play(Write(step1))
        self.wait(1)

        # Draw first step
        point1 = Dot([0, 1, 0], color=GREEN)
        line1 = Line([0, 0, 0], [0, 1, 0], color=GREEN)
        label1 = MathTex("(0, 1)", font_size=24).next_to(point1, UP, buff=0.2)
        self.play(Create(line1), FadeIn(point1), Write(label1))
        self.wait(1)

        # Step 2: (0, 1) -> (1, 1)
        step2 = MathTex("Krell\\ step:\\ (0, 1) \\to (1, 1)", font_size=24).to_edge(DOWN)
        self.play(Transform(step1, step2))
        self.wait(1)

        # Draw second step
        point2 = Dot([1, 1, 0], color=GREEN)
        line2 = Line([0, 1, 0], [1, 1, 0], color=GREEN)
        label2 = MathTex("(1, 1)", font_size=24).next_to(point2, UP, buff=0.2)
        self.play(Create(line2), FadeIn(point2), Write(label2))
        self.wait(1)

        # Step 3: (1, 1) -> (1, 2)
        step3 = MathTex("Krell\\ step:\\ (1, 1) \\to (1, 2)", font_size=24).to_edge(DOWN)
        self.play(Transform(step1, step3))
        self.wait(1)

        # Draw third step
        point3 = Dot([1, 2, 0], color=GREEN)
        line3 = Line([1, 1, 0], [1, 2, 0], color=GREEN)
        label3 = MathTex("(1, 2)", font_size=24).next_to(point3, UP, buff=0.2)
        self.play(Create(line3), FadeIn(point3), Write(label3))
        self.wait(1)

        # Step 4: (1, 2) -> (2, 2)
        step4 = MathTex("Krell\\ step:\\ (1, 2) \\to (2, 2)", font_size=24).to_edge(DOWN)
        self.play(Transform(step1, step4))
        self.wait(1)

        # Draw fourth step
        point4 = Dot([2, 2, 0], color=GREEN)
        line4 = Line([1, 2, 0], [2, 2, 0], color=GREEN)
        label4 = MathTex("(2, 2)", font_size=24).next_to(point4, UP, buff=0.2)
        self.play(Create(line4), FadeIn(point4), Write(label4))
        self.wait(1)

        # Show example: (0, 0) -> (0, 1) -> (1, 1)
        example_text = Text("Let's apply the rule to (0, 0).", font_size=24).to_edge(DOWN)
        self.play(Transform(step1, example_text))
        self.wait(1.5)

        # Show first step explicitly
        swap_text = MathTex("\\text{Swap } (0, 0) \\to (0, 0)", font_size=24).next_to(step1, DOWN)
        add_text = MathTex("\\text{Add 1 to second: } (0, 0) \\to (0, 1)", font_size=24).next_to(swap_text, DOWN)
        self.play(Write(swap_text))
        self.wait(1.5)
        self.play(Write(add_text))
        self.wait(1.5)

        # Show second step explicitly
        swap_text2 = MathTex("\\text{Swap } (0, 1) \\to (1, 0)", font_size=24).next_to(step1, DOWN)
        add_text2 = MathTex("\\text{Add 1 to second: } (1, 0) \\to (1, 1)", font_size=24).next_to(swap_text2, DOWN)
        self.play(Transform(swap_text, swap_text2))
        self.wait(1.5)
        self.play(Transform(add_text, add_text2))
        self.wait(1.5)

        # Show third step: (1, 2) -> (2, 3)
        self.play(FadeOut(swap_text), FadeOut(add_text), FadeOut(step1))

        final_step_text = Text("The third step takes us from (1,2) to (2,3)", font_size=24).to_edge(DOWN)
        self.play(Write(final_step_text))
        self.wait(1.5)

        # Draw final arrow
        arrow = Arrow([1, 2, 0], [2, 3, 0], color=RED, buff=0.1)
        final_label = MathTex("(2, 3)", font_size=24).next_to([2, 3, 0], UP, buff=0.2)
        self.play(Create(arrow), Write(final_label))
        self.wait(2)

        # Cleanup
        self.play(FadeOut(title), FadeOut(grid), FadeOut(origin), FadeOut(origin_label),
                  FadeOut(point1), FadeOut(label1), FadeOut(line1),
                  FadeOut(point2), FadeOut(label2), FadeOut(line2),
                  FadeOut(point3), FadeOut(label3), FadeOut(line3),
                  FadeOut(point4), FadeOut(label4), FadeOut(line4),
                  FadeOut(arrow), FadeOut(final_label), FadeOut(final_step_text))
        self.wait(0.5)
