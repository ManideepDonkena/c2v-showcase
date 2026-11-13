from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Topological Insight", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial curve dissolving into grid of dots (torus representation)
        curve = Circle(radius=2, color=WHITE)
        self.play(Create(curve), run_time=1)
        self.wait(0.5)

        # Dissolve to grid
        grid_dots = VGroup()
        for i in range(20):
            for j in range(20):
                dot = Dot(point=[-3 + i*0.3, -1.8 + j*0.2, 0], color=WHITE)
                grid_dots.add(dot)
        self.play(Transform(curve, grid_dots), run_time=1.5)

        # Two paths on torus intersecting
        path1 = Line([-3, -1.8, 0], [3, 1.8, 0], color=YELLOW)
        path2 = Line([3, -1.8, 0], [-3, 1.8, 0], color=GREEN)
        self.play(Create(path1), Create(path2), run_time=1)

        # Intersection point glowing green
        intersection = Dot(point=[0, 0, 0], color=GREEN)
        self.play(FadeIn(intersection))
        self.wait(0.5)

        # Brouwer Fixed-Point Theorem text
        brouwer_text = Text("Brouwer Fixed-Point Theorem", font_size=24).next_to(intersection, DOWN)
        self.play(Write(brouwer_text))
        self.wait(1)

        # Fade out
        self.play(FadeOut(title), FadeOut(curve), FadeOut(path1), FadeOut(path2), FadeOut(intersection), FadeOut(brouwer_text))

        # Timeline overlay with Emil Artin 1911
        timeline = VGroup(
            Text("1911", font_size=24).next_to(ORIGIN, LEFT),
            Text("Emil Artin", font_size=24).next_to(ORIGIN, RIGHT)
        ).arrange(DOWN)
        self.play(Write(timeline))
        self.wait(0.5)

        # Ellipse with inscribed square
        ellipse = Ellipse(width=4, height=2.5, color=BLUE)
        square_in_ellipse = Square(side_length=2, color=RED).move_to(ellipse.get_center())
        self.play(Create(ellipse), Create(square_in_ellipse))
        self.wait(1)

        # Fade out
        self.play(FadeOut(timeline), FadeOut(ellipse), FadeOut(square_in_ellipse))

        # Rectangle vs Square comparison
        rect = Rectangle(width=2, height=1.5, color=YELLOW)
        square = Square(side_length=1.5, color=GREEN)
        rect_label = Text("Rectangle", font_size=20).next_to(rect, DOWN)
        square_label = Text("Square", font_size=20).next_to(square, DOWN)
        self.play(Create(rect), Create(square))
        self.play(Write(rect_label), Write(square_label))
        self.wait(1)

        # Fade out
        self.play(FadeOut(rect), FadeOut(square), FadeOut(rect_label), FadeOut(square_label))

        # Symmetry example (rounded square)
        rounded_square = Polygon(
            [0, 2, 0], [1.4, 1.4, 0], [2, 0, 0], [1.4, -1.4, 0],
            [0, -2, 0], [-1.4, -1.4, 0], [-2, 0, 0], [-1.4, 1.4, 0],
            color=BLUE
        )
        inscribed_square = Square(side_length=2, color=RED).move_to(rounded_square.get_center())
        self.play(Create(rounded_square), Create(inscribed_square))
        self.wait(1)

        # Fade out
        self.play(FadeOut(rounded_square), FadeOut(inscribed_square))

        # Split screen: fractal vs smooth curve
        fractal_curve = VMobject(color=RED)
        fractal_curve.set_points_as_corners([
            [-3, -2, 0], [-2.5, -1.5, 0], [-2, -2, 0],
            [-1.5, -1.5, 0], [-1, -2, 0], [-0.5, -1.5, 0],
            [0, -2, 0], [0.5, -1.5, 0], [1, -2, 0],
            [1.5, -1.5, 0], [2, -2, 0], [2.5, -1.5, 0],
            [3, -2, 0]
        ])
        smooth_curve = Circle(radius=2, color=BLUE)
        self.play(Create(fractal_curve), Create(smooth_curve))
        self.wait(0.5)

        # Labels
        fractal_label = Text("Counterexample Found", font_size=24).next_to(fractal_curve, UP)
        smooth_label = Text("Proven True", font_size=24).next_to(smooth_curve, UP)
        self.play(Write(fractal_label), Write(smooth_label))
        self.wait(1)

        # Fade out
        self.play(FadeOut(fractal_curve), FadeOut(smooth_curve), FadeOut(fractal_label), FadeOut(smooth_label))

        # Fixed point metaphor
        self.play(Write(Text("Fixed Point Theorem", font_size=24).to_edge(UP)))
        self.wait(0.5)

        # Circle with inscribed square
        circle = Circle(radius=1, color=BLUE)
        inscribed_square_in_circle = Square(side_length=np.sqrt(2), color=RED)
        self.play(Create(circle), Create(inscribed_square_in_circle))
        self.wait(0.5)

        # Pythagorean theorem explanation
        triangle = Triangle().scale(0.5).move_to([0, 0, 0])
        diag = Line([-1, -1, 0], [1, 1, 0], color=WHITE)
        side1 = Line([-1, -1, 0], [1, -1, 0], color=GREEN)
        side2 = Line([1, -1, 0], [1, 1, 0], color=GREEN)
        diag_label = MathTex("d = 2", font_size=24).next_to(diag, UP)
        side_label = MathTex("s = \\sqrt{2}", font_size=24).next_to(side1, DOWN)
        self.play(Create(diag), Create(side1), Create(side2))
        self.play(Write(diag_label), Write(side_label))
        self.wait(1)

        # Fade out
        self.play(FadeOut(circle), FadeOut(inscribed_square_in_circle), FadeOut(triangle),
                  FadeOut(diag), FadeOut(side1), FadeOut(side2),
                  FadeOut(diag_label), FadeOut(side_label))

        # Self-intersecting curve
        figure_eight = VMobject(color=RED)
        figure_eight.set_points_as_corners([
            [-2, 0, 0], [0, 2, 0], [2, 0, 0], [0, -2, 0],
            [-2, 0, 0]
        ])
        self.play(Create(figure_eight))
        self.wait(0.5)

        # Label
        eight_label = Text("Self-intersecting", font_size=24).next_to(figure_eight, UP)
        self.play(Write(eight_label))
        self.wait(1)

        # Normal loop
        normal_loop = Circle(radius=2, color=WHITE)
        self.play(Create(normal_loop))
        self.wait(0.5)

        # No crossing allowed
        no_crossing = Text("No crossing allowed", font_size=24).next_to(normal_loop, DOWN)
        self.play(Write(no_crossing))
        self.wait(1)

        # Final fade out
        self.play(FadeOut(figure_eight), FadeOut(eight_label),
                  FadeOut(normal_loop), FadeOut(no_crossing))
