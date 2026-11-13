from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Rule: Swapping b and c", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Initial grid
        grid1 = Matrix([['a', 'b'], ['c', 'd']], 
                       left_bracket='[[', right_bracket=']]').scale(0.8)
        grid1.to_corner(UL)
        grid1_label = Text('Grid 1', font_size=24).next_to(grid1, UP)

        # Transformed grid
        grid2 = Matrix([['a', 'c'], ['b', 'd']], 
                       left_bracket='[[', right_bracket=']]').scale(0.8)
        grid2.to_corner(UR)
        grid2_label = Text('Grid 2', font_size=24).next_to(grid2, UP)

        # Determinant formulas
        vell1 = MathTex('a d - b c', font_size=32)
        vell1.next_to(grid1, DOWN)
        vell2 = MathTex("a d - c b", font_size=32)
        vell2.next_to(grid2, DOWN)

        # Show grids and formulas
        self.play(Write(grid1), Write(grid1_label))
        self.wait(0.5)
        self.play(Write(vell1))
        self.wait(0.5)
        self.play(Write(grid2), Write(grid2_label))
        self.wait(0.5)
        self.play(Write(vell2))
        self.wait(0.5)

        # Highlight swapping b and c
        b1 = grid1.get_entries()[1]
        c1 = grid1.get_entries()[2]
        b2 = grid2.get_entries()[1]
        c2 = grid2.get_entries()[0]

        self.play(
            b1.animate.set_color(YELLOW),
            c1.animate.set_color(YELLOW),
            b2.animate.set_color(YELLOW),
            c2.animate.set_color(YELLOW)
        )
        self.wait(0.5)

        # Show that order doesn't matter
        swap_text = Text("Subtraction order does not affect result", font_size=24).to_edge(DOWN)
        self.play(Write(swap_text))
        self.wait(1)

        # Fade out text
        self.play(FadeOut(swap_text))

        # Example with numbers
        grid1_num = Matrix([[2, 1], [2, 4]], left_bracket="[[", right_bracket="]]").scale(0.7)
        grid1_num.to_corner(UL)
        grid1_num_label = Text("Grid 1: b=1, c=2", font_size=24).next_to(grid1_num, UP, buff=0.2)

        grid2_num = Matrix([[2, 2], [1, 4]], left_bracket="[[", right_bracket="]]").scale(0.7)
        grid2_num.to_corner(UR)
        grid2_num_label = Text("Grid 2: b=2, c=1", font_size=24).next_to(grid2_num, UP, buff=0.2)

        vell1_num = MathTex("2 \\times 4 - 1 \\times 2 = 8 - 2 = 6", font_size=28)
        vell1_num.next_to(grid1_num, DOWN, buff=0.3)
        vell2_num = MathTex("2 \\times 4 - 2 \\times 1 = 8 - 2 = 6", font_size=28)
        vell2_num.next_to(grid2_num, DOWN, buff=0.3)

        # Adjust positions to avoid overlap
        grid1_num_label.shift(DOWN * 0.4)
        grid2_num_label.shift(DOWN * 0.4)
        vell1_num.shift(RIGHT * 2.4)
        vell2_num.shift(LEFT * 2.4)

        grid1_num_label.shift(0.0 * RIGHT + 0.35 * UP)  # layout: separation vector
        self.play(Write(grid1_num), Write(grid1_num_label))
        self.wait(0.5)
        self.play(Write(vell1_num))
        self.wait(0.5)
        self.play(Write(grid2_num), Write(grid2_num_label))
        self.wait(0.5)
        self.play(Write(vell2_num))
        self.wait(0.5)

        # Checkmark
        check = Tex(r"$\checkmark$").scale(2).set_color(GREEN).to_edge(DOWN)
        self.play(Write(check))
        self.wait(1)

        # Fade out everything
        self.play(
            FadeOut(grid1), FadeOut(grid1_label), FadeOut(vell1),
            FadeOut(grid2), FadeOut(grid2_label), FadeOut(vell2),
            FadeOut(grid1_num), FadeOut(grid1_num_label), FadeOut(vell1_num),
            FadeOut(grid2_num), FadeOut(grid2_num_label), FadeOut(vell2_num),
            FadeOut(check), FadeOut(title)
        )
