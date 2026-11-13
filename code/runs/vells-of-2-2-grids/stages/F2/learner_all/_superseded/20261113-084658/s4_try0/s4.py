from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Rule: Swapping b and c", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial grid
        grid1 = Matrix([[2, 1], [3, 4]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        grid1_label = Text("Original Grid", font_size=24).next_to(grid1, DOWN)
        self.play(Write(grid1), Write(grid1_label))
        self.wait(1)

        # Vell calculation for original
        vell1 = MathTex("2 \\times 4 - 1 - 3 = 8 - 1 - 3 = 4", font_size=30)
        vell1.next_to(grid1, DOWN, buff=1)
        self.play(Write(vell1))
        self.wait(1.5)

        # Swap b and c
        grid2 = Matrix([[2, 3], [1, 4]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        grid2_label = Text("After Swapping", font_size=24).next_to(grid2, DOWN)
        self.play(Transform(grid1, grid2), Transform(grid1_label, grid2_label))
        self.wait(1)

        # Vell calculation for swapped
        vell2 = MathTex("2 \\times 4 - 3 - 1 = 8 - 3 - 1 = 4", font_size=30)
        vell2.next_to(grid2, DOWN, buff=1)
        self.play(Write(vell2))
        self.wait(1.5)

        # Show equality
        equal = MathTex("a \\times d - b - c = a \\times d - c - b", font_size=30)
        equal.to_edge(DOWN)
        self.play(Write(equal))
        self.wait(1.5)

        # Final narration text
        rule_text = Text("Rule two states that swapping b and c keeps the vell unchanged.", font_size=24)
        rule_text.to_edge(BOTTOM)
        self.play(Write(rule_text))
        self.wait(2)

        self.play(FadeOut(title, grid1, grid2, grid1_label, grid2_label, vell1, vell2, equal, rule_text))
        self.wait(0.5)
