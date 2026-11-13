from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Length Paradox", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial curve and length labels
        curve1 = Line(LEFT, RIGHT, color=BLUE).scale(0.5)
        label1 = MathTex("3").next_to(curve1, DOWN, buff=0.2)
        self.play(Create(curve1), Write(label1))
        self.wait(0.5)

        # Iteration 2
        curve2 = VGroup(
            Line(LEFT, UP, color=BLUE).scale(0.25),
            Line(UP, RIGHT, color=BLUE).scale(0.25),
            Line(RIGHT, DOWN, color=BLUE).scale(0.25),
            Line(DOWN, LEFT, color=BLUE).scale(0.25)
        ).arrange_in_grid(rows=2, cols=2, buff=0.1)
        label2 = MathTex("9").next_to(curve2, DOWN, buff=0.2)
        self.play(Transform(curve1, curve2), Transform(label1, label2))
        self.wait(0.5)

        # Iteration 3
        curve3 = VGroup(
            Line(LEFT, UP, color=BLUE).scale(0.125),
            Line(UP, RIGHT, color=BLUE).scale(0.125),
            Line(RIGHT, DOWN, color=BLUE).scale(0.125),
            Line(DOWN, LEFT, color=BLUE).scale(0.125),
            Line(LEFT, UP, color=BLUE).scale(0.125),
            Line(UP, RIGHT, color=BLUE).scale(0.125),
            Line(RIGHT, DOWN, color=BLUE).scale(0.125),
            Line(DOWN, LEFT, color=BLUE).scale(0.125)
        ).arrange_in_grid(rows=2, cols=4, buff=0.05)
        label3 = MathTex("27").next_to(curve3, DOWN, buff=0.2)
        self.play(Transform(curve1, curve3), Transform(label1, label3))
        self.wait(0.5)

        # Show increasing length
        counter = ValueTracker(3)
        length_text = always_redraw(
            lambda: MathTex(f"Length: {int(counter.get_value())}").to_corner(UL)
        )
        self.add(length_text)
        self.play(counter.animate.set_value(81), run_time=2)
        self.wait(0.5)

        # Paradox text
        paradox = Text("Paradox: Infinite length in finite space", font_size=24).to_edge(DOWN)
        self.play(Write(paradox))
        self.wait(1)

        # Show two points mapping to same location
        dot_a = Dot(color=YELLOW).move_to(LEFT * 0.5)
        dot_b = Dot(color=GREEN).move_to(RIGHT * 0.5)
        label_a = MathTex("a").next_to(dot_a, DOWN)
        label_b = MathTex("b").next_to(dot_b, DOWN)
        square = Square(side_length=1, color=WHITE).move_to(ORIGIN)
        f_a = Dot(color=YELLOW).move_to(square.get_center())
        f_b = Dot(color=GREEN).move_to(square.get_center())
        f_label = MathTex("f(a) = f(b)").next_to(square, UP)

        square.shift(0.0 * RIGHT + 0.3 * UP)  # layout: separation vector
        self.play(
            Create(square),
            FadeIn(dot_a, dot_b),
            Write(label_a),
            Write(label_b),
            FadeIn(f_a, f_b),
            Write(f_label)
        )
        self.wait(1.5)

        # Show that curve must overlap
        self.play(FadeOut(f_label))
        self.play(
            Transform(dot_a, f_a),
            Transform(dot_b, f_b),
            run_time=1
        )
        self.wait(0.5)

        # Show adjacent points in square with distant pre-images
        point1 = Dot(color=RED).move_to(square.get_corner(UL))
        point2 = Dot(color=BLUE).move_to(square.get_corner(UR))
        line1 = Line(point1, point2, color=GRAY)
        self.play(Create(line1), FadeIn(point1, point2))
        self.wait(0.5)

        # Show inverse mapping
        pre1 = Dot(color=RED).move_to(LEFT * 0.3)
        pre2 = Dot(color=BLUE).move_to(RIGHT * 0.7)
        line2 = Line(pre1, pre2, color=GRAY)
        self.play(Create(line2), FadeIn(pre1, pre2))
        self.wait(1)

        # Show unit interval vs square
        interval = Line(LEFT, RIGHT, color=WHITE).scale(0.5)
        interval_label = MathTex("1").next_to(interval, DOWN)
        square_area = Square(side_length=1, color=WHITE).move_to(RIGHT * 2)
        area_label = MathTex("1").next_to(square_area, DOWN)

        self.play(
            Transform(curve1, interval),
            Transform(label1, interval_label),
            FadeIn(square_area, area_label)
        )
        self.wait(0.5)

        # Hilbert curve scaling
        hilbert = VGroup(
            Line(LEFT, UP, color=BLUE).scale(0.25),
            Line(UP, RIGHT, color=BLUE).scale(0.25),
            Line(RIGHT, DOWN, color=BLUE).scale(0.25),
            Line(DOWN, LEFT, color=BLUE).scale(0.25)
        ).arrange_in_grid(rows=2, cols=2, buff=0.1)
        label1.shift(0.0 * RIGHT + -0.2 * UP)  # layout: separation vector
        self.play(Transform(curve1, hilbert))
        self.wait(0.5)

        # Scaling factor explanation
        scale_text = MathTex(r"\log(4)/\log(2) = 2").to_edge(DOWN)
        scale_text.shift(0.0 * RIGHT + 0.49 * UP)  # layout: separation vector
        self.play(Write(scale_text))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title, curve1, label1, paradox, point1, point2, line1, pre1, pre2, line2, interval, interval_label, square_area, area_label, scale_text)
        )
        self.wait(0.5)
