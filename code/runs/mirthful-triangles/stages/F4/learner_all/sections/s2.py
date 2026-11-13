from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Equilateral Case", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Draw equilateral triangle with sides labeled '5'
        triangle_eq = Triangle().scale(1.5).shift(UP * 0.5)
        label_a = MathTex("5").next_to(triangle_eq, UL)
        label_b = MathTex("5").next_to(triangle_eq, UR)
        label_c = MathTex("5").next_to(triangle_eq, DOWN)
        triangle_group_eq = VGroup(triangle_eq, label_a, label_b, label_c)

        self.play(Create(triangle_eq), run_time=0.5)
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(0.5)

        # Show calculation for equilateral case
        calc1 = MathTex("2 \\times 5 \\leq 3 \\times 5").scale(1.2).to_edge(DOWN)
        calc1_num = MathTex("10 \\leq 15").scale(1.2).to_edge(DOWN)
        self.play(Write(calc1))
        self.wait(1)

        # Animate calculation
        self.play(Transform(calc1, calc1_num))
        self.wait(1)

        # Highlight triangle as mirthful (green and bounce)
        self.play(triangle_eq.animate.set_color(GREEN), run_time=0.2)
        self.play(triangle_eq.animate.shift(DOWN * 0.1).shift(UP * 0.1), run_time=0.4)
        self.wait(1)

        # Fade out equilateral triangle and calculation
        self.play(FadeOut(triangle_group_eq), FadeOut(calc1))
        self.wait(0.5)

        # Show new triangle with sides 5, 7, 8
        triangle_new = Triangle().scale(1.5).shift(UP * 0.5)
        label_5 = MathTex("5").next_to(triangle_new, DL)
        label_7 = MathTex("7").next_to(triangle_new, UR)
        label_8 = MathTex("8").next_to(triangle_new, DOWN)
        triangle_group_new = VGroup(triangle_new, label_5, label_7, label_8)

        self.play(Create(triangle_new), run_time=0.5)
        self.play(Write(label_5), Write(label_7), Write(label_8))
        self.wait(1)

        # Narration text: "Check the rule: Is twice the longest side at most three times the shortest?"
        rule_text = Text("Check the rule:", font_size=24).to_edge(DOWN)
        rule_text2 = Text("Is twice the longest side at most three times the shortest?", font_size=24).next_to(rule_text, DOWN)
        rule_text2.shift(0.0 * RIGHT + 0.23 * UP)  # layout: separation vector
        self.play(Write(rule_text), Write(rule_text2))
        self.wait(2)

        # Fade out narration
        self.play(FadeOut(rule_text), FadeOut(rule_text2))

        # Show calculation for new triangle: 2 * 8 <= 3 * 5
        calc2 = MathTex("2 \\times 8 \\leq 3 \\times 5").scale(1.2).to_edge(DOWN)
        self.play(Write(calc2))
        self.wait(1)

        # Animate to result: 16 <= 15
        calc2_result = MathTex("16 \\leq 15").scale(1.2).to_edge(DOWN)
        self.play(Transform(calc2, calc2_result))
        self.wait(1)

        # Show red X or pulse red to indicate failure
        cross = Cross(calc2, color=RED, stroke_width=10)
        self.play(Create(cross))
        self.wait(1.5)

        # Fade out everything
        self.play(FadeOut(triangle_group_new), FadeOut(calc2), FadeOut(cross), FadeOut(title))
        self.wait(0.5)
