from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Symmetry Rule", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First pair of rectangles: 4x2 and 2x4
        rect1 = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.3).move_to(LEFT * 2)
        rect2 = Rectangle(width=2, height=4, color=GREEN, fill_opacity=0.3).move_to(RIGHT * 2)

        # Labels
        label1 = Text("4×2", font_size=24).next_to(rect1, DOWN)
        label2 = Text("2×4", font_size=24).next_to(rect2, DOWN)

        # Point counts
        inside1 = MathTex(r"(w-1)(h-1) = (4-1)(2-1) = 3 \cdot 1 = 3", font_size=24)
        edge1 = MathTex(r"2(w+h) = 2(4+2) = 12", font_size=24)
        count1 = MathTex(r"\text{Sorrel Count} = 3 - 12 = -9", font_size=24)

        inside2 = MathTex(r"(w-1)(h-1) = (2-1)(4-1) = 1 \cdot 3 = 3", font_size=24)
        edge2 = MathTex(r"2(w+h) = 2(2+4) = 12", font_size=24)
        count2 = MathTex(r"\text{Sorrel Count} = 3 - 12 = -9", font_size=24)

        # Show rectangles and labels
        self.play(Create(rect1), Create(rect2), Write(label1), Write(label2))
        self.wait(1)

        # Show point counts for first rectangle
        inside1.next_to(rect1, UP)
        edge1.next_to(inside1, DOWN)
        count1.next_to(edge1, DOWN)
        self.play(Write(inside1), Write(edge1), Write(count1))
        self.wait(1.5)

        # Fade out first set of calculations
        self.play(FadeOut(inside1), FadeOut(edge1), FadeOut(count1))

        # Show point counts for second rectangle
        inside2.next_to(rect2, UP)
        edge2.next_to(inside2, DOWN)
        count2.next_to(edge2, DOWN)
        self.play(Write(inside2), Write(edge2), Write(count2))
        self.wait(1.5)

        # Fade out second set of calculations
        self.play(FadeOut(inside2), FadeOut(edge2), FadeOut(count2))

        # Show final comparison
        final_text = Text("Sorrel Count = -9", font_size=30).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1)

        # Highlight that both are equal
        highlight1 = SurroundingRectangle(rect1, color=YELLOW, buff=0.1)
        highlight2 = SurroundingRectangle(rect2, color=YELLOW, buff=0.1)
        self.play(Create(highlight1), Create(highlight2))
        self.wait(1)

        # Fade out everything
        self.play(FadeOut(highlight1), FadeOut(highlight2), FadeOut(final_text), FadeOut(rect1), FadeOut(rect2), FadeOut(label1), FadeOut(label2))

        # Show the algebraic invariance
        algebra = MathTex(r"(w-1)(h-1) - 2(w+h)", font_size=30)
        swap = MathTex(r"= (h-1)(w-1) - 2(h+w)", font_size=30)
        self.play(Write(algebra))
        self.wait(1)
        self.play(Transform(algebra, swap))
        self.wait(1.5)

        # Final narration text
        narration = Text("Swapping width and height preserves the sorrel count.", font_size=24).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)

        self.play(FadeOut(algebra), FadeOut(narration), FadeOut(title))
