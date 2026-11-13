from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Wrapping Around", font_size=36).to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # Lumen clock circle
        circle = Circle(radius=2.5, color=WHITE)
        circle.move_to(ORIGIN)
        self.play(Create(circle))

        # Marks 0 to 6
        marks = VGroup()
        for i in range(7):
            angle = TAU * i / 7
            mark = Dot(color=WHITE).move_to(circle.point_from_proportion(angle))
            label = MathTex(str(i), font_size=24).move_to(mark.get_center() + UP * 0.3)
            marks.add(mark, label)

        self.play(FadeIn(marks))

        # Hand at mark 3
        hand = Dot(color=YELLOW)
        angle_3 = TAU * 3 / 7
        hand.move_to(circle.point_from_proportion(angle_3))
        self.play(FadeIn(hand))
        self.wait(0.5)

        # Tick 1: 3 → 5
        angle_5 = TAU * 5 / 7
        self.play(
            hand.animate.move_to(circle.point_from_proportion(angle_5)),
            run_time=1
        )
        self.wait(0.5)

        # Tick 2: 5 → 0
        angle_0 = TAU * 0 / 7
        self.play(
            hand.animate.move_to(circle.point_from_proportion(angle_0)),
            run_time=1
        )
        self.wait(0.5)

        # Curved arrow from 6 back to 0
        angle_6 = TAU * 6 / 7
        arrow_start = circle.point_from_proportion(angle_6)
        arrow_end = circle.point_from_proportion(angle_0)
        curved_arrow = CurvedArrow(
            start_point=arrow_start,
            end_point=arrow_end,
            radius=3.2,
            angle=TAU/2,
            color=RED
        )
        self.play(Create(curved_arrow))
        self.wait(0.5)

        # Text: 3 → 5 → 0
        text = Text("3 → 5 → 0", font_size=30)
        text.next_to(title, DOWN, buff=0.5)
        self.play(Write(text))
        self.wait(1.5)

        # Narration words
        word_1 = Text("When the hand passes mark 6,", font_size=24).to_edge(DOWN, buff=0.3)
        self.play(Write(word_1))
        self.wait(1.5)
        self.play(FadeOut(word_1))

        word_2 = Text("it wraps around to 0.", font_size=24).to_edge(DOWN, buff=0.3)
        self.play(Write(word_2))
        self.wait(1.5)
        self.play(FadeOut(word_2))

        word_3 = Text("For example, starting at 3,", font_size=24).to_edge(DOWN, buff=0.3)
        self.play(Write(word_3))
        self.wait(1.5)
        self.play(FadeOut(word_3))

        word_4 = Text("two ticks take us to 5,", font_size=24).to_edge(DOWN, buff=0.3)
        self.play(Write(word_4))
        self.wait(1.5)
        self.play(FadeOut(word_4))

        word_5 = Text("and the next tick lands us on 0.", font_size=24).to_edge(DOWN, buff=0.3)
        self.play(Write(word_5))
        self.wait(1.5)
        self.play(FadeOut(word_5))

        # Final fade out
        self.play(
            FadeOut(title),
            FadeOut(circle),
            FadeOut(marks),
            FadeOut(hand),
            FadeOut(curved_arrow),
            FadeOut(text)
        )
        self.wait(0.5)
