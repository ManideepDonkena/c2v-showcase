from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Asymmetric Grid", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY, "stroke_opacity": 0.5}
        )
        grid.scale(0.8)
        grid.to_edge(DOWN, buff=0.5)

        # Draw grid
        self.play(Create(grid), run_time=1)
        self.wait(0.5)

        # Points A and B
        A = Dot(color=YELLOW).move_to(grid.c2p(0, 0))
        B = Dot(color=RED).move_to(grid.c2p(1, 1))

        label_A = Tex("A").next_to(A, DOWN, buff=0.2)
        label_B = Tex("B").next_to(B, UP, buff=0.2)

        self.play(FadeIn(A), FadeIn(B), Write(label_A), Write(label_B))
        self.wait(0.5)

        # Horizontal arrow from A to B
        arrow_h = Arrow(start=grid.c2p(0, 0), end=grid.c2p(1, 0), color=BLUE)
        label_h = Tex("Cost: 1").next_to(arrow_h, DOWN, buff=0.2)
        self.play(GrowArrow(arrow_h), Write(label_h))
        self.wait(0.5)

        # Vertical arrow from (1,0) to B
        arrow_v = Arrow(start=grid.c2p(1, 0), end=grid.c2p(1, 1), color=GREEN)
        label_v = Tex("Cost: 2").next_to(arrow_v, RIGHT, buff=0.2)
        self.play(GrowArrow(arrow_v), Write(label_v))
        self.wait(0.5)

        # Formula
        formula = MathTex(r"\text{Quill Distance} = |x_1 - x_2| + 2 \cdot |y_1 - y_2|")
        formula.to_edge(UP, buff=0.5)
        self.play(FadeIn(formula))
        self.wait(1)

        # Path from (1,1) to (1,4): 3 vertical segments
        path_points = [grid.c2p(1, 1), grid.c2p(1, 2), grid.c2p(1, 3), grid.c2p(1, 4)]
        path_lines = VGroup()
        for i in range(len(path_points) - 1):
            line = Line(path_points[i], path_points[i+1], color=GREEN)
            path_lines.add(line)

        self.play(Create(path_lines))
        self.wait(0.5)

        # Labels for each vertical segment
        labels = VGroup()
        for i in range(3):
            label = Tex("Cost: 2").next_to(Line(path_points[i], path_points[i+1]), RIGHT, buff=0.2)
            labels.add(label)
            self.play(Write(label))
            self.wait(0.3)

        total_label = Tex("Total Cost: 6").to_edge(DOWN, buff=0.5)
        self.play(Write(total_label))
        self.wait(1)

        # Clear previous elements
        self.play(FadeOut(arrow_h), FadeOut(label_h), FadeOut(arrow_v), FadeOut(label_v),
                  FadeOut(path_lines), FadeOut(labels), FadeOut(total_label))

        # Show standard Manhattan grid overlay
        manhattan_grid = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY, "stroke_opacity": 0.3}
        )
        manhattan_grid.scale(0.8)
        manhattan_grid.to_edge(DOWN, buff=0.5)

        self.play(Transform(grid, manhattan_grid))
        self.wait(0.5)

        # Show Quill path on Manhattan grid
        quill_path = VGroup()
        for i in range(len(path_points) - 1):
            line = Line(path_points[i], path_points[i+1], color=GREEN)
            quill_path.add(line)
        self.play(Create(quill_path))
        self.wait(0.5)

        # Show horizontal movement example
        self.play(FadeOut(quill_path))

        C = Dot(color=YELLOW).move_to(grid.c2p(0, 0))
        D = Dot(color=RED).move_to(grid.c2p(3, 0))

        label_C = Tex("C").next_to(C, DOWN, buff=0.2)
        label_D = Tex("D").next_to(D, DOWN, buff=0.2)

        self.play(FadeIn(C), FadeIn(D), Write(label_C), Write(label_D))
        self.wait(0.5)

        # Horizontal arrow
        arrow_h2 = Arrow(start=grid.c2p(0, 0), end=grid.c2p(3, 0), color=BLUE)
        label_h2 = Tex("Cost: 3").next_to(arrow_h2, DOWN, buff=0.2)
        self.play(GrowArrow(arrow_h2), Write(label_h2))
        self.wait(0.5)

        # Calculation
        calc = MathTex(r"|3 - 0| + 2 \cdot |0 - 0| = 3 + 0 = 3")
        calc.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(calc))
        self.wait(1.5)

        # Final cleanup
        self.play(FadeOut(arrow_h2), FadeOut(label_h2), FadeOut(C), FadeOut(D),
                  FadeOut(label_C), FadeOut(label_D), FadeOut(calc), FadeOut(title), FadeOut(formula))
        self.wait(0.5)
