from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Pythagoras Theorem: Visual Proof", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        # Large right triangle
        triangle = Triangle()
        triangle.width = 5
        triangle.height = 4
        triangle.shift(DOWN * 0.5)
        triangle_color = triangle.set_stroke(WHITE, width=3)

        # Legs labeled a and b
        leg_a = Line(triangle.get_vertices()[0], triangle.get_vertices()[1])
        leg_b = Line(triangle.get_vertices()[1], triangle.get_vertices()[2])
        leg_a_label = MathTex("a", font_size=30).next_to(leg_a, LEFT, buff=0.1)
        leg_b_label = MathTex("b", font_size=30).next_to(leg_b, DOWN, buff=0.1)

        # Hypotenuse labeled c
        hypotenuse = Line(triangle.get_vertices()[2], triangle.get_vertices()[0])
        hypotenuse_label = MathTex("c", font_size=30).next_to(hypotenuse, RIGHT, buff=0.1)

        # Right angle marker (small square)
        right_angle_marker = Square(side_length=0.3, stroke_width=2, color=YELLOW)
        right_angle_marker.move_to(triangle.get_vertices()[1])

        # Show triangle and labels
        self.play(Create(triangle_color), run_time=1)
        self.wait(0.5)
        self.play(Write(leg_a_label), Write(leg_b_label))
        self.wait(0.5)
        self.play(Write(hypotenuse_label))
        self.wait(0.5)

        # Animate right angle marker
        self.play(Create(right_angle_marker), run_time=0.5)
        self.wait(1)

        # Narration text
        narration = Text("Every right-angled triangle has a special relationship between its three sides.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)

        # Clear narration and show key points
        self.play(FadeOut(narration))

        # Reveal legs and hypotenuse definitions
        leg_def = Text("The two shorter sides touching the right angle are called legs.", font_size=24)
        leg_def.to_edge(DOWN)
        self.play(Write(leg_def))
        self.wait(2)

        self.play(FadeOut(leg_def))

        hyp_def = Text("The longest side opposite the right angle is known as the hypotenuse.", font_size=24)
        hyp_def.to_edge(DOWN)
        self.play(Write(hyp_def))
        self.wait(2)

        self.play(FadeOut(hyp_def))
        self.wait(0.5)

        # Final cleanup
        self.play(FadeOut(title, triangle_color, leg_a_label, leg_b_label, hypotenuse_label, right_angle_marker))
        self.wait(0.5)
