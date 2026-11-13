from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Full Cycle", font_size=36).to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # Lumen clock setup
        radius = 2.5
        center = ORIGIN
        marks = []
        for i in range(7):
            angle = TAU * i / 7
            mark_point = center + radius * (RIGHT * np.cos(angle) + UP * np.sin(angle))
            marks.append(mark_point)

        # Draw circle and marks
        circle = Circle(radius=radius, color=WHITE)
        self.play(Create(circle))

        mark_labels = VGroup()
        for i, point in enumerate(marks):
            label = Text(str(i), font_size=24).move_to(point)  # Changed MathTex to Text
            mark_labels.add(label)
        mark_labels.shift(0.23 * RIGHT + 0.0 * UP)  # layout: separation vector
        mark_labels.shift(0.0 * RIGHT + 0.33 * UP)  # layout: separation vector
        self.play(Write(mark_labels))
        self.wait(0.5)

        # Hand starting at 0
        hand = Arrow(start=center, end=marks[0], color=YELLOW, buff=0)
        self.play(GrowArrow(hand))
        self.wait(0.5)

        # Animation of ticks
        current_mark = 0
        visited_marks = [0]

        for i in range(7):
            next_mark = (current_mark + 2) % 7
            self.play(
                hand.animate.put_start_and_end_on(center, marks[next_mark]),
                run_time=0.4
            )
            current_mark = next_mark
            visited_marks.append(current_mark)

        # Show checkmarks
        checkmarks = VGroup()
        for i, mark in enumerate(visited_marks):
            check = Text("✓", font_size=30).next_to(mark_labels[mark], DOWN, buff=0.2)  # Changed Tex to Text
            checkmarks.add(check)
            self.play(Write(check))
            self.wait(0.2)

        # Narration text
        narration = Text("After exactly seven ticks...", font_size=24).to_edge(DOWN, buff=0.3)
        self.play(Write(narration))
        self.wait(1.5)

        # Clear narration and show final message
        self.play(FadeOut(narration))

        final_text = Text("Every mark visited before cycle repeats", font_size=24).to_edge(DOWN, buff=0.3)
        self.play(Write(final_text))
        self.wait(1.5)

        # Cleanup
        self.play(FadeOut(title, circle, mark_labels, hand, checkmarks, final_text))
