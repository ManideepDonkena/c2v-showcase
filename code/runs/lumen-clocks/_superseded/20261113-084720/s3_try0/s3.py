from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Wrapping Around", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Lumen clock
        circle = Circle(radius=2.5, color=WHITE)
        marks = VGroup()
        for i in range(7):
            angle = 2 * PI * i / 7
            mark = MathTex(str(i), font_size=24)
            mark.move_to(circle.point_at_angle(angle))
            marks.add(mark)
        
        clock = VGroup(circle, marks)
        self.play(Create(circle), Write(marks))
        self.wait(0.5)

        # Initial hand at 3
        hand = Arrow(start=circle.get_center(), end=circle.point_at_angle(2*PI*3/7), color=YELLOW, buff=0)
        self.play(GrowArrow(hand))
        self.wait(0.5)

        # Tick 1: 3 -> 5
        self.play(
            Rotate(hand, angle=2*PI*2/7, about_point=circle.get_center()),
            run_time=1
        )
        self.wait(0.5)

        # Tick 2: 5 -> 0
        self.play(
            Rotate(hand, angle=2*PI*2/7, about_point=circle.get_center()),
            run_time=1
        )
        self.wait(0.5)

        # Curved arrow from 6 to 0
        start_arrow = circle.point_at_angle(2*PI*6/7)
        end_arrow = circle.point_at_angle(2*PI*0/7)
        curved_arrow = CurvedArrow(start_arrow, end_arrow, angle=2*PI/3, color=RED)
        self.play(GrowArrow(curved_arrow))
        self.wait(0.5)
        
        # Text: 3 → 5 → 0
        text = MathTex("3 \\rightarrow 5 \\rightarrow 0", font_size=40)
        text.to_edge(DOWN)
        self.play(Write(text))
        self.wait(1)

        # Narration words
        word1 = Text("wraps", font_size=24).to_corner(DR)
        self.play(Write(word1))
        self.wait(1)
        self.play(FadeOut(word1))

        word2 = Text("example", font_size=24).to_corner(DR)
        self.play(Write(word2))
        self.wait(1)
        self.play(FadeOut(word2))

        word3 = Text("ticks", font_size=24).to_corner(DR)
        self.play(Write(word3))
        self.wait(1)
        self.play(FadeOut(word3))

        self.wait(1)
        self.play(FadeOut(title, clock, hand, curved_arrow, text))
