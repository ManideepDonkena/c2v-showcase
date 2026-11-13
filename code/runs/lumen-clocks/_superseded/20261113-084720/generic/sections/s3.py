from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Wrapping Around", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Lumen clock setup
        circle = Circle(radius=2.5, color=WHITE)
        marks = VGroup()
        for i in range(7):
            angle = 2 * PI * i / 7
            mark = MathTex(str(i), font_size=24).move_to(circle.point_from_proportion(i/7))
            marks.add(mark)
        
        clock = VGroup(circle, marks)
        marks.shift(0.2 * RIGHT + 0.0 * UP)  # layout: separation vector
        marks.shift(0.0 * RIGHT + 0.3 * UP)  # layout: separation vector
        self.play(Create(circle), Write(marks))
        self.wait(0.5)

        # Initial hand at 3
        hand = Arrow(start=circle.get_center(), end=circle.point_from_proportion(3/7), color=YELLOW)
        self.play(GrowArrow(hand))
        self.wait(0.5)

        # Tick 1: 3 -> 5
        hand.shift(0.0 * RIGHT + 0.29 * UP)  # layout: separation vector
        self.play(
            Rotate(hand, angle=2 * 2 * PI / 7, about_point=circle.get_center()),
            run_time=1
        )
        self.wait(0.5)

        # Tick 2: 5 -> 0
        self.play(
            Rotate(hand, angle=2 * 2 * PI / 7, about_point=circle.get_center()),
            run_time=1
        )
        self.wait(0.5)

        # Curved arrow from 6 back to 0
        arc = ArcBetweenPoints(circle.point_from_proportion(6/7), circle.point_from_proportion(0/7), angle=PI*1.2, color=RED)
        arc_arrow = Arrow(arc.get_start(), arc.get_end(), tip_length=0.2, color=RED)
        self.play(Create(arc_arrow))
        self.wait(0.5)

        # Text: 3 → 5 → 0
        text = MathTex("3 \\rightarrow 5 \\rightarrow 0", font_size=40).to_edge(DOWN)
        self.play(Write(text))
        self.wait(1)

        # Explanation text
        explanation = Text("When the hand passes mark 6, it wraps around to 0.", font_size=24)
        self.play(Write(explanation))
        self.wait(1.5)
        self.play(FadeOut(explanation))

        # Example: from 3, two ticks go 3 → 5 → 0
        example = Text("Example: from mark 3, two ticks go 3 → 5 → 0", font_size=24)
        self.play(Write(example))
        self.wait(1.5)
        self.play(FadeOut(example))

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(clock),
            FadeOut(hand),
            FadeOut(arc_arrow),
            FadeOut(text)
        )
        self.wait(0.5)
