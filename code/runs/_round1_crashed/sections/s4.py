from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Pythagoras Theorem: Visual Proof", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Formula appears
        formula = MathTex("a^2 + b^2 = c^2", font_size=40)
        self.play(Write(formula))
        self.wait(1)

        # Pulsing variables
        a, b, c = Tex("a", font_size=36), Tex("b", font_size=36), Tex("c", font_size=36)
        a.next_to(formula, DOWN, buff=0.5).shift(LEFT * 1.5)
        b.next_to(formula, DOWN, buff=0.5).shift(RIGHT * 0.5)
        c.next_to(formula, DOWN, buff=0.5).shift(RIGHT * 2.5)

        self.play(Write(a), Write(b), Write(c))
        self.play(
            a.animate.scale(1.2),
            b.animate.scale(1.2),
            c.animate.scale(1.2),
            run_time=0.3
        )
        self.play(
            a.animate.scale(1/1.2),
            b.animate.scale(1/1.2),
            c.animate.scale(1/1.2),
            run_time=0.3
        )

        # Isolate 'c'
        self.wait(0.5)
        c_eq = MathTex("c = \\sqrt{a^2 + b^2}", font_size=36).next_to(formula, DOWN, buff=1)
        self.play(Write(c_eq))
        self.wait(1)

        # Rearrange for 'b'
        b_eq = MathTex("b = \\sqrt{c^2 - a^2}", font_size=36).next_to(c_eq, DOWN, buff=0.5)
        self.play(Write(b_eq))
        self.wait(1)

        # Irrational number explanation
        irrational = Text("√2 ≈ 1.41 (irrational)", font_size=24).next_to(b_eq, DOWN, buff=0.5)
        self.play(Write(irrational))
        self.wait(1.5)

        # Step-by-step calculation: √(81 + 144) = √225 = 15
        calc1 = MathTex("\\sqrt{81 + 144} = \\sqrt{225} = 15", font_size=28).next_to(irrational, DOWN, buff=0.5)
        calc1.shift(0.0 * RIGHT + 0.36 * UP)  # layout: separation vector
        self.play(Write(calc1))
        self.wait(1.5)

        # Visual confirmation: c > a and c > b
        confirm = Text("c must be longer than a or b", font_size=24).next_to(calc1, DOWN, buff=0.5)
        self.play(Write(confirm))
        self.wait(1.5)

        # Subtraction vs addition
        sub_add = Text("Subtract when solving for leg: c² - a²", font_size=24).next_to(confirm, DOWN, buff=0.5)
        self.play(Write(sub_add))
        self.wait(1.5)

        # Another example: √(49 + 576) = √625 = 25
        calc2 = MathTex("\\sqrt{49 + 576} = \\sqrt{625} = 25", font_size=28).next_to(sub_add, DOWN, buff=0.5)
        self.play(Write(calc2))
        self.wait(1.5)

        # More examples
        calc3 = MathTex("\\sqrt{81 + 1600} = \\sqrt{1681} = 41", font_size=28).next_to(calc2, DOWN, buff=0.5)
        self.play(Write(calc3))
        self.wait(1.5)

        calc4 = MathTex("\\sqrt{100 + 576} = \\sqrt{676} = 26", font_size=28).next_to(calc3, DOWN, buff=0.5)
        self.play(Write(calc4))
        self.wait(1.5)

        calc5 = MathTex("\\sqrt{225 + 64} = \\sqrt{289} = 17", font_size=28).next_to(calc4, DOWN, buff=0.5)
        self.play(Write(calc5))
        self.wait(1.5)

        # Final fade
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(a),
            FadeOut(b),
            FadeOut(c),
            FadeOut(c_eq),
            FadeOut(b_eq),
            FadeOut(irrational),
            FadeOut(calc1),
            FadeOut(confirm),
            FadeOut(sub_add),
            FadeOut(calc2),
            FadeOut(calc3),
            FadeOut(calc4),
            FadeOut(calc5)
        )
        self.wait(0.5)
