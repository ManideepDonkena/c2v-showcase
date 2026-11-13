from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Wrapping Around", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Clock setup: 7 marks (0-6) in a circle
        radius = 2.5
        center = ORIGIN
        marks = []
        for i in range(7):
            angle = TAU * i / 7
            mark = Dot(color=WHITE).move_to(center + radius * UR * np.cos(angle) + radius * UL * np.sin(angle))
            label = MathTex(str(i), font_size=24).move_to(center + 1.3 * UR * np.cos(angle) + 1.3 * UL * np.sin(angle))
            marks.append((mark, label))

        clock_group = VGroup(*[m[0] for m in marks], *[m[1] for m in marks])
        clock_group.shift(0.0 * RIGHT + 0.22 * UP)  # layout: separation vector
        self.play(Create(clock_group))
        self.wait(0.5)

        # Hand
        hand = Arrow(start=ORIGIN, end=UP * 0.8, color=YELLOW, tip_length=0.2)
        hand.move_to(center + radius * UR * np.cos(TAU * 3 / 7) + radius * UL * np.sin(TAU * 3 / 7))
        self.play(GrowArrow(hand))
        self.wait(0.5)

        # First example: 3 → 5 → 0
        narration1 = Text("3 → 5 → 0", font_size=24).to_edge(DOWN)
        self.play(Write(narration1))
        self.wait(0.5)

        # Tick 1: 3 → 5
        angle1 = TAU * 3 / 7
        angle2 = TAU * 5 / 7
        self.play(
            hand.animate.move_to(center + radius * UR * np.cos(angle2) + radius * UL * np.sin(angle2)),
            run_time=0.8
        )
        self.wait(0.5)

        # Tick 2: 5 → 0 (wrap around)
        angle3 = TAU * 0 / 7
        self.play(
            hand.animate.move_to(center + radius * UR * np.cos(angle3) + radius * UL * np.sin(angle3)),
            run_time=0.8
        )
        self.wait(0.5)

        # Narration: "From 5, add 2 marks: 5 plus 2 is 7, which wraps around to 0."
        narration2 = Text("From 5, add 2 marks: 5 plus 2 is 7, which wraps around to 0.", font_size=24).to_edge(DOWN)
        narration2.shift(0.0 * RIGHT + -0.18 * UP)  # layout: separation vector
        self.play(ReplacementTransform(narration1, narration2))
        self.wait(0.5)

        # Reset hand to 5
        self.play(
            hand.animate.move_to(center + radius * UR * np.cos(TAU * 5 / 7) + radius * UL * np.sin(TAU * 5 / 7)),
            run_time=0.5
        )
        self.wait(0.5)

        # Show that 3 → 5 (explicitly label)
        mark5_label = MathTex("Mark 5", font_size=24).next_to(marks[5][1], DOWN)
        self.play(Write(mark5_label))
        self.wait(0.5)

        # Tick to 0 again
        self.play(
            hand.animate.move_to(center + radius * UR * np.cos(angle3) + radius * UL * np.sin(angle3)),
            run_time=0.8
        )
        self.wait(0.5)

        # Show that the circle has only 7 positions (0–6)
        self.play(FadeOut(mark5_label))
        self.wait(0.5)

        # Demonstrate +2 rule from any starting point: start at 1, go to 3
        self.play(
            hand.animate.move_to(center + radius * UR * np.cos(TAU * 1 / 7) + radius * UL * np.sin(TAU * 1 / 7)),
            run_time=0.5
        )
        self.wait(0.5)

        angle4 = TAU * 3 / 7
        self.play(
            hand.animate.move_to(center + radius * UR * np.cos(angle4) + radius * UL * np.sin(angle4)),
            run_time=0.8
        )
        self.wait(0.5)

        # Show that the movement is relative to current position
        narration3 = Text("Movement is relative to current position", font_size=24).to_edge(DOWN)
        narration3.shift(0.0 * RIGHT + -0.18 * UP)  # layout: separation vector
        self.play(ReplacementTransform(narration2, narration3))
        self.wait(0.5)

        # Show clock with 6 marks (0–5) and only even numbers visited
        self.play(FadeOut(hand), FadeOut(clock_group), FadeOut(narration3))
        self.wait(0.5)

        # New clock: 6 marks (0–5)
        radius2 = 2.0
        center2 = ORIGIN
        marks6 = []
        for i in range(6):
            angle = TAU * i / 6
            mark = Dot(color=WHITE).move_to(center2 + radius2 * UR * np.cos(angle) + radius2 * UL * np.sin(angle))
            label = MathTex(str(i), font_size=24).move_to(center2 + 1.3 * UR * np.cos(angle) + 1.3 * UL * np.sin(angle))
            marks6.append((mark, label))

        clock6_group = VGroup(*[m[0] for m in marks6], *[m[1] for m in marks6])
        self.play(Create(clock6_group))
        self.wait(0.5)

        hand6 = Arrow(start=ORIGIN, end=UP * 0.8, color=YELLOW, tip_length=0.2)
        hand6.move_to(center2 + radius2 * UR * np.cos(TAU * 0 / 6) + radius2 * UL * np.sin(TAU * 0 / 6))
        self.play(GrowArrow(hand6))
        self.wait(0.5)

        # Visit only even numbers: 0 → 2 → 4 → 0
        angles6 = [TAU * i / 6 for i in [0, 2, 4, 0]]
        for i in range(3):
            self.play(
                hand6.animate.move_to(center2 + radius2 * UR * np.cos(angles6[i+1]) + radius2 * UL * np.sin(angles6[i+1])),
                run_time=0.8
            )
            self.wait(0.5)

        # Show odd numbers are missed
        narration4 = Text("Only even numbers visited", font_size=24).to_edge(DOWN)
        narration4.shift(0.0 * RIGHT + -0.18 * UP)  # layout: separation vector
        self.play(Write(narration4))
        self.wait(0.5)

        # Back to 7-mark clock
        self.play(FadeOut(hand6), FadeOut(clock6_group), FadeOut(narration4))
        self.wait(0.5)

        # Show cumulative distance: 7 jumps of size 2 = 14 total, fits exactly twice on circle of size 7
        self.play(Create(clock_group))
        self.wait(0.5)

        hand = Arrow(start=ORIGIN, end=UP * 0.8, color=YELLOW, tip_length=0.2)
        hand.move_to(center + radius * UR * np.cos(TAU * 3 / 7) + radius * UL * np.sin(TAU * 3 / 7))
        self.play(GrowArrow(hand))
        self.wait(0.5)

        # Stack of blocks to show total distance
        block1 = Rectangle(height=0.4, width=0.8, color=BLUE).shift(LEFT * 2 + DOWN * 1)
        block2 = Rectangle(height=0.4, width=0.8, color=BLUE).next_to(block1, RIGHT, buff=0)
        block3 = Rectangle(height=0.4, width=0.8, color=BLUE).next_to(block2, RIGHT, buff=0)
        block4 = Rectangle(height=0.4, width=0.8, color=BLUE).next_to(block3, RIGHT, buff=0)
        block5 = Rectangle(height=0.4, width=0.8, color=BLUE).next_to(block4, RIGHT, buff=0)
        block6 = Rectangle(height=0.4, width=0.8, color=BLUE).next_to(block5, RIGHT, buff=0)
        block7 = Rectangle(height=0.4, width=0.8, color=BLUE).next_to(block6, RIGHT, buff=0)

        blocks = VGroup(block1, block2, block3, block4, block5, block6, block7)
        self.play(Write(blocks))
        self.wait(0.5)

        total_distance = MathTex("7 \\times 2 = 14", font_size=30).next_to(blocks, UP)
        self.play(Write(total_distance))
        self.wait(0.5)

        # Show that 14 fits exactly twice on a circle of size 7
        self.play(
            hand.animate.move_to(center + radius * UR * np.cos(TAU * 0 / 7) + radius * UL * np.sin(TAU * 0 / 7)),
            run_time=1.2
        )
        self.wait(0.5)

        # Final text
        final_text = Text("You complete two full loops and land back at start", font_size=24).to_edge(DOWN)
        final_text.shift(0.0 * RIGHT + -0.18 * UP)  # layout: separation vector
        self.play(Write(final_text))
        self.wait(1.0)

        self.play(FadeOut(title, clock_group, hand, blocks, total_distance, final_text))
        self.wait(0.5)
