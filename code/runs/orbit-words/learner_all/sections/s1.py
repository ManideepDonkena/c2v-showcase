from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Origin and the Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial X
        x_large = Tex("X", font_size=120).move_to(ORIGIN)
        self.play(FadeIn(x_large))
        self.wait(1)

        # Arrows and rules
        blue_arrow = Arrow(start=LEFT, end=RIGHT, color=BLUE).shift(UP * 0.5)
        green_arrow = Arrow(start=LEFT, end=RIGHT, color=GREEN).shift(DOWN * 0.5)
        x_rule = Tex("X $\\rightarrow$ XYY", font_size=32).next_to(blue_arrow, UP)
        y_rule = Tex("Y $\\rightarrow$ YX", font_size=32).next_to(green_arrow, DOWN)

        blue_arrow.shift(0.0 * RIGHT + 0.25 * UP)  # layout: separation vector
        self.play(
            GrowArrow(blue_arrow),
            Write(x_rule),
            run_time=1
        )
        self.wait(0.5)

        green_arrow.shift(0.0 * RIGHT + -0.25 * UP)  # layout: separation vector
        self.play(
            GrowArrow(green_arrow),
            Write(y_rule),
            run_time=1
        )
        self.wait(1)

        # Simultaneous Rewrite pulse
        simultaneous = Text("Simultaneous Rewrite", font_size=36).move_to(UP * 2)
        self.play(FadeIn(simultaneous))
        self.play(simultaneous.animate.scale(1.2), run_time=0.5)
        self.play(FadeOut(simultaneous))
        self.wait(0.5)

        # Expansion comparison: X → XYY and Y → YX
        x_in = Tex("X", font_size=40).shift(LEFT * 3 + UP * 1.5)
        x_out = Tex("XYY", font_size=40).shift(RIGHT * 3 + UP * 1.5)
        y_in = Tex("Y", font_size=40).shift(LEFT * 3 + DOWN * 1.5)
        y_out = Tex("YX", font_size=40).shift(RIGHT * 3 + DOWN * 1.5)

        self.play(
            Write(x_in),
            Write(x_out),
            Write(y_in),
            Write(y_out),
            run_time=1
        )
        self.wait(1)

        # Cross out Y
        cross = Cross(y_in)
        self.play(Create(cross))
        self.wait(0.5)

        # Say "The process never begins with Y"
        not_y = Text("The process never begins with Y", font_size=24).to_edge(DOWN)
        self.play(Write(not_y))
        self.wait(1)
        self.play(FadeOut(not_y))

        # Show that starting from Y is invalid
        y_start = Tex("Y", font_size=40).shift(LEFT * 3 + DOWN * 1.5)
        y_start.shift(0.0 * RIGHT + 0.43 * UP)  # layout: separation vector
        self.play(Write(y_start))
        self.wait(0.5)
        self.play(FadeOut(y_start), FadeOut(cross))

        # Show first letter comparison
        xyy = Tex("XYY", font_size=40).shift(UP * 0.5)
        arrow_first = Arrow(start=LEFT * 2, end=RIGHT * 2, color=YELLOW).shift(UP * 0.5)
        self.play(
            Write(xyy),
            GrowArrow(arrow_first),
            run_time=1
        )
        self.wait(1)

        # Show transformation of first letter in XYYYXYX
        word = Tex("XYYYXYX", font_size=40).shift(DOWN * 1.5)
        self.play(Write(word))
        self.wait(0.5)

        xyy_block = Tex("XYY", font_size=40).shift(DOWN * 2.5)
        arrow_x = Arrow(start=LEFT * 3, end=RIGHT * 3, color=RED).shift(DOWN * 2.5)
        self.play(
            Write(xyy_block),
            GrowArrow(arrow_x),
            run_time=1
        )
        self.wait(1)

        # Show that Y appears from first step
        step0 = Tex("Step 0: X", font_size=32).shift(UP * 2)
        step1 = Tex("Step 1: XYY", font_size=32).shift(UP * 1)
        self.play(Write(step0))
        self.wait(0.5)
        self.play(Write(step1))
        self.wait(1)

        # Final cleanup
        self.play(
            FadeOut(x_large),
            FadeOut(blue_arrow),
            FadeOut(green_arrow),
            FadeOut(x_rule),
            FadeOut(y_rule),
            FadeOut(x_in),
            FadeOut(x_out),
            FadeOut(y_in),
            FadeOut(y_out),
            FadeOut(xyy),
            FadeOut(arrow_first),
            FadeOut(word),
            FadeOut(xyy_block),
            FadeOut(arrow_x),
            FadeOut(step0),
            FadeOut(step1),
            FadeOut(title)
        )
        self.wait(0.5)
