from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Symmetry Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial rectangle 4x2
        rect1 = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.3).move_to(LEFT * 2)
        label1 = MathTex("4 \\times 2", font_size=24).next_to(rect1, DOWN)
        self.play(Create(rect1), Write(label1))
        self.wait(0.5)

        # Inside points count
        inside_count1 = MathTex("(w-1)(h-1) = (4-1)(2-1) = 3 \\times 1 = 3", font_size=24)
        inside_count1.next_to(rect1, LEFT, buff=0.5)
        self.play(Write(inside_count1))
        self.wait(1)

        # Edge points count
        edge_count1 = MathTex("2(w+h) = 2(4+2) = 12", font_size=24)
        edge_count1.next_to(inside_count1, DOWN)
        self.play(Write(edge_count1))
        self.wait(1)

        # Sorrel count calculation
        sorrel1 = MathTex("\\text{Sorrel Count} = 3 - 12 = -9", font_size=24)
        sorrel1.next_to(edge_count1, DOWN)
        self.play(Write(sorrel1))
        self.wait(1.5)

        # Rotate to 2x4
        rect2 = Rectangle(width=2, height=4, color=GREEN, fill_opacity=0.3).move_to(RIGHT * 2)
        label2 = MathTex("2 \\times 4", font_size=24).next_to(rect2, DOWN)
        self.play(Transform(rect1, rect2), Transform(label1, label2))
        self.wait(0.5)

        # Inside points count for 2x4
        inside_count2 = MathTex("(w-1)(h-1) = (2-1)(4-1) = 1 \\times 3 = 3", font_size=24)
        inside_count2.next_to(rect2, LEFT, buff=0.5)
        self.play(Write(inside_count2))
        self.wait(1)

        # Edge points count for 2x4
        edge_count2 = MathTex("2(w+h) = 2(2+4) = 12", font_size=24)
        edge_count2.next_to(inside_count2, DOWN)
        self.play(Write(edge_count2))
        self.wait(1)

        # Sorrel count for 2x4
        sorrel2 = MathTex("\\text{Sorrel Count} = 3 - 11 = -8", font_size=24)
        sorrel2.next_to(edge_count2, DOWN)
        self.play(Write(sorrel2))
        self.wait(1.5)

        # Highlight that both are equal
        equal_text = Text("Sorrel Counts Equal!", font_size=24).set_color(YELLOW).next_to(sorrel1, DOWN, buff=0.5)
        self.play(Write(equal_text))
        self.wait(1.5)

        # Show symmetry rule
        symmetry_rule = Text("Swapping width and height preserves the sorrel count.", font_size=24)
        symmetry_rule.to_edge(DOWN)
        self.play(Write(symmetry_rule))
        self.wait(1.5)

        # Final algebraic explanation
        algebra = MathTex("\\text{Expression: } (w-1)(h-1) - 2(w+h)", font_size=24)
        algebra.next_to(symmetry_rule, UP)
        self.play(Write(algebra))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(rect1),
            FadeOut(label1),
            FadeOut(inside_count1),
            FadeOut(edge_count1),
            FadeOut(sorrel1),
            FadeOut(rect2),
            FadeOut(label2),
            FadeOut(inside_count2),
            FadeOut(edge_count2),
            FadeOut(sorrel2),
            FadeOut(equal_text),
            FadeOut(symmetry_rule),
            FadeOut(algebra),
            FadeOut(title)
        )
        self.wait(0.5)
