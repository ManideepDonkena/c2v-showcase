from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Definition and Formula", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Main formula: a ⊕ b
        a_op_b = MathTex("a \\oplus b").scale(2)
        self.play(Write(a_op_b))
        self.wait(1)

        # Arrow down to equation
        arrow = Arrow(start=DOWN, end=UP).next_to(a_op_b, DOWN)
        eq = MathTex("a + b + (a \\times b)").next_to(arrow, DOWN)
        self.play(GrowArrow(arrow), Write(eq))
        self.wait(1.5)

        # Show 0 ⊕ b
        zero_eq = MathTex("0 \\oplus b").scale(1.5).to_edge(LEFT).shift(DOWN * 1.5)
        self.play(Write(zero_eq))
        self.wait(0.5)

        expanded = MathTex("= 0 + b + (0 \\times b)").next_to(zero_eq, DOWN)
        expanded.shift(0.66 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(expanded))
        self.wait(1)

        simplify = MathTex("= b + 0 = b").next_to(expanded, DOWN)
        self.play(Write(simplify))
        self.wait(1.5)

        # Explanation for zero
        zero_text = Text("Adding zero contributes nothing", font_size=24).next_to(simplify, DOWN)
        zero_text.shift(0.78 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(Write(zero_text))
        self.wait(1.5)
        self.play(FadeOut(zero_text))

        # Show nested structure: a ⊕ (b ⊕ c)
        nested = MathTex("a \\oplus (b \\oplus c)").to_edge(RIGHT).shift(UP * 1.5)
        self.play(Write(nested))
        self.wait(0.5)

        # Highlight inner parentheses
        inner_highlight = SurroundingRectangle(MathTex("b \\oplus c"), color=YELLOW, buff=0.1)
        inner_highlight.shift(0.0 * RIGHT + 0.83 * UP)  # layout: separation vector
        self.play(Create(inner_highlight))
        self.wait(1)

        # Calculate b ⊕ c first (e.g., 3 ⊕ 4 = 19)
        calc1 = MathTex("3 \\oplus 4 = 3 + 4 + 12 = 19").next_to(nested, DOWN)
        self.play(Write(calc1))
        self.wait(1.5)

        # Now outer operation: a ⊕ 19
        outer = MathTex("2 \\oplus 19 = 2 + 19 + 38 = 60").next_to(calc1, DOWN)
        self.play(Write(outer))
        self.wait(1.5)

        # Comparison with standard multiplication
        comp_title = Text("Comparison with Standard Multiplication", font_size=24).to_edge(UP).shift(DOWN * 3)
        self.play(Write(comp_title))
        self.wait(0.5)

        comp = MathTex("2 \\oplus 3 = 11, \\quad 2 \\times 3 = 6").next_to(comp_title, DOWN)
        self.play(Write(comp))
        self.wait(1.5)

        # Chain with -1
        chain = VGroup(
            Circle().scale(0.4).set_color(BLUE).move_to(LEFT * 2),
            Text("4", font_size=24).move_to(LEFT * 2),
            Circle().scale(0.4).set_color(GREEN).move_to(ORIGIN),
            Text("-1", font_size=24).move_to(ORIGIN),
            Circle().scale(0.4).set_color(RED).move_to(RIGHT * 2),
            Text("2", font_size=24).move_to(RIGHT * 2)
        ).arrange(RIGHT, buff=0.5)

        self.play(FadeIn(chain))
        self.wait(1)

        # Show that -1 swallows everything
        step1 = MathTex("(4 \\oplus -1) = -1").next_to(chain, DOWN)
        self.play(Write(step1))
        self.wait(1.5)

        step2 = MathTex("(-1 \\oplus 2) = -1").next_to(step1, DOWN)
        self.play(Write(step2))
        self.wait(1.5)

        # Final explanation
        final_text = Text("The -1 element swallows all", font_size=24).next_to(step2, DOWN)
        self.play(Write(final_text))
        self.wait(1.5)

        # Cleanup
        self.play(FadeOut(title), FadeOut(a_op_b), FadeOut(arrow), FadeOut(eq),
                  FadeOut(zero_eq), FadeOut(expanded), FadeOut(simplify),
                  FadeOut(nested), FadeOut(inner_highlight), FadeOut(calc1),
                  FadeOut(outer), FadeOut(comp_title), FadeOut(comp),
                  FadeOut(chain), FadeOut(step1), FadeOut(step2), FadeOut(final_text))
