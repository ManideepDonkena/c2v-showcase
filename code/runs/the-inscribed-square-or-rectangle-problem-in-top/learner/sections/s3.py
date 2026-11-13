from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Inscribed Square Problem: A Topological Journey", font_size=24)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial rectangle
        rect = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.5)
        rect.move_to(ORIGIN)
        self.play(Create(rect))
        self.wait(0.5)

        # Shrink and rotate animation
        anim1 = rect.animate.scale(0.7).rotate(PI/6)
        anim2 = rect.animate.scale(0.8).rotate(-PI/4)
        anim3 = rect.animate.scale(0.9).rotate(PI/8)
        self.play(anim1, run_time=1)
        self.play(anim2, run_time=1)
        self.play(anim3, run_time=1)

        # Show stuck positions
        stuck1 = rect.copy().rotate(PI/4).scale(0.9)
        stuck2 = rect.copy().rotate(-PI/3).scale(0.85)
        self.play(Transform(rect, stuck1), run_time=0.5)
        self.wait(0.5)
        self.play(Transform(rect, stuck2), run_time=0.5)
        self.wait(0.5)

        # Text: Inscribed Square Problem?
        problem_text = Text("Inscribed Square Problem?", font_size=40, color=YELLOW)
        problem_text.to_edge(UP)
        problem_text.shift(0.0 * RIGHT + -0.48 * UP)  # layout: separation vector
        self.play(Write(problem_text))
        self.wait(1)

        # Fade out
        self.play(FadeOut(rect), FadeOut(problem_text))

        # Timeline overlay with Emil Artin
        timeline = VGroup(
            Text("1911", font_size=24),
            Text("Emil Artin", font_size=24)
        ).arrange(DOWN, buff=0.3).to_corner(UL)
        self.play(Write(timeline))

        # Convex curve with inscribed square
        ellipse = Ellipse(width=4, height=2.5, color=GREEN)
        ellipse.shift(UP * 1.5)
        square_in_ellipse = Square(side_length=1.2, color=RED, fill_opacity=0.3).move_to(ellipse.get_center())
        self.play(Create(ellipse), Create(square_in_ellipse))
        self.wait(1)

        # Fade out timeline and ellipse
        self.play(FadeOut(timeline), FadeOut(ellipse), FadeOut(square_in_ellipse))

        # Show that continuity doesn't guarantee solution
        rect2 = Rectangle(width=3, height=1.5, color=BLUE, fill_opacity=0.5)
        rect2.shift(DOWN * 1.5)
        self.play(Create(rect2))
        self.wait(0.5)

        # Animate to square shape
        self.play(rect2.animate.scale(0.8).rotate(PI/6), run_time=1.5)
        self.wait(0.5)

        # Show that it can't touch all sides
        stuck_pos = rect2.copy().rotate(PI/3).scale(0.9)
        self.play(Transform(rect2, stuck_pos), run_time=0.5)
        self.wait(0.5)

        # Fade out
        self.play(FadeOut(rect2))

        # Split screen: fractal vs smooth curve
        # Left side - Koch snowflake (no inscribed square)
        koch = VMobject(color=ORANGE)
        koch.set_points_as_corners([
            LEFT * 3, RIGHT * 3, UP * 1.732,
            LEFT * 3, RIGHT * 3, UP * 1.732
        ])
        koch.shift(LEFT * 3)
        self.play(Create(koch))
        no_square = Text("Counterexample Found", font_size=24).next_to(koch, UP)
        self.play(Write(no_square))
        self.wait(0.5)

        # Right side - smooth rectifiable curve
        smooth_curve = ParametricFunction(lambda t: np.array([
            2 * np.cos(t),
            2 * np.sin(t),
            0
        ]), t_range=[0, TAU], color=GREEN)
        self.play(Create(smooth_curve))
        square_in_smooth = Square(side_length=1.5, color=RED, fill_opacity=0.3).move_to(ORIGIN)
        self.play(Create(square_in_smooth))
        yes_square = Text("Proven True", font_size=24).next_to(smooth_curve, UP)
        self.play(Write(yes_square))
        self.wait(1)

        # Fade out
        self.play(FadeOut(koch), FadeOut(no_square), FadeOut(smooth_curve), FadeOut(square_in_smooth), FadeOut(yes_square))

        # Final statement
        final_text = Text("For all curves? No.", font_size=30, color=YELLOW)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(FadeOut(final_text), FadeOut(title))
