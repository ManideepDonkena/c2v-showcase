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
        mirthful_condition = 2 * longest <= 3 * shortest

        # Draw initial triangle
        tri = Triangle().scale(0.8).shift(LEFT * 2)
        tri.set_color(GREEN)
        tri_label = MathTex(f"\\text{{Sides: }} {a}, {b}, {c}").next_to(tri, DOWN)
        self.play(Create(tri), Write(tri_label))
        self.wait(1)

        # Show mirthfulness check
        condition_text = MathTex(
            f"2 \\times {longest} = {2*longest} \\leq 3 \\times {shortest} = {3*shortest}"
        ).next_to(tri, DOWN, buff=1.5)
        self.play(Write(condition_text))
        self.wait(1)

        # Scaling up to 8, 10, 12
        tri_up = Triangle().scale(1.6).shift(LEFT * 2)
        tri_up.set_color(GREEN)
        tri_up_label = MathTex(f"\\text{{Sides: }} 8, 10, 12").next_to(tri_up, DOWN)
        self.play(Transform(tri, tri_up), Transform(tri_label, tri_up_label))
        self.wait(1)

        # Show new ratio
        long_new = 12
        short_new = 8
        ratio_new = long_new / short_new
        condition_text_new = MathTex(
            f"2 \\times {long_new} = {2*long_new} \\leq 3 \\times {short_new} = {3*short_new}"
        ).next_to(tri_up, DOWN, buff=1.5)
        self.play(Write(condition_text_new))
        self.wait(1)

        # Scaling down to 2, 2.5, 3
        tri_down = Triangle().scale(0.4).shift(LEFT * 2)
        tri_down.set_color(GREEN)
        tri_down_label = MathTex(f"\\text{{Sides: }} 2, 2.5, 3").next_to(tri_down, DOWN)
        self.play(Transform(tri, tri_down), Transform(tri_label, tri_down_label))
        self.wait(1)

        # Show final ratio
        long_final = 3
        short_final = 2
        ratio_final = long_final / short_final
        condition_text_final = MathTex(
            f"2 \\times {long_final} = {2*long_final} \\leq 3 \\times {short_final} = {3*short_final}"
        ).next_to(tri_down, DOWN, buff=1.5)
        condition_text_final.shift(0.0 * RIGHT + 0.25 * UP)  # layout: separation vector
        self.play(Write(condition_text_final))
        self.wait(1)

        # Final statement
        statement = Text("Scaling preserves mirth", font_size=24).to_edge(DOWN)
        self.play(Write(statement))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(tri),
            FadeOut(tri_label),
            FadeOut(condition_text),
            FadeOut(condition_text_new),
            FadeOut(condition_text_final),
            FadeOut(statement),
            FadeOut(title)
        )
