from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Shape of Distance 2", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Central point C(0,0)
        center = Dot([0, 0, 0], color=WHITE)
        c_label = MathTex("C(0,0)", font_size=24).next_to(center, DOWN)
        self.play(FadeIn(center), Write(c_label))
        self.wait(0.5)

        # Points at distance 2
        p1 = Dot([2, 0, 0], color=YELLOW)
        p1_label = MathTex("(2,0)", font_size=24).next_to(p1, UR)
        calc1 = MathTex("2 + 0 = 2", font_size=24).next_to(p1_label, DOWN)
        self.play(FadeIn(p1), Write(p1_label), Write(calc1))
        self.wait(1)

        p2 = Dot([-2, 0, 0], color=YELLOW)
        p2_label = MathTex("(-2,0)", font_size=24).next_to(p2, UL)
        calc2 = MathTex("0 + 2 = 2", font_size=24).next_to(p2_label, DOWN)
        self.play(FadeIn(p2), Write(p2_label), Write(calc2))
        self.wait(1)

        p3 = Dot([0, 1, 0], color=YELLOW)
        p3_label = MathTex("(0,1)", font_size=24).next_to(p3, UP)
        calc3 = MathTex("0 + 2 = 2", font_size=24).next_to(p3_label, DOWN)
        self.play(FadeIn(p3), Write(p3_label), Write(calc3))
        self.wait(1)

        p4 = Dot([0, -1, 0], color=YELLOW)
        p4_label = MathTex("(0,-1)", font_size=24).next_to(p4, DOWN)
        calc4 = MathTex("0 + 2 = 2", font_size=24).next_to(p4_label, UP)
        self.play(FadeIn(p4), Write(p4_label), Write(calc4))
        self.wait(1)

        # Dim point (1,1) with cost 3
        p5 = Dot([1, 1, 0], color=GRAY)
        p5_label = MathTex("(1,1)", font_size=24).next_to(p5, UR)
        cost5 = MathTex("Cost: 3", font_size=24).next_to(p5_label, DOWN)
        self.play(FadeIn(p5), Write(p5_label), Write(cost5))
        self.wait(1.5)

        # Path from (1,1) to (1,4) with 3 vertical segments
        path_start = [1, 1, 0]
        path_end = [1, 4, 0]
        segment1 = Line(path_start, [1, 2, 0], color=BLUE)
        seg1_label = MathTex("Cost: 2", font_size=24).next_to(segment1, RIGHT)
        segment2 = Line([1, 2, 0], [1, 3, 0], color=BLUE)
        seg2_label = MathTex("Cost: 2", font_size=24).next_to(segment2, RIGHT)
        segment3 = Line([1, 3, 0], path_end, color=BLUE)
        seg3_label = MathTex("Cost: 2", font_size=24).next_to(segment3, RIGHT)
        total_cost = MathTex("Total Cost: 6", font_size=24).to_edge(DOWN)

        self.play(Create(segment1), Write(seg1_label))
        self.wait(0.5)
        self.play(Create(segment2), Write(seg2_label))
        self.wait(0.5)
        self.play(Create(segment3), Write(seg3_label))
        self.wait(0.5)
        self.play(Write(total_cost))
        self.wait(1.5)

        # Overlay Manhattan grid
        grid = NumberPlane(x_range=[-7, 7], y_range=[-4, 4], axis_config={"stroke_color": GRAY})
        self.play(Create(grid))
        self.wait(0.5)

        # Show Quill path on grid
        quill_path = Line([0, 0, 0], [2, 0, 0], color=RED)
        self.play(Create(quill_path))
        self.wait(0.5)

        # Show horizontal movement only (cost = |x| + 2*|y| = 3 + 0 = 3)
        h_point = Dot([3, 0, 0], color=GREEN)
        h_label = MathTex("(3,0)", font_size=24).next_to(h_point, DOWN)
        h_calc = MathTex("|3 - 0| + 2 \\times |0 - 0| = 3 + 0 = 3", font_size=24).to_edge(DOWN)
        self.play(FadeIn(h_point), Write(h_label))
        self.wait(0.5)
        self.play(Write(h_calc))
        self.wait(1.5)

        # Show that vertical movement is scaled
        v_point = Dot([0, 2, 0], color=PURPLE)
        v_label = MathTex("(0,2)", font_size=24).next_to(v_point, UP)
        v_calc = MathTex("|0 - 0| + 2 \\times |2 - 0| = 0 + 4 = 4", font_size=24).to_edge(DOWN)
        self.play(FadeIn(v_point), Write(v_label))
        self.wait(0.5)
        self.play(Write(v_calc))
        self.wait(1.5)

        # Show example with distance 4
        dist4_label = MathTex("Distance 4", font_size=30).to_edge(UP)
        self.play(Transform(title, dist4_label))
        self.wait(0.5)

        # Point B (4,0) -> |4| + 2×|0| = 4
        b_point = Dot([4, 0, 0], color=ORANGE)
        b_label = MathTex("(4,0)", font_size=24).next_to(b_point, DOWN)
        b_calc = MathTex("4 + 0 = 4", font_size=24).to_edge(DOWN)
        self.play(FadeIn(b_point), Write(b_label))
        self.wait(0.5)
        self.play(Write(b_calc))
        self.wait(1.5)

        # Point A (2,1) -> |2| + 2×|1| = 4
        a_point = Dot([2, 1, 0], color=PINK)
        a_label = MathTex("(2,1)", font_size=24).next_to(a_point, UP)
        a_calc = MathTex("2 + 2 = 4", font_size=24).to_edge(DOWN)
        self.play(FadeIn(a_point), Write(a_label))
        self.wait(0.5)
        self.play(Write(a_calc))
        self.wait(1.5)

        # Show general rule
        rule_text = Text("Any point where horizontal distance equals target cost", font_size=24).to_edge(DOWN)
        self.play(Write(rule_text))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(center), FadeOut(c_label),
            FadeOut(p1), FadeOut(p1_label), FadeOut(calc1),
            FadeOut(p2), FadeOut(p2_label), FadeOut(calc2),
            FadeOut(p3), FadeOut(p3_label), FadeOut(calc3),
            FadeOut(p4), FadeOut(p4_label), FadeOut(calc4),
            FadeOut(p5), FadeOut(p5_label), FadeOut(cost5),
            FadeOut(segment1), FadeOut(seg1_label),
            FadeOut(segment2), FadeOut(seg2_label),
            FadeOut(segment3), FadeOut(seg3_label),
            FadeOut(total_cost),
            FadeOut(grid),
            FadeOut(h_point), FadeOut(h_label), FadeOut(h_calc),
            FadeOut(v_point), FadeOut(v_label), FadeOut(v_calc),
            FadeOut(b_point), FadeOut(b_label), FadeOut(b_calc),
            FadeOut(a_point), FadeOut(a_label), FadeOut(a_calc),
            FadeOut(rule_text)
        )
        self.wait(0.5)
