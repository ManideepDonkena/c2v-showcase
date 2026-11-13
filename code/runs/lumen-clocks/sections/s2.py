from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Two-Mark Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Circle with marks
        circle = Circle(radius=2, color=WHITE).move_to(ORIGIN)
        marks = VGroup()
        for i in range(7):
            angle = TAU * i / 7
            mark = Dot(circle.point_at_angle(angle), color=WHITE)
            label = MathTex(str(i), font_size=24).move_to(circle.point_at_angle(angle) + UP*0.3)
            marks.add(mark)
            marks.add(label)
        self.play(Create(circle), run_time=1)
        marks.shift(0.2 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(FadeIn(marks), run_time=1)
        self.wait(0.5)

        # Initial hand at mark 0
        hand = Dot(circle.point_at_angle(0), color=YELLOW)
        self.play(FadeIn(hand))
        self.wait(0.5)

        # First jump: 0 -> 2
        self.play(
            hand.animate.move_to(circle.point_at_angle(2 * TAU / 7)),
            run_time=1
        )
        plus_two = MathTex("+2", font_size=30).move_to(hand.get_center() + UP*0.5)
        self.play(Write(plus_two))
        self.wait(0.5)
        self.play(FadeOut(plus_two))

        # Second jump: 2 -> 4
        self.play(
            hand.animate.move_to(circle.point_at_angle(4 * TAU / 7)),
            run_time=1
        )
        plus_two = MathTex("+2", font_size=30).move_to(hand.get_center() + UP*0.5)
        self.play(Write(plus_two))
        self.wait(0.5)
        self.play(FadeOut(plus_two))

        # Narration text
        narration = Text("One tick = +2 marks", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1)

        self.play(FadeOut(title), FadeOut(circle), FadeOut(marks), FadeOut(hand), FadeOut(narration))
        self.wait(0.5)
