from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Grid Point Validity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY}
        )
        self.play(Create(grid))
        self.wait(0.5)

        # Initial point (4, 6)
        x, y = 4, 6
        start_point = Dot(color=YELLOW).move_to(grid.c2p(x, y))
        label_start = MathTex(f"({x}, {y})", font_size=24).next_to(start_point, UR)
        start_point.shift(0.0 * RIGHT + -2.23 * UP)  # layout: separation vector
        self.play(FadeIn(start_point), Write(label_start))
        self.wait(0.5)

        # Arrow for Step 1
        arrow = Arrow(start_point.get_center(), grid.c2p(y, x + 1), color=RED, buff=0.1)
        step_label = MathTex("Step\ 1", font_size=24).next_to(arrow, UP)
        self.play(GrowArrow(arrow), Write(step_label))
        self.wait(0.5)

        # Final point (6, 7)
        end_x, end_y = y, x + 1
        end_point = Dot(color=YELLOW).move_to(grid.c2p(end_x, end_y))
        label_end = MathTex(f"({end_x}, {end_y})", font_size=24).next_to(end_point, UR)
        self.play(FadeIn(end_point), Write(label_end))
        self.wait(0.5)

        # Narration text
        narration = Text("The first step takes us from (4, 6) to (6, 7)", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)

        # Fade out narration and labels
        self.play(FadeOut(narration, label_start, label_end, step_label, arrow))

        # Show general rule: Krell step always lands on grid point
        rule_text = Text("Because we start with integers and only perform swapping and addition,", font_size=24)
        rule_text2 = Text("every Krell step always lands exactly on another valid grid point.", font_size=24)
        rule_text.to_edge(DOWN).shift(UP * 0.5)
        rule_text2.next_to(rule_text, DOWN)
        self.play(Write(rule_text))
        self.wait(1.0)
        self.play(Write(rule_text2))
        self.wait(1.5)

        # Checkmark
        check = Tex(r"$\checkmark$").scale(2).set_color(GREEN).next_to(rule_text2, LEFT)
        self.play(Write(check))
        self.wait(1.0)

        # Fade out everything
        self.play(FadeOut(title, grid, start_point, end_point, check, rule_text, rule_text2))
        self.wait(0.5)
