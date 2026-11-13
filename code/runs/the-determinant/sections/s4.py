from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Computational Formula", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Matrix setup
        matrix = Matrix([[ "a", "b" ], [ "c", "d" ]], bracket_h_buff=0.4, bracket_v_buff=0.4)
        matrix.scale(1.2)
        matrix.to_edge(UP, buff=1.5)
        self.play(Write(matrix))
        self.wait(0.5)

        # Highlight ad and bc
        ad = VGroup(matrix.get_entries()[0], matrix.get_entries()[3])
        bc = VGroup(matrix.get_entries()[1], matrix.get_entries()[2])

        ad_copy = ad.copy()
        bc_copy = bc.copy()

        self.play(ad_copy.animate.set_color(YELLOW), run_time=0.5)
        self.wait(0.5)
        self.play(bc_copy.animate.set_color(GREEN), run_time=0.5)
        self.wait(0.5)

        # Formula text
        formula = MathTex("ad - bc", font_size=40)
        formula.next_to(matrix, DOWN, buff=1)
        self.play(Write(formula))
        self.wait(0.5)

        # Show ad growing and bc shrinking
        ad_rect = SurroundingRectangle(ad_copy, color=YELLOW, fill_opacity=0.2)
        bc_rect = SurroundingRectangle(bc_copy, color=GREEN, fill_opacity=0.2)

        self.play(Write(ad_rect), Write(bc_rect))
        self.wait(0.5)

        # Simulate growth/shrink
        ad_rect_copy = ad_rect.copy()
        bc_rect_copy = bc_rect.copy()

        self.play(
            ad_rect_copy.animate.scale(1.5, about_edge=DOWN),
            bc_rect_copy.animate.scale(0.5, about_edge=UP),
            run_time=1
        )
        self.wait(0.5)

        # Final result
        result = MathTex("= \\text{Area}", font_size=32)
        result.next_to(formula, RIGHT, buff=0.5)
        self.play(Write(result))
        self.wait(0.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(matrix),
            FadeOut(ad_rect),
            FadeOut(bc_rect),
            FadeOut(formula),
            FadeOut(result),
            FadeOut(ad_copy),
            FadeOut(bc_copy),
        )
        self.wait(0.5)
