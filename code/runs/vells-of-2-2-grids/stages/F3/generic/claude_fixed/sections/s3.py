from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Rule: Multiplication Scope", font_size=36).to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # First grid: [[a, b], [c, d]]
        grid1 = Matrix([["a", "b"], ["c", "d"]], bracket_h_buff=0.4, bracket_v_buff=0.4)
        grid1.scale(0.8)

        # Second grid: [[d, c], [b, a]]
        grid2 = Matrix([["d", "c"], ["b", "a"]], bracket_h_buff=0.4, bracket_v_buff=0.4)
        grid2.scale(0.8)

        grids = VGroup(grid1, grid2).arrange(RIGHT, buff=1.5)
        grids.next_to(title, DOWN, buff=0.6)
        grids.set_x(0)

        # Lines connecting a to d (top-left to bottom-right)
        line1 = Line(
            grid1.get_entries()[0].get_center(),  # a
            grid1.get_entries()[3].get_center()   # d
        )
        line1.set_color(YELLOW)
        line1.set_stroke(width=3)

        # Lines connecting d to a (bottom-left to top-right)
        line2 = Line(
            grid2.get_entries()[2].get_center(),  # b
            grid2.get_entries()[3].get_center()   # a
        )
        line2.set_color(YELLOW)
        line2.set_stroke(width=3)

        self.play(Write(grid1))
        self.wait(0.5)
        self.play(Create(line1))
        self.wait(0.5)

        self.play(Write(grid2))
        self.wait(0.5)
        self.play(Create(line2))
        self.wait(0.5)

        # Fade out lines that are not part of the rule
        line_b_c_1 = Line(
            grid1.get_entries()[1].get_center(),  # b
            grid1.get_entries()[2].get_center()   # c
        )
        line_b_c_1.set_color(GRAY)
        line_b_c_1.set_stroke(width=2)
        line_b_c_1.set_opacity(0.5)

        line_b_c_2 = Line(
            grid2.get_entries()[1].get_center(),  # c
            grid2.get_entries()[2].get_center()   # b
        )
        line_b_c_2.set_color(GRAY)
        line_b_c_2.set_stroke(width=2)
        line_b_c_2.set_opacity(0.5)

        self.play(Create(line_b_c_1), Create(line_b_c_2))
        self.wait(0.5)

        # Show rule text
        rule_text = Text("Rule one states that only the top-left and bottom-right numbers are multiplied.", font_size=24)
        if rule_text.width > 12.5:
            rule_text.scale_to_fit_width(12.5)
        rule_text.next_to(grids, DOWN, buff=0.8)
        rule_text.set_x(0)
        self.play(Write(rule_text))
        self.wait(1.5)

        # Emphasize position matters
        pos_matters = Text("This means the position matters:", font_size=24)
        pos_matters.next_to(rule_text, DOWN, buff=0.3)
        self.play(Write(pos_matters))
        self.wait(1.0)

        not_adjacent = Text("We never multiply adjacent elements like b and c directly.", font_size=24)
        not_adjacent.next_to(pos_matters, DOWN, buff=0.3)
        self.play(Write(not_adjacent))
        self.wait(1.5)

        # Fade out everything except title
        self.play(
            FadeOut(grid1),
            FadeOut(grid2),
            FadeOut(line1),
            FadeOut(line2),
            FadeOut(line_b_c_1),
            FadeOut(line_b_c_2),
            FadeOut(rule_text),
            FadeOut(pos_matters),
            FadeOut(not_adjacent)
        )
        self.wait(0.5)
