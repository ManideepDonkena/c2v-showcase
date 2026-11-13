from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Rule: Swapping b and c", font_size=36).to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # Initial grid
        a, b, c, d = 2, 1, 3, 4
        grid1 = Matrix([[a, b], [c, d]], bracket_h_buff=0.4, bracket_v_buff=0.4)
        grid1_label = Text("Original Grid", font_size=24).next_to(grid1, UP)
        
        # Vell formula for original grid
        vell1 = MathTex("a \\times d - b - c", font_size=36)
        vell1_label = Text("Vell =", font_size=24).next_to(vell1, LEFT)
        vell_group1 = VGroup(vell1_label, vell1).arrange(RIGHT, buff=0.2).next_to(grid1, DOWN, buff=0.5)

        self.play(Write(grid1), Write(grid1_label))
        self.wait(0.5)
        self.play(Write(vell_group1))
        self.wait(1)

        # Transform grid
        grid2 = Matrix([[a, c], [b, d]], bracket_h_buff=0.4, bracket_v_buff=0.4)
        grid2_label = Text("After Swapping b and c", font_size=24).next_to(grid2, UP)

        self.play(ReplacementTransform(grid1, grid2), ReplacementTransform(grid1_label, grid2_label))
        self.wait(0.5)

        # Vell formula for new grid
        vell2 = MathTex("a \\times d - c - b", font_size=36)
        vell2_label = Text("Vell =", font_size=24).next_to(vell2, LEFT)
        vell_group2 = VGroup(vell2_label, vell2).arrange(RIGHT, buff=0.2).next_to(grid2, DOWN, buff=0.5)

        vell2_label.shift(0.0 * RIGHT + -0.4 * UP)  # layout: separation vector
        vell2.shift(0.0 * RIGHT + -0.41 * UP)  # layout: separation vector
        self.play(Write(vell_group2))
        self.wait(1)

        # Show equality
        equal_sign = MathTex("=", font_size=36).next_to(vell1, RIGHT, buff=0.2)
        self.play(Write(equal_sign))
        self.wait(0.5)

        # Rearranging terms
        vell_rearranged = MathTex("a \\times d - b - c", font_size=36)
        vell_rearranged.next_to(equal_sign, RIGHT, buff=0.2)
        self.play(Write(vell_rearranged))
        self.wait(1)

        # Checkmark
        check = Tex(r"$\checkmark$").scale(2).set_color(GREEN).next_to(vell_rearranged, RIGHT, buff=0.5)
        self.play(Write(check))
        self.wait(1.5)

        # Final narration text
        narration = Text("Since subtraction is commutative in this context", font_size=24)
        narration.next_to(vell_group2, DOWN, buff=0.5)
        narration.set_x(0)
        self.play(Write(narration))
        self.wait(1.5)

        self.play(FadeOut(title, grid2, grid2_label, vell_group1, vell_group2, equal_sign, vell_rearranged, check, narration))
        self.wait(0.5)
