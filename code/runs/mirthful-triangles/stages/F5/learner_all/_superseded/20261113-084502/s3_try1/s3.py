from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Mirthful Triangles: A Manim Animation", font_size=30)
        title.to_edge(UP, buff=0.2)
        self.play(Write(title))
        self.wait(0.5)

        # Initial triangle
        a, b, c = 4, 5, 6
        longest = max(a, b, c)
        shortest = min(a, b, c)
        ratio = longest / shortest

        # Draw initial triangle
        triangle = Polygon(
            LEFT * 3, RIGHT * 3, UP * 2,
            color=GREEN, fill_opacity=0.5
        )
        triangle.shift(LEFT * 1.5 + DOWN * 0.5)
        self.play(Create(triangle))
        self.wait(0.5)

        # Label sides
        label_a = MathTex(f"a={a}").next_to(triangle.get_left(), LEFT, buff=0.2)
        label_b = MathTex(f"b={b}").next_to(triangle.get_bottom(), DOWN, buff=0.2)
        label_c = MathTex(f"c={c}").next_to(triangle.get_right(), RIGHT, buff=0.2)
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(1)

        # Check mirthfulness
        check_text = Text("Is mirthful?", font_size=24).next_to(triangle, DOWN, buff=0.5)
        check_text.shift(0.0 * RIGHT + -0.21 * UP)  # layout: separation vector
        self.play(Write(check_text))
        self.wait(1)

        # Mirthfulness condition: longest <= 1.5 * shortest
        cond = MathTex(r"2 \times \text{longest} \leq 3 \times \text{shortest}")
        cond.next_to(check_text, DOWN, buff=0.3)
        self.play(Write(cond))
        self.wait(1)
        # Compute ratio
        ratio_text = MathTex(f"\\frac{{\\text{{long}}}}{{\\text{{short}}}} = {ratio:.2f}").next_to(cond, DOWN, buff=0.3)
        self.play(Write(ratio_text))
        self.wait(1)

        # Scaling up: multiply by 2
        triangle.shift(0.54 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(triangle.animate.scale(2), run_time=1)
        self.wait(0.5)

        # Update labels
        label_a_up = MathTex(f"a={a*2}").next_to(triangle.get_left(), LEFT, buff=0.2)
        label_b_up = MathTex(f"b={b*2}").next_to(triangle.get_bottom(), DOWN, buff=0.2)
        label_c_up = MathTex(f"c={c*2}").next_to(triangle.get_right(), RIGHT, buff=0.2)
        label_b_up.shift(0.0 * RIGHT + 0.44 * UP)  # layout: separation vector
        label_b_up.shift(0.0 * RIGHT + -0.39 * UP)  # layout: separation vector
        self.play(ReplacementTransform(label_a, label_a_up),
                  ReplacementTransform(label_b, label_b_up),
                  ReplacementTransform(label_c, label_c_up))
        self.wait(1)

        # Show scaling preserves mirthfulness
        scale_text = Text("Scaling preserves mirth", font_size=24).next_to(triangle, DOWN, buff=0.5)
        self.play(ReplacementTransform(check_text, scale_text))
        self.wait(1)

        # Fade out old ratio and condition
        self.play(FadeOut(ratio_text), FadeOut(cond))
        self.wait(0.5)

        # Scale down: multiply by 0.5
        self.play(triangle.animate.scale(0.5), run_time=1)
        self.wait(0.5)

        # Update labels again
        label_a_down = MathTex(f"a={a*0.5}").next_to(triangle.get_left(), LEFT, buff=0.2)
        label_b_down = MathTex(f"b={b*0.5}").next_to(triangle.get_bottom(), DOWN, buff=0.2)
        label_c_down = MathTex(f"c={c*0.5}").next_to(triangle.get_right(), RIGHT, buff=0.2)
        self.play(ReplacementTransform(label_a_up, label_a_down),
                  ReplacementTransform(label_b_up, label_b_down),
                  ReplacementTransform(label_c_up, label_c_down))
        self.wait(1)

        # Final text
        final_text = Text("Scaling does not change mirthfulness", font_size=24).next_to(triangle, DOWN, buff=0.5)
        self.play(ReplacementTransform(scale_text, final_text))
        self.wait(2)

        # Clean up
        self.play(FadeOut(final_text), FadeOut(triangle), FadeOut(label_a_down), FadeOut(label_b_down),
                  FadeOut(label_c_down), FadeOut(title))
        self.wait(0.5)
