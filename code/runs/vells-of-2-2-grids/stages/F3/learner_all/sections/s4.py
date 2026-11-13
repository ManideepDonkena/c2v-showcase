from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Rule: Swapping b and c", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial grid
        grid1 = Matrix([[5, 2], [3, 1]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        grid1.to_corner(UL)
        grid1_label = Text("Grid", font_size=24).next_to(grid1, UP)
        self.play(Write(grid1_label), Write(grid1))
        self.wait(1)

        # Show calculation steps for first grid
        a, b, c, d = 5, 2, 3, 1
        ad = a * d
        step1 = MathTex("a \\times d = ", f"{a} \\times {d} = {ad}", font_size=30).to_edge(DOWN).shift(UP*0.5)
        self.play(Write(step1))
        self.wait(1)

        step2 = MathTex(f"{ad} - b = ", f"{ad} - {b} = {ad - b}", font_size=30).next_to(step1, DOWN)
        self.play(Write(step2))
        self.wait(1)

        step3 = MathTex(f"{ad - b} - c = ", f"{ad - b} - {c} = {ad - b - c}", font_size=30).next_to(step2, DOWN)
        self.play(Write(step3))
        self.wait(1.5)

        # Show result
        result1 = MathTex("\text{Vell} = ", f"{ad - b - c}", font_size=30).to_edge(DOWN).shift(DOWN*0.5)
        result1.shift(0.0 * RIGHT + 0.43 * UP)  # layout: separation vector
        self.play(Write(result1))
        self.wait(1.5)

        # Swap b and c
        grid2 = Matrix([[5, 3], [2, 1]], bracket_h_buff=0.2, bracket_v_buff=0.2)
        grid2.to_corner(UR)
        grid2_label = Text("After swapping b and c", font_size=24).next_to(grid2, UP)
        self.play(Write(grid2_label), Write(grid2))
        self.wait(1)

        # Show same vell
        ad2 = a * d
        step4 = MathTex("a \\times d = ", f"{a} \\times {d} = {ad2}", font_size=30).to_edge(DOWN).shift(UP*0.5)
        self.play(Write(step4))
        self.wait(1)

        step5 = MathTex(f"{ad2} - c = ", f"{ad2} - {c} = {ad2 - c}", font_size=24).next_to(step4, DOWN)
        self.play(Write(step5))
        self.wait(1)

        step6 = MathTex(f"{ad2 - c} - b = ", f"{ad2 - c} - {b} = {ad2 - c - b}", font_size=30).next_to(step5, DOWN)
        self.play(Write(step6))
        self.wait(1.5)

        result2 = MathTex("\\text{Vell} = ", f"{ad2 - c - b}", font_size=30).to_edge(DOWN).shift(DOWN*0.5)
        self.play(Write(result2))
        self.wait(1.5)

        # Show equality
        equal = MathTex("a \\times d - b - c = a \\times d - c - b", font_size=30).to_edge(DOWN).shift(DOWN*1.2)
        self.play(Write(equal))
        self.wait(2)

        # Checkmark
        check = Tex("\\checkmark", font_size=40).next_to(equal, RIGHT)
        self.play(Write(check))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(grid1), FadeOut(grid2), FadeOut(step1), FadeOut(step2),
                  FadeOut(step3), FadeOut(step4), FadeOut(step5), FadeOut(step6), FadeOut(result1),
                  FadeOut(result2), FadeOut(equal), FadeOut(check))
        self.wait(0.5)
