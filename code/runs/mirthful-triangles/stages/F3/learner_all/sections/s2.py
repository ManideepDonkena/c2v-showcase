from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Equilateral Case", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Equilateral triangle
        triangle_eq = Triangle().scale(1.5).move_to(ORIGIN)
        label_5 = MathTex("5").next_to(triangle_eq, DOWN)
        triangle_eq.add(label_5)
        self.play(Create(triangle_eq))
        self.wait(0.5)

        # Rule 1: All equilateral triangles are mirthful
        rule_text = Text("Rule 1: All equilateral triangles are mirthful.", font_size=24)
        rule_text.next_to(triangle_eq, DOWN, buff=0.5)
        self.play(Write(rule_text))
        self.wait(1)

        # Calculation for equilateral case
        calc1 = MathTex("2 \\times 5 \\leq 3 \\times 5", font_size=30)
        calc1.next_to(rule_text, DOWN, buff=0.5)
        self.play(Write(calc1))
        self.wait(0.5)

        # Evaluate the inequality
        eval1 = MathTex("10 \\leq 15").next_to(calc1, DOWN, buff=0.3)
        self.play(Write(eval1))
        self.wait(1)

        # Animate triangle turning green and bouncing
        self.play(
            triangle_eq.animate.set_fill(GREEN, opacity=0.8),
            triangle_eq.animate.shift(DOWN * 0.2).scale(1.05),
            run_time=0.5
        )
        self.play(
            triangle_eq.animate.shift(UP * 0.2).scale(0.95),
            run_time=0.5
        )
        self.wait(1)

        # Fade out first part
        self.play(FadeOut(triangle_eq), FadeOut(calc1), FadeOut(eval1), FadeOut(rule_text))

        # New triangle: sides 2, 3, 4
        triangle_new = Triangle().scale(1.5).move_to(ORIGIN)
        labels = VGroup(
            MathTex("2").next_to(triangle_new, DL),
            MathTex("3").next_to(triangle_new, UP),
            MathTex("4").next_to(triangle_new, DR)
        )
        triangle_new.add(labels)
        self.play(Create(triangle_new))
        self.wait(0.5)

        # Identify longest and shortest
        longest_label = MathTex("4").set_color(YELLOW).move_to(triangle_new.get_vertices()[2])
        shortest_label = MathTex("2").set_color(BLUE).move_to(triangle_new.get_vertices()[0])
        self.play(Write(longest_label), Write(shortest_label))
        self.wait(1)

        # Ask the question
        question = Text("Check the rule: Is twice the longest side at most three times the shortest?", font_size=24)
        question.next_to(triangle_new, DOWN, buff=0.5)
        self.play(Write(question))
        self.wait(1.5)

        # Show calculation
        calc2 = MathTex("2 \\times 4 \\leq 3 \\times 2", font_size=30).next_to(question, DOWN, buff=0.5)
        self.play(Write(calc2))
        self.wait(0.5)

        # Evaluate the inequality
        eval2 = MathTex("8 \\leq 6").next_to(calc2, DOWN, buff=0.3)
        self.play(Write(eval2))
        self.wait(1)

        # Red X to indicate failure
        cross = Cross(eval2).set_color(RED)
        self.play(Create(cross))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(triangle_new),
            FadeOut(longest_label),
            FadeOut(shortest_label),
            FadeOut(question),
            FadeOut(calc2),
            FadeOut(eval2),
            FadeOut(cross),
            FadeOut(title)
        )
        self.wait(0.5)
