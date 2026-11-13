from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Worked Example Calculation", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First grid: [[2, 1], [3, 4]]
        grid1 = Matrix([[2, 1], [3, 4]])
        grid1.to_corner(UL)
        grid1[0].set_style(stroke_width=2)  # Use stroke_width instead of bracket_style
        self.play(Write(grid1))
        self.wait(0.5)

        # Pulse 2 and 4
        a = grid1.get_entries()[0]
        d = grid1.get_entries()[3]
        self.play(a.animate.scale(1.2).set_color(YELLOW), d.animate.scale(1.2).set_color(YELLOW))
        self.wait(0.5)
        self.play(a.animate.scale(1/1.2).set_color(WHITE), d.animate.scale(1/1.2).set_color(WHITE))

        # Show multiplication 2 * 4 = 8
        mult_result = MathTex("2 \\times 4 =", "8", font_size=30)
        mult_result.next_to(grid1, DOWN, buff=0.5)
        self.play(Write(mult_result))
        self.wait(1)

        # Subtract 1 and 3 sequentially
        sub1 = MathTex("8 - 1 =", "7", font_size=30)
        sub1.next_to(mult_result, DOWN, buff=0.3)
        self.play(Write(sub1))
        self.wait(1)

        sub2 = MathTex("7 - 3 =", "4", font_size=30)
        sub2.next_to(sub1, DOWN, buff=0.3)
        self.play(Write(sub2))
        self.wait(1.5)

        # Fade out first grid and result
        self.play(FadeOut(grid1), FadeOut(mult_result), FadeOut(sub1), FadeOut(sub2))

        # Second grid: [[5, 2], [3, 1]]
        grid2 = Matrix([[5, 2], [3, 1]])
        grid2.to_corner(UL)
        grid2[0].set_style(stroke_width=2)  # Use stroke_width instead of bracket_style
        self.play(Write(grid2))
        self.wait(0.5)

        # Multiply top-left (5) and bottom-right (1)
        a2 = grid2.get_entries()[0]
        d2 = grid2.get_entries()[3]
        self.play(a2.animate.scale(1.2).set_color(YELLOW), d2.animate.scale(1.2).set_color(YELLOW))
        self.wait(0.5)
        self.play(a2.animate.scale(1/1.2).set_color(WHITE), d2.animate.scale(1/1.2).set_color(WHITE))

        mult_result2 = MathTex("5 \\times 1 =", "5", font_size=30)
        mult_result2.next_to(grid2, DOWN, buff=0.5)
        self.play(Write(mult_result2))
        self.wait(1)

        # Subtract middle-top (2)
        b2 = grid2.get_entries()[1]
        self.play(b2.animate.scale(1.2).set_color(RED))
        self.wait(0.5)
        self.play(b2.animate.scale(1/1.2).set_color(WHITE))

        sub_result2 = MathTex("5 - 2 =", "3", font_size=30)
        sub_result2.next_to(mult_result2, DOWN, buff=0.3)
        self.play(Write(sub_result2))
        self.wait(1)

        # Subtract middle-bottom (3)
        c2 = grid2.get_entries()[2]
        self.play(c2.animate.scale(1.2).set_color(RED))
        self.wait(0.5)
        self.play(c2.animate.scale(1/1.2).set_color(WHITE))

        sub_result3 = MathTex("3 - 3 =", "0", font_size=30)
        sub_result3.next_to(sub_result2, DOWN, buff=0.3)
        self.play(Write(sub_result3))
        self.wait(1.5)

        # Fade out second grid and result
        self.play(FadeOut(grid2), FadeOut(mult_result2), FadeOut(sub_result2), FadeOut(sub_result3))

        # Third grid: [[10, 5], [2, 3]]
        grid3 = Matrix([[10, 5], [2, 3]])
        grid3.to_corner(UL)
        grid3[0].set_style(stroke_width=2)  # Use stroke_width instead of bracket_style
        self.play(Write(grid3))
        self.wait(0.5)

        # Multiply top-left (10) and bottom-right (3)
        a3 = grid3.get_entries()[0]
        d3 = grid3.get_entries()[3]
        self.play(a3.animate.scale(1.2).set_color(YELLOW), d3.animate.scale(1.2).set_color(YELLOW))
        self.wait(0.5)
        self.play(a3.animate.scale(1/1.2).set_color(WHITE), d3.animate.scale(1/1.2).set_color(WHITE))

        mult_result3 = MathTex("10 \\times 3 =", "30", font_size=30)
        mult_result3.next_to(grid3, DOWN, buff=0.5)
        self.play(Write(mult_result3))
        self.wait(1)

        # Show that this is not final answer
        not_final = Text("This is not the final answer.", font_size=24).next_to(mult_result3, DOWN, buff=0.3)
        not_final.shift(0.56 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(not_final))
        self.wait(1)

        # Subtract b (5)
        b3 = grid3.get_entries()[1]
        self.play(b3.animate.scale(1.2).set_color(RED))
        self.wait(0.5)
        self.play(b3.animate.scale(1/1.2).set_color(WHITE))

        sub_result4 = MathTex("30 - 5 =", "25", font_size=30)
        sub_result4.next_to(not_final, DOWN, buff=0.3)
        self.play(Write(sub_result4))
        self.wait(1)

        # Subtract c (2)
        c3 = grid3.get_entries()[2]
        self.play(c3.animate.scale(1.2).set_color(RED))
        self.wait(0.5)
        self.play(c3.animate.scale(1/1.2).set_color(WHITE))

        sub_result5 = MathTex("25 - 2 =", "23", font_size=30)
        sub_result5.next_to(sub_result4, DOWN, buff=0.3)
        self.play(Write(sub_result5))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(grid3), FadeOut(mult_result3), FadeOut(not_final), FadeOut(sub_result4), FadeOut(sub_result5))
        self.wait(0.5)
