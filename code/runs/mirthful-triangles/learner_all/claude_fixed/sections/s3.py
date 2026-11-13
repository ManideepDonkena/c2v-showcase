from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Scaling Invariance", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        def side_label(tex, tri, i, j):
            v = tri.get_vertices()
            mid = (v[i] + v[j]) / 2
            cen = np.mean(v, axis=0)
            d = mid - cen
            d = d / np.linalg.norm(d)
            return MathTex(tex).next_to(mid, d, buff=0.15)

        # Initial triangle: sides 4, 5, 6
        a, b, c = 4, 5, 6
        longest = c
        shortest = a
        ratio = longest / shortest

        # Draw initial triangle
        tri1 = Triangle().scale(0.8).move_to(LEFT * 4 + DOWN * 0.3)
        tri1.set_stroke(color=GREEN, width=3)
        self.play(Create(tri1))
        self.wait(0.5)

        # Label sides
        label_a = side_label(f"{a}", tri1, 1, 2)
        label_b = side_label(f"{b}", tri1, 0, 1)
        label_c = side_label(f"{c}", tri1, 2, 0)
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(0.5)

        # Check mirthfulness
        check = MathTex(r"2 \times 6 = 12 \leq 3 \times 4 = 12").scale(0.8)
        check.move_to(UP * 2.2)
        self.play(Write(check))
        self.wait(1)

        # Scale up to 8, 10, 12
        tri2 = Triangle().scale(1.6).move_to(RIGHT * 3.5 + DOWN * 0.3)
        tri2.set_stroke(color=GREEN, width=3)
        self.play(Transform(tri1, tri2))
        self.wait(0.5)

        # Update labels
        label_a2 = side_label("8", tri2, 1, 2)
        label_b2 = side_label("10", tri2, 0, 1)
        label_c2 = side_label("12", tri2, 2, 0)
        self.play(ReplacementTransform(label_a, label_a2),
                  ReplacementTransform(label_b, label_b2),
                  ReplacementTransform(label_c, label_c2))
        self.wait(0.5)

        # Check mirthfulness again
        check2 = MathTex(r"2 \times 12 = 24 \leq 3 \times 8 = 24").scale(0.8)
        check2.move_to(UP * 2.2)
        self.play(ReplacementTransform(check, check2))
        self.wait(1)

        # Scale down to 2, 2.5, 3
        tri3 = Triangle().scale(0.4).move_to(RIGHT * 3.5 + DOWN * 0.3)
        tri3.set_stroke(color=GREEN, width=3)
        self.play(Transform(tri1, tri3))
        self.wait(0.5)

        # Update labels
        label_a3 = side_label("2", tri3, 1, 2)
        label_b3 = side_label("2.5", tri3, 0, 1)
        label_c3 = side_label("3", tri3, 2, 0)
        self.play(ReplacementTransform(label_a2, label_a3),
                  ReplacementTransform(label_b2, label_b3),
                  ReplacementTransform(label_c2, label_c3))
        self.wait(0.5)

        # Final check
        check3 = MathTex(r"2 \times 3 = 6 \leq 3 \times 2 = 6").scale(0.8)
        check3.move_to(UP * 2.2)
        self.play(ReplacementTransform(check2, check3))
        self.wait(1)

        # Text: Scaling preserves mirth
        msg = Text("Scaling preserves mirth", font_size=24).to_edge(DOWN)
        self.play(Write(msg))
        self.wait(1)

        # Narration text
        narration = Text("Scaling does not change mirthfulness.", font_size=20)
        narration.next_to(msg, UP, buff=0.3)
        self.play(Write(narration))
        self.wait(1.5)

        self.play(FadeOut(title, tri1, label_a3, label_b3, label_c3, check3, msg, narration))
        self.wait(0.5)
