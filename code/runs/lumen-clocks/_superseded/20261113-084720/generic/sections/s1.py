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

        # Add 7 tick marks and labels
        ticks = []
        labels = []
        for i in range(7):
            angle = 90 - i * (360 / 7)  # Start from top (90 degrees), go clockwise
            x = 2.5 * np.cos(np.radians(angle))
            y = 2.5 * np.sin(np.radians(angle))
            tick = Line(start=(x, y, 0), end=(x, y + 0.1, 0), color=WHITE)
            label = MathTex(str(i), font_size=24).move_to((x, y + 0.3, 0))
            ticks.append(tick)
            labels.append(label)
            self.play(Create(tick), Write(label))
            self.wait(0.1)

        # Initial hand at mark 0
        hand = Arrow(start=(0, 0, 0), end=(0, 2.5, 0), color=YELLOW, tip_length=0.2)
        self.play(Create(hand))
        self.wait(0.5)

        # Narration text: "Welcome to the Lumen clock..."
        welcome = Text("Welcome to the Lumen clock", font_size=24).to_edge(DOWN)
        self.play(Write(welcome))
        self.wait(1.5)
        self.play(FadeOut(welcome))

        # Show rules
        rule1 = Text("1. After 7 ticks, hand returns to start.", font_size=24)
        rule2 = Text("2. Hand visits every mark before returning.", font_size=24)
        example = Text("Example: 3 → 5 → 0", font_size=24)

        rule1.to_edge(LEFT).shift(UP * 1.5)
        rule2.next_to(rule1, DOWN)
        example.next_to(rule2, DOWN)

        rule1.shift(0.0 * RIGHT + 1.3 * UP)  # layout: separation vector
        self.play(Write(rule1))
        self.wait(1.5)
        self.play(Write(rule2))
        self.wait(1.5)
        self.play(Write(example))
        self.wait(2.0)

        # Move hand 2 ticks from mark 3 to 5
        self.play(hand.animate.rotate(-2 * (360 / 7), about_point=ORIGIN), run_time=1)
        self.wait(0.5)

        # Move hand 2 more ticks from 5 to 0
        self.play(hand.animate.rotate(-2 * (360 / 7), about_point=ORIGIN), run_time=1)
        self.wait(1.0)

        # Clear example and rules
        self.play(FadeOut(rule1, rule2, example))
        self.wait(0.5)

        # Final narration text
        final = Text("A lumen tick moves the hand forward by 2 marks.", font_size=24).to_edge(DOWN)
        self.play(Write(final))
        self.wait(2.0)
        self.play(FadeOut(final))

        self.wait(1.0)
