from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Infinite Length, Finite Area: A Manim Journey", font_size=24).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Fade in curve and show it filling square
        square = Square(side_length=3, color=BLUE, fill_opacity=0.2)
        square.to_corner(DL)
        self.play(Create(square))

        # Hilbert curve approximation (approximate with 4 steps)
        curve = VMobject(color=YELLOW)
        curve.set_points_as_corners([
            [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]
        ])
        self.play(Create(curve), run_time=2)

        # Fade to solid square
        self.play(FadeOut(curve), run_time=0.5)
        self.wait(0.5)

        # Show dimensions
        top_dim = Text("Topological Dimension = 1", font_size=24).to_edge(UP).shift(DOWN * 0.5)
        haus_dim = Text("Hausdorff Dimension = 2", font_size=24).next_to(top_dim, DOWN)
        self.play(Write(top_dim), Write(haus_dim))
        self.wait(1)

        # Show fractal dimension formula
        formula = MathTex("D = \\frac{\\log(N)}{\\log(1/r)}", font_size=36)
        formula.to_edge(UP).shift(DOWN * 1.5)
        self.play(Write(formula))
        self.wait(1)

        # Show scaling example
        N = MathTex("N = 4", font_size=24).next_to(formula, DOWN)
        r = MathTex("r = \\frac{1}{2}", font_size=24).next_to(N, DOWN)
        self.play(Write(N), Write(r))
        self.wait(1)

        # Show Hilbert curve scaling
        self.play(FadeOut(N), FadeOut(r), run_time=0.5)
        self.play(Transform(formula, MathTex("D = \\frac{\\log(4)}{\\log(2)} = 2", font_size=36)), run_time=1)
        self.wait(1)

        # Show f(a) = f(b)
        point_a = Dot([0.5, 0.5, 0])
        point_b = Dot([0.7, 0.7, 0])
        label = Text("f(a) = f(b)", font_size=24).next_to(point_a, UP)
        self.play(Write(label))
        self.wait(1)

        # Show tearing example
        self.play(FadeOut(label), run_time=0.5)
        tear_line = Line([-3, 0, 0], [3, 0, 0], color=RED, stroke_width=2)
        self.play(Create(tear_line))
        self.wait(1)

        # Show continuity breaking
        point1 = Dot([0.2, 0.2, 0])
        point2 = Dot([0.25, 0.25, 0])
        label1 = Text("Close in square", font_size=24).next_to(point1, UP)
        self.play(Write(label1))
        self.wait(1)

        # Show pre-images are far apart
        self.play(FadeOut(label1), run_time=0.5)
        pre_point1 = Dot([-3, 0, 0])
        pre_point2 = Dot([3, 0, 0])
        label2 = Text("Far in line", font_size=24).next_to(pre_point1, UP)
        self.play(Write(label2))
        self.wait(1)

        # Show length counter
        self.play(FadeOut(label2), run_time=0.5)
        counter = ValueTracker(3)
        length_text = always_redraw(lambda: Text(f"Length: {int(counter.get_value())}", font_size=24).to_edge(DOWN))
        self.add(length_text)
        self.play(counter.animate.set_value(9), run_time=1)
        self.play(counter.animate.set_value(27), run_time=1)
        self.play(counter.animate.set_value(81), run_time=1)
        self.wait(0.5)

        # Show finite area vs infinite length
        self.play(FadeOut(length_text), run_time=0.5)
        area_label = Text("Area: 1", font_size=24).to_edge(DOWN)
        self.play(Write(area_label))
        self.wait(1)

        # Show unit interval and square with same measure
        self.play(FadeOut(area_label), run_time=0.5)
        interval = Line([-3, -1, 0], [-2, -1, 0], color=GREEN)
        interval_label = Text("Length: 1", font_size=24).next_to(interval, UP)
        self.play(Create(interval), Write(interval_label))
        self.wait(0.5)

        square2 = Square(side_length=1, color=BLUE, fill_opacity=0.2).to_edge(DOWN)
        area_label2 = Text("Area: 1", font_size=24).next_to(square2, UP)
        self.play(Create(square2), Write(area_label2))
        self.wait(1)

        # Show grid traversal
        self.play(FadeOut(interval), FadeOut(interval_label), FadeOut(square2), FadeOut(area_label2), run_time=0.5)
        grid = VGroup(*[Line([i, -3, 0], [i, 3, 0], color=GRAY) for i in range(-7, 8)] +
                      [Line([-7, j, 0], [7, j, 0], color=GRAY) for j in range(-4, 5)])
        self.play(Create(grid))
        self.wait(1)

        # Show curve traversing grid
        curve_path = VMobject(color=YELLOW)
        curve_path.set_points_as_corners([
            [-7, -3, 0], [-6, -3, 0], [-6, -2, 0], [-5, -2, 0],
            [-5, -1, 0], [-4, -1, 0], [-4, 0, 0], [-3, 0, 0],
            [-3, 1, 0], [-2, 1, 0], [-2, 2, 0], [-1, 2, 0],
            [-1, 3, 0]
        ])
        self.play(Create(curve_path), run_time=2)
        self.wait(1)

        # Final title
        final_title = Text("Infinity in Finite Space", font_size=36).to_edge(UP)
        final_title.shift(0.0 * RIGHT + -0.49 * UP)  # layout: separation vector
        self.play(Write(final_title))
        self.wait(1.5)
