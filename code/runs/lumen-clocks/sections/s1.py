from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Lumen Circle", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Draw circle
        circle = Circle(radius=2.5, color=WHITE)
        self.play(Create(circle))
        self.wait(0.5)

        # Create tick marks and labels
        ticks = VGroup()
        labels = VGroup()
        for i in range(7):
            angle = 90 - i * (360 / 7)  # Start from top (90 degrees), go clockwise
            x = 2.5 * np.cos(np.radians(angle))
            y = 2.5 * np.sin(np.radians(angle))
            tick = Line(start=(x, y, 0), end=(x, y + 0.1, 0), color=WHITE)
            label = MathTex(str(i), font_size=24).move_to((x, y + 0.3, 0))
            ticks.add(tick)
            labels.add(label)

        self.play(Write(ticks), Write(labels))
        self.wait(0.5)

        # Initial hand pointing to 0
        hand = Arrow(start=(0, 0, 0), end=(0, 2.5, 0), color=YELLOW, tip_length=0.2)
        self.play(GrowArrow(hand))
        self.wait(0.5)

        # Narration text
        welcome_text = Text("Welcome to the Lumen clock", font_size=24).to_edge(DOWN)
        self.play(Write(welcome_text))
        self.wait(1.0)
        self.play(FadeOut(welcome_text))

        # Show structure
        structure_text = Text("7 marks, 0 to 6, in a circle", font_size=24).to_edge(DOWN)
        self.play(Write(structure_text))
        self.wait(1.5)
        self.play(FadeOut(structure_text))

        # Fade out everything except title and circle
        self.play(FadeOut(ticks), FadeOut(labels), FadeOut(hand))
        self.wait(0.5)

        # Show rules
        rule1 = Text("1. After 7 ticks, hand returns to start", font_size=24).to_edge(DOWN)
        self.play(Write(rule1))
        self.wait(1.5)
        self.play(FadeOut(rule1))

        rule2 = Text("2. Visits every mark before returning", font_size=24).to_edge(DOWN)
        self.play(Write(rule2))
        self.wait(1.5)
        self.play(FadeOut(rule2))

        # Example: from 3, two ticks go 3 → 5 → 0
        example_text = Text("Example: from 3, two ticks", font_size=24).to_edge(DOWN)
        self.play(Write(example_text))
        self.wait(1.0)
        self.play(FadeOut(example_text))

        # Reintroduce hand at 3
        hand3 = Arrow(start=(0, 0, 0), end=(0, 2.5, 0), color=YELLOW, tip_length=0.2)
        self.play(GrowArrow(hand3))
        self.wait(0.5)

        # Move hand two ticks (2 steps of 2 each = 4 total positions)
        # From 3, move clockwise by 2: 3 -> 5
        angle_3_to_5 = 90 - 5 * (360 / 7)  # 5 is index
        x5 = 2.5 * np.cos(np.radians(angle_3_to_5))
        y5 = 2.5 * np.sin(np.radians(angle_3_to_5))
        self.play(hand3.animate.put_start_and_end_on((0, 0, 0), (x5, y5, 0)))
        self.wait(0.5)

        # From 5, move clockwise by 2: 5 -> 0
        angle_5_to_0 = 90 - 0 * (360 / 7)  # 0 is index
        x0 = 2.5 * np.cos(np.radians(angle_5_to_0))
        y0 = 2.5 * np.sin(np.radians(angle_5_to_0))
        self.play(hand3.animate.put_start_and_end_on((0, 0, 0), (x0, y0, 0)))
        self.wait(1.0)

        # Final fade out
        self.play(FadeOut(title), FadeOut(circle), FadeOut(hand3))
        self.wait(0.5)
