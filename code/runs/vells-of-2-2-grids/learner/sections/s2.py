from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Worked Example Calculation", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First example: [[2, 1], [3, 4]]
        grid1 = [[2, 1], [3, 4]]
        grid1_mobs = [[Integer(grid1[i][j], font_size=36) for j in range(2)] for i in range(2)]
        grid1_mob = VGroup(*[VGroup(*grid1_mobs[i]) for i in range(2)]).arrange_in_grid(rows=2, cols=2, buff=0.5)
        grid1_mob.move_to(ORIGIN)
        self.play(Write(grid1_mob))
        self.wait(0.5)

        # Highlight 2 and 4
        a = grid1_mobs[0][0]
        d = grid1_mobs[1][1]
        a_copy = a.copy()
        d_copy = d.copy()
        self.play(a.animate.set_color(YELLOW), d.animate.set_color(YELLOW))
        self.wait(0.5)
        # Multiply 2 * 4
        mult = MathTex("2 \\times 4 = 8", font_size=36).next_to(grid1_mob, DOWN)
        self.play(Write(mult))
        self.wait(1)

        # Subtract 1 and 3
        b = grid1_mobs[0][1]
        c = grid1_mobs[1][0]
        self.play(b.animate.set_color(RED), c.animate.set_color(RED))
        self.wait(0.5)
        sub1 = MathTex("8 - 1 = 7", font_size=36).next_to(mult, DOWN)
        self.play(Write(sub1))
        self.wait(0.5)
        sub2 = MathTex("7 - 3 = 4", font_size=36).next_to(sub1, DOWN)
        self.play(Write(sub2))
        self.wait(1)

        # Final answer
        final1 = MathTex("\\text{Vell} = 4", font_size=40).set_color(GREEN).move_to(DOWN * 1.5)
        self.play(Write(final1))
        self.wait(1.5)
        self.play(FadeOut(grid1_mob), FadeOut(mult), FadeOut(sub1), FadeOut(sub2), FadeOut(final1))

        # Second example: [[5, 2], [3, 1]]
        grid2 = [[5, 2], [3, 1]]
        grid2_mobs = [[Integer(grid2[i][j], font_size=36) for j in range(2)] for i in range(2)]
        grid2_mob = VGroup(*[VGroup(*grid2_mobs[i]) for i in range(2)]).arrange_in_grid(rows=2, cols=2, buff=0.5)
        grid2_mob.move_to(ORIGIN)
        self.play(Write(grid2_mob))
        self.wait(0.5)

        # Highlight 5 and 1
        a2 = grid2_mobs[0][0]
        d2 = grid2_mobs[1][1]
        self.play(a2.animate.set_color(YELLOW), d2.animate.set_color(YELLOW))
        self.wait(0.5)
        mult2 = MathTex("5 \\times 1 = 5", font_size=36).next_to(grid2_mob, DOWN)
        self.play(Write(mult2))
        self.wait(1)

        # Subtract 2
        b2 = grid2_mobs[0][1]
        self.play(b2.animate.set_color(RED))
        self.wait(0.5)
        sub3 = MathTex("5 - 2 = 3", font_size=36).next_to(mult2, DOWN)
        self.play(Write(sub3))
        self.wait(0.5)

        # Subtract 3
        c2 = grid2_mobs[1][0]
        self.play(c2.animate.set_color(RED))
        self.wait(0.5)
        sub4 = MathTex("3 - 3 = 0", font_size=36).next_to(sub3, DOWN)
        self.play(Write(sub4))
        self.wait(1)

        final2 = MathTex("\\text{Vell} = 0", font_size=40).set_color(GREEN).move_to(DOWN * 1.5)
        self.play(Write(final2))
        self.wait(1.5)
        self.play(FadeOut(grid2_mob), FadeOut(mult2), FadeOut(sub3), FadeOut(sub4), FadeOut(final2))

        # Third example: [[10, 5], [2, 3]]
        grid3 = [[10, 5], [2, 3]]
        grid3_mobs = [[Integer(grid3[i][j], font_size=36) for j in range(2)] for i in range(2)]
        grid3_mob = VGroup(*[VGroup(*grid3_mobs[i]) for i in range(2)]).arrange_in_grid(rows=2, cols=2, buff=0.5)
        grid3_mob.move_to(ORIGIN)
        self.play(Write(grid3_mob))
        self.wait(0.5)

        # Highlight 10 and 3
        a3 = grid3_mobs[0][0]
        d3 = grid3_mobs[1][1]
        self.play(a3.animate.set_color(YELLOW), d3.animate.set_color(YELLOW))
        self.wait(0.5)
        mult3 = MathTex("10 \\times 3 = 30", font_size=36).next_to(grid3_mob, DOWN)
        self.play(Write(mult3))
        self.wait(1)

        # Subtract 5
        b3 = grid3_mobs[0][1]
        self.play(b3.animate.set_color(RED))
        self.wait(0.5)
        sub5 = MathTex("30 - 5 = 25", font_size=36).next_to(mult3, DOWN)
        self.play(Write(sub5))
        self.wait(0.5)

        # Subtract 2
        c3 = grid3_mobs[1][0]
        self.play(c3.animate.set_color(RED))
        self.wait(0.5)
        sub6 = MathTex("25 - 2 = 23", font_size=36).next_to(sub5, DOWN)
        self.play(Write(sub6))
        self.wait(1)

        final3 = MathTex("\\text{Vell} = 23", font_size=40).set_color(GREEN).move_to(DOWN * 1.5)
        self.play(Write(final3))
        self.wait(1.5)
        self.play(FadeOut(grid3_mob), FadeOut(mult3), FadeOut(sub5), FadeOut(sub6), FadeOut(final3))

        # Fourth example: [[0, 5], [5, 0]]
        grid4 = [[0, 5], [5, 0]]
        grid4_mobs = [[Integer(grid4[i][j], font_size=36) for j in range(2)] for i in range(2)]
        grid4_mob = VGroup(*[VGroup(*grid4_mobs[i]) for i in range(2)]).arrange_in_grid(rows=2, cols=2, buff=0.5)
        grid4_mob.move_to(ORIGIN)
        self.play(Write(grid4_mob))
        self.wait(0.5)

        # Highlight 0 and 0
        a4 = grid4_mobs[0][0]
        d4 = grid4_mobs[1][1]
        self.play(a4.animate.set_color(YELLOW), d4.animate.set_color(YELLOW))
        self.wait(0.5)
        mult4 = MathTex("0 \\times 0 = 0", font_size=36).next_to(grid4_mob, DOWN)
        self.play(Write(mult4))
        self.wait(1)

        # Subtract 5
        b4 = grid4_mobs[0][1]
        self.play(b4.animate.set_color(RED))
        self.wait(0.5)
        sub7 = MathTex("0 - 5 = -5", font_size=36).next_to(mult4, DOWN)
        self.play(Write(sub7))
        self.wait(0.5)

        # Subtract 5 again
        c4 = grid4_mobs[1][0]
        self.play(c4.animate.set_color(RED))
        self.wait(0.5)
        sub8 = MathTex("-5 - 5 = -10", font_size=36).next_to(sub7, DOWN)
        self.play(Write(sub8))
        self.wait(1)

        final4 = MathTex("\\text{Vell} = -10", font_size=40).set_color(GREEN).move_to(DOWN * 1.5)
        self.play(Write(final4))
        self.wait(2)

        self.play(FadeOut(grid4_mob), FadeOut(mult4), FadeOut(sub7), FadeOut(sub8), FadeOut(final4), FadeOut(title))
