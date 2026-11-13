from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Full Cycle", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Lumen clock setup
        circle = Circle(radius=2.5, color=WHITE)
        marks = VGroup()
        for i in range(7):
            angle = 2 * PI * i / 7
            mark = Tex(str(i), font_size=24).move_to(circle.point_at_angle(angle))
            marks.add(mark)
        
        clock_group = VGroup(circle, marks)
        marks.shift(0.2 * RIGHT + 0.0 * UP)  # layout: separation vector
        marks.shift(0.0 * RIGHT + 0.3 * UP)  # layout: separation vector
        self.play(Create(circle), Write(marks))

        # Initial hand at 0
        hand = Arrow(start=circle.get_center(), end=circle.point_at_angle(0), color=YELLOW, buff=0)
        self.play(GrowArrow(hand))
        self.wait(0.5)
        # Animation of ticks: 0→2→4→6→1→3→5→0
        tick_labels = []
        for i in range(7):
            angle = 2 * PI * i / 7
            label = Tex(str(i), font_size=24).move_to(circle.point_at_angle(angle))
            # Adjust position to avoid overlap with circle
            if i == 0:
                label.shift(UP * 0.3)
            elif i == 1:
                label.shift(UP * 0.2 + RIGHT * 0.2)
            elif i == 2:
                label.shift(RIGHT * 0.3)
            elif i == 3:
                label.shift(DOWN * 0.2 + RIGHT * 0.2)
            elif i == 4:
                label.shift(DOWN * 0.3)
            elif i == 5:
                label.shift(DOWN * 0.2 + LEFT * 0.2)
            elif i == 6:
                label.shift(LEFT * 0.3)
            tick_labels.append(label)

        # Start at 0
        start_mark = 0
        visited_marks = [start_mark]
        current = start_mark

        # Show the sequence of ticks
        self.play(Write(tick_labels[0]))
        self.wait(0.5)

        for i in range(7):
            next_mark = (current + 2) % 7
            current = next_mark
            
            # Animate hand movement
            target_angle = 2 * PI * current / 7
            self.play(
                hand.animate.put_start_and_end_on(
                    circle.get_center(),
                    circle.point_at_angle(target_angle)
                ),
                run_time=0.5
            )
            
            # Show the mark just visited
            if i < 6:
                self.play(Write(tick_labels[current]))
            else:
                # On last tick, show checkmarks
                self.play(Write(tick_labels[current]))
                self.wait(0.3)
                
                # Add checkmarks next to each visited mark
                for j in range(7):
                    check = Tex(r"\checkmark", color=GREEN, font_size=24).next_to(tick_labels[j], RIGHT, buff=0.1)
                    self.play(Write(check), run_time=0.3)
            visited_marks.append(current)

        # Narration text
        narration = Text("After exactly seven ticks...", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1.5)

        # Clear narration and show final point
        self.play(FadeOut(narration))

        final_text = Text("Every mark visited before cycle repeats", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2.0)

        self.play(FadeOut(final_text), FadeOut(title), FadeOut(clock_group), FadeOut(hand))
