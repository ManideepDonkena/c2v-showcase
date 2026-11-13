from manim import *

class S4(Scene):
    def construct(self):
        # Title
        title = Text("The Double Step Identity", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        # Setup grid and axes
        axes = Axes(x_range=[-7, 7], y_range=[-4, 4])
        axes_labels = axes.get_axis_labels()
        axes_labels.shift(0.0 * RIGHT + -0.52 * UP)  # layout: separation vector
        self.play(Create(axes), Write(axes_labels))
        self.wait(0.5)

        # Initial point A at (x, y)
        x, y = 2, 1
        A = Dot(axes.c2p(x, y), color=BLUE)
        label_A = MathTex(f"({x}, {y})").next_to(A, DOWN, buff=0.2)
        self.play(FadeIn(A), Write(label_A))
        self.wait(0.5)

        # Step 1: Krell step from A to intermediate point
        step1_arrow = Arrow(axes.c2p(x, y), axes.c2p(y, x + 1), buff=0.1, color=YELLOW)
        label_step1 = MathTex("Step\ 1").next_to(step1_arrow, UP, buff=0.2)
        self.play(GrowArrow(step1_arrow), Write(label_step1))
        self.wait(0.5)

        # Intermediate point B1 at (y, x+1)
        B1 = Dot(axes.c2p(y, x + 1), color=GREEN)
        label_B1 = MathTex(f"({y}, {x+1})").next_to(B1, DOWN, buff=0.2)
        label_B1.shift(-0.6 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(FadeIn(B1), Write(label_B1))
        self.wait(0.5)

        # Step 2: Krell step from B1 to final point
        step2_arrow = Arrow(axes.c2p(y, x + 1), axes.c2p(x + 1, y), buff=0.1, color=YELLOW)
        label_step2 = MathTex("Step\ 2").next_to(step2_arrow, UP, buff=0.2)
        self.play(GrowArrow(step2_arrow), Write(label_step2))
        self.wait(0.5)

        # Final point B at (x+1, y)
        B = Dot(axes.c2p(x + 1, y), color=RED)
        label_B = MathTex(f"({x+1}, {y})").next_to(B, DOWN, buff=0.2)
        self.play(FadeIn(B), Write(label_B))
        self.wait(0.5)

        # Apply Krell step again to (x+1, y) → (y, x+2)
        step3_arrow = Arrow(axes.c2p(x + 1, y), axes.c2p(y, x + 2), buff=0.1, color=YELLOW)
        label_step3 = MathTex("Step\ 3").next_to(step3_arrow, UP, buff=0.2)
        self.play(GrowArrow(step3_arrow), Write(label_step3))
        self.wait(0.5)

        # Final point C at (y, x+2)
        C = Dot(axes.c2p(y, x + 2), color=PURPLE)
        label_C = MathTex(f"({y}, {x+2})").next_to(C, DOWN, buff=0.2)
        self.play(FadeIn(C), Write(label_C))
        self.wait(0.5)

        # Show dashed arrow from A to (x+1, y+1) — net result
        dashed_arrow = DashedLine(axes.c2p(x, y), axes.c2p(x + 1, y + 1), color=ORANGE)
        label_net = MathTex("(x+1, y+1)").next_to(dashed_arrow, UR, buff=0.2)
        self.play(Create(dashed_arrow), Write(label_net))
        self.wait(0.5)

        # Show that (x+1, y) + 1 to second coord gives (x+1, y+1)
        calc_label = MathTex("Apply\ Krell\ step\ again:").to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(calc_label))
        self.wait(0.5)

        # Show intermediate point (y, x+1) → swap and add 1 to second
        calc1 = MathTex("(y, x+1)", "\\rightarrow", "(x+1, y)", "\\rightarrow", "(x+1, y+1)").scale(0.8)
        calc1.next_to(calc_label, DOWN, buff=0.3)
        self.play(Write(calc1))
        self.wait(1)

        # Show total steps: 2 + 2 + 1 = 5
        total_steps = MathTex("Total\ Steps:", "2", "+", "2", "+", "1", "=", "5").to_edge(DOWN).shift(DOWN * 0.5)
        self.play(Write(total_steps))
        self.wait(1)

        # Fade out everything except title and final result
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(axes_labels),
            FadeOut(A),
            FadeOut(label_A),
            FadeOut(step1_arrow),
            FadeOut(label_step1),
            FadeOut(B1),
            FadeOut(label_B1),
            FadeOut(step2_arrow),
            FadeOut(label_step2),
            FadeOut(B),
            FadeOut(label_B),
            FadeOut(step3_arrow),
            FadeOut(label_step3),
            FadeOut(C),
            FadeOut(label_C),
            FadeOut(dashed_arrow),
            FadeOut(label_net),
            FadeOut(calc_label),
            FadeOut(calc1),
            FadeOut(total_steps)
        )
        self.wait(0.5)
