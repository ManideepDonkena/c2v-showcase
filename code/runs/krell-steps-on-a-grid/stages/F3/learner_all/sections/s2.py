from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Grid Point Validity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(x_range=[-7, 7], y_range=[-4, 4], faded_line_ratio=1)
        grid.set_opacity(0.5)
        self.play(Create(grid))
        self.wait(0.5)

        # Initial point (x, y)
        x, y = 2, 1
        point = Dot(color=YELLOW).move_to(grid.c2p(x, y))
        label = MathTex(f"({x}, {y})").next_to(point, UR, buff=0.2)
        self.play(FadeIn(point), Write(label))
        self.wait(0.5)

        # Krell step: (x, y) -> (y, x+1)
        new_x, new_y = y, x + 1
        arrow = Arrow(grid.c2p(x, y), grid.c2p(new_x, new_y), color=RED, buff=0.1)
        new_point = Dot(color=YELLOW).move_to(grid.c2p(new_x, new_y))
        new_label = MathTex(f"({new_x}, {new_y})").next_to(new_point, UR, buff=0.2)

        new_point.shift(0.0 * RIGHT + -0.23 * UP)  # layout: separation vector
        new_label.shift(0.0 * RIGHT + -0.93 * UP)  # layout: separation vector
        self.play(Create(arrow), FadeIn(new_point), Write(new_label))
        self.wait(1)

        # Checkmark
        check = Tex(r"$\checkmark$").scale(1.5).set_color(GREEN).next_to(new_label, RIGHT)
        self.play(Write(check))
        self.wait(1)

        # Clear previous
        self.play(FadeOut(point), FadeOut(label), FadeOut(arrow), FadeOut(new_point), FadeOut(new_label))

        # Specific numeric example: (0, 0) -> (0, 1) -> (1, 1)
        start = Dot(color=YELLOW).move_to(grid.c2p(0, 0))
        start_label = MathTex("(0, 0)").next_to(start, UR, buff=0.2)
        self.play(FadeIn(start), Write(start_label))
        self.wait(0.5)

        # Step 1: (0, 0) -> swap -> (0, 0) -> add 1 to second -> (0, 1)
        step1_x, step1_y = 0, 1
        arrow1 = Arrow(grid.c2p(0, 0), grid.c2p(step1_x, step1_y), color=BLUE, buff=0.1)
        point1 = Dot(color=YELLOW).move_to(grid.c2p(step1_x, step1_y))
        label1 = MathTex("(0, 1)").next_to(point1, UR, buff=0.2)
        self.play(Create(arrow1), FadeIn(point1), Write(label1))
        self.wait(1)

        # Step 2: (0, 1) -> swap -> (1, 0) -> add 1 to second -> (1, 1)
        step2_x, step2_y = 1, 1
        arrow2 = Arrow(grid.c2p(step1_x, step1_y), grid.c2p(step2_x, step2_y), color=BLUE, buff=0.1)
        point2 = Dot(color=YELLOW).move_to(grid.c2p(step2_x, step2_y))
        label2 = MathTex("(1, 1)").next_to(point2, UR, buff=0.2)
        self.play(Create(arrow2), FadeIn(point2), Write(label2))
        self.wait(1)

        # Clear
        self.play(FadeOut(start), FadeOut(start_label), FadeOut(arrow1), FadeOut(point1), FadeOut(label1),
                  FadeOut(arrow2), FadeOut(point2), FadeOut(label2))

        # Third step: (1, 2) -> (2, 3)
        third_start = Dot(color=YELLOW).move_to(grid.c2p(1, 2))
        third_label = MathTex("(1, 2)").next_to(third_start, UR, buff=0.2)
        self.play(FadeIn(third_start), Write(third_label))
        self.wait(0.5)

        third_arrow = Arrow(grid.c2p(1, 2), grid.c2p(2, 3), color=GREEN, buff=0.1)
        third_end = Dot(color=YELLOW).move_to(grid.c2p(2, 3))
        third_end_label = MathTex("(2, 3)").next_to(third_end, UR, buff=0.2)

        self.play(Create(third_arrow), FadeIn(third_end), Write(third_end_label))
        self.wait(1)

        # Narration text
        narration = Text("Because we start with integers and only perform swapping and addition, every Krell step always lands exactly on another valid grid point.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)

        self.play(FadeOut(narration), FadeOut(title), FadeOut(grid), FadeOut(third_start), FadeOut(third_label),
                  FadeOut(third_arrow), FadeOut(third_end), FadeOut(third_end_label))
