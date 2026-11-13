from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Shape of Distance 2", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Central point C(0,0)
        C = Dot(color=WHITE).move_to(ORIGIN)
        c_label = MathTex("(0,0)", font_size=24).next_to(C, DOWN)
        self.play(FadeIn(C), Write(c_label))
        self.wait(0.5)

        # Points at distance 2
        p1 = Dot(color=YELLOW).move_to(RIGHT * 2)
        p1_label = MathTex("(2,0)", font_size=24).next_to(p1, DOWN)
        calc1 = MathTex("2 + 0 = 2", font_size=24).next_to(p1, UP)
        self.play(FadeIn(p1), Write(p1_label), Write(calc1))
        self.wait(1)

        p2 = Dot(color=YELLOW).move_to(LEFT * 2)
        p2_label = MathTex("(-2,0)", font_size=24).next_to(p2, DOWN)
        calc2 = MathTex("0 + 2 = 2", font_size=24).next_to(p2, UP)
        self.play(FadeIn(p2), Write(p2_label), Write(calc2))
        self.wait(1)

        p3 = Dot(color=YELLOW).move_to(UP * 1)
        p3_label = MathTex("(0,1)", font_size=24).next_to(p3, RIGHT)
        calc3 = MathTex("0 + 2 = 2", font_size=24).next_to(p3, UP)
        self.play(FadeIn(p3), Write(p3_label), Write(calc3))
        self.wait(1)

        p4 = Dot(color=YELLOW).move_to(DOWN * 1)
        p4_label = MathTex("(0,-1)", font_size=24).next_to(p4, RIGHT)
        calc4 = MathTex("0 + 2 = 2", font_size=24).next_to(p4, UP)
        calc4.shift(0.0 * RIGHT + -0.25 * UP)  # layout: separation vector
        self.play(FadeIn(p4), Write(p4_label), Write(calc4))
        self.wait(1)

        # Dim point (1,1) with cost 3
        p5 = Dot(color=GREY).move_to(UP * 1 + RIGHT * 1)
        p5_label = MathTex("(1,1)", font_size=24).next_to(p5, UP)
        cost_label = MathTex("Cost: 3", font_size=24).next_to(p5, DOWN)
        self.play(FadeIn(p5), Write(p5_label), Write(cost_label))
        self.wait(1.5)

        # Path from (1,1) to (1,4) with 3 vertical segments
        path_start = UP * 1 + RIGHT * 1
        path_end = UP * 4 + RIGHT * 1
        segment1 = Line(path_start, path_start + UP * 1, color=BLUE)
        segment2 = Line(path_start + UP * 1, path_start + UP * 2, color=BLUE)
        segment3 = Line(path_start + UP * 2, path_end, color=BLUE)
        cost1 = MathTex("Cost: 2", font_size=24).next_to(segment1, LEFT)
        cost2 = MathTex("Cost: 2", font_size=24).next_to(segment2, LEFT)
        cost3 = MathTex("Cost: 2", font_size=24).next_to(segment3, LEFT)
        total_cost = MathTex("Total: 6", font_size=24).to_edge(DOWN)

        cost1.shift(0.0 * RIGHT + 0.26 * UP)  # layout: separation vector
        self.play(Create(segment1), Write(cost1))
        self.wait(0.5)
        self.play(Create(segment2), Write(cost2))
        self.wait(0.5)
        cost3.shift(0.0 * RIGHT + 0.24 * UP)  # layout: separation vector
        self.play(Create(segment3), Write(cost3))
        self.wait(0.5)
        self.play(Write(total_cost))
        self.wait(1.5)

        # Clear previous content
        self.play(FadeOut(VGroup(p1, p2, p3, p4, p5, c_label, calc1, calc2, calc3, calc4, cost_label, segment1, segment2, segment3, cost1, cost2, cost3, total_cost)))

        # Show Manhattan grid and overlay Quill path
        grid = NumberPlane(x_range=[-6, 6], y_range=[-4, 4], color=GREY)
        self.play(Create(grid))
        self.wait(0.5)

        # Overlay a Quill path from (0,0) to (3,2)
        path_quill = Line(ORIGIN, RIGHT * 3 + UP * 2, color=RED)
        self.play(Create(path_quill))
        self.wait(1.5)

        # Show that vertical steps are twice as costly
        self.play(Write(Text("Vertical steps cost 2", font_size=24).to_edge(UP)))
        self.wait(1.5)
        self.play(FadeOut(Text("Vertical steps cost 2", font_size=24)))

        # Show horizontal movement only: (0,0) to (3,0)
        pA = Dot(color=GREEN).move_to(ORIGIN)
        pB = Dot(color=GREEN).move_to(RIGHT * 3)
        lineAB = Line(pA.get_center(), pB.get_center(), color=GREEN)
        cost_text = MathTex("|3 - 0| + 2 \\times |0 - 0| = 3 + 0 = 3", font_size=24).to_edge(DOWN)
        self.play(FadeIn(pA), FadeIn(pB), Create(lineAB), Write(cost_text))
        self.wait(1.5)

        # Clear previous content
        self.play(FadeOut(VGroup(grid, path_quill, pA, pB, lineAB, cost_text)))

        # Show points at distance 4: (4,0) and (2,1)
        C2 = Dot(color=WHITE).move_to(ORIGIN)
        c2_label = MathTex("(0,0)", font_size=24).next_to(C2, DOWN)
        self.play(FadeIn(C2), Write(c2_label))
        self.wait(0.5)

        pB2 = Dot(color=YELLOW).move_to(RIGHT * 4)
        calc_B = MathTex("4 + 0 = 4", font_size=24).next_to(pB2, UP)
        self.play(FadeIn(pB2), Write(calc_B))
        self.wait(1.5)

        pC2 = Dot(color=YELLOW).move_to(RIGHT * 2 + UP * 1)
        calc_C = MathTex("2 + 2 = 4", font_size=24).next_to(pC2, UP)
        self.play(FadeIn(pC2), Write(calc_C))
        self.wait(1.5)

        # Generalization: horizontal movement scales linearly
        general_text = Text("Horizontal cost = steps\nVertical cost = 2 × steps", font_size=24).to_edge(DOWN)
        self.play(Write(general_text))
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, C, c_label, pB2, calc_B, pC2, calc_C, general_text)))
