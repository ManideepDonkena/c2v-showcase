from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Scaling Invariance", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial triangle: sides 4, 5, 6
        a, b, c = 4, 5, 6
        longest = c
        shortest = a
        ratio = longest / shortest

        # Draw initial triangle
        tri1 = Triangle().scale(0.8).to_edge(LEFT)
        tri1.shift(DOWN * 0.5)
        tri1.set_stroke(color=GREEN, width=3)
        self.play(Create(tri1))
        self.wait(0.5)

        # Label sides
        label_a = MathTex(f"{a}").next_to(tri1.get_vertices()[0], DOWN)
        label_b = MathTex(f"{b}").next_to(tri1.get_vertices()[1], UP)
        label_c = MathTex(f"{c}").next_to(tri1.get_vertices()[2], UP)
        label_b.shift(-0.25 * RIGHT + 0.0 * UP)  # layout: separation vector
        label_c.shift(0.25 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(0.5)

        # Check mirthfulness
        check = MathTex(r"2 \times 6 = 12 \leq 3 \times 4 = 12").scale(0.8)
        check.to_edge(DOWN)
        self.play(Write(check))
        self.wait(1)

        # Scale up to 8, 10, 12
        tri2 = Triangle().scale(1.6).to_edge(RIGHT)
        tri2.shift(DOWN * 0.5)
        tri2.set_stroke(color=GREEN, width=3)
        self.play(Transform(tri1, tri2))
        self.wait(0.5)

        # Update labels
        label_a2 = MathTex(f"8").next_to(tri2.get_vertices()[0], DOWN)
        label_b2 = MathTex(f"10").next_to(tri2.get_vertices()[1], UP)
        label_c2 = MathTex(f"12").next_to(tri2.get_vertices()[2], UP)
        label_b2.shift(-0.37 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(ReplacementTransform(label_a, label_a2),
                  ReplacementTransform(label_b, label_b2),
                  ReplacementTransform(label_c, label_c2))
        self.wait(0.5)

        # Check mirthfulness again
        check2 = MathTex(r"2 \times 12 = 24 \leq 3 \times 8 = 24").scale(0.8)
        self.play(ReplacementTransform(check, check2))
        self.wait(1)

        # Scale down to 2, 2.5, 3
        tri3 = Triangle().scale(0.4).to_edge(RIGHT)
        tri3.shift(DOWN * 0.5)
        tri3.set_stroke(color=GREEN, width=3)
        self.play(Transform(tri1, tri3))
        self.wait(0.5)

        # Update labels
        label_a3 = MathTex(f"2").next_to(tri3.get_vertices()[0], DOWN)
        label_b3 = MathTex(f"2.5").next_to(tri3.get_vertices()[1], UP)
        label_c3 = MathTex(f"3").next_to(tri3.get_vertices()[2], UP)
        self.play(ReplacementTransform(label_a2, label_a3),
                  ReplacementTransform(label_b2, label_b3),
                  ReplacementTransform(label_c2, label_c3))
        self.wait(0.5)

        # Final check
        check3 = MathTex(r"2 \times 3 = 6 \leq 3 \times 2 = 6").scale(0.8)
        self.play(ReplacementTransform(check2, check3))
        self.wait(1)

        # Text: Scaling preserves mirth
        msg = Text("Scaling preserves mirth", font_size=24).to_edge(DOWN)
        self.play(Write(msg))
        self.wait(1)

        # Narration text
        narration = Text("Scaling does not change mirthfulness.", font_size=20)
        narration.to_corner(DL)
        self.play(Write(narration))
        self.wait(1.5)

        self.play(FadeOut(title, tri1, label_a3, label_b3, label_c3, check3, msg, narration))
        self.wait(0.5)
