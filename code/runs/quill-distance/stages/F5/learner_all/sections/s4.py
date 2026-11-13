from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Worked Example Calculation", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Points P and Q
        P = Dot([0, 0, 0], color=BLUE)
        Q = Dot([3, 2, 0], color=RED)
        label_P = Tex("(0,0)", font_size=24).next_to(P, DOWN)
        label_Q = Tex("(3,2)", font_size=24).next_to(Q, UR)

        self.play(FadeIn(P), FadeIn(Q), Write(label_P), Write(label_Q))
        self.wait(1)

        # Draw stepped path
        path = VGroup()
        # Horizontal segments (3)
        for i in range(3):
            segment = Line([i, 0, 0], [i+1, 0, 0], color=YELLOW)
            path.add(segment)
        # Vertical segments (2)
        for i in range(2):
            segment = Line([3, i, 0], [3, i+1, 0], color=YELLOW)
            path.add(segment)

        self.play(Create(path))
        self.wait(1)

        # Annotate horizontal segments
        h_labels = VGroup()
        for i in range(3):
            label = MathTex("1", font_size=24).move_to([i+0.5, -0.3, 0])
            h_labels.add(label)
        self.play(Write(h_labels))
        self.wait(1)

        # Annotate vertical segments
        v_labels = VGroup()
        for i in range(2):
            label = MathTex("2", font_size=24).move_to([3.3, i+0.5, 0])
            v_labels.add(label)
        self.play(Write(v_labels))
        self.wait(1)

        # Show total cost
        equation = MathTex("3 + 4 = 7", font_size=40).to_edge(DOWN)
        self.play(Write(equation))
        self.wait(2)

        # Fade out everything except title and final result
        self.play(
            FadeOut(path),
            FadeOut(h_labels),
            FadeOut(v_labels),
            FadeOut(P),
            FadeOut(Q),
            FadeOut(label_P),
            FadeOut(label_Q)
        )
        self.wait(1)

        # New part: Show central point and four specific points lighting up in sequence
        center = Dot([0, 0, 0], color=WHITE)
        self.play(FadeIn(center))
        self.wait(0.5)

        # Point 6 units right (cost 6+0=6)
        point1 = Dot([6, 0, 0], color=YELLOW)
        self.play(FadeIn(point1))
        self.wait(0.5)

        # Point 6 units left (cost 6+0=6)
        point2 = Dot([-6, 0, 0], color=YELLOW)
        self.play(FadeIn(point2))
        self.wait(0.5)

        # Point 3 units up (cost 0+6=6)
        point3 = Dot([0, 3, 0], color=YELLOW)
        point3.shift(0.0 * RIGHT + -0.23 * UP)  # layout: separation vector
        self.play(FadeIn(point3))
        self.wait(0.5)

        # Point 3 units down (cost 0+6=6)
        point4 = Dot([0, -3, 0], color=YELLOW)
        point4.shift(0.0 * RIGHT + 0.27 * UP)  # layout: separation vector
        self.play(FadeIn(point4))
        self.wait(0.5)

        # Say the explanation
        explanation = Text("Just as distance 2 required 2 sideways or 1 vertical step, distance 6 requires 6 sideways steps or 3 vertical steps.", font_size=24).to_edge(DOWN)
        explanation.shift(0.0 * RIGHT + 0.46 * UP)  # layout: separation vector
        self.play(Write(explanation))
        self.wait(3)

        # Fade out the explanation
        self.play(FadeOut(explanation))
        self.wait(1)
