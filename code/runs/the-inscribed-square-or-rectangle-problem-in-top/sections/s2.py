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
        self.play(Create(curve))
        self.wait(1)

        # Initial square
        square = Square(side_length=2, color=RED, fill_opacity=0.3)
        square.move_to(curve.get_center())
        self.play(FadeIn(square))
        self.wait(1)

        # Labels for square vertices
        labels = VGroup()
        for i, corner in enumerate(square.get_vertices()):
            label = MathTex(f"P_{{{i+1}}}", font_size=24)
            label.next_to(corner, UR, buff=0.1)
            labels.add(label)
        
        self.play(Write(labels))
        self.wait(1)

        # Morph square into rectangle
        rectangle = Rectangle(width=3, height=2, color=RED, fill_opacity=0.3)
        rectangle.move_to(curve.get_center())
        
        self.play(Transform(square, rectangle), run_time=2)
        self.wait(1)

        # Update labels for rectangle
        self.play(FadeOut(labels))
        labels = VGroup()
        for i, corner in enumerate(rectangle.get_vertices()):
            label = MathTex(f"P_{{{i+1}}}", font_size=24)
            label.next_to(corner, UR, buff=0.1)
            labels.add(label)
        
        self.play(Write(labels))
        self.wait(1)

        # Show right angles
        right_angles = VGroup()
        for i in range(4):
            angle = Angle(
                Line(rectangle.get_vertices()[i], rectangle.get_vertices()[(i+1)%4]),
                Line(rectangle.get_vertices()[(i+1)%4], rectangle.get_vertices()[(i+2)%4]),
                radius=0.3,
                other_angle=False
            )
            right_angles.add(angle)
        
        right_angles.shift(-0.35 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(right_angles), run_time=1)
        self.wait(1)

        # Key text overlays
        four_points = Text("4 Points", font_size=24).to_corner(UL)
        right_angles_text = Text("Right Angles", font_size=24).to_corner(UR)
        
        self.play(Write(four_points), Write(right_angles_text))
        self.wait(2)

        # Final theorem statement
        theorem = Text("Every simple closed curve contains an inscribed rectangle.", 
                      font_size=24, color=YELLOW)
        theorem.to_edge(DOWN)
        self.play(Write(theorem))
        self.wait(3)

        # Cleanup
        self.play(
            FadeOut(title),
            FadeOut(curve),
            FadeOut(square),
            FadeOut(labels),
            FadeOut(right_angles),
            FadeOut(four_points),
            FadeOut(right_angles_text),
            FadeOut(theorem)
        )
        self.wait(0.5)
