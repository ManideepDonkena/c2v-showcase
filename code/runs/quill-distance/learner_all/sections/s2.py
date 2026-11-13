from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Symmetry and Direction", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Points A and B
        A = Dot([0, 0, 0], color=BLUE)
        B = Dot([2, 1, 0], color=RED)
        A_label = MathTex("A", font_size=24).next_to(A, DOWN)
        B_label = MathTex("B", font_size=24).next_to(B, UP)

        self.play(FadeIn(A), FadeIn(B), Write(A_label), Write(B_label))
        self.wait(0.5)

        # Path from A to B
        path1 = Line(A.get_center(), [2, 0, 0], color=YELLOW)
        path2 = Line([2, 0, 0], B.get_center(), color=YELLOW)
        cost1 = MathTex("2", font_size=24).next_to(path1, DOWN)
        cost2 = MathTex("2", font_size=24).next_to(path2, RIGHT)

        self.play(Create(path1), Write(cost1))
        self.wait(0.5)
        self.play(Create(path2), Write(cost2))
        self.wait(0.5)

        # Total cost
        total_cost = MathTex("2 + 2 = 4", font_size=30).next_to(B, RIGHT)
        self.play(Write(total_cost))
        self.wait(1)

        # Reverse path from B to A
        path3 = Line(B.get_center(), [2, 0, 0], color=GREEN)
        path4 = Line([2, 0, 0], A.get_center(), color=GREEN)
        cost3 = MathTex("2", font_size=24).next_to(path3, UP)
        cost4 = MathTex("2", font_size=24).next_to(path4, LEFT)

        # Adjust positions to avoid overlap
        cost3.shift(0.0 * RIGHT + 0.23 * UP)  # layout: separation vector
        self.play(Create(path3), Write(cost3))
        self.wait(0.5)
        self.play(Create(path4), Write(cost4))
        self.wait(0.5)

        total_cost_rev = MathTex("2 + 2 = 4", font_size=30).next_to(A, LEFT)
        self.play(Write(total_cost_rev))
        self.wait(1)

        # Symmetry statement
        symmetry = MathTex(r"d(A,B) = d(B,A)", font_size=36).to_edge(UP)
        self.play(Transform(title, symmetry))
        self.wait(1.5)

        # Vertical path (1,1) to (1,4)
        self.play(FadeOut(path1), FadeOut(path2), FadeOut(path3), FadeOut(path4),
                  FadeOut(cost1), FadeOut(cost2), FadeOut(cost3), FadeOut(cost4),
                  FadeOut(total_cost), FadeOut(total_cost_rev))

        v_start = Dot([1, 1, 0], color=ORANGE)
        v_end = Dot([1, 4, 0], color=ORANGE)
        v_label = MathTex("A", font_size=24).next_to(v_start, DOWN)
        v_label2 = MathTex("B", font_size=24).next_to(v_end, UP)

        # Adjust positions to avoid overlap
        v_end.shift(0.0 * RIGHT + -0.25 * UP)  # layout: separation vector
        v_label2.shift(0.0 * RIGHT + -0.65 * UP)  # layout: separation vector

        self.play(FadeIn(v_start), FadeIn(v_end), Write(v_label), Write(v_label2))
        self.wait(0.5)

        seg1 = Line([1, 1, 0], [1, 2, 0], color=GREEN)
        seg2 = Line([1, 2, 0], [1, 3, 0], color=GREEN)
        seg3 = Line([1, 3, 0], [1, 4, 0], color=GREEN)

        cost_label1 = MathTex("Cost: 2", font_size=24).next_to(seg1, LEFT)
        cost_label2 = MathTex("Cost: 2", font_size=24).next_to(seg2, LEFT)
        cost_label3 = MathTex("Cost: 2", font_size=24).next_to(seg3, LEFT)

        # Adjust positions to avoid overlap
        cost_label3.shift(0.0 * RIGHT + 0.25 * UP)  # layout: separation vector

        self.play(Create(seg1), Write(cost_label1))
        self.wait(0.5)
        self.play(Create(seg2), Write(cost_label2))
        self.wait(0.5)
        self.play(Create(seg3), Write(cost_label3))
        self.wait(0.5)

        total_vertical = MathTex("2 + 2 + 2 = 6", font_size=30).next_to(v_end, RIGHT)
        # Adjust position to avoid overlap
        total_vertical.shift(0.0 * RIGHT + -0.27 * UP)  # layout: separation vector
        self.play(Write(total_vertical))
        self.wait(1.5)

        # Manhattan grid overlay
        self.play(FadeOut(seg1), FadeOut(seg2), FadeOut(seg3),
                  FadeOut(cost_label1), FadeOut(cost_label2), FadeOut(cost_label3),
                  FadeOut(total_vertical), FadeOut(v_start), FadeOut(v_end),
                  FadeOut(v_label), FadeOut(v_label2))

        grid = NumberPlane(x_range=[-7, 7], y_range=[-4, 4], faded_line_ratio=1)
        self.play(Create(grid))
        self.wait(0.5)

        # Quill path on Manhattan grid
        q_start = Dot([0, 0, 0], color=PURPLE)
        q_end = Dot([3, 0, 0], color=PURPLE)
        q_label1 = MathTex("A", font_size=24).next_to(q_start, DOWN)
        q_label2 = MathTex("B", font_size=24).next_to(q_end, DOWN)

        # Adjust positions to avoid overlap
        q_label1.shift(0.32 * RIGHT + 0.0 * UP)  # layout: separation vector
        q_label2.shift(0.32 * RIGHT + 0.0 * UP)  # layout: separation vector

        self.play(FadeIn(q_start), FadeIn(q_end), Write(q_label1), Write(q_label2))
        self.wait(0.5)

        h_path = Line([0, 0, 0], [3, 0, 0], color=RED)
        cost_h = MathTex("3", font_size=24).next_to(h_path, DOWN)
        self.play(Create(h_path), Write(cost_h))
        self.wait(1)

        # Horizontal only
        calc_text = MathTex(r"|3 - 0| + 2 \cdot |0 - 0| = 3 + 0 = 3", font_size=24).to_edge(DOWN)
        self.play(Write(calc_text))
        self.wait(1.5)

        # Show point at distance 4
        self.play(FadeOut(h_path), FadeOut(cost_h), FadeOut(calc_text),
                  FadeOut(q_start), FadeOut(q_end), FadeOut(q_label1), FadeOut(q_label2))

        center = Dot([0, 0, 0], color=BLUE)
        center_label = MathTex("C", font_size=24).next_to(center, DOWN)
        self.play(FadeIn(center), Write(center_label))
        self.wait(0.5)

        # Option B (4,0)
        b_point = Dot([4, 0, 0], color=GREEN)
        b_label = MathTex("B", font_size=24).next_to(b_point, DOWN)
        self.play(FadeIn(b_point), Write(b_label))
        self.wait(0.5)

        calc_b = MathTex(r"|4| + 2 \cdot |0| = 4 + 0 = 4", font_size=24).to_edge(DOWN)
        self.play(Write(calc_b))
        self.wait(1.5)

        # Option A (2,1)
        a_point = Dot([2, 1, 0], color=YELLOW)
        a_label = MathTex("A", font_size=24).next_to(a_point, UP)
        # Adjust position to avoid overlap
        a_label.shift(0.0 * RIGHT + 0.32 * UP)  # layout: separation vector

        self.play(FadeIn(a_point), Write(a_label))
        self.wait(0.5)

        calc_a = MathTex(r"|2| + 2 \cdot |1| = 2 + 2 = 4", font_size=24).to_edge(DOWN)
        self.play(Transform(calc_b, calc_a))
        self.wait(1.5)

        # Generalize idea
        self.play(FadeOut(a_point), FadeOut(b_point), FadeOut(center),
                  FadeOut(a_label), FadeOut(b_label), FadeOut(center_label),
                  FadeOut(calc_a), FadeOut(calc_b))

        general = MathTex(r"\text{Any point where } h = d \text{ or } v = d/2", font_size=30).to_edge(UP)
        # Adjust position to avoid overlap
        general.shift(0.0 * RIGHT + 0.46 * UP)  # layout: separation vector
        self.play(Write(general))
        self.wait(1.5)

        # Final summary
        final_text = Text("Quill distance is symmetric.", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(general), FadeOut(final_text), FadeOut(grid))
