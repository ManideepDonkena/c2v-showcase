from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Commutativity and Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Left scene: 0 ⊕ b -> b
        left_eq = MathTex("0 \\oplus b", font_size=40).to_corner(UL)
        self.play(Write(left_eq))
        self.wait(1)

        expand = MathTex("= 0 + b + (0 \\times b)", font_size=40).next_to(left_eq, DOWN, buff=0.5)
        expand.shift(0.71 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(expand))
        self.wait(1.5)

        simplify = MathTex("= 0 + b + 0", font_size=40).next_to(expand, DOWN, buff=0.5)
        self.play(Transform(expand, simplify))
        self.wait(1.5)

        final = MathTex("= b", font_size=40).next_to(simplify, DOWN, buff=0.5)
        self.play(Transform(expand, final))
        self.wait(2)

        # Right scene: 0 ⊕ b -> b (visual fade)
        right_eq = MathTex("0 \\oplus b", font_size=40).to_corner(UR)
        self.play(Write(right_eq))
        self.wait(1)

        zero_fade = right_eq[0][0].animate.set_color(GRAY)
        self.play(zero_fade)
        self.wait(1.5)

        result = MathTex("b", font_size=40).next_to(right_eq, DOWN, buff=0.5)
        self.play(Write(result))
        self.wait(2)

        # Show commutativity
        comm_left = MathTex("3 \\oplus 5", font_size=40).to_corner(DL)
        self.play(Write(comm_left))
        self.wait(1)

        comm_right = MathTex("5 \\oplus 3", font_size=40).to_corner(DR)
        self.play(Write(comm_right))
        self.wait(1.5)

        # Show both equal to same value
        eq_result = MathTex("= 3 + 5 + (3 \\times 5) = 38", font_size=32).next_to(comm_left, DOWN, buff=0.5)
        eq_result.shift(0.82 * RIGHT + 0.48 * UP)  # layout: separation vector
        self.play(Write(eq_result))
        self.wait(1.5)

        # Associativity example
        assoc = MathTex("a \\oplus (b \\oplus c)", font_size=40).to_edge(UP)
        self.play(Transform(title, assoc))
        self.wait(1.5)

        # Highlight inner part first
        inner_part = MathTex("b \\oplus c", font_size=40).next_to(assoc, DOWN, buff=0.5)
        self.play(Write(inner_part))
        self.wait(1.5)

        calc_inner = MathTex("= 4 + 3 + (4 \\times 3) = 19", font_size=32).next_to(inner_part, DOWN, buff=0.5)
        self.play(Write(calc_inner))
        self.wait(1.5)

        outer_step = MathTex("a \\oplus 19", font_size=40).next_to(calc_inner, DOWN, buff=0.5)
        self.play(Write(outer_step))
        self.wait(1.5)

        final_assoc = MathTex("= 2 + 19 + (2 \\times 19) = 60", font_size=32).next_to(outer_step, DOWN, buff=0.5)
        self.play(Write(final_assoc))
        self.wait(2)

        # Comparison with standard multiplication
        comp_left = MathTex("2 \\oplus 3 = 11", font_size=40).to_corner(UL)
        self.play(Transform(comm_left, comp_left))
        self.wait(1.5)

        comp_right = MathTex("2 \\times 3 = 6", font_size=40).to_corner(UR)
        self.play(Write(comp_right))
        self.wait(2)

        # Swallowing effect with -1
        chain = VGroup(
            Circle().scale(0.5),
            Text("4", font_size=24).move_to(Circle().scale(0.5).get_center()),
            Circle().scale(0.5),
            Text("-1", font_size=24).move_to(Circle().scale(0.5).get_center()),
            Circle().scale(0.5),
            Text("2", font_size=24).move_to(Circle().scale(0.5).get_center())
        ).arrange(RIGHT, buff=0.3).to_edge(DOWN)

        self.play(Write(chain))
        self.wait(1.5)

        # Show first step: 4 ⊕ -1 = -1
        step1 = MathTex("4 \\oplus (-1) = -1", font_size=32).next_to(chain, UP, buff=0.5)
        self.play(Write(step1))
        self.wait(2)

        # Show second step: -1 ⊕ 2 = -1
        step2 = MathTex("(-1) \\oplus 2 = -1", font_size=32).next_to(step1, DOWN, buff=0.5)
        step2.shift(0.0 * RIGHT + 0.48 * UP)  # layout: separation vector to avoid overlap
        self.play(Write(step2))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(VGroup(title, left_eq, right_eq, expand, simplify, final, eq_result,
                                 assoc, inner_part, calc_inner, outer_step, final_assoc,
                                 comp_left, comp_right, step1, step2, chain)))
        self.wait(0.5)
