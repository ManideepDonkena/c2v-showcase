from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Asymmetric Grid", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(
            x_range=[-4, 5, 1],
            y_range=[-2, 5, 1],
            axis_config={"stroke_width": 1},
            background_line_style={"stroke_opacity": 0.3}
        )
        self.play(Create(grid))
        self.wait(0.5)

        # Points A and B
        A = Dot([0, 0, 0], color=BLUE)
        B = Dot([1, 1, 0], color=RED)
        label_A = Tex("A").next_to(A, DOWN, buff=0.2)
        label_B = Tex("B").next_to(B, UP, buff=0.2)
        self.play(FadeIn(A), FadeIn(B), Write(label_A), Write(label_B))
        self.wait(0.5)

        # Horizontal arrow from A to B
        h_arrow = Arrow(start=A.get_center(), end=[1, 0, 0], color=YELLOW)
        h_label = MathTex("Cost: 1").next_to(h_arrow, DOWN, buff=0.2)
        self.play(GrowArrow(h_arrow), Write(h_label))
        self.wait(0.5)

        # Vertical arrow from (1,0) to B
        v_arrow = Arrow(start=[1, 0, 0], end=B.get_center(), color=PURPLE)
        v_label = MathTex("Cost: 2").next_to(v_arrow, RIGHT, buff=0.2)
        self.play(GrowArrow(v_arrow), Write(v_label))
        self.wait(0.5)

        # Formula
        formula = MathTex(r"\text{Quill Distance} = |x_1 - x_2| + 2 \cdot |y_1 - y_2|")
        formula.to_edge(UP)
        self.play(Write(formula))
        self.wait(0.5)

        # Path from (1,1) to (1,4): 3 vertical segments
        path_points = [[1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0]]
        path_arrows = []
        path_labels = []
        for i in range(3):
            start = path_points[i]
            end = path_points[i+1]
            arrow = Arrow(start=start, end=end, color=GREEN)
            label = MathTex("Cost: 2").next_to(arrow, LEFT, buff=0.2)
            path_arrows.append(arrow)
            path_labels.append(label)
        self.play(*[GrowArrow(a) for a in path_arrows])
        self.play(*[Write(l) for l in path_labels])
        self.wait(0.5)

        # Show Manhattan grid overlay
        manhattan_grid = NumberPlane(
            x_range=[-4, 5, 1],
            y_range=[-2, 5, 1],
            axis_config={"stroke_width": 1},
            background_line_style={"stroke_opacity": 0.1}
        )
        self.play(FadeIn(manhattan_grid))
        self.wait(0.5)

        # Show that Quill grid is stretched vertically
        self.play(FadeOut(manhattan_grid))

        # Horizontal movement only: (0,0) to (3,0)
        C = Dot([0, 0, 0], color=BLUE)
        D = Dot([3, 0, 0], color=RED)
        label_C = Tex("C").next_to(C, DOWN, buff=0.2)
        label_D = Tex("D").next_to(D, DOWN, buff=0.2)
        self.play(FadeIn(C), FadeIn(D), Write(label_C), Write(label_D))
        self.wait(0.5)

        h_arrow2 = Arrow(start=C.get_center(), end=D.get_center(), color=YELLOW)
        h_label2 = MathTex("Cost: 3").next_to(h_arrow2, DOWN, buff=0.2)
        self.play(GrowArrow(h_arrow2), Write(h_label2))
        self.wait(0.5)

        # Calculation
        calc = MathTex(r"|3 - 0| + 2 \cdot |0 - 0| = 3 + 0 = 3")
        calc.to_edge(DOWN)
        self.play(Write(calc))
        self.wait(1)

        # Show multiple points at distance 4
        self.play(FadeOut(calc), FadeOut(h_arrow2), FadeOut(h_label2))

        # Point (4,0) - horizontal only
        E = Dot([4, 0, 0], color=GREEN)
        label_E = Tex("E").next_to(E, DOWN, buff=0.2)
        self.play(FadeIn(E), Write(label_E))
        self.wait(0.5)

        calc1 = MathTex(r"|4| + 2 \cdot |0| = 4 + 0 = 4")
        calc1.to_edge(DOWN)
        self.play(Write(calc1))
        self.wait(0.5)

        # Point (2,1) - mixed
        F = Dot([2, 1, 0], color=ORANGE)
        label_F = Tex("F").next_to(F, UP, buff=0.2)
        self.play(FadeIn(F), Write(label_F))
        self.wait(0.5)

        calc2 = MathTex(r"|2| + 2 \cdot |1| = 2 + 2 = 4")
        calc2.next_to(calc1, DOWN)
        self.play(Write(calc2))
        self.wait(0.5)

        # Final explanation
        note = Text("Any point where horizontal distance equals target cost\nor vertical is half the cost is valid.", font_size=24)
        note.to_edge(DOWN)
        self.play(Write(note))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(grid), FadeOut(A), FadeOut(B), FadeOut(C), FadeOut(D), FadeOut(E), FadeOut(F),
                  FadeOut(label_A), FadeOut(label_B), FadeOut(label_C), FadeOut(label_D), FadeOut(label_E), FadeOut(label_F),
                  FadeOut(h_arrow), FadeOut(v_arrow), FadeOut(h_label), FadeOut(v_label),
                  FadeOut(path_arrows[0]), FadeOut(path_arrows[1]), FadeOut(path_arrows[2]),
                  FadeOut(path_labels[0]), FadeOut(path_labels[1]), FadeOut(path_labels[2]),
                  FadeOut(formula), FadeOut(calc1), FadeOut(calc2), FadeOut(note))
