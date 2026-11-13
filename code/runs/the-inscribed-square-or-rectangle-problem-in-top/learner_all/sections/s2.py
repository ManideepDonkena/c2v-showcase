from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Inscribed Square Problem: A Topological Journey", font_size=24)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial curve and square
        curve = ParametricFunction(lambda t: np.array([
            1.5 * np.cos(t) + 0.5 * np.cos(3*t),
            1.5 * np.sin(t) + 0.5 * np.sin(3*t),
            0
        ]), t_range=[0, TAU], color=WHITE)
        square = Square(side_length=2, color=RED)
        square.move_to(curve.get_center())
        self.play(Create(curve))
        self.play(Create(square))
        self.wait(1)

        # Labels for square
        label_4p = MathTex("4\\text{ Points}", font_size=24).next_to(square, UR)
        label_ra = MathTex("90^\\circ", font_size=24).next_to(square, UL)
        label_4p.shift(0.0 * RIGHT + 0.31 * UP)  # layout: separation vector
        label_ra.shift(0.0 * RIGHT + 0.31 * UP)  # layout: separation vector
        self.play(Write(label_4p), Write(label_ra))
        self.wait(1)

        # Morph square into rectangle
        rect = Rectangle(width=3, height=1.5, color=RED)
        rect.move_to(curve.get_center())
        self.play(Transform(square, rect))
        self.wait(1)

        # Labels for rectangle
        self.play(ReplacementTransform(label_4p, MathTex("4\\text{ Points}", font_size=24).next_to(rect, UR)),
                  ReplacementTransform(label_ra, MathTex("90^\\circ", font_size=24).next_to(rect, UL)))
        self.wait(1)

        # Timeline overlay
        timeline = VGroup(
            Text("Emil Artin", font_size=20),
            Text("1911", font_size=20)
        ).arrange(DOWN, buff=0.2)
        timeline.to_corner(UL)
        ellipse = Ellipse(width=2, height=1.5, color=WHITE).move_to(timeline.get_center())
        self.play(Write(timeline), Create(ellipse))
        self.wait(1)

        # Show that square is not always possible
        self.play(FadeOut(timeline), FadeOut(ellipse))

        # Irregular curve with no inscribed square
        irregular = ParametricFunction(lambda t: np.array([
            2 * np.cos(t) + 0.5 * np.cos(10*t),
            2 * np.sin(t) + 0.5 * np.sin(10*t),
            0
        ]), t_range=[0, TAU], color=WHITE)
        self.play(Transform(curve, irregular))
        self.wait(1)

        # Show that even with continuous adjustment, no square fits
        self.play(FadeOut(square))

        # Split screen: fractal vs smooth
        fractal = ParametricFunction(lambda t: np.array([
            (1.5 + 0.5 * np.cos(3*t)) * np.cos(t),
            (1.5 + 0.5 * np.cos(3*t)) * np.sin(t),
            0
        ]), t_range=[0, TAU], color=WHITE)
        smooth = Circle(radius=2, color=WHITE)

        fractal_label = Text("Counterexample Found", font_size=24).next_to(fractal, UP)
        smooth_label = Text("Proven True", font_size=24).next_to(smooth, UP)

        self.play(Create(fractal), Write(fractal_label))
        self.wait(1)
        self.play(Transform(fractal, smooth), Transform(fractal_label, smooth_label))
        self.wait(1)

        # Fixed point metaphor
        self.play(FadeOut(fractal), FadeOut(fractal_label), FadeOut(smooth), FadeOut(smooth_label))

        # Circle with inscribed square
        circle = Circle(radius=1, color=WHITE)
        square_in_circle = Square(side_length=np.sqrt(2), color=RED)
        square_in_circle.move_to(circle.get_center())
        self.play(Create(circle))
        self.play(Create(square_in_circle))
        self.wait(1)

        # Pythagorean theorem
        diag = Line(circle.get_left(), circle.get_right(), color=YELLOW)
        side1 = Line(circle.get_left(), square_in_circle.get_corner(DL), color=GREEN)
        side2 = Line(square_in_circle.get_corner(DL), square_in_circle.get_corner(UL), color=GREEN)
        self.play(Create(diag), Create(side1), Create(side2))
        self.wait(1)

        # Formula
        formula = MathTex("d = s\\sqrt{2} \\Rightarrow s = \\frac{d}{\\sqrt{2}} = \\sqrt{2}", font_size=30)
        formula.to_edge(DOWN)
        self.play(Write(formula))
        self.wait(1)

        # Rectangle vs square comparison
        rect_comp = Rectangle(width=2, height=1.5, color=BLUE).move_to(LEFT * 3)
        square_comp = Square(side_length=1.5, color=BLUE).move_to(RIGHT * 3)
        self.play(Create(rect_comp), Create(square_comp))
        self.wait(1)

        # Explanation
        explanation = Text("Rectangle: 2 degrees of freedom\nSquare: 1 degree of freedom", font_size=24)
        explanation.next_to(square_comp, DOWN)
        self.play(Write(explanation))
        self.wait(1)

        # Self-intersecting curve
        self_int = ParametricFunction(lambda t: np.array([
            2 * np.cos(t) + 0.5 * np.cos(2*t),
            2 * np.sin(t) + 0.5 * np.sin(2*t),
            0
        ]), t_range=[0, TAU], color=WHITE)
        self_int_label = Text("Self-intersecting", font_size=24).next_to(self_int, UP)
        self.play(Create(self_int), Write(self_int_label))
        self.wait(1)

        # Final statement
        final = Text("No crossing allowed", font_size=24).next_to(self_int, DOWN)
        self.play(Write(final))
        self.wait(1)

        self.play(FadeOut(title), FadeOut(curve), FadeOut(square), FadeOut(rect), FadeOut(label_4p),
                  FadeOut(label_ra), FadeOut(formula), FadeOut(explanation), FadeOut(self_int),
                  FadeOut(self_int_label), FadeOut(final), FadeOut(rect_comp), FadeOut(square_comp))
