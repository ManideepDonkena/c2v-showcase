from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Staircase Path from Origin", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(x_range=[-1, 4], y_range=[-1, 4], 
                           axis_config={"stroke_color": GREY, "stroke_width": 1})
        grid.set_opacity(0.5)
        self.play(Create(grid))
        self.wait(0.5)

        # Start point
        start_point = Dot(color=RED).move_to(grid.c2p(0, 0))
        origin_label = MathTex("(0, 0)", font_size=24).next_to(start_point, DOWN)
        self.play(FadeIn(start_point), Write(origin_label))
        self.wait(1)

        # First step: (0,0) -> (0,1)
        step1 = Dot(color=GREEN).move_to(grid.c2p(0, 1))
        label1 = MathTex("(0, 1)", font_size=24).next_to(step1, UP)
        line1 = Line(start_point.get_center(), step1.get_center(), color=BLUE)
        self.play(Create(line1), FadeIn(step1), Write(label1))
        self.wait(1.5)

        # Narration: one step
        narration1 = Text("After 1 step", font_size=24).next_to(label1, UP)
        self.play(Write(narration1))
        self.wait(1)
        self.play(FadeOut(narration1))

        # Second step: (0,1) -> (1,1)
        step2 = Dot(color=GREEN).move_to(grid.c2p(1, 1))
        label2 = MathTex("(1, 1)", font_size=24).next_to(step2, UP)
        line2 = Line(step1.get_center(), step2.get_center(), color=BLUE)
        self.play(Create(line2), FadeIn(step2), Write(label2))
        self.wait(1.5)

        # Third step: (1,1) -> (1,2)
        step3 = Dot(color=GREEN).move_to(grid.c2p(1, 2))
        label3 = MathTex("(1, 2)", font_size=24).next_to(step3, UP)
        line3 = Line(step2.get_center(), step3.get_center(), color=BLUE)
        self.play(Create(line3), FadeIn(step3), Write(label3))
        self.wait(1.5)

        # Fourth step: (1,2) -> (2,2)
        step4 = Dot(color=GREEN).move_to(grid.c2p(2, 2))
        label4 = MathTex("(2, 2)", font_size=24).next_to(step4, UP)
        line4 = Line(step3.get_center(), step4.get_center(), color=BLUE)
        self.play(Create(line4), FadeIn(step4), Write(label4))
        self.wait(1.5)

        # Show the rule: swap and add 1 to second
        rule = MathTex("Krell\\;step:\\;(x, y) \\to (y, x + 1)", font_size=30).to_edge(UP)
        self.play(Transform(title, rule))
        self.wait(1.5)

        # Arrow from (2,2) to next point
        arrow = Arrow(step4.get_center(), grid.c2p(2, 3), color=YELLOW, buff=0.1)
        step_label = MathTex("Step\\;3", font_size=24).next_to(arrow, RIGHT)
        arrow.shift(0.5 * RIGHT + 0.0 * UP)  # layout: separation vector
        step_label.shift(0.4 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(arrow), Write(step_label))
        self.wait(1.5)

        # Show (2,2) -> (2,3)
        next_point = Dot(color=ORANGE).move_to(grid.c2p(2, 3))
        label_next = MathTex("(2, 3)", font_size=24).next_to(next_point, UP)
        self.play(FadeIn(next_point), Write(label_next))
        self.wait(1.5)

        # Show change in x vs y
        change_x = MathTex("\\Delta x = 0", font_size=24).to_corner(DL)
        change_y = MathTex("\\Delta y = +1", font_size=24).next_to(change_x, DOWN)
        self.play(Write(change_x), Write(change_y))
        self.wait(2)

        # Continue path: (2,2) -> (2,3) -> (3,3)
        line5 = Line(step4.get_center(), next_point.get_center(), color=BLUE)
        self.play(Create(line5))

        # Apply rule again to (2,3): swap to (3,2), add 1 to second → (3,3)
        step5 = Dot(color=ORANGE).move_to(grid.c2p(3, 3))
        label5 = MathTex("(3, 3)", font_size=24).next_to(step5, UP)
        arrow2 = Arrow(next_point.get_center(), step5.get_center(), color=YELLOW, buff=0.1)
        step_label2 = MathTex("Step\\;4", font_size=24).next_to(arrow2, RIGHT)
        self.play(Create(arrow2), Write(step_label2))
        self.wait(1.5)

        # Show final path
        line6 = Line(next_point.get_center(), step5.get_center(), color=BLUE)
        self.play(Create(line6), FadeIn(step5), Write(label5))
        self.wait(1.5)

        # Final fade out
        self.play(FadeOut(title, grid, start_point, origin_label, step1, label1, line1,
                          step2, label2, line2, step3, label3, line3, step4, label4, line4,
                          arrow, step_label, next_point, label_next, change_x, change_y,
                          arrow2, step_label2, step5, label5, line5, line6))
        self.wait(0.5)
