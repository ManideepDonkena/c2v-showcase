from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Pythagoras Theorem", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Formula appears
        formula = MathTex("a^2 + b^2 = c^2", font_size=40)
        self.play(Write(formula))
        self.wait(1)
        
        # Pulse variables a, b, c
        a = MathTex("a").move_to(formula.get_part_by_tex("a"))
        b = MathTex("b").move_to(formula.get_part_by_tex("b"))
        c = MathTex("c").move_to(formula.get_part_by_tex("c"))

        self.play(
            a.animate.scale(1.2).set_color(YELLOW),
            b.animate.scale(1.2).set_color(GREEN),
            c.animate.scale(1.2).set_color(RED),
            run_time=0.5
        )
        self.play(
            a.animate.scale(1/1.2).set_color(WHITE),
            b.animate.scale(1/1.2).set_color(WHITE),
            c.animate.scale(1/1.2).set_color(WHITE),
            run_time=0.5
        )

        self.wait(1)

        # Step-by-step calculation: √(81 + 144) = 15
        calc1 = MathTex("81 + 144 = 225", font_size=24).to_edge(DOWN)
        self.play(Write(calc1))
        self.wait(0.5)

        calc2 = MathTex("\\sqrt{225} = 15", font_size=24).next_to(calc1, UP)
        self.play(Write(calc2))
        self.wait(1.5)

        # Algebraic rearrangement: find leg a
        self.play(FadeOut(calc1), FadeOut(calc2))

        rearrange = MathTex("c^2 - b^2 = a^2", font_size=24).to_edge(DOWN)
        self.play(Write(rearrange))
        self.wait(0.5)

        calc3 = MathTex("100 - 36 = 64", font_size=24).next_to(rearrange, UP)
        self.play(Write(calc3))
        self.wait(0.5)

        calc4 = MathTex("\\sqrt{64} = 8", font_size=24).next_to(calc3, UP)
        self.play(Write(calc4))
        self.wait(1.5)

        # Final numerical example
        self.play(FadeOut(rearrange), FadeOut(calc3), FadeOut(calc4))

        example = MathTex("8^2 + 15^2 = 64 + 225 = 289", font_size=24).to_edge(DOWN)
        self.play(Write(example))
        self.wait(0.5)

        example2 = MathTex("\\sqrt{289} = 17", font_size=24).next_to(example, UP)
        self.play(Write(example2))
        self.wait(1.5)

        # Keep formula on screen
        self.play(FadeOut(title), FadeOut(example), FadeOut(example2))
        self.wait(0.5)
