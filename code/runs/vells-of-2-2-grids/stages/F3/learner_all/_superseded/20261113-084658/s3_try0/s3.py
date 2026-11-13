from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Rule: Multiplication Scope", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First grid
        grid1 = [[2, 1], [3, 4]]
        grid1_mob = Matrix(grid1, bracket_h_buff=0.3, bracket_v_buff=0.3).scale(0.8)
        grid1_mob.next_to(title, DOWN, buff=0.5)

        # Labels for elements
        a1 = Tex("$a$").next_to(grid1_mob.get_entries()[0], UR, buff=0.1)
        b1 = Tex("$b$").next_to(grid1_mob.get_entries()[1], UL, buff=0.1)
        c1 = Tex("$c$").next_to(grid1_mob.get_entries()[2], DL, buff=0.1)
        d1 = Tex("$d$").next_to(grid1_mob.get_entries()[3], DR, buff=0.1)

        # Lines connecting a to d
        line1 = Line(
            grid1_mob.get_entries()[0].get_corner(UR),
            grid1_mob.get_entries()[3].get_corner(DL)
        ).set_color(YELLOW)

        a1.shift(0.0 * RIGHT + 0.29 * UP)  # layout: separation vector
        b1.shift(0.0 * RIGHT + 0.29 * UP)  # layout: separation vector
        c1.shift(0.0 * RIGHT + -0.29 * UP)  # layout: separation vector
        self.play(Write(grid1_mob), Write(a1), Write(b1), Write(c1), Write(d1))
        self.play(Create(line1))
        self.wait(1)

        # Fade out b and c
        self.play(FadeOut(b1), FadeOut(c1))
        self.wait(0.5)

        # Second grid
        grid2 = [[4, 3], [1, 2]]
        grid2_mob = Matrix(grid2, bracket_h_buff=0.3, bracket_v_buff=0.3).scale(0.8)
        grid2_mob.next_to(grid1_mob, RIGHT, buff=1.5)

        # Labels for elements
        a2 = Tex("$d$").next_to(grid2_mob.get_entries()[0], UR, buff=0.1)
        b2 = Tex("$c$").next_to(grid2_mob.get_entries()[1], UL, buff=0.1)
        c2 = Tex("$b$").next_to(grid2_mob.get_entries()[2], DL, buff=0.1)
        d2 = Tex("$a$").next_to(grid2_mob.get_entries()[3], DR, buff=0.1)

        # Lines connecting d to a
        line2 = Line(
            grid2_mob.get_entries()[0].get_corner(UR),
            grid2_mob.get_entries()[3].get_corner(DL)
        ).set_color(YELLOW)

        self.play(Write(grid2_mob), Write(a2), Write(b2), Write(c2), Write(d2))
        self.play(Create(line2))
        self.wait(1)

        # Fade out b and c
        self.play(FadeOut(b2), FadeOut(c2))
        self.wait(0.5)

        # Rule text
        rule = Text("Rule one states that only the top-left and bottom-right numbers are multiplied.", font_size=24)
        rule.to_edge(DOWN)
        self.play(Write(rule))
        self.wait(1.5)

        # Fade out everything except title and rule
        self.play(FadeOut(grid1_mob), FadeOut(grid2_mob), FadeOut(line1), FadeOut(line2), FadeOut(a1), FadeOut(d1), FadeOut(a2), FadeOut(d2), FadeOut(rule))
        self.wait(0.5)

        # Worked example
        example = MathTex("Vell = a \\times d - b - c", font_size=36)
        example.to_edge(UP)
        self.play(Write(example))
        self.wait(1)

        # Show substitution
        example2 = MathTex("Vell = 2 \\times 4 - 1 - 3 = 4", font_size=36)
        example2.next_to(example, DOWN)
        self.play(Write(example2))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(example), FadeOut(example2), FadeOut(title))
        self.wait(0.5)
