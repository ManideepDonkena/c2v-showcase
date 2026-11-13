from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Surjectivity vs. Injectivity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # 1D line segment with two points
        line = Line(start=LEFT * 3, end=RIGHT * 3, color=WHITE)
        t1 = Dot(line.get_start() + RIGHT * 1, color=RED)
        t2 = Dot(line.get_start() + RIGHT * 2.5, color=BLUE)
        label_t1 = MathTex("t_1", font_size=24).next_to(t1, DOWN)
        label_t2 = MathTex("t_2", font_size=24).next_to(t2, DOWN)
        self.play(Create(line), DrawBorderThenFill(t1), DrawBorderThenFill(t2))
        self.play(Write(label_t1), Write(label_t2))
        self.wait(0.5)

        # Square
        square = Square(side_length=4, color=WHITE).to_edge(DOWN)
        square.shift(0.23 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(square))
        self.wait(0.5)

        # Mapping curve (Hilbert-like)
        def hilbert_curve(n, scale=1):
            if n == 0:
                return Line(ORIGIN, RIGHT * scale)
            else:
                prev = hilbert_curve(n - 1, scale / 2)
                return VGroup(
                    prev.copy().rotate(90 * DEGREES).shift(UP * scale / 2),
                    prev.copy().shift(RIGHT * scale / 2),
                    prev.copy().rotate(-90 * DEGREES).shift(DOWN * scale / 2),
                    prev.copy().rotate(180 * DEGREES).shift(LEFT * scale / 2)
                )

        curve = hilbert_curve(3, 4)
        self.play(Create(curve), run_time=2)
        self.wait(0.5)

        # Highlight overlapping paths
        path1 = Line(line.get_start() + RIGHT * 1, line.get_start() + RIGHT * 2.5, color=YELLOW)
        path2 = Line(line.get_start() + RIGHT * 2.5, line.get_start() + RIGHT * 1, color=YELLOW)
        self.play(ShowPassingFlash(path1), ShowPassingFlash(path2))
        label_overlap = MathTex("f(t_1) = f(t_2)", font_size=24).move_to(square.get_center())
        self.play(Write(label_overlap))
        self.wait(0.5)

        # Surjectivity
        self.play(FadeOut(label_overlap))
        surj_label = Text("Surjective", font_size=24).to_edge(LEFT)
        self.play(Write(surj_label))
        self.wait(0.5)

        # Injectivity
        inj_label = Text("Not Injective", font_size=24).to_edge(RIGHT)
        self.play(Write(inj_label))
        self.wait(0.5)

        # Measure comparison
        unit_interval = Line(start=LEFT * 3, end=RIGHT * 3, color=WHITE)
        interval_label = MathTex("1", font_size=24).next_to(unit_interval, DOWN)
        area_square = Square(side_length=4, color=WHITE).to_edge(DOWN)
        area_label = MathTex("1", font_size=24).next_to(area_square, DOWN)
        self.play(Create(unit_interval), Write(interval_label))
        self.wait(0.5)
        area_square.shift(0.23 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(area_square), Write(area_label))
        self.wait(0.5)

        # Length doubling
        length_text = MathTex("3, 9, 27, 81, ...", font_size=24).to_edge(UP)
        length_text.shift(0.0 * RIGHT + 0.37 * UP)  # layout: separation vector
        self.play(Write(length_text))
        self.wait(0.5)

        # Grid traversal
        grid = VGroup(*[Line(start=LEFT * 4 + j * UP * 0.5, end=RIGHT * 4 + j * UP * 0.5) for j in range(-4, 5)] +
                      [Line(start=DOWN * 4 + j * RIGHT * 0.5, end=UP * 4 + j * RIGHT * 0.5) for j in range(-8, 9)])
        self.play(Create(grid))
        self.wait(0.5)

        # Hilbert scaling
        scale_label = MathTex("N=4, r=\\frac{1}{2} \\Rightarrow \\log(4)/\\log(2)=2", font_size=24).to_edge(DOWN)
        self.play(Write(scale_label))
        self.wait(0.5)

        # End
        self.play(FadeOut(title), FadeOut(line), FadeOut(t1), FadeOut(t2), FadeOut(label_t1), FadeOut(label_t2),
                  FadeOut(square), FadeOut(curve), FadeOut(surj_label), FadeOut(inj_label), FadeOut(unit_interval),
                  FadeOut(interval_label), FadeOut(area_square), FadeOut(area_label), FadeOut(length_text),
                  FadeOut(grid), FadeOut(scale_label))
        self.wait(0.5)
