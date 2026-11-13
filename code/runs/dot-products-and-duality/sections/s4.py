from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Duality Isomorphism", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Left side: Linear Functional L (contour lines)
        functional_group = VGroup()
        for i in range(-5, 6):
            line = Line(
                start=LEFT * 7 + UP * i * 0.5,
                end=RIGHT * 7 + UP * i * 0.5,
                color=YELLOW
            )
            functional_group.add(line)
        
        L_text = Text("L", font_size=24).next_to(functional_group[0], LEFT)
        functional_group.add(L_text)

        # Right side: Vector A'
        A_prime = Vector([3, 2], color=BLUE)
        A_prime_label = MathTex(r"\vec{A'}", font_size=24).next_to(A_prime.get_end(), UR)
        
        # Create dot product function
        def dot_product_func(B):
            return A_prime.get_end() @ B.get_end()
        
        # Show vector A' and its effect
        vector_group = VGroup(A_prime, A_prime_label)
        vector_group.to_edge(RIGHT)

        L_text.shift(0.47 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(
            FadeIn(functional_group),
            Write(vector_group)
        )
        self.wait(1)

        # Morph contour lines to match level sets of dot product
        morph_group = VGroup()
        for i in range(-5, 6):
            line = Line(
                start=LEFT * 7 + UP * i * 0.5,
                end=RIGHT * 7 + UP * i * 0.5,
                color=YELLOW,
                stroke_width=2
            )
            morph_group.add(line)
        
        # Show the transformation
        self.play(
            Transform(functional_group, morph_group),
            run_time=2
        )
        self.wait(1)

        # Flash the formula
        formula = MathTex(r"L(\vec{B}) = \vec{A'} \cdot \vec{B}", font_size=40)
        formula.to_edge(DOWN)
        self.play(Write(formula))
        self.wait(2)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(functional_group),
            FadeOut(vector_group),
            FadeOut(formula)
        )
        self.wait(0.5)
