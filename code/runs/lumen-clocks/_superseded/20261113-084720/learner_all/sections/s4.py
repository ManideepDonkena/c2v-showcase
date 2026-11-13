from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Full Cycle", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Clock setup: 7 marks around a circle
        radius = 2.5
        center = ORIGIN
        marks = []
        for i in range(7):
            angle = TAU * i / 7
            mark = Dot(color=WHITE).move_to(center + radius * (RIGHT * np.cos(angle) + UP * np.sin(angle)))
            label = MathTex(str(i), font_size=24).move_to(center + 1.3 * (RIGHT * np.cos(angle) + UP * np.sin(angle)))
            marks.append((mark, label))

        # Draw circle and marks
        circle = Circle(radius=radius, color=WHITE)
        self.play(Create(circle))
        for mark, label in marks:
            self.play(FadeIn(mark), Write(label))
        self.wait(0.5)

        # Show 7 ticks: 0→2→4→6→1→3→5→0
        hand = Dot(color=YELLOW)
        start_pos = marks[0][0]
        hand.move_to(start_pos)
        self.play(FadeIn(hand))
        self.wait(0.5)

        # Animate the full cycle
        positions = [0, 2, 4, 6, 1, 3, 5]
        for i in range(len(positions)):
            next_mark = marks[positions[i]]
            self.play(hand.animate.move_to(next_mark[0]), run_time=0.5)
            self.wait(0.2)

        # Return to start
        self.play(hand.animate.move_to(marks[0][0]), run_time=0.5)
        self.wait(0.5)
        # Add checkmarks next to each visited mark
        for i in positions:
            check = Text("✓", font_size=30).next_to(marks[i][1], RIGHT, buff=0.2)
            self.play(Write(check))
            self.wait(0.2)
        check_start = Text("✓", font_size=30).next_to(marks[0][1], RIGHT, buff=0.2)
        check_start.shift(0.39 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(check_start))
        self.wait(0.5)

        # Narration text
        narration = Text("After exactly seven ticks, the hand returns to its starting position.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.0)
        self.play(FadeOut(narration))

        # Show 5 + 2 = 7 wraps to 0
        self.play(hand.animate.move_to(marks[5][0]))
        self.wait(0.5)
        move_text = Text("From 5, add 2 marks: 5 plus 2 is 7, which wraps around to 0.", font_size=24)
        move_text.to_edge(DOWN)
        self.play(Write(move_text))
        self.wait(1.0)
        self.play(FadeOut(move_text))

        # Show 3 + 2 = 5
        self.play(hand.animate.move_to(marks[3][0]))
        self.wait(0.5)
        self.play(hand.animate.move_to(marks[5][0]))
        label_5 = Text("Mark 5", font_size=24).next_to(marks[5][1], UP, buff=0.2)
        self.play(Write(label_5))
        self.wait(1.0)
        self.play(FadeOut(label_5))

        # Show wraparound: circle has only 7 positions
        self.play(hand.animate.move_to(marks[6][0]))
        self.wait(0.5)
        self.play(hand.animate.move_to(marks[0][0]))
        self.wait(0.5)

        # Demonstrate that +2 works from any starting point
        self.play(hand.animate.move_to(marks[1][0]))
        self.wait(0.5)
        self.play(hand.animate.move_to(marks[3][0]))
        self.wait(0.5)

        # Show 6-mark clock (0-5) with only even numbers visited
        self.play(FadeOut(circle), *[FadeOut(m[0]) for m in marks], *[FadeOut(m[1]) for m in marks])
        self.wait(0.5)
        radius_6 = 2.0
        center_6 = ORIGIN
        marks_6 = []
        for i in range(6):
            angle = TAU * i / 6
            mark = Dot(color=WHITE).move_to(center_6 + radius_6 * (RIGHT * np.cos(angle) + UP * np.sin(angle)))
            label = MathTex(str(i), font_size=24).move_to(center_6 + 1.3 * (RIGHT * np.cos(angle) + UP * np.sin(angle)))
            marks_6.append((mark, label))

        circle_6 = Circle(radius=radius_6, color=WHITE)
        circle_6.shift(-0.21 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Create(circle_6))
        for mark, label in marks_6:
            self.play(FadeIn(mark), Write(label))
        self.wait(0.5)

        hand_6 = Dot(color=YELLOW)
        hand_6.move_to(marks_6[0][0])
        self.play(FadeIn(hand_6))
        self.wait(0.5)

        # 0→2→4→0
        positions_6 = [0, 2, 4]
        for i in range(len(positions_6)):
            next_mark = marks_6[positions_6[i]]
            self.play(hand_6.animate.move_to(next_mark[0]), run_time=0.5)
            self.wait(0.2)

        # Return to start
        self.play(hand_6.animate.move_to(marks_6[0][0]), run_time=0.5)
        self.wait(0.5)

        # Show odd numbers not visited
        for i in range(6):
            if i % 2 == 1:
                label = marks_6[i][1]
                cross = Cross(label, color=RED)
                self.play(Create(cross))
                self.wait(0.3)
        self.wait(0.5)

        # Show cumulative distance: 7 jumps of size 2 = 14 total
        self.play(FadeOut(circle_6), *[FadeOut(m[0]) for m in marks_6], *[FadeOut(m[1]) for m in marks_6])
        self.wait(0.5)

        # Number line or stack of blocks
        block_size = 0.4
        total_length = 14
        num_blocks = int(total_length / block_size)
        blocks = VGroup()
        for i in range(num_blocks):
            b = Rectangle(width=block_size, height=block_size, color=BLUE).move_to(LEFT * (total_length/2 - i*block_size))
            blocks.add(b)
        blocks.to_edge(DOWN)
        self.play(Create(blocks))
        self.wait(0.5)

        # Show 14 = 2 × 7
        eq = MathTex("14 = 2 \\times 7", font_size=30).next_to(blocks, UP, buff=0.5)
        self.play(Write(eq))
        self.wait(1.0)
        self.play(FadeOut(eq), FadeOut(blocks))

        # Final summary
        summary = Text("The +2 rule visits all marks and returns after 7 steps.", font_size=24).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(1.5)
        self.play(FadeOut(summary))
        self.play(FadeOut(title))
