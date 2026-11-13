from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Full Cycle", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Clock setup
        circle = Circle(radius=2.5, color=WHITE)
        marks = VGroup()
        for i in range(7):
            angle = 2 * PI * i / 7
            mark = MathTex(str(i), font_size=24)
            mark.move_to(circle.point_at_angle(angle))
            marks.add(mark)

        marks.shift(0.2 * RIGHT + 0.0 * UP)  # layout: separation vector
        marks.shift(0.0 * RIGHT + 0.3 * UP)  # layout: separation vector
        self.play(Create(circle), Write(marks))
        self.wait(0.5)

        # Initial hand at 0
        hand = Arrow(start=circle.get_center(), end=circle.get_center() + UP * 2.5, color=YELLOW)
        self.play(GrowArrow(hand))
        self.wait(0.5)

        # Animation of ticks: 0→2→4→6→1→3→5→0
        positions = [0, 2, 4, 6, 1, 3, 5]
        checkmarks = VGroup()
        
        for i, pos in enumerate(positions):
            # Move hand to next position
            angle = 2 * PI * pos / 7
            target_point = circle.get_center() + rotate_vector(UP * 2.5, angle)
            self.play(hand.animate.move_to(target_point), run_time=0.3)
            self.wait(0.1)

            # Add checkmark next to visited number
            mark_text = marks[pos]
            check = Text("✓", color=GREEN, font_size=24).next_to(mark_text, RIGHT)
            self.play(Write(check))
            checkmarks.add(check)
            self.wait(0.1)

        # Final checkmark at 0
        angle = 2 * PI * 0 / 7
        target_point = circle.get_center() + rotate_vector(UP * 2.5, angle)
        self.play(hand.animate.move_to(target_point), run_time=0.3)
        self.wait(0.1)

        # Key text overlay
        key_text = Text("After exactly seven ticks...", font_size=24).to_edge(DOWN)
        self.play(Write(key_text))
        self.wait(1.0)

        # Fade out key text
        self.play(FadeOut(key_text))

        # Show that all marks were visited
        all_visited = Text("Every mark from 0 to 6 is visited", font_size=24).to_edge(DOWN)
        self.play(Write(all_visited))
        self.wait(1.5)

        self.play(FadeOut(all_visited), FadeOut(title), FadeOut(circle), FadeOut(marks), FadeOut(hand), FadeOut(checkmarks))
