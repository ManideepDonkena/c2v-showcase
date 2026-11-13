from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Equilateral Case", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Start with equilateral triangle labeled 5
        tri1 = Triangle().scale(1.5).set_color(WHITE)
        tri1.shift(LEFT * 2 + UP * 0.5)
        side_labels1 = VGroup(
            MathTex("5").next_to(tri1.get_vertices()[0], DOWN),
            MathTex("5").next_to(tri1.get_vertices()[1], DOWN),
            MathTex("5").next_to(tri1.get_vertices()[2], DOWN)
        )
        calc1 = MathTex("2 \\times 5 \\leq 3 \\times 5", font_size=30).next_to(tri1, DOWN, buff=0.8)
        self.play(Create(tri1), Write(side_labels1), Write(calc1))
        self.wait(1)

        # Animate triangle turning green and bouncing
        self.play(tri1.animate.set_color(GREEN), run_time=0.2)
        self.play(tri1.animate.shift(DOWN * 0.2).shift(UP * 0.2), run_time=0.4)
        self.wait(0.5)

        # Narration text
        narration1 = Text("Every equilateral triangle is mirthful", font_size=24).to_edge(DOWN)
        self.play(Write(narration1))
        self.wait(1.5)
        self.play(FadeOut(narration1))

        # Show a general triangle with sides a and c
        tri2 = Triangle().scale(1.5).set_color(WHITE).shift(RIGHT * 2 + UP * 0.5)
        side_labels2 = VGroup(
            MathTex("a").next_to(tri2.get_vertices()[0], DOWN),
            MathTex("c").next_to(tri2.get_vertices()[1], DOWN),
            MathTex("b").next_to(tri2.get_vertices()[2], DOWN)
        )
        calc2 = MathTex("2 \\times c \\leq 3 \\times a", font_size=30).next_to(tri2, DOWN, buff=0.8)
        self.play(Create(tri2), Write(side_labels2), Write(calc2))
        self.wait(1)

        # Algebraic manipulation
        calc3 = MathTex("c \\leq 1.5 a", font_size=30).next_to(calc2, DOWN, buff=0.5)
        self.play(Write(calc3))
        self.wait(1.5)
        self.play(FadeOut(calc2), FadeOut(calc3))

        # Show triangle with sides 10, 20, 30
        tri3 = Triangle().scale(1.2).set_color(WHITE).shift(LEFT * 2 + DOWN * 1.5)
        side_labels3 = VGroup(
            MathTex("10").next_to(tri3.get_vertices()[0], DOWN),
            MathTex("20").next_to(tri3.get_vertices()[1], DOWN),
            MathTex("30").next_to(tri3.get_vertices()[2], DOWN)
        )
        calc4 = MathTex("2 \times 30", font_size=30).move_to(LEFT * 3 + DOWN * 2.5)
        calc5 = MathTex("3 \times 10", font_size=30).move_to(RIGHT * 3 + DOWN * 2.5)
        comp = MathTex(">").next_to(calc4, RIGHT, buff=0.3)
        calc4.shift(0.0 * RIGHT + 0.27 * UP)  # layout: separation vector
        self.play(Create(tri3), Write(side_labels3), Write(calc4), Write(calc5), Write(comp))
        self.wait(1)

        # Highlight that 60 > 30
        highlight = SurroundingRectangle(VGroup(calc4, comp, calc5), color=RED, buff=0.2)
        self.play(Create(highlight))
        self.wait(1.5)
        self.play(FadeOut(calc4), FadeOut(calc5), FadeOut(comp), FadeOut(highlight))

        # Show triangle with sides 4, 10, 12
        tri4 = Triangle().scale(1.2).set_color(WHITE).shift(RIGHT * 2 + DOWN * 1.5)
        side_labels4 = VGroup(
            MathTex("4").next_to(tri4.get_vertices()[0], DOWN),
            MathTex("10").next_to(tri4.get_vertices()[1], DOWN),
            MathTex("12").next_to(tri4.get_vertices()[2], DOWN)
        )
        calc6 = MathTex("2 \\times 12", font_size=30).move_to(LEFT * 3 + DOWN * 2.5)
        calc7 = MathTex("3 \\times 4", font_size=30).move_to(RIGHT * 3 + DOWN * 2.5)
        comp2 = MathTex("\\leq").next_to(calc6, RIGHT, buff=0.3)
        result = MathTex("24 \\leq 12", color=RED, font_size=30).next_to(comp2, RIGHT, buff=0.3)
        cross = Cross(result)
        calc6.shift(0.0 * RIGHT + 0.35 * UP)  # layout: separation vector
        self.play(Create(tri4), Write(side_labels4), Write(calc6), Write(calc7), Write(comp2))
        self.wait(1)
        self.play(Write(result), Create(cross))
        self.wait(1.5)
        self.play(FadeOut(calc6), FadeOut(calc7), FadeOut(comp2), FadeOut(result), FadeOut(cross))

        # Show triangle with sides 5, 100, 101
        tri5 = Triangle().scale(1.2).set_color(WHITE).shift(LEFT * 2 + DOWN * 3)
        side_labels5 = VGroup(
            MathTex("5").next_to(tri5.get_vertices()[0], DOWN),
            MathTex("100").next_to(tri5.get_vertices()[1], DOWN),
            MathTex("101").next_to(tri5.get_vertices()[2], DOWN)
        )
        calc8 = MathTex("2 \\times 101", font_size=30).move_to(LEFT * 3 + DOWN * 4)
        calc9 = MathTex("3 \\times 5", font_size=30).move_to(RIGHT * 3 + DOWN * 4)
        comp3 = MathTex("\\leq").next_to(calc8, RIGHT, buff=0.3)
        result2 = MathTex("202 \\leq 15", color=RED, font_size=30).next_to(comp3, RIGHT, buff=0.3)
        cross2 = Cross(result2)
        self.play(Create(tri5), Write(side_labels5), Write(calc8), Write(calc9), Write(comp3))
        self.wait(1)
        self.play(Write(result2), Create(cross2))
        self.wait(1.5)
        self.play(FadeOut(calc8), FadeOut(calc9), FadeOut(comp3), FadeOut(result2), FadeOut(cross2))

        # Show triangle with sides 10, 14, 15
        tri6 = Triangle().scale(1.2).set_color(WHITE).shift(RIGHT * 2 + DOWN * 3)
        side_labels6 = VGroup(
            MathTex("10").next_to(tri6.get_vertices()[0], DOWN),
            MathTex("14").next_to(tri6.get_vertices()[1], DOWN),
            MathTex("15").next_to(tri6.get_vertices()[2], DOWN)
        )
        question = Text("Check the rule: Is 2 times the longest side at most 3 times the shortest side?", font_size=24).to_edge(DOWN)
        self.play(Create(tri6), Write(side_labels6), Write(question))
        self.wait(1.5)
        self.play(FadeOut(question))

        calc10 = MathTex("2 \\times 15 \\leq 3 \\times 10", font_size=30).move_to(LEFT * 3 + DOWN * 4)
        result3 = MathTex("30 \\leq 30", font_size=30).next_to(calc10, RIGHT, buff=0.3)
        self.play(Write(calc10))
        self.wait(1)
        self.play(Write(result3))
        self.wait(1)

        # Pulse green
        self.play(tri6.animate.set_color(GREEN), run_time=0.2)
        self.play(tri6.animate.shift(DOWN * 0.2).shift(UP * 0.2), run_time=0.4)
        self.wait(1.5)
        self.play(FadeOut(calc10), FadeOut(result3))

        # Show triangle with sides 2, 3, 4
        tri7 = Triangle().scale(1.2).set_color(WHITE).shift(LEFT * 2 + DOWN * 5)
        side_labels7 = VGroup(
            MathTex("2").next_to(tri7.get_vertices()[0], DOWN),
            MathTex("3").next_to(tri7.get_vertices()[1], DOWN),
            MathTex("4").next_to(tri7.get_vertices()[2], DOWN)
        )
        calc11 = MathTex("2 \\times 4", font_size=30).move_to(LEFT * 3 + DOWN * 6)
        calc12 = MathTex("3 \\times 2", font_size=30).move_to(RIGHT * 3 + DOWN * 6)
        comp4 = MathTex("\\leq").next_to(calc11, RIGHT, buff=0.3)
        result4 = MathTex("8 \\leq 6", color=RED, font_size=30).next_to(comp4, RIGHT, buff=0.3)
        cross3 = Cross(result4)
        self.play(Create(tri7), Write(side_labels7), Write(calc11), Write(calc12), Write(comp4))
        self.wait(1)
        self.play(Write(result4), Create(cross3))
        self.wait(1.5)
        self.play(FadeOut(calc11), FadeOut(calc12), FadeOut(comp4), FadeOut(result4), FadeOut(cross3))

        # Show equilateral triangle with side x
        tri8 = Triangle().scale(1.5).set_color(WHITE).shift(RIGHT * 2 + DOWN * 5)
        side_labels8 = VGroup(
            MathTex("x").next_to(tri8.get_vertices()[0], DOWN),
            MathTex("x").next_to(tri8.get_vertices()[1], DOWN),
            MathTex("x").next_to(tri8.get_vertices()[2], DOWN)
        )
        calc13 = MathTex("2 \\times x \\leq 3 \\times x", font_size=30).next_to(tri8, DOWN, buff=0.8)
        self.play(Create(tri8), Write(side_labels8), Write(calc13))
        self.wait(1)

        # Simplify to 2 <= 3
        calc14 = MathTex("2 \\leq 3", font_size=30).next_to(calc13, DOWN, buff=0.5)
        self.play(Write(calc14))
        self.wait(1.5)
        self.play(FadeOut(calc13), FadeOut(calc14))

        # Show two triangles with same shortest and longest but different middle
        tri9 = Triangle().scale(1.2).set_color(WHITE).shift(LEFT * 2 + DOWN * 7)
        side_labels9 = VGroup(
            MathTex("4").next_to(tri9.get_vertices()[0], DOWN),
            MathTex("5").next_to(tri9.get_vertices()[1], DOWN),
            MathTex("6").next_to(tri9.get_vertices()[2], DOWN)
        )
        tri10 = Triangle().scale(1.2).set_color(WHITE).shift(RIGHT * 2 + DOWN * 7)
        side_labels10 = VGroup(
            MathTex("4").next_to(tri10.get_vertices()[0], DOWN),
            MathTex("2").next_to(tri10.get_vertices()[1], DOWN),
            MathTex("6").next_to(tri10.get_vertices()[2], DOWN)
        )
        self.play(Create(tri9), Write(side_labels9), Create(tri10), Write(side_labels10))
        self.wait(1)

        # Calculate 2 * longest and 3 * shortest for both
        calc15 = MathTex("2 \\times 6", font_size=30).move_to(LEFT * 3 + DOWN * 8)
        calc16 = MathTex("3 \\times 4", font_size=30).move_to(RIGHT * 3 + DOWN * 8)
        comp5 = MathTex("\\leq").next_to(calc15, RIGHT, buff=0.3)
        result5 = MathTex("12 \\leq 12", font_size=30).next_to(comp5, RIGHT, buff=0.3)
        self.play(Write(calc15), Write(calc16), Write(comp5))
        self.wait(1)
        self.play(Write(result5))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(tri1), FadeOut(side_labels1), FadeOut(calc1),
                  FadeOut(tri2), FadeOut(side_labels2), FadeOut(calc2),
                  FadeOut(tri3), FadeOut(side_labels3), FadeOut(calc4), FadeOut(calc5), FadeOut(comp),
                  FadeOut(tri4), FadeOut(side_labels4), FadeOut(calc6), FadeOut(calc7), FadeOut(comp2), FadeOut(result), FadeOut(cross),
                  FadeOut(tri5), FadeOut(side_labels5), FadeOut(calc8), FadeOut(calc9), FadeOut(comp3), FadeOut(result2), FadeOut(cross2),
                  FadeOut(tri6), FadeOut(side_labels6), FadeOut(calc10), FadeOut(result3),
                  FadeOut(tri7), FadeOut(side_labels7), FadeOut(calc11), FadeOut(calc12), FadeOut(comp4), FadeOut(result4), FadeOut(cross3),
                  FadeOut(tri8), FadeOut(side_labels8), FadeOut(calc13), FadeOut(calc14),
                  FadeOut(tri9), FadeOut(side_labels9), FadeOut(tri10), FadeOut(side_labels10),
                  FadeOut(calc15), FadeOut(calc16), FadeOut(comp5), FadeOut(result5))
        self.wait(0.5)

        # Final title fade out
        self.play(FadeOut(title))
        self.wait(0.5)
