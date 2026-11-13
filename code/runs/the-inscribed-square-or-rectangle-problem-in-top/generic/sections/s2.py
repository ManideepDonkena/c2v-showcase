from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Rectangle Case", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial curve
        curve = ParametricFunction(
            lambda t: np.array([
                2 * np.cos(t) + 0.5 * np.cos(3 * t),
                2 * np.sin(t) + 0.5 * np.sin(3 * t),
                0
            ]),
            t_range=[0, TAU],
            color=WHITE,
            stroke_width=3
        )
        self.play(Create(curve), run_time=2)
        self.wait(1)

        # Initial square
        square = Square(side_length=2, color=RED, fill_opacity=0.3)
        square.move_to(curve.get_center())
        self.play(FadeIn(square))
        self.wait(0.5)

        # Labels for square
        label_4_points = Text("4 Points", font_size=24).next_to(square, DL)
        label_right_angles = Text("Right Angles", font_size=24).next_to(square, UR)
        label_right_angles.shift(0.0 * RIGHT + 0.68 * UP)  # layout: separation vector
        self.play(Write(label_4_points), Write(label_right_angles))
        self.wait(1)

        # Morph square into rectangle
        rectangle = Rectangle(width=3, height=2, color=RED, fill_opacity=0.3)
        rectangle.move_to(curve.get_center())
        
        morph_animation = Transform(square, rectangle)
        self.play(morph_animation, run_time=2)
        
        # Update labels for rectangle
        self.play(
            label_4_points.animate.next_to(rectangle, DL),
            label_right_angles.animate.next_to(rectangle, UR),
            run_time=0.5
        )
        self.wait(1)

        # Clear labels and show theorem statement
        self.play(FadeOut(label_4_points), FadeOut(label_right_angles))
        self.wait(0.5)
        
        theorem_text = Text("Every simple closed curve contains an inscribed rectangle", font_size=24)
        theorem_text.to_edge(DOWN)
        self.play(Write(theorem_text))
        self.wait(1)

        # Show point tracking concept
        point_a = Dot(curve.point_from_proportion(0.1), color=YELLOW)
        point_b = Dot(curve.point_from_proportion(0.3), color=YELLOW)
        point_c = Dot(curve.point_from_proportion(0.7), color=YELLOW)
        point_d = Dot(curve.point_from_proportion(0.9), color=YELLOW)
        
        self.play(FadeIn(point_a), FadeIn(point_b), FadeIn(point_c), FadeIn(point_d))
        self.wait(1)

        # Highlight right angles
        angle_label = Text("Right Angles", font_size=24).next_to(rectangle, UP)
        self.play(Write(angle_label))
        self.wait(1.5)

        # Final cleanup
        self.play(
            FadeOut(curve),
            FadeOut(square),
            FadeOut(point_a),
            FadeOut(point_b),
            FadeOut(point_c),
            FadeOut(point_d),
            FadeOut(theorem_text),
            FadeOut(angle_label),
            FadeOut(title)
        )
        self.wait(0.5)
