from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Mechanism: Syndrome Calculation", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Venn diagram setup
        p1 = Circle(radius=1.5, color=GREEN, fill_opacity=0.3).shift(LEFT * 1.5 + UP * 0.5)
        p2 = Circle(radius=1.5, color=GREEN, fill_opacity=0.3).shift(RIGHT * 1.5 + UP * 0.5)
        p4 = Circle(radius=1.5, color=GREEN, fill_opacity=0.3).shift(UP * -1.5)

        # Data bits
        d1, d2, d3, d4, d5, d6, d7 = [
            Tex(f"D{i}").scale(0.7)
            for i in [1, 2, 3, 4, 5, 6, 7]
        ]
        
        # Position data bits manually to avoid overlap
        d1.move_to(p1.get_center() + DOWN * 0.5)
        d2.move_to(p1.get_center() + DOWN * 0.5 + LEFT * 0.5)
        d3.move_to(p1.get_center() + DOWN * 0.5 + RIGHT * 0.5)
        d4.move_to(p1.get_center() + DOWN * 0.5 + RIGHT * 1.0)
        d5.move_to(p2.get_center() + DOWN * 0.5)
        d6.move_to(p2.get_center() + DOWN * 0.5 + LEFT * 0.5)
        d7.move_to(p2.get_center() + DOWN * 0.5 + RIGHT * 0.5)

        # Parity bits
        p1_label = Tex("P1").scale(0.7).move_to(p1.get_center())
        p2_label = Tex("P2").scale(0.7).move_to(p2.get_center())
        p4_label = Tex("P4").scale(0.7).move_to(p4.get_center())

        # Show circles and labels
        self.play(Create(p1), Create(p2), Create(p4))
        self.play(Write(p1_label), Write(p2_label), Write(p4_label))
        self.wait(0.5)

        # Show data bits
        d1.shift(0.0 * RIGHT + 0.27 * UP)  # layout: separation vector
        d3.shift(0.0 * RIGHT + 0.27 * UP)  # layout: separation vector
        self.play(Write(d1), Write(d2), Write(d3), Write(d4), Write(d5), Write(d6), Write(d7))
        self.wait(0.5)

        # Simulate error in D2
        d2_copy = d2.copy()
        self.play(d2_copy.animate.set_fill(RED, opacity=1), run_time=0.3)
        self.wait(0.5)

        # Show failed checks
        p1_fail = p1.copy().set_color(RED)
        p4_fail = p4.copy().set_color(RED)
        self.play(Transform(p1, p1_fail), Transform(p4, p4_fail))
        self.wait(0.5)

        # Show syndrome text
        syndrome_text = Text("Syndrome = 101", font_size=30).to_edge(DOWN)
        self.play(Write(syndrome_text))
        self.wait(0.5)

        # Highlight position 5
        pos_5 = Tex("Position 5").scale(0.7).move_to(p2.get_center() + DOWN * 0.5)
        self.play(Write(pos_5))
        self.wait(0.5)

        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(p1), FadeOut(p2), FadeOut(p4),
            FadeOut(p1_label), FadeOut(p2_label), FadeOut(p4_label),
            FadeOut(d1), FadeOut(d2), FadeOut(d3), FadeOut(d4), FadeOut(d5), FadeOut(d6), FadeOut(d7),
            FadeOut(syndrome_text),
            FadeOut(pos_5),
        )
        self.wait(0.5)
