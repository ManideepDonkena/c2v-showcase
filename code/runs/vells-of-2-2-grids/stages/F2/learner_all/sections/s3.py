from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Rule: Multiplication Scope", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grids with lines
        grid1 = Matrix([[5, 2], [3, 1]], left_bracket="[[", right_bracket="]]").scale(0.8)
        grid2 = Matrix([[10, 5], [2, 3]], left_bracket="[[", right_bracket="]]").scale(0.8)
        grid3 = Matrix([[0, 5], [5, 0]], left_bracket="[[", right_bracket="]]").scale(0.8)

        # Position grids side by side
        grid1.shift(LEFT * 4 + DOWN * 0.5)
        grid2.shift(RIGHT * 0.5 + DOWN * 0.5)
        grid3.shift(RIGHT * 5 + DOWN * 0.5)

        # Highlight diagonal elements and show multiplication
        a1 = grid1.get_entries()[0]
        d1 = grid1.get_entries()[3]
        b1 = grid1.get_entries()[1]
        c1 = grid1.get_entries()[2]

        a1_copy = a1.copy()
        d1_copy = d1.copy()

        self.play(Write(grid1))
        self.wait(0.5)

        # Show lines connecting a to d
        line1 = Line(a1.get_center(), d1.get_center(), color=YELLOW)
        self.play(Create(line1), run_time=0.5)
        self.wait(0.5)

        # Highlight a and d for multiplication
        self.play(a1_copy.animate.set_color(YELLOW), d1_copy.animate.set_color(YELLOW))
        self.wait(0.5)

        # Multiply a*d = 5*1 = 5
        product = MathTex("5 \\times 1 = 5", font_size=24).next_to(grid1, DOWN)
        self.play(Write(product))
        self.wait(0.5)

        # Subtract b (2) from 5 to get 3
        self.play(b1.animate.set_color(RED), run_time=0.3)
        result1 = MathTex("5 - 2 = 3", font_size=24).next_to(product, DOWN)
        self.play(Write(result1))
        self.wait(0.5)

        # Subtract c (3) from 3 to get 0
        self.play(c1.animate.set_color(RED), run_time=0.3)
        result2 = MathTex("3 - 3 = 0", font_size=24).next_to(result1, DOWN)
        self.play(Write(result2))
        self.wait(0.5)

        # Fade out grid1 and results
        self.play(FadeOut(grid1), FadeOut(line1), FadeOut(product), FadeOut(result1), FadeOut(result2))

        # Show second grid
        self.play(Write(grid2))
        self.wait(0.5)

        a2 = grid2.get_entries()[0]
        d2 = grid2.get_entries()[3]
        b2 = grid2.get_entries()[1]
        c2 = grid2.get_entries()[2]

        line2 = Line(a2.get_center(), d2.get_center(), color=YELLOW)
        self.play(Create(line2), run_time=0.5)
        self.wait(0.5)

        # Pulse a and d
        self.play(a2.animate.set_color(YELLOW).scale(1.2), d2.animate.set_color(YELLOW).scale(1.2), run_time=0.3)
        self.play(a2.animate.scale(1/1.2), d2.animate.scale(1/1.2), run_time=0.3)

        # Multiply a*d = 10*3 = 30
        product2 = MathTex("10 \\times 3 = 30", font_size=24).next_to(grid2, DOWN)
        self.play(Write(product2))
        self.wait(0.5)

        # Subtract b (5) from 30 to get 25
        self.play(b2.animate.set_color(RED), run_time=0.3)
        result3 = MathTex("30 - 5 = 25", font_size=24).next_to(product2, DOWN)
        self.play(Write(result3))
        self.wait(0.5)

        # Subtract c (2) from 25 to get 23
        self.play(c2.animate.set_color(RED), run_time=0.3)
        result4 = MathTex("25 - 2 = 23", font_size=24).next_to(result3, DOWN)
        self.play(Write(result4))
        self.wait(0.5)

        # Fade out grid2 and results
        self.play(FadeOut(grid2), FadeOut(line2), FadeOut(product2), FadeOut(result3), FadeOut(result4))

        # Show third grid
        self.play(Write(grid3))
        self.wait(0.5)

        a3 = grid3.get_entries()[0]
        d3 = grid3.get_entries()[3]
        b3 = grid3.get_entries()[1]
        c3 = grid3.get_entries()[2]

        line3 = Line(a3.get_center(), d3.get_center(), color=YELLOW)
        self.play(Create(line3), run_time=0.5)
        self.wait(0.5)

        # Pulse a and d
        self.play(a3.animate.set_color(YELLOW).scale(1.2), d3.animate.set_color(YELLOW).scale(1.2), run_time=0.3)
        self.play(a3.animate.scale(1/1.2), d3.animate.scale(1/1.2), run_time=0.3)

        # Multiply a*d = 0*0 = 0
        product3 = MathTex("0 \\times 0 = 0", font_size=24).next_to(grid3, DOWN)
        self.play(Write(product3))
        self.wait(0.5)

        # Subtract b (5) from 0 to get -5
        self.play(b3.animate.set_color(RED), run_time=0.3)
        result5 = MathTex("0 - 5 = -5", font_size=24).next_to(product3, DOWN)
        self.play(Write(result5))
        self.wait(0.5)

        # Subtract c (5) from -5 to get -10
        self.play(c3.animate.set_color(RED), run_time=0.3)
        result6 = MathTex("-5 - 5 = -10", font_size=24).next_to(result5, DOWN)
        self.play(Write(result6))
        self.wait(0.5)

        # Fade out grid3 and results
        self.play(FadeOut(grid3), FadeOut(line3), FadeOut(product3), FadeOut(result5), FadeOut(result6))

        # Show formula
        formula = MathTex("a \\times d - b - c", font_size=30).to_edge(UP)
        self.play(Write(formula))
        self.wait(0.5)

        # Show equation a*d - b - c = 0 with result labeled as 0
        eq = MathTex("a \\times d - b - c = 0", font_size=30).to_edge(DOWN)
        self.play(Write(eq))
        self.wait(0.5)

        # Move b and c to the right side
        moved_eq = MathTex("a \\times d = b + c", font_size=30).to_edge(DOWN)
        self.play(Transform(eq, moved_eq))
        self.wait(1)

        # Show two grids with swapped middle elements
        grid4 = Matrix([[2, 1], [3, 4]], left_bracket="[[", right_bracket="]]").scale(0.7).shift(LEFT * 3 + UP)
        grid5 = Matrix([[2, 2], [1, 4]], left_bracket="[[", right_bracket="]]").scale(0.7).shift(RIGHT * 3 + UP)

        self.play(Write(grid4), Write(grid5))
        self.wait(0.5)

        # Show formula for both
        f1 = MathTex("2 \\times 4 - 1 - 3 = 0", font_size=24).next_to(grid4, DOWN)
        f2 = MathTex("2 \\times 4 - 2 - 1 = 0", font_size=24).next_to(grid5, DOWN)

        self.play(Write(f1), Write(f2))
        self.wait(1)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(formula), FadeOut(eq), FadeOut(grid4), FadeOut(grid5), FadeOut(f1), FadeOut(f2))
        self.wait(0.5)
