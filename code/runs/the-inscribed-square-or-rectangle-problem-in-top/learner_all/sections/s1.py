from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Inscribed Square Problem: A Topological Journey", font_size=24).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Fade in black screen and draw the curve
        self.play(FadeIn(Rectangle(width=14, height=7.8, color=BLACK)))
        self.wait(0.5)

        # Draw a smooth white loop (irregular convex shape)
        curve = ParametricFunction(
            lambda t: np.array([
                2 * np.cos(t) + 0.5 * np.cos(3*t),
                1.5 * np.sin(t) + 0.5 * np.sin(3*t),
                0
            ]),
            t_range=[0, TAU],
            color=WHITE,
            stroke_width=4
        )
        curve_group = VGroup(curve)
        self.play(Create(curve_group), run_time=2)

        # Label and arrow
        label = Text("Simple Closed Curve", font_size=24).next_to(curve, UP)
        arrow = Arrow(label.get_bottom(), curve.get_center(), color=YELLOW)
        self.play(Write(label), Create(arrow))
        self.wait(1)
        # Narration text
        narration1 = Text("We begin with a simple closed curve...", font_size=20).to_edge(DOWN)
        self.play(Write(narration1))
        self.wait(1.5)
        self.play(FadeOut(narration1))

        # Statement about unsolved problem
        statement = Text("Finding four points forming a square is an unsolved mystery.", font_size=20).to_edge(DOWN)
        self.play(Write(statement))
        self.wait(1.5)
        self.play(FadeOut(statement))

        # Timeline overlay with Emil Artin
        timeline = VGroup(
            Text("Emil Artin", font_size=20),
            Text("1911", font_size=20)
        ).arrange(DOWN, buff=0.3).to_corner(UL)
        self.play(Write(timeline))
        self.wait(0.5)

        # Ellipse with inscribed square (solved case)
        ellipse = Ellipse(width=4, height=2.5, color=BLUE)
        inscribed_square = Square(side_length=2 * np.sqrt(2), color=YELLOW).move_to(ellipse.get_center())
        self.play(Create(ellipse))
        self.wait(0.5)
        self.play(Create(inscribed_square))
        self.wait(1)

        # Show that rectangle can adjust but square cannot
        rect = Rectangle(width=3, height=1.5, color=GREEN)
        self.play(Transform(rect, Rectangle(width=2, height=2, color=RED)))
        self.wait(0.5)
        self.play(FadeOut(rect))

        # Visual comparison: jagged vs smooth curve
        jagged_curve = VMobject().set_points_as_corners([
            [0, 0, 0], [1, 0, 0], [1, 1, 0], [2, 1, 0],
            [2, 2, 0], [3, 2, 0], [3, 3, 0], [4, 3, 0]
        ])
        smooth_curve = Circle(radius=2, color=BLUE)
        jagged_label = Text("Counterexample Found", font_size=20).next_to(jagged_curve, UP)
        smooth_label = Text("Proven True", font_size=20).next_to(smooth_curve, UP)

        self.play(Create(jagged_curve), Write(jagged_label))
        self.wait(0.5)
        self.play(Transform(jagged_curve, smooth_curve), Transform(jagged_label, smooth_label))
        self.wait(1)

        # Symmetry example
        rounded_square = Polygon(
            [2, 0, 0], [3, 1, 0], [2, 2, 0], [1, 1, 0],
            color=ORANGE
        )
        self.play(Create(rounded_square))
        self.wait(0.5)
        self.play(FadeOut(rounded_square))

        # Fixed point metaphor
        fixed_point = Dot(color=RED).move_to([0, 0, 0])
        self.play(Write(Text("Fixed Point Theorem", font_size=20).next_to(fixed_point, UP)))
        self.wait(1)
        self.play(FadeOut(fixed_point))

        # Circle with inscribed square
        circle = Circle(radius=1, color=BLUE)
        insquare = Square(side_length=np.sqrt(2), color=YELLOW)
        self.play(Create(circle))
        self.wait(0.5)
        self.play(Create(insquare))
        self.wait(0.5)

        # Pythagorean theorem explanation
        triangle = Triangle().scale(0.5).move_to([0, 0, 0])
        side_label = MathTex("a^2 + a^2 = (2)^2").next_to(triangle, DOWN)
        self.play(Write(side_label))
        self.wait(1)
        self.play(FadeOut(side_label))

        # Rectangle vs square comparison
        rect_comp = Rectangle(width=3, height=2, color=GREEN).move_to([-3, 0, 0])
        square_comp = Square(side_length=2.5, color=RED).move_to([3, 0, 0])
        self.play(Create(rect_comp), Create(square_comp))
        self.wait(0.5)
        self.play(FadeOut(rect_comp), FadeOut(square_comp))

        # Self-intersecting curve
        self_intersect = ParametricFunction(
            lambda t: np.array([
                np.cos(t) * (2 + 0.5 * np.sin(3*t)),
                np.sin(t) * (2 + 0.5 * np.sin(3*t)),
                0
            ]),
            t_range=[0, TAU],
            color=RED,
            stroke_width=4
        )
        self.play(Create(self_intersect))
        self.wait(0.5)
        self.play(Write(Text("Self-intersecting", font_size=20).next_to(self_intersect, UP)))
        self.wait(1)

        # Final summary text
        final_text = Text("No crossing allowed.", font_size=20).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)
        self.play(FadeOut(final_text))

        # End scene
        self.play(FadeOut(title), FadeOut(curve_group), FadeOut(timeline), FadeOut(self_intersect))
        self.wait(0.5)
