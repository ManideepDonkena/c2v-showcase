from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Duality Isomorphism", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Left side: functional L with contour lines
        L_func = always_redraw(lambda: Line(LEFT * 7, RIGHT * 7).set_color(BLUE).shift(DOWN * 1.5))
        contour_lines_L = VGroup()
        for i in range(-5, 6):
            line = DashedLine(LEFT * 7, RIGHT * 7).shift(DOWN * (i * 0.5 + 1.5)).set_color(BLUE)
            contour_lines_L.add(line)
        L_text = Text("Functional L", font_size=24).next_to(L_func, UP)

        # Right side: vector A'
        A_prime = Vector([2, 1], color=YELLOW)
        A_label = MathTex(r"\vec{A'}", font_size=30).next_to(A_prime, UR)
        dot_product_text = MathTex(r"L(\vec{B}) = \vec{A'} \cdot \vec{B}", font_size=30).to_edge(DOWN)

        # Show L and A'
        self.play(Create(L_func), Create(contour_lines_L), Write(L_text))
        self.wait(1)
        self.play(Create(A_prime), Write(A_label))
        self.wait(1)

        # Morph L contours to match dot product level sets of A'
        def get_level_set_line(vec, c):
            # Line perpendicular to vec at distance c from origin
            perp = Vector([vec[0], vec[1]], color=YELLOW)
            perp.rotate(PI/2)
            perp.scale(c / np.linalg.norm(vec))
            line = DashedLine(LEFT * 7, RIGHT * 7).shift(perp.get_end()).set_color(YELLOW)
            return line

        # Animate contour lines morphing to match A'
        new_contours = VGroup()
        for i in range(-5, 6):
            c = i * 0.5
            line = always_redraw(lambda c=c: get_level_set_line([2, 1], c))
            new_contours.add(line)
        
        self.play(Transform(contour_lines_L, new_contours), run_time=2)
        self.wait(1)

        # Show the dot product formula
        self.play(Write(dot_product_text))
        self.wait(1.5)

        # Show two different vectors A and C
        A = Vector([1, 0], color=GREEN)
        C = Vector([2, 0], color=RED)
        A_label2 = MathTex(r"\vec{A}", font_size=30).next_to(A, UR)
        C_label = MathTex(r"\vec{C}", font_size=30).next_to(C, UR)

        self.play(FadeOut(L_func, contour_lines_L, L_text, dot_product_text))
        self.play(Create(A), Write(A_label2))
        self.wait(1)
        self.play(Transform(A, C), Transform(A_label2, C_label))
        self.wait(1.5)

        # Show level sets for A and C
        contours_A = VGroup()
        for i in range(-5, 6):
            line = DashedLine(LEFT * 7, RIGHT * 7).shift(DOWN * (i * 0.5 + 1.5)).set_color(GREEN)
            contours_A.add(line)

        contours_C = VGroup()
        for i in range(-5, 6):
            line = DashedLine(LEFT * 7, RIGHT * 7).shift(DOWN * (i * 0.25 + 1.5)).set_color(RED)
            contours_C.add(line)

        self.play(Create(contours_A))
        self.wait(1)
        self.play(Transform(contours_A, contours_C))
        self.wait(1.5)

        # Conclusion text
        conclusion = Text("Each vector maps to a unique functional,\nand vice versa — an isomorphism!", font_size=24).to_edge(DOWN)
        conclusion.shift(0.0 * RIGHT + 0.53 * UP)  # layout: separation vector
        self.play(Write(conclusion))
        self.wait(2)

        self.play(FadeOut(title, A_prime, A_label, conclusion))
