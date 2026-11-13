from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Grid Point Validity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial point (x, y)
        x, y = 3, 5
        point = Dot([x, y], color=YELLOW)
        label = MathTex(f"({x}, {y})", font_size=24).next_to(point, UR)
        self.play(FadeIn(point), Write(label))
        self.wait(1)

        # Krell step: (x, y) -> (y, x+1)
        new_x, new_y = y, x + 1
        new_point = Dot([new_x, new_y], color=GREEN)
        new_label = MathTex(f"({new_x}, {new_y})", font_size=24).next_to(new_point, UR)

        # Show transformation
        self.play(
            point.animate.move_to([new_x, new_y]),
            label.animate.move_to([new_x, new_y]).shift(UR * 0.3),
            run_time=1
        )
        self.wait(0.5)

        # Fade out old point and label
        self.play(FadeOut(point), FadeOut(label))

        # Show new point and label
        self.play(FadeIn(new_point), Write(new_label))
        self.wait(1)

        # Grid lines
        grid = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            axis_config={"stroke_color": GREY},
            background_line_style={"stroke_color": GREY}
        )
        self.play(Create(grid))
        self.wait(0.5)

        # Snap to grid intersection
        self.play(
            new_point.animate.move_to([new_x, new_y]),
            run_time=0.5
        )
        self.wait(1)

        # Checkmark and text
        check = Tex("✓", font_size=40).set_color(GREEN).next_to(new_label, RIGHT)
        validity_text = Text("Always lands on a grid point", font_size=24).next_to(check, RIGHT)
        self.play(Write(check), Write(validity_text))
        self.wait(1.5)

        # Narration words
        narration = Text("Because we start with integers", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        narration2 = Text("and only perform swapping and addition", font_size=24).to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(1.5)
        self.play(FadeOut(narration2))

        narration3 = Text("every Krell step always lands exactly on another valid grid point.", font_size=24).to_edge(DOWN)
        self.play(Write(narration3))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(grid), FadeOut(new_point), FadeOut(new_label), FadeOut(check), FadeOut(validity_text), FadeOut(narration3))
