from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Asymmetric Grid", font_size=36).to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # Grid setup
        grid = NumberPlane(
            x_range=[-4, 5, 1],
            y_range=[-2, 3, 1],
            axis_config={"stroke_width": 1},
            background_line_style={"stroke_width": 1}
        )
        grid.scale(0.8)
        grid.to_edge(DOWN, buff=0.5)
        self.play(Create(grid))
        self.wait(0.5)

        # Points A and B
        A = Dot(grid.c2p(0, 0), color=BLUE)
        B = Dot(grid.c2p(1, 1), color=RED)
        label_A = Text("A", font_size=24).next_to(A, DOWN, buff=0.1)
        label_B = Text("B", font_size=24).next_to(B, UP, buff=0.1)

        self.play(FadeIn(A), FadeIn(label_A))
        self.wait(0.3)
        self.play(FadeIn(B), FadeIn(label_B))
        self.wait(0.5)

        # Horizontal arrow from A to B
        arrow_h = Arrow(grid.c2p(0, 0), grid.c2p(1, 0), color=YELLOW, buff=0)
        label_h = Text("Cost: 1", font_size=24).next_to(arrow_h, DOWN, buff=0.2)
        label_h.shift(0.0 * RIGHT + -0.27 * UP)  # layout: separation vector
        self.play(GrowArrow(arrow_h), Write(label_h))
        self.wait(1)

        # Vertical arrow from A to B
        arrow_v = Arrow(grid.c2p(1, 0), grid.c2p(1, 1), color=PURPLE, buff=0)
        label_v = Text("Cost: 2", font_size=24).next_to(arrow_v, RIGHT, buff=0.2)
        self.play(GrowArrow(arrow_v), Write(label_v))
        self.wait(1.5)

        # Fade out arrows and labels
        self.play(FadeOut(arrow_h), FadeOut(label_h), FadeOut(arrow_v), FadeOut(label_v))

        # Formula
        formula = MathTex(r"|x_1 - x_2| + 2 \times |y_1 - y_2|", font_size=40)
        formula.to_edge(UP, buff=0.8)
        self.play(FadeIn(formula))
        self.wait(1.5)

        # Narration text
        narration = Text("In quill distance, space is not uniform.", font_size=24)
        narration.to_edge(DOWN, buff=0.3)
        self.play(Write(narration))
        self.wait(1.5)

        self.play(FadeOut(narration))

        narration2 = Text("Moving sideways costs 1 unit.", font_size=24)
        narration2.to_edge(DOWN, buff=0.3)
        self.play(Write(narration2))
        self.wait(1.5)

        self.play(FadeOut(narration2))

        narration3 = Text("Moving up or down costs 2 units.", font_size=24)
        narration3.to_edge(DOWN, buff=0.3)
        self.play(Write(narration3))
        self.wait(1.5)

        self.play(FadeOut(narration3))

        # Final explanation
        explanation = Text("This creates a grid where vertical travel is twice as expensive.", font_size=24)
        explanation.to_edge(DOWN, buff=0.3)
        self.play(Write(explanation))
        self.wait(2)

        self.play(FadeOut(explanation), FadeOut(formula), FadeOut(A), FadeOut(B), FadeOut(label_A), FadeOut(label_B), FadeOut(grid), FadeOut(title))

        # New part: Central point and four specific points lighting up in sequence
        center = Dot(grid.c2p(0, 0), color=WHITE)
        self.play(FadeIn(center))
        self.wait(0.5)

        # Point 1: 6 units right (cost 6)
        point1 = Dot(grid.c2p(6, 0), color=GREEN)
        self.play(FadeIn(point1))
        self.wait(0.5)

        # Point 2: 6 units left (cost 6)
        point2 = Dot(grid.c2p(-6, 0), color=GREEN)
        self.play(FadeIn(point2))
        self.wait(0.5)

        # Point 3: 3 units up (cost 6)
        point3 = Dot(grid.c2p(0, 3), color=GREEN)
        self.play(FadeIn(point3))
        self.wait(0.5)

        # Point 4: 3 units down (cost 6)
        point4 = Dot(grid.c2p(0, -3), color=GREEN)
        self.play(FadeIn(point4))
        self.wait(0.5)

        # Narration for the new part
        narration_new = Text("Just as distance 2 required 2 sideways or 1 vertical step, distance 6 requires 6 sideways steps or 3 vertical steps.", font_size=24)
        narration_new.to_edge(DOWN, buff=0.3)
        self.play(Write(narration_new))
        self.wait(2)

        self.play(FadeOut(narration_new), FadeOut(point1), FadeOut(point2), FadeOut(point3), FadeOut(point4), FadeOut(center))
