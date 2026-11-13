from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Worked Example Calculation", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # First grid: [[2, 1], [3, 4]]
        grid1 = Matrix([[2, 1], [3, 4]]).scale(0.8)
        grid1.to_corner(UL)
        # Use set_style with bracket_style parameter correctly
        grid1[0].set_style(stroke_width=2, fill_opacity=0)  # Remove brackets by setting stroke width to 0 or use custom brackets
        self.play(Write(grid1))
        self.wait(0.5)

        # Highlight 2 and 4
        rect2 = SurroundingRectangle(grid1.get_entries()[0], color=YELLOW, buff=0.1)
        rect4 = SurroundingRectangle(grid1.get_entries()[3], color=YELLOW, buff=0.1)
        self.play(Create(rect2), Create(rect4))
        self.wait(0.5)

        # Multiply 2 and 4
        prod_text = MathTex("2 \\times 4 = 8", font_size=30).next_to(grid1, DOWN, buff=0.5)
        self.play(Write(prod_text))
        self.wait(1)

        # Remove highlight
        self.play(FadeOut(rect2), FadeOut(rect4))

        # Subtract 1 and then 3
        sub1 = MathTex("8 - 1 = 7", font_size=30).next_to(prod_text, DOWN, buff=0.5)
        self.play(Write(sub1))
        self.wait(1)

        sub2 = MathTex("7 - 3 = 4", font_size=30).next_to(sub1, DOWN, buff=0.5)
        self.play(Write(sub2))
        self.wait(1)

        # Final result
        final_result = MathTex("\\text{Vell} = 4", font_size=36).set_color(GREEN).next_to(sub2, DOWN, buff=0.5)
        self.play(Write(final_result))
        self.wait(1.5)

        # Fade out first grid and result
        self.play(FadeOut(grid1), FadeOut(prod_text), FadeOut(sub1), FadeOut(sub2), FadeOut(final_result))

        # Second grid: [[5, 2], [3, 1]]
        grid2 = Matrix([[5, 2], [3, 1]]).scale(0.8)
        grid2.to_corner(UL)
        grid2[0].set_style(stroke_width=2, fill_opacity=0)  # Remove brackets
        self.play(Write(grid2))
        self.wait(0.5)

        # Multiply top-left (5) and bottom-right (1)
        rect5 = SurroundingRectangle(grid2.get_entries()[0], color=YELLOW, buff=0.1)
        rect1 = SurroundingRectangle(grid2.get_entries()[3], color=YELLOW, buff=0.1)
        self.play(Create(rect5), Create(rect1))
        self.wait(0.5)

        prod_text2 = MathTex("5 \\times 1 = 5", font_size=30).next_to(grid2, DOWN, buff=0.5)
        self.play(Write(prod_text2))
        self.wait(1)

        # Remove highlight
        self.play(FadeOut(rect5), FadeOut(rect1))

        # Subtract middle-top (2)
        sub_top = MathTex("5 - 2 = 3", font_size=30).next_to(prod_text2, DOWN, buff=0.5)
        self.play(Write(sub_top))
        self.wait(1)

        # Subtract middle-bottom (3)
        sub_bottom = MathTex("3 - 3 = 0", font_size=30).next_to(sub_top, DOWN, buff=0.5)
        self.play(Write(sub_bottom))
        self.wait(1)

        final_result2 = MathTex("\\text{Vell} = 0", font_size=36).set_color(GREEN).next_to(sub_bottom, DOWN, buff=0.5)
        self.play(Write(final_result2))
        self.wait(1.5)

        # Fade out second grid and result
        self.play(FadeOut(grid2), FadeOut(prod_text2), FadeOut(sub_top), FadeOut(sub_bottom), FadeOut(final_result2))

        # Third grid: [[10, 5], [2, 3]]
        grid3 = Matrix([[10, 5], [2, 3]]).scale(0.8)
        grid3.to_corner(UL)
        grid3[0].set_style(stroke_width=2, fill_opacity=0)  # Remove brackets
        self.play(Write(grid3))
        self.wait(0.5)

        # Multiply top-left (10) and bottom-right (3)
        rect10 = SurroundingRectangle(grid3.get_entries()[0], color=YELLOW, buff=0.1)
        rect3 = SurroundingRectangle(grid3.get_entries()[3], color=YELLOW, buff=0.1)
        self.play(Create(rect10), Create(rect3))
        self.wait(0.5)

        prod_text3 = MathTex("10 \\times 3 = 30", font_size=30).next_to(grid3, DOWN, buff=0.5)
        self.play(Write(prod_text3))
        self.wait(1)

        # Remove highlight
        self.play(FadeOut(rect10), FadeOut(rect3))

        # Show intermediate steps: subtract 5 then 2
        step1 = MathTex("30 - 5 = 25", font_size=30).next_to(prod_text3, DOWN, buff=0.5)
        self.play(Write(step1))
        self.wait(1)

        step2 = MathTex("25 - 2 = 23", font_size=30).next_to(step1, DOWN, buff=0.5)
        self.play(Write(step2))
        self.wait(1)

        # Final result
        final_result3 = MathTex("\\text{Vell} = 23", font_size=36).set_color(GREEN).next_to(step2, DOWN, buff=0.5)
        self.play(Write(final_result3))
        self.wait(1.5)

        # Show that 23 is not among the options
        note = Text("Note: 23 is not among the given options.", font_size=24).next_to(final_result3, DOWN, buff=0.5)
        note.shift(1.8 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(note))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(grid3), FadeOut(prod_text3), FadeOut(step1), FadeOut(step2), FadeOut(final_result3), FadeOut(note))

        # End title
        end_title = Text("End of Section S2", font_size=36).to_edge(UP)
        end_title.shift(0.0 * RIGHT + -0.65 * UP)  # layout: separation vector
        self.play(Write(end_title))
        self.wait(1)

        self.play(FadeOut(end_title))
