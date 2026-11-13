from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Odd Number Property", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial terms with glowing circles and checkmarks
        terms = [1, 3, 5, 11]
        circles = []
        checkmarks = []
        labels = []
        for i, term in enumerate(terms):
            circle = Circle(radius=0.4, color=["BLUE", "GREEN", "ORANGE", "PURPLE"][i]).set_fill(opacity=0.2)
            circle.move_to([-3 + i*1.5, 0, 0])
            circles.append(circle)
            num = MathTex(str(term), font_size=30).move_to(circle.get_center())
            checkmark = Tex("\checkmark", font_size=30)
            checkmark.next_to(circle, DOWN, buff=0.2)
            label = Text("Odd", font_size=24).next_to(checkmark, RIGHT)
            labels.append(label)

            self.play(Write(circle), Write(num), Write(checkmark), Write(label))
            self.wait(0.5)

        # Highlight coefficient 2 in formula
        formula = MathTex("v(n) = v(n-1) + 2 \\times v(n-2)", font_size=30)
        formula.to_edge(DOWN)
        self.play(Write(formula))
        self.wait(0.5)

        # Highlight '2'
        highlight_2 = SurroundingRectangle(formula[0][7:9], color=YELLOW, buff=0.1)
        highlight_2.shift(0.0 * RIGHT + -0.46 * UP)  # layout: separation vector
        self.play(Create(highlight_2))
        self.wait(0.5)
        self.play(FadeOut(highlight_2))

        # Show initial conditions
        init_label = Text("Initial Conditions:", font_size=24).to_edge(LEFT).shift(UP*1.5)
        v1 = MathTex("v(1) = 1", font_size=24).next_to(init_label, DOWN)
        v2 = MathTex("v(2) = 3", font_size=24).next_to(v1, DOWN)

        self.play(Write(init_label), Write(v1), Write(v2))
        self.wait(0.5)

        # Show calculation breakdown
        calc = MathTex("Odd + 2 \\times Odd", font_size=30)
        calc.to_edge(LEFT).shift(DOWN*1.5)
        self.play(Write(calc))
        self.wait(0.5)

        even_part = MathTex("= Odd + Even", font_size=30).next_to(calc, DOWN)
        self.play(Write(even_part))
        self.wait(0.5)

        result = MathTex("= Odd", font_size=30).next_to(even_part, DOWN)
        self.play(Write(result))
        self.wait(0.5)

        # Algebraic proof
        proof_label = Text("Algebraic Proof:", font_size=24).to_edge(LEFT).shift(DOWN*2.5)
        proof_label.shift(0.0 * RIGHT + -0.41 * UP)  # layout: separation vector
        self.play(Write(proof_label))
        self.wait(0.5)

        odd_plus_even = MathTex("Odd + 2 \\times Odd", font_size=30).to_edge(LEFT).shift(DOWN*3)
        even_label = Text("Even", font_size=24).next_to(odd_plus_even[0][7:10], DOWN)
        final_result = MathTex("= Odd", font_size=30).next_to(odd_plus_even, RIGHT)

        odd_plus_even.shift(0.0 * RIGHT + -0.35 * UP)  # layout: separation vector
        self.play(Write(odd_plus_even), Write(even_label), Write(final_result))
        self.wait(0.5)

        # Ratio of consecutive terms
        ratio_text = Text("Ratio v(n)/v(n-1):", font_size=24).to_edge(RIGHT).shift(UP*1.5)
        ratio_calc = MathTex("\\frac{11}{5} = 2.2", font_size=30).next_to(ratio_text, DOWN)

        self.play(Write(ratio_text), Write(ratio_calc))
        self.wait(0.5)

        # Emphasize v(n-1) in formula
        v_n_minus_1 = MathTex("v(n-1)", font_size=24)
        v_n_minus_1.next_to(formula[0][3:7], DOWN)
        self.play(Write(v_n_minus_1))
        self.wait(0.5)

        # Statement about growth
        growth_statement = Text("Each term is about twice the previous one.", font_size=24).to_edge(DOWN).shift(UP*0.5)
        self.play(Write(growth_statement))
        self.wait(0.5)

        # Final emphasis on v(n-1) being added
        add_statement = Text("Because we add v(n-1) to 2×v(n-2), the result is larger than 2×v(n-2).", font_size=24)
        add_statement.to_edge(DOWN).shift(UP*0.5)
        self.play(Transform(growth_statement, add_statement))
        self.wait(1)

        # Cleanup
        self.play(FadeOut(title), FadeOut(formula), FadeOut(calc), FadeOut(even_part), FadeOut(result),
                  FadeOut(proof_label), FadeOut(odd_plus_even), FadeOut(even_label), FadeOut(final_result),
                  FadeOut(ratio_text), FadeOut(ratio_calc), FadeOut(v_n_minus_1), FadeOut(growth_statement),
                  *[FadeOut(c) for c in circles], 
                  *[FadeOut(m) for m in checkmarks],
                  *[FadeOut(l) for l in labels], 
                  *[FadeOut(v) for v in [v1, v2, init_label]])
        self.wait(0.5)
