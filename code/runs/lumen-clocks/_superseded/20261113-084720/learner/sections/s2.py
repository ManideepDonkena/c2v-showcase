from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Two-Mark Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Lumen clock circle
        circle = Circle(radius=2.5, color=WHITE)
        circle.move_to(ORIGIN)
        self.play(Create(circle))

        # Mark labels
        marks = VGroup()
        for i in range(7):
            angle = 2 * PI * i / 7
            label = MathTex(str(i), font_size=24)
            label.move_to(circle.point_at_angle(angle))
            marks.add(label)
        marks.shift(0.2 * RIGHT + 0.0 * UP)  # layout: separation vector
        marks.shift(0.0 * RIGHT + 0.3 * UP)  # layout: separation vector
        self.play(Write(marks))
        self.wait(0.5)

        # Hand at mark 0
        hand = Dot(color=YELLOW)
        hand.move_to(circle.point_at_angle(2 * PI * 0 / 7))
        self.play(FadeIn(hand))
        self.wait(0.5)

        # First jump: 0 -> 2
        arrow1 = Arrow(start=hand.get_center(), end=circle.point_at_angle(2 * PI * 2 / 7), color=RED)
        arrow1.shift(0.0 * RIGHT + -0.26 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow1))
        self.play(hand.animate.move_to(circle.point_at_angle(2 * PI * 2 / 7)))
        plus2_1 = MathTex("+2", font_size=30).next_to(arrow1, UP)
        self.play(Write(plus2_1))
        self.wait(0.5)
        self.play(FadeOut(plus2_1))

        # Second jump: 2 -> 4
        arrow2 = Arrow(start=hand.get_center(), end=circle.point_at_angle(2 * PI * 4 / 7), color=RED)
        self.play(GrowArrow(arrow2))
        self.play(hand.animate.move_to(circle.point_at_angle(2 * PI * 4 / 7)))
        plus2_2 = MathTex("+2", font_size=30).next_to(arrow2, UP)
        self.play(Write(plus2_2))
        self.wait(0.5)
        self.play(FadeOut(plus2_2))

        # Narration text
        narration1 = Text("One tick = +2 marks", font_size=24).to_edge(DOWN)
        self.play(Write(narration1))
        self.wait(1)

        # Fade out first part
        self.play(FadeOut(arrow1), FadeOut(arrow2), FadeOut(hand), FadeOut(narration1))

        # New hand at mark 1
        hand2 = Dot(color=YELLOW)
        hand2.move_to(circle.point_at_angle(2 * PI * 1 / 7))
        self.play(FadeIn(hand2))
        self.wait(0.5)

        # Jump: 1 -> 3
        arrow3 = Arrow(start=hand2.get_center(), end=circle.point_at_angle(2 * PI * 3 / 7), color=RED)
        self.play(GrowArrow(arrow3))
        self.play(hand2.animate.move_to(circle.point_at_angle(2 * PI * 3 / 7)))
        plus2_3 = MathTex("+2", font_size=30).next_to(arrow3, UP)
        self.play(Write(plus2_3))
        self.wait(0.5)
        self.play(FadeOut(plus2_3))

        # Narration text
        narration2 = Text("The rule applies to any starting mark", font_size=24).to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(1)

        # Final fade out
        self.play(FadeOut(title), FadeOut(circle), FadeOut(marks), FadeOut(hand2), FadeOut(arrow3), FadeOut(narration2))
        self.wait(0.5)
