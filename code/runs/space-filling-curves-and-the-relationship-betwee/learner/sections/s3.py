from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Surjectivity vs. Injectivity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # 1D line segment
        line = Line(start=LEFT * 3, end=RIGHT * 3, color=WHITE)
        line_label = MathTex("I = [0,1]", font_size=24).next_to(line, DOWN)
        self.play(Create(line), Write(line_label))
        self.wait(0.5)

        # Two points on the line
        a_point = Dot(line.get_start(), color=RED)
        b_point = Dot(line.get_end(), color=BLUE)
        a_label = MathTex("t_1", font_size=24).next_to(a_point, DOWN)
        b_label = MathTex("t_2", font_size=24).next_to(b_point, DOWN)

        self.play(FadeIn(a_point), Write(a_label))
        self.play(FadeIn(b_point), Write(b_label))
        self.wait(0.5)

        # 2D square
        square = Square(side_length=4, color=WHITE)
        square.to_edge(DOWN)
        square_label = MathTex("S", font_size=24).next_to(square, UP)
        self.play(Create(square), Write(square_label))
        self.wait(0.5)

        # Mapping function (approximate space-filling curve)
        # We simulate the mapping with a path that overlaps
        path_a = always_redraw(lambda: Line(
            start=line.get_start(),
            end=square.get_corner(DL) + UP * 1.5 + RIGHT * 0.5,
            color=RED
        ))
        path_b = always_redraw(lambda: Line(
            start=line.get_end(),
            end=square.get_corner(DL) + UP * 1.5 + RIGHT * 0.5,
            color=BLUE
        ))

        self.play(Create(path_a), Create(path_b))
        self.wait(1)

        # Show overlapping paths
        overlap = Dot(
            point=square.get_corner(DL) + UP * 1.5 + RIGHT * 0.5,
            color=YELLOW
        )
        overlap_label = MathTex("f(t_1) = f(t_2)", font_size=24).next_to(overlap, UR)
        self.play(FadeIn(overlap), Write(overlap_label))
        self.wait(1.5)

        # Show that it's surjective
        all_points = VGroup()
        for i in range(10):
            p = Dot(
                point=square.get_corner(DL) + UP * (i / 9) * 2 + RIGHT * (i % 3) * 0.5,
                color=GREEN
            )
            all_points.add(p)
        self.play(FadeIn(all_points))
        self.wait(1)

        # Show that it's not injective
        self.play(
            FadeOut(overlap_label),
            FadeOut(path_a),
            FadeOut(path_b)
        )
        self.wait(0.5)

        # Demonstrate non-injective nature with two points mapping to same output
        a_point2 = Dot(line.get_start(), color=RED)
        b_point2 = Dot(line.get_end(), color=BLUE)
        self.play(FadeIn(a_point2), FadeIn(b_point2))

        # Simulate mapping to same point in square
        mapped_a = Dot(square.get_corner(DL) + UP * 1.5 + RIGHT * 0.5, color=RED)
        mapped_b = Dot(square.get_corner(DL) + UP * 1.5 + RIGHT * 0.5, color=BLUE)

        self.play(FadeIn(mapped_a), FadeIn(mapped_b))
        f_label = MathTex("f(a) = f(b)", font_size=24).next_to(mapped_a, UR)
        self.play(Write(f_label))
        self.wait(1.5)

        # Show that injective would break continuity
        self.play(FadeOut(f_label), FadeOut(mapped_a), FadeOut(mapped_b))

        # Show that if it were injective, it would have to tear
        tear_line = Line(start=LEFT * 3, end=RIGHT * 3, color=RED, stroke_width=2)
        tear_line.to_edge(DOWN)
        tear_label = Text("If injective → must tear", font_size=24).next_to(tear_line, UP)
        self.play(Create(tear_line), Write(tear_label))
        self.wait(1.5)

        # Show that nearby points in square come from far apart points on line
        self.play(FadeOut(tear_line), FadeOut(tear_label))

        # Two adjacent points in square
        p1 = Dot(point=square.get_corner(DL) + UP * 0.5 + RIGHT * 0.2, color=GREEN)
        p2 = Dot(point=square.get_corner(DL) + UP * 0.5 + RIGHT * 0.3, color=GREEN)

        # Show pre-images on line
        pre1 = Dot(line.get_start() + RIGHT * 0.1, color=RED)
        pre2 = Dot(line.get_end() - RIGHT * 0.1, color=BLUE)

        self.play(FadeIn(p1), FadeIn(p2))
        self.wait(0.5)
        self.play(FadeIn(pre1), FadeIn(pre2))

        # Show distance in square vs. on line
        dist_square = Line(start=p1.get_center(), end=p2.get_center(), color=YELLOW)
        dist_line = Line(start=pre1.get_center(), end=pre2.get_center(), color=ORANGE)

        dist_label_sq = MathTex("d(p_1, p_2) \ll 1", font_size=24).next_to(dist_square, UP)
        dist_label_line = MathTex("d(f^{-1}(p_1), f^{-1}(p_2)) \gg 1", font_size=24).next_to(dist_line, DOWN)

        self.play(Create(dist_square), Create(dist_line))
        self.play(Write(dist_label_sq), Write(dist_label_line))
        self.wait(1.5)

        # Final summary
        self.play(
            FadeOut(p1),
            FadeOut(p2),
            FadeOut(pre1),
            FadeOut(pre2),
            FadeOut(dist_square),
            FadeOut(dist_line),
            FadeOut(dist_label_sq),
            FadeOut(dist_label_line),
            FadeOut(title)
        )
        self.wait(0.5)
