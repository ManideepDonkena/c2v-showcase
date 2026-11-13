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
            background_line_style={"stroke_opacity": 0.3}
        )
        self.play(Create(grid))
        self.wait(0.5)
        # Points A and B
        A = Dot([0, 0, 0], color=RED)
        B = Dot([1, 1, 0], color=BLUE)
        label_A = Tex("A").next_to(A, DOWN)
        label_B = Tex("B").next_to(B, UP)
        self.play(FadeIn(A), FadeIn(B), Write(label_A), Write(label_B))
        self.wait(0.5)

        # Horizontal arrow from A to B
        arrow_h = Arrow(start=A.get_center(), end=[1, 0, 0], color=YELLOW)
        label_h = MathTex("Cost: 1").next_to(arrow_h, DOWN)
        self.play(GrowArrow(arrow_h), Write(label_h))
        self.wait(1)

        # Vertical arrow from (1,0) to B
        arrow_v = Arrow(start=[1, 0, 0], end=B.get_center(), color=PURPLE)
        label_v = MathTex("Cost: 2").next_to(arrow_v, RIGHT)
        self.play(GrowArrow(arrow_v), Write(label_v))
        self.wait(1.5)

        # Fade out arrows and labels
        self.play(FadeOut(arrow_h), FadeOut(arrow_v), FadeOut(label_h), FadeOut(label_v))

        # Formula
        formula = MathTex(r"\text{Quill Distance} = |x_1 - x_2| + 2 \cdot |y_1 - y_2|", font_size=36)
        formula.to_edge(UP)
        self.play(FadeIn(formula))
        self.wait(1.5)

        # Show example: (0,0) to (3,2)
        example_start = Dot([0, 0, 0], color=RED)
        example_end = Dot([3, 2, 0], color=BLUE)
        label_start = Tex("Start").next_to(example_start, DOWN)
        label_end = Tex("End").next_to(example_end, UP)
        self.play(FadeIn(example_start), FadeIn(example_end), Write(label_start), Write(label_end))
        self.wait(0.5)
        # Show horizontal and vertical distances
        h_dist = MathTex("3", color=YELLOW).move_to([1.5, 0, 0])
        v_dist = MathTex("2 \\times 2 = 4", color=PURPLE).move_to([3, 1, 0])
        self.play(Write(h_dist), Write(v_dist))
        self.wait(1)

        # Final sum
        total = MathTex("3 + 4 = 7").next_to(formula, DOWN)
        self.play(Write(total))
        self.wait(2)

        # Clean up
        self.play(FadeOut(title), FadeOut(grid), FadeOut(A), FadeOut(B), FadeOut(label_A), FadeOut(label_B),
                  FadeOut(formula), FadeOut(example_start), FadeOut(example_end), FadeOut(label_start),
                  FadeOut(label_end), FadeOut(h_dist), FadeOut(v_dist), FadeOut(total))
        self.wait(0.5)
