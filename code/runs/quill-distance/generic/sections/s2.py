from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Symmetry and Direction", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid points A and B
        A = Dot([0, 0, 0], color=BLUE)
        B = Dot([2, 1, 0], color=RED)
        label_A = Tex("A").next_to(A, DOWN)
        label_B = Tex("B").next_to(B, UP)

        # Draw grid and points
        self.play(Create(A), Create(B), Write(label_A), Write(label_B))
        self.wait(1)

        # Path from A to B: 2 right + 1 up
        path1 = Line(A.get_center(), [2, 0, 0], color=YELLOW)
        path2 = Line([2, 0, 0], B.get_center(), color=YELLOW)
        self.play(Create(path1), Create(path2))
        self.wait(1)

        # Cost calculation: 2 + 2 = 4
        cost_text = MathTex("2 + 2 = 4", font_size=30).next_to(B, RIGHT)
        self.play(Write(cost_text))
        self.wait(1.5)

        # Reverse path from B to A
        reverse_path1 = Line(B.get_center(), [2, 0, 0], color=GREEN)
        reverse_path2 = Line([2, 0, 0], A.get_center(), color=GREEN)
        self.play(Create(reverse_path1), Create(reverse_path2))
        self.wait(1)

        # Cost again: 2 + 2 = 4
        cost_text_rev = MathTex("2 + 2 = 4", font_size=30).next_to(A, LEFT)
        self.play(ReplacementTransform(cost_text, cost_text_rev))
        self.wait(1.5)

        # Show symmetry: d(A,B) = d(B,A)
        symm_eq = MathTex("d(A,B) = d(B,A)", font_size=40).to_edge(UP)
        self.play(ReplacementTransform(title, symm_eq))
        self.wait(2)

        # Narration text
        narration1 = Text("Despite the vertical cost,", font_size=24).to_edge(DOWN)
        narration2 = Text("quill distance is symmetric.", font_size=24).next_to(narration1, DOWN)
        self.play(Write(narration1))
        self.wait(1)
        narration2.shift(0.0 * RIGHT + 0.23 * UP)  # layout: separation vector
        self.play(Write(narration2))
        self.wait(2)

        # Clear narration
        self.play(FadeOut(narration1), FadeOut(narration2))

        # New rule explanation
        rule1 = Text("Rule 1: Quill distance is symmetric", font_size=28).to_edge(UP)
        self.play(ReplacementTransform(symm_eq, rule1))
        self.wait(1)

        # Definition and example
        definition = MathTex(r"d(A,B) = |x_1 - x_2| + 2 \cdot |y_1 - y_2|", font_size=30).next_to(rule1, DOWN)
        self.play(Write(definition))
        self.wait(2)

        # Example: from (0,0) to (3,2)
        example = MathTex("d((0,0), (3,2)) = 3 + 4 = 7", font_size=30).next_to(definition, DOWN)
        self.play(Write(example))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(A), FadeOut(B), FadeOut(label_A), FadeOut(label_B),
                  FadeOut(path1), FadeOut(path2), FadeOut(reverse_path1), FadeOut(reverse_path2),
                  FadeOut(cost_text_rev), FadeOut(definition), FadeOut(example), FadeOut(rule1))
        self.wait(0.5)
