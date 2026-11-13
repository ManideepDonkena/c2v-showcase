from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("Worked Examples", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Triangles
        # Left triangle: 4, 5, 6
        a1, b1, c1 = 4, 5, 6
        side1 = Line(start=LEFT * 2, end=RIGHT * 2, color=GREEN)
        side2 = Line(start=RIGHT * 2, end=UP * 1.5, color=GREEN)
        side3 = Line(start=UP * 1.5, end=LEFT * 2, color=GREEN)
        tri1 = VGroup(side1, side2, side3).scale(0.7).to_edge(LEFT)
        label1 = MathTex("4, 5, 6", font_size=24).next_to(tri1, DOWN)

        # Right triangle: 3, 4, 5
        a2, b2, c2 = 3, 4, 5
        side1_2 = Line(start=LEFT * 2, end=RIGHT * 2, color=RED)
        side2_2 = Line(start=RIGHT * 2, end=UP * 1.5, color=RED)
        side3_2 = Line(start=UP * 1.5, end=LEFT * 2, color=RED)
        tri2 = VGroup(side1_2, side2_2, side3_2).scale(0.7).to_edge(RIGHT)
        label2 = MathTex("3, 4, 5", font_size=24).next_to(tri2, DOWN)

        # Draw triangles
        self.play(Create(tri1), Write(label1))
        self.wait(0.5)
        self.play(Create(tri2), Write(label2))
        self.wait(0.5)

        # Check mirthfulness for left triangle (4, 5, 6)
        calc1 = MathTex("2 \\times 6 = 12", font_size=24).to_edge(DOWN).shift(LEFT * 2)
        calc2 = MathTex("3 \\times 4 = 12", font_size=24).next_to(calc1, RIGHT)
        check = Text("✓", font_size=40, color=GREEN).next_to(calc2, RIGHT)

        self.play(Write(calc1), Write(calc2))
        self.wait(0.5)
        self.play(Write(check))
        self.wait(0.5)

        # Check mirthfulness for right triangle (3, 4, 5)
        calc3 = MathTex("2 \\times 5 = 10", font_size=24).to_edge(DOWN).shift(RIGHT * 2)
        calc4 = MathTex("3 \\times 3 = 9", font_size=24).next_to(calc3, RIGHT)
        x = Text("✗", font_size=40, color=RED).next_to(calc4, RIGHT)

        self.play(Write(calc3), Write(calc4))
        self.wait(0.5)
        self.play(Write(x))
        self.wait(1)

        # Narration text
        narration1 = Text("Consider sides 4, 5, 6", font_size=24).to_edge(UP).shift(DOWN * 3)
        narration2 = Text("twice the longest is 12", font_size=24).next_to(narration1, DOWN)
        narration3 = Text("three times the shortest is 12", font_size=24).next_to(narration2, DOWN)
        narration4 = Text("so it is mirthful", font_size=24).next_to(narration3, DOWN)

        self.play(Write(narration1))
        self.wait(0.5)
        self.play(Write(narration2))
        self.wait(0.5)
        self.play(Write(narration3))
        self.wait(0.5)
        self.play(Write(narration4))
        self.wait(1)

        # Clear narration
        self.play(FadeOut(narration1), FadeOut(narration2), FadeOut(narration3), FadeOut(narration4))

        narration5 = Text("But for 3, 4, 5", font_size=24).to_edge(UP).shift(DOWN * 3)
        narration6 = Text("twice the longest is 10", font_size=24).next_to(narration5, DOWN)
        narration7 = Text("which exceeds nine", font_size=24).next_to(narration6, DOWN)
        narration8 = Text("so it is not mirthful", font_size=24).next_to(narration7, DOWN)

        self.play(Write(narration5))
        self.wait(0.5)
        self.play(Write(narration6))
        self.wait(0.5)
        self.play(Write(narration7))
        self.wait(0.5)
        self.play(Write(narration8))
        self.wait(1)

        # Clear narration
        self.play(FadeOut(narration5), FadeOut(narration6), FadeOut(narration7), FadeOut(narration8))

        # New triangle: 5, 7, 8
        a3, b3, c3 = 5, 7, 8
        side1_3 = Line(start=LEFT * 2, end=RIGHT * 2, color=YELLOW)
        side2_3 = Line(start=RIGHT * 2, end=UP * 1.5, color=YELLOW)
        side3_3 = Line(start=UP * 1.5, end=LEFT * 2, color=YELLOW)
        tri3 = VGroup(side1_3, side2_3, side3_3).scale(0.7).to_edge(LEFT).shift(DOWN * 2)
        label3 = MathTex("5, 7, 8", font_size=24).next_to(tri3, DOWN)

        # Labels for sides
        label_a = MathTex("5", font_size=24).next_to(side1_3, DOWN)
        label_b = MathTex("7", font_size=24).next_to(side2_3, RIGHT)
        label_c = MathTex("8", font_size=24).next_to(side3_3, LEFT)

        self.play(Create(tri3), Write(label3))
        self.wait(0.5)
        label_a.shift(0.0 * RIGHT + 0.32 * UP)  # layout: separation vector
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(0.5)

        # Narration for new triangle
        narration_new = Text("Check the rule: Is twice the longest side at most three times the shortest?", font_size=24).to_edge(UP).shift(DOWN * 3)
        self.play(Write(narration_new))
        self.wait(1)

        # Calculation
        calc_rule = MathTex("2 \\times 8 \\leq 3 \\times 5", font_size=36).to_edge(DOWN)
        self.play(Write(calc_rule))
        self.wait(1)

        # Evaluate the rule
        calc_result = MathTex("16 \\leq 15", font_size=36).to_edge(DOWN)
        self.play(Transform(calc_rule, calc_result))
        self.wait(1)

        # Red X or pulse
        red_x = Text("✗", font_size=72, color=RED).move_to(calc_result.get_center())
        self.play(Write(red_x))
        self.wait(1)

        # Fade out narration and red x
        self.play(FadeOut(narration_new), FadeOut(red_x))

        self.wait(1)
