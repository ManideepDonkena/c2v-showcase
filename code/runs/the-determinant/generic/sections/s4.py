from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Computational Formula", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Matrix setup
        matrix = Matrix([[ "a", "b" ], [ "c", "d" ]], bracket_h_buff=0.2, bracket_v_buff=0.2)
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
        self.play(bc_copy.animate.set_color(GREEN), run_time=0.5)
        
        self.wait(0.5)

        # Show ad and bc products
        ad_text = MathTex("ad", font_size=30).next_to(ad_copy, DOWN)
        bc_text = MathTex("bc", font_size=30).next_to(bc_copy, DOWN)

        bc_text.shift(0.0 * RIGHT + 0.37 * UP)  # layout: separation vector
        self.play(Write(ad_text), Write(bc_text))
        self.wait(1)

        # Animate ad growing and bc shrinking
        ad_anim = ad_text.animate.scale(1.5).set_color(YELLOW)
        bc_anim = bc_text.animate.scale(1.5).set_color(GREEN)

        self.play(ad_anim, bc_anim, run_time=1)

        # Show final formula
        det_formula = MathTex("ad - bc", font_size=36).next_to(matrix, DOWN, buff=0.8)
        self.play(Write(det_formula))
        self.wait(1)

        # Show unit square and its transformation
        unit_square = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        unit_square.to_corner(DL)
        
        self.play(FadeIn(unit_square))
        self.wait(0.5)

        # Transform the square with matrix
        transformed_square = always_redraw(
            lambda: Square(side_length=1, color=RED, fill_opacity=0.5).move_to(unit_square.get_center())
        )
        
        self.play(Transform(unit_square, transformed_square), run_time=2)
        self.wait(0.5)

        # Show area value
        area_value = MathTex("=", "ad - bc", font_size=30).next_to(unit_square, RIGHT, buff=0.5)
        self.play(Write(area_value))
        self.wait(1.5)

        # Final fade out
        self.play(
            FadeOut(title),
            FadeOut(matrix),
            FadeOut(ad_copy),
            FadeOut(bc_copy),
            FadeOut(ad_text),
            FadeOut(bc_text),
            FadeOut(det_formula),
            FadeOut(unit_square),
            FadeOut(area_value)
        )
        self.wait(0.5)
