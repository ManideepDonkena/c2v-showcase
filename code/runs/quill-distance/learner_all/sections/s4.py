from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Worked Example Calculation", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Points P(0,0) and Q(3,2)
        P = Dot([0, 0, 0], color=BLUE)
        Q = Dot([3, 2, 0], color=RED)
        p_label = MathTex("(0,0)", font_size=24).next_to(P, DOWN)
        q_label = MathTex("(3,2)", font_size=24).next_to(Q, UP)

        self.play(FadeIn(P), FadeIn(Q), Write(p_label), Write(q_label))
        self.wait(1)

        # Stepped path: 3 horizontal + 2 vertical
        path = VGroup()
        start = P.get_center()
        for i in range(3):
            segment = Line(start, [start[0]+1, start[1], 0], color=YELLOW)
            path.add(segment)
            start = segment.get_end()

        for i in range(2):
            segment = Line(start, [start[0], start[1]+1, 0], color=YELLOW)
            path.add(segment)
            start = segment.get_end()

        self.play(Create(path))
        self.wait(1)

        # Labels on segments
        h_labels = VGroup()
        for i in range(3):
            label = MathTex("1", font_size=24).move_to([i+0.5, -0.3, 0])
            h_labels.add(label)
        v_labels = VGroup()
        for i in range(2):
            label = MathTex("2", font_size=24).move_to([3.3, i+0.5, 0])
            v_labels.add(label)

        self.play(Write(h_labels), Write(v_labels))
        self.wait(1)

        # Final equation
        eq = MathTex("3 + 4 = 7", font_size=32).to_edge(DOWN)
        self.play(Write(eq))
        self.wait(1.5)

        # Clear screen
        self.play(FadeOut(title), FadeOut(P), FadeOut(Q), FadeOut(p_label), FadeOut(q_label),
                  FadeOut(path), FadeOut(h_labels), FadeOut(v_labels), FadeOut(eq))

        # Show vertical path from (1,1) to (1,4)
        p1 = Dot([1, 1, 0], color=GREEN)
        p2 = Dot([1, 4, 0], color=GREEN)
        p1_label = MathTex("(1,1)", font_size=24).next_to(p1, DOWN)
        p2_label = MathTex("(1,4)", font_size=24).next_to(p2, UP)

        p2.shift(0.0 * RIGHT + -0.23 * UP)  # layout: separation vector
        self.play(FadeIn(p1), FadeIn(p2), Write(p1_label), Write(p2_label))
        self.wait(0.5)

        v_path = VGroup()
        start = p1.get_center()
        for i in range(3):
            segment = Line(start, [start[0], start[1]+1, 0], color=ORANGE)
            v_path.add(segment)
            start = segment.get_end()

        self.play(Create(v_path))
        self.wait(0.5)

        cost_labels = VGroup()
        for i in range(3):
            label = MathTex("Cost: 2", font_size=24).move_to([1.3, i+1.5, 0])
            cost_labels.add(label)

        self.play(Write(cost_labels))
        self.wait(1.5)

        total_cost = MathTex("Total Cost = 6", font_size=28).to_edge(DOWN)
        self.play(Write(total_cost))
        self.wait(1.5)

        # Clear screen
        self.play(FadeOut(p1), FadeOut(p2), FadeOut(p1_label), FadeOut(p2_label),
                  FadeOut(v_path), FadeOut(cost_labels), FadeOut(total_cost))

        # Show Manhattan grid with Quill overlay
        grid = NumberPlane(x_range=[-4, 4], y_range=[-2, 2], axis_config={"stroke_width": 1})
        self.play(Create(grid))
        self.wait(0.5)

        # Overlay Quill path from (0,0) to (3,2)
        q_path = VGroup()
        start = [0, 0, 0]
        for i in range(3):
            segment = Line(start, [start[0]+1, start[1], 0], color=PURPLE)
            q_path.add(segment)
            start = segment.get_end()
        for i in range(2):
            segment = Line(start, [start[0], start[1]+1, 0], color=PURPLE)
            q_path.add(segment)
            start = segment.get_end()

        self.play(Create(q_path))
        self.wait(1.5)

        # Explanation text
        explanation = Text("Quill distance stretches vertical axis", font_size=24).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(1.5)

        # Clear screen
        self.play(FadeOut(grid), FadeOut(q_path), FadeOut(explanation))

        # Show horizontal movement only: (0,0) to (3,0)
        h_start = Dot([0, 0, 0], color=BLUE)
        h_end = Dot([3, 0, 0], color=RED)
        h_start_label = MathTex("(0,0)", font_size=24).next_to(h_start, DOWN)
        h_end_label = MathTex("(3,0)", font_size=24).next_to(h_end, UP)

        self.play(FadeIn(h_start), FadeIn(h_end), Write(h_start_label), Write(h_end_label))
        self.wait(0.5)

        h_path = VGroup()
        start = h_start.get_center()
        for i in range(3):
            segment = Line(start, [start[0]+1, start[1], 0], color=YELLOW)
            h_path.add(segment)
            start = segment.get_end()

        self.play(Create(h_path))
        self.wait(0.5)

        calc_text = MathTex("|3 - 0| + 2 \\times |0 - 0| = 3 + 0 = 3", font_size=28).to_edge(DOWN)
        self.play(Write(calc_text))
        self.wait(1.5)

        # Clear screen
        self.play(FadeOut(h_start), FadeOut(h_end), FadeOut(h_start_label), FadeOut(h_end_label),
                  FadeOut(h_path), FadeOut(calc_text))

        # Show points at distance 4: (4,0) and (2,1)
        center = Dot([0, 0, 0], color=WHITE)
        center_label = MathTex("(0,0)", font_size=24).next_to(center, DOWN)

        self.play(FadeIn(center), Write(center_label))
        self.wait(0.5)

        # Point B (4,0)
        b_point = Dot([4, 0, 0], color=GREEN)
        b_label = MathTex("(4,0)", font_size=24).next_to(b_point, DOWN)
        self.play(FadeIn(b_point), Write(b_label))
        self.wait(0.5)

        calc_b = MathTex("|4| + 2 \\times |0| = 4 + 0 = 4", font_size=28).to_edge(DOWN)
        self.play(Write(calc_b))
        self.wait(1.5)

        # Point A (2,1)
        a_point = Dot([2, 1, 0], color=ORANGE)
        a_label = MathTex("(2,1)", font_size=24).next_to(a_point, UP)
        self.play(FadeIn(a_point), Write(a_label))
        self.wait(0.5)

        calc_a = MathTex("|2| + 2 \\times |1| = 2 + 2 = 4", font_size=28).to_edge(DOWN)
        self.play(Transform(calc_b, calc_a))
        self.wait(1.5)

        # Final explanation
        final_text = Text("Both A and B have distance 4", font_size=24).to_edge(DOWN)
        self.play(Transform(calc_b, final_text))
        self.wait(1.5)

        # Show generalization: horizontal vs vertical displacement
        gen_text = Text("Horizontal: cost = steps\nVertical: cost = 2 × steps", font_size=24).to_edge(DOWN)
        self.play(Transform(calc_b, gen_text))
        self.wait(1.5)

        self.play(FadeOut(center), FadeOut(center_label), FadeOut(b_point), FadeOut(b_label),
                  FadeOut(a_point), FadeOut(a_label), FadeOut(calc_b))
