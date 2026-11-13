from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Inscribed Square Problem: A Topological Journey", font_size=24).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial rectangle shrinking and rotating
        rect = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.5)
        rect.move_to(ORIGIN)
        self.play(Create(rect))
        self.wait(0.5)

        # Shrink and rotate animation
        anims = [
            rect.animate.scale(0.7).rotate(PI/6),
            rect.animate.scale(0.8).rotate(-PI/4),
            rect.animate.scale(0.9).rotate(PI/3),
            rect.animate.scale(1.1).rotate(-PI/5),
        ]
        self.play(*anims, run_time=2)
        self.wait(0.5)

        # Show stuck orientations
        stuck1 = rect.copy().scale(0.6).rotate(PI/4)
        stuck2 = rect.copy().scale(0.6).rotate(-PI/3)
        self.play(Transform(rect, stuck1), run_time=0.5)
        self.wait(0.5)
        self.play(Transform(rect, stuck2), run_time=0.5)
        self.wait(0.5)

        # Text: Inscribed Square Problem?
        problem_text = Text("Inscribed Square Problem?", font_size=36, color=YELLOW).to_edge(UP)
        problem_text.shift(0.0 * RIGHT + -0.48 * UP)  # layout: separation vector
        self.play(Write(problem_text))
        self.wait(1)

        # Fade out
        self.play(FadeOut(rect), FadeOut(problem_text))

        # Timeline overlay with Emil Artin
        timeline = VGroup(
            Text("1911", font_size=24).next_to(DOWN, buff=0.5),
            Text("Emil Artin", font_size=24).next_to(DOWN, buff=0.5).shift(RIGHT * 2)
        ).to_edge(LEFT, buff=0.5)

        ellipse = Ellipse(width=3, height=2, color=GREEN).move_to(ORIGIN)
        self.play(Create(ellipse), Write(timeline))
        self.wait(1)

        # Show inscribed square in ellipse
        insq = Square(side_length=2, color=RED, fill_opacity=0.5).move_to(ellipse.get_center())
        self.play(Create(insq))
        self.wait(1)
        self.play(FadeOut(ellipse), FadeOut(insq), FadeOut(timeline))

        # Visual demonstration of constraint
        curve = ParametricFunction(lambda t: np.array([np.cos(t), np.sin(t) * 0.5, 0]), t_range=[0, TAU], color=WHITE)
        self.play(Create(curve))
        self.wait(0.5)

        # Show square trying to fit
        sq = Square(side_length=1.2, color=YELLOW).move_to(ORIGIN)
        self.play(Create(sq))
        self.wait(0.5)
        self.play(sq.animate.rotate(PI/4), run_time=1)
        self.wait(0.5)
        self.play(FadeOut(sq))

        # Rectangle vs Square comparison
        rect2 = Rectangle(width=3, height=1.5, color=BLUE).move_to(ORIGIN)
        self.play(Create(rect2))
        self.wait(0.5)

        sq2 = Square(side_length=2, color=RED).move_to(ORIGIN)
        self.play(Transform(rect2, sq2))
        self.wait(1)
        self.play(FadeOut(rect2))

        # Symmetry example
        rounded_square = Polygon(
            [2, 0, 0], [1, 1, 0], [0, 2, 0], [-1, 1, 0],
            [-2, 0, 0], [-1, -1, 0], [0, -2, 0], [1, -1, 0]
        ).set_color(GREEN)
        self.play(Create(rounded_square))
        self.wait(0.5)

        insq_sym = Square(side_length=2.8, color=YELLOW).move_to(rounded_square.get_center())
        self.play(Create(insq_sym))
        self.wait(1)
        self.play(FadeOut(rounded_square), FadeOut(insq_sym))

        # Split screen: fractal vs smooth
        koch = VMobject(color=RED)
        koch.set_points_as_corners([
            np.array([-2, -1, 0]),
            np.array([0, 1, 0]),
            np.array([2, -1, 0]),
            np.array([-2, -1, 0])
        ])
        self.play(Create(koch))
        koch_label = Text("Counterexample Found", font_size=24).next_to(koch, DOWN)
        self.play(Write(koch_label))

        smooth_curve = Circle(radius=1.5, color=BLUE)
        smooth_curve.shift(0.0 * RIGHT + 0.4 * UP)  # layout: separation vector
        self.play(Create(smooth_curve))
        insq_smooth = Square(side_length=np.sqrt(2), color=YELLOW).move_to(smooth_curve.get_center())
        self.play(Create(insq_smooth))
        smooth_label = Text("Proven True", font_size=24).next_to(smooth_curve, DOWN)
        smooth_label.shift(0.0 * RIGHT + -0.38 * UP)  # layout: separation vector
        self.play(Write(smooth_label))

        self.wait(1.5)

        # Fade out
        self.play(FadeOut(koch), FadeOut(koch_label), FadeOut(smooth_curve), FadeOut(insq_smooth), FadeOut(smooth_label))

        # Fixed point metaphor
        self.play(Write(Text("Fixed Point Theorems", font_size=24).to_edge(UP)))
        self.wait(0.5)

        # Circle with inscribed square
        circle = Circle(radius=1, color=WHITE)
        self.play(Create(circle))
        self.wait(0.5)

        diag = Line(circle.get_left(), circle.get_right(), color=YELLOW)
        self.play(Create(diag))
        self.wait(0.5)

        # Pythagorean calculation
        calc = MathTex("d^2 = a^2 + a^2", "=", "2a^2", font_size=36).to_edge(DOWN)
        self.play(Write(calc))
        self.wait(0.5)

        side_length = MathTex("a = \\sqrt{2}", font_size=36).next_to(calc, DOWN)
        self.play(Write(side_length))
        self.wait(1)

        # Rectangle vs Square comparison
        rect3 = Rectangle(width=2, height=1, color=BLUE)
        sq3 = Square(side_length=1.414, color=RED)
        group = VGroup(rect3, sq3).arrange(RIGHT, buff=1)
        self.play(Create(group))
        self.wait(0.5)

        self.play(FadeOut(calc), FadeOut(side_length), FadeOut(group))

        # Self-intersecting curve
        figure_eight = VMobject(color=RED)
        figure_eight.set_points_as_corners([
            np.array([-1, 0, 0]),
            np.array([0, 1, 0]),
            np.array([1, 0, 0]),
            np.array([0, -1, 0]),
            np.array([-1, 0, 0])
        ])
        self.play(Create(figure_eight))
        self.wait(0.5)

        label8 = Text("Self-intersecting", font_size=24).next_to(figure_eight, DOWN)
        self.play(Write(label8))

        # Normal curve
        normal_curve = Circle(radius=1.2, color=WHITE)
        self.play(Create(normal_curve))
        self.wait(0.5)

        label_normal = Text("No crossing allowed", font_size=24).next_to(normal_curve, DOWN)
        self.play(Write(label_normal))

        self.wait(1.5)

        # Final fade
        self.play(FadeOut(figure_eight), FadeOut(label8), FadeOut(normal_curve), FadeOut(label_normal))
        self.play(FadeOut(title))
