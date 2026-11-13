from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Calculating v(3) and v(4)", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial sequence
        seq = MathTex("1, 3").scale(1.2)
        seq.to_edge(UP).shift(DOWN * 0.8)
        self.play(Write(seq))
        self.wait(0.5)

        # v(3) calculation
        calc3 = MathTex("v(3) = 3 + 2 \\times 1 = 5").scale(1.2)
        calc3.next_to(seq, DOWN, buff=0.8)
        self.play(Write(calc3))
        self.wait(1)

        # Highlight result
        if len(calc3) > 2:
            result3 = MathTex("5").set_color(YELLOW).scale(1.2)
            result3.move_to(calc3[2])
            self.play(Transform(calc3[2], result3))
            self.wait(1)

        # v(4) calculation
        calc4 = MathTex("v(4) = 5 + 2 \\times 3 = 11").scale(1.2)
        calc4.next_to(calc3, DOWN, buff=0.8)
        self.play(Write(calc4))
        self.wait(1)

        # Highlight result
        result4 = MathTex("11").set_color(YELLOW).scale(1.2)
        if len(calc4) > 2:
            result4.move_to(calc4[2])
            self.play(Transform(calc4[2], result4))
        self.wait(1)

        # Narration text
        narration1 = Text("To find v(3), we add 3 to twice 1, resulting in 5.", font_size=24)
        narration1.to_edge(DOWN)
        self.play(Write(narration1))
        self.wait(1.5)
        self.play(FadeOut(narration1))

        narration2 = Text("For v(4), we take that 5 and add it to twice 3, giving us 11.", font_size=24)
        narration2.to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(1.5)
        self.play(FadeOut(narration2))

        # Cleanup
        self.play(FadeOut(title), FadeOut(seq), FadeOut(calc3), FadeOut(calc4))
        self.wait(0.5)
