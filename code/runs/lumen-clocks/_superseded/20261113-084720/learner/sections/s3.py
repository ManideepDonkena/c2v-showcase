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
            mark = MathTex(str(i), font_size=24).move_to(circle.point_at_angle(angle))
            marks.add(mark)
        
        clock = VGroup(circle, marks)
        marks.shift(0.2 * RIGHT + 0.0 * UP)  # layout: separation vector
        marks.shift(0.0 * RIGHT + 0.3 * UP)  # layout: separation vector
        self.play(Create(circle), Write(marks))
        self.wait(0.5)

        # Hand at mark 3
        hand = Arrow(start=circle.get_center(), end=circle.point_at_angle(2 * PI * 3 / 7), color=YELLOW)
        self.play(GrowArrow(hand))
        self.wait(0.5)

        # First example: 3 → 5 → 0
        label_3 = MathTex("3", font_size=24).next_to(hand, DOWN)
        self.play(Write(label_3))
        self.wait(0.5)

        # Tick 1: 3 → 5
        hand.shift(0.0 * RIGHT + 0.29 * UP)  # layout: separation vector
        self.play(
            Rotate(hand, angle=2 * 2 * PI / 7, about_point=circle.get_center()),
            run_time=0.8
        )
        label_5 = MathTex("5", font_size=24).next_to(hand, DOWN)
        self.play(ReplacementTransform(label_3, label_5))
        self.wait(0.5)

        # Tick 2: 5 → 0
        self.play(
            Rotate(hand, angle=2 * 2 * PI / 7, about_point=circle.get_center()),
            run_time=0.8
        )
        label_0 = MathTex("0", font_size=24).next_to(hand, DOWN)
        self.play(ReplacementTransform(label_5, label_0))
        self.wait(0.5)

        # Show wrap-around arrow from 6 to 0
        start_arrow = circle.point_at_angle(2 * PI * 6 / 7)
        end_arrow = circle.point_at_angle(2 * PI * 0 / 7)
        wrap_arrow = CurvedArrow(start_arrow, end_arrow, angle=PI, color=RED)
        self.play(Create(wrap_arrow))
        self.wait(0.5)

        # Text: "3 → 5 → 0"
        text_350 = MathTex("3 \\rightarrow 5 \\rightarrow 0", font_size=30).to_edge(DOWN)
        self.play(Write(text_350))
        self.wait(1)

        # Clear previous
        self.play(FadeOut(hand), FadeOut(label_0), FadeOut(wrap_arrow), FadeOut(text_350))

        # Second example: from 5, add 2 marks
        hand2 = Arrow(start=circle.get_center(), end=circle.point_at_angle(2 * PI * 5 / 7), color=YELLOW)
        self.play(GrowArrow(hand2))
        label_5_2 = MathTex("5", font_size=24).next_to(hand2, DOWN)
        self.play(Write(label_5_2))
        self.wait(0.5)

        # Add 2: 5 → 0
        self.play(
            Rotate(hand2, angle=2 * 2 * PI / 7, about_point=circle.get_center()),
            run_time=0.8
        )
        label_0_2 = MathTex("0", font_size=24).next_to(hand2, DOWN)
        self.play(ReplacementTransform(label_5_2, label_0_2))
        self.wait(0.5)

        # Narration text
        narration = Text("From 5, add 2 marks: 5 plus 2 is 7, which wraps around to 0.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)
        self.play(FadeOut(narration))

        # Clear
        self.play(FadeOut(hand2), FadeOut(label_0_2))

        # Show visual comparison: 7 positions, wrap-around
        self.play(FadeOut(title))
        comparison_text = Text("Circle has 7 positions (0–6)", font_size=24).to_edge(UP)
        self.play(Write(comparison_text))
        self.wait(0.5)

        # Show the cycle
        self.play(
            Rotate(hand, angle=2 * 2 * PI / 7, about_point=circle.get_center()),
            run_time=0.8
        )
        label_5_final = MathTex("5", font_size=24).next_to(hand, DOWN)
        self.play(Write(label_5_final))
        self.wait(0.5)

        # Next tick: 5 → 0 (wrap)
        self.play(
            Rotate(hand, angle=2 * 2 * PI / 7, about_point=circle.get_center()),
            run_time=0.8
        )
        label_0_final = MathTex("0", font_size=24).next_to(hand, DOWN)
        self.play(ReplacementTransform(label_5_final, label_0_final))
        self.wait(1)

        # Final explanation
        final_text = Text("Numbers repeat in cycle: 0 → 1 → 2 → 3 → 4 → 5 → 6 → 0", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)

        self.play(FadeOut(final_text), FadeOut(circle), FadeOut(marks), FadeOut(hand))
