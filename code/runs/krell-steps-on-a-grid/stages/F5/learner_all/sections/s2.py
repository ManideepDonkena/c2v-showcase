from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Grid Point Validity", font_size=36).to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # Grid
        grid = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-3.9, 3.9, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY}
        )
        grid.scale(0.8)
        self.play(Create(grid))
        self.wait(0.5)

        # Initial point (x, y)
        x, y = 2, 1
        point = Dot(color=YELLOW)
        point.move_to(grid.c2p(x, y))
        label_x = MathTex("x", font_size=24).next_to(point, DOWN, buff=0.1)
        label_y = MathTex("y", font_size=24).next_to(point, RIGHT, buff=0.1)
        point_group = VGroup(point, label_x, label_y)

        self.play(FadeIn(point_group))
        self.wait(0.5)

        # Show (x, y) text
        xy_text = MathTex("(x, y)", font_size=24).next_to(point, UP, buff=0.3)
        self.play(Write(xy_text))
        self.wait(0.5)

        # Krell step: swap and add 1
        new_x, new_y = y, x + 1
        new_point = Dot(color=RED)
        new_point.move_to(grid.c2p(new_x, new_y))

        # Show transformation
        arrow = Arrow(start=point.get_center(), end=new_point.get_center(), buff=0.1, color=BLUE)
        arrow.shift(-0.37 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow))
        self.wait(0.5)

        # Show (y, x+1) label
        yx1_text = MathTex("(y, x + 1)", font_size=24).next_to(new_point, UP, buff=0.3)
        self.play(Write(yx1_text))
        self.wait(0.5)

        # Fade out old labels and point
        self.play(FadeOut(xy_text, yx1_text, arrow))

        # Show new point with labels
        label_new_x = MathTex("y", font_size=24).next_to(new_point, DOWN, buff=0.1)
        label_new_y = MathTex("x + 1", font_size=24).next_to(new_point, RIGHT, buff=0.1)
        new_point_group = VGroup(new_point, label_new_x, label_new_y)

        self.play(FadeIn(new_point_group))
        self.wait(0.5)
        # Checkmark
        check = Text("✓", font_size=40).set_color(GREEN).next_to(yx1_text, RIGHT, buff=0.3)
        self.play(Write(check))
        self.wait(0.5)

        # Narration text
        narration = Text("Because we start with integers and only perform swapping and addition, every Krell step always lands exactly on another valid grid point.", font_size=24)
        narration.to_edge(DOWN, buff=0.3)
        self.play(Write(narration))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title, grid, point_group, new_point_group, check, narration),
            run_time=1
        )
        self.wait(0.5)

        # NEW: Show (4, 6) and arrow to (6, 7)
        x2, y2 = 4, 6
        point2 = Dot(color=YELLOW)
        point2.move_to(grid.c2p(x2, y2))
        label_x2 = MathTex("x", font_size=24).next_to(point2, DOWN, buff=0.1)
        label_y2 = MathTex("y", font_size=24).next_to(point2, RIGHT, buff=0.1)
        point_group2 = VGroup(point2, label_x2, label_y2)

        self.play(FadeIn(point_group2))
        self.wait(0.5)

        # Show (4, 6) text
        xy_text2 = MathTex("(4, 6)", font_size=24).next_to(point2, UP, buff=0.3)
        self.play(Write(xy_text2))
        self.wait(0.5)

        # New point (6, 7)
        new_x2, new_y2 = 6, 7
        new_point2 = Dot(color=RED)
        new_point2.move_to(grid.c2p(new_x2, new_y2))

        # Arrow from (4, 6) to (6, 7)
        arrow2 = Arrow(start=point2.get_center(), end=new_point2.get_center(), buff=0.1, color=BLUE)
        arrow2.shift(-0.37 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow2))
        self.wait(0.5)

        # Label 'Step 1'
        step_label = MathTex("Step\ 1", font_size=24).next_to(arrow2, UP, buff=0.2)
        self.play(Write(step_label))
        self.wait(0.5)

        # Show final point (6, 7) label
        final_label = MathTex("(6, 7)", font_size=24).next_to(new_point2, UP, buff=0.3)
        self.play(Write(final_label))
        self.wait(0.5)

        # Narration for step
        narration2 = Text("The first step takes us from (4, 6) to (6, 7)", font_size=24)
        narration2.to_edge(DOWN, buff=0.3)
        self.play(Write(narration2))
        self.wait(1.5)

        # Fade out
        self.play(
            FadeOut(point_group2, xy_text2, arrow2, step_label, final_label, narration2),
            run_time=1
        )
        self.wait(0.5)
