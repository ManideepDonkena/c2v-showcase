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
