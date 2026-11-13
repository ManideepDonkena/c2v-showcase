from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Lumen Circle", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Draw circle with 7 marks
        circle = Circle(radius=2.5, color=WHITE)
        self.play(Create(circle))
        self.wait(0.5)

        # Add tick marks and labels (0 to 6)
        ticks = VGroup()
        labels = VGroup()
        for i in range(7):
            angle = 90 - i * (360 / 7)  # Start from top (12 o'clock)
            x = 2.5 * np.cos(np.radians(angle))
            y = 2.5 * np.sin(np.radians(angle))
            tick = Line(start=(x, y, 0), end=(x, y + 0.1, 0), color=WHITE)
            label = MathTex(str(i), font_size=24).move_to((x, y + 0.3, 0))
            ticks.add(tick)
            labels.add(label)

        self.play(Write(ticks), Write(labels))
        self.wait(0.5)

        # Initial hand at mark 0
        hand = Arrow(start=(0, 0, 0), end=(0, 2.5, 0), color=YELLOW, tip_length=0.2)
        self.play(Create(hand))
        self.wait(0.5)

        # Narration: From 5, add 2 marks
        narration1 = Text("From 5, add 2 marks: 5 plus 2 is 7, which wraps around to 0.", font_size=24)
        narration1.to_edge(DOWN)
        self.play(Write(narration1))
        self.wait(0.5)

        # Move hand from 5 to 0 (jumping past 6)
        self.play(
            Rotate(hand, angle=-2*(360/7), about_point=ORIGIN),
            run_time=1
        )
        self.wait(0.5)
        self.play(FadeOut(narration1))

        # Show hand at mark 3, move to mark 5 (explicitly label destination)
        narration2 = Text("From 3, add 2 marks: 3 → 5", font_size=24)
        narration2.to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(0.5)

        # Move hand from 3 to 5
        self.play(
            Rotate(hand, angle=-2*(360/7), about_point=ORIGIN),
            run_time=1
        )
        self.wait(0.5)
        self.play(FadeOut(narration2))

        # Show that it's a cycle: 0 → 2 → 4 → 6 → 1 → 3 → 5 → 0
        narration3 = Text("The numbers repeat in a cycle, not linearly.", font_size=24)
        narration3.to_edge(DOWN)
        self.play(Write(narration3))
        self.wait(1)

        # Show jump from 1 to 3 (relative movement)
        self.play(
            Rotate(hand, angle=-1*(360/7), about_point=ORIGIN),
            run_time=0.5
        )
        self.play(
            Rotate(hand, angle=-2*(360/7), about_point=ORIGIN),
            run_time=0.5
        )
        self.wait(0.5)
        self.play(FadeOut(narration3))

        # Show 6-mark clock (0-5) and only even numbers visited
        self.play(FadeOut(circle, ticks, labels, hand))
        title2 = Text("Comparison: 6-Mark Clock", font_size=36).to_edge(UP)
        self.play(Write(title2))
        self.wait(0.5)

        circle6 = Circle(radius=2.5, color=WHITE)
        self.play(Create(circle6))
        self.wait(0.5)

        ticks6 = VGroup()
        labels6 = VGroup()
        for i in range(6):
            angle = 90 - i * (360 / 6)
            x = 2.5 * np.cos(np.radians(angle))
            y = 2.5 * np.sin(np.radians(angle))
            tick = Line(start=(x, y, 0), end=(x, y + 0.1, 0), color=WHITE)
            label = MathTex(str(i), font_size=24).move_to((x, y + 0.3, 0))
            ticks6.add(tick)
            labels6.add(label)

        self.play(Write(ticks6), Write(labels6))
        self.wait(0.5)

        hand6 = Arrow(start=(0, 0, 0), end=(0, 2.5, 0), color=YELLOW, tip_length=0.2)
        self.play(Create(hand6))
        self.wait(0.5)

        # Move 3 times: 0 → 2 → 4 → 0
        for i in range(3):
            self.play(
                Rotate(hand6, angle=-2*(360/6), about_point=ORIGIN),
                run_time=0.5
            )
            self.wait(0.5)

        narration4 = Text("Only even numbers visited: 0 → 2 → 4 → 0", font_size=24)
        narration4.to_edge(DOWN)
        self.play(Write(narration4))
        self.wait(1.5)
        self.play(FadeOut(title2, circle6, ticks6, labels6, hand6, narration4))

        # Show cumulative distance: 7 jumps of size 2 = 14 total
        # Stack of blocks or number line
        self.play(FadeIn(circle), FadeIn(ticks), FadeIn(labels))
        self.wait(0.5)

        # Show 7 jumps of +2
        hand = Arrow(start=(0, 0, 0), end=(0, 2.5, 0), color=YELLOW, tip_length=0.2)
        self.play(Create(hand))
        self.wait(0.5)

        # Simulate 7 jumps
        for i in range(7):
            self.play(
                Rotate(hand, angle=-2*(360/7), about_point=ORIGIN),
                run_time=0.5
            )
            self.wait(0.5)

        # Show total distance = 14 on a circle of size 7
        narration5 = Text("Total distance: 7 jumps × 2 = 14", font_size=24)
        narration5.to_edge(DOWN)
        self.play(Write(narration5))
        self.wait(1.5)

        # Show that 14 = 2 * 7
        eq = MathTex("14 = 2 \\times 7", font_size=30)
        eq.next_to(narration5, DOWN)
        self.play(Write(eq))
        self.wait(1.5)

        self.play(FadeOut(title, circle, ticks, labels, hand, narration5, eq))
        self.wait(0.5)
