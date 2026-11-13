from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Duality via Linear Functionals", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Vector A
        A = Arrow(start=ORIGIN, end=[2, 1, 0], color=YELLOW)
        A_label = MathTex("\\vec{A}", font_size=24).next_to(A.get_end(), UR, buff=0.1)
        
        self.play(Create(A), Write(A_label))
        self.wait(0.5)

        # Grid of points
        grid = VGroup()
        for i in range(-6, 7):
            for j in range(-4, 5):
                dot = Dot([i, j, 0], color=WHITE, radius=0.03)
                grid.add(dot)
        grid.shift(0.0 * RIGHT + -0.18 * UP)  # layout: separation vector
        self.play(FadeIn(grid))
        self.wait(0.5)

        # Level sets (contours)
        level_lines = VGroup()
        for k in range(-4, 5):
            line = Line(
                start=[-7, k * 2 - 1, 0],
                end=[7, k * 2 - 1, 0],
                color=BLUE,
                stroke_width=1
            )
            level_lines.add(line)
        self.play(Create(level_lines))
        self.wait(0.5)

        # Show one test vector B
        B = Arrow(start=ORIGIN, end=[3, 1, 0], color=GREEN)
        B_label = MathTex("\\vec{B}", font_size=24).next_to(B.get_end(), UR, buff=0.1)
        
        self.play(Create(B), Write(B_label))
        self.wait(0.5)

        # Show dot product value
        dot_product_value = MathTex("\\vec{A} \\cdot \\vec{B} =", "3.5", font_size=32)
        dot_product_value.to_edge(DOWN)
        self.play(Write(dot_product_value))
        self.wait(1)

        # Move B along contour
        B_target = Arrow(start=ORIGIN, end=[1, 3, 0], color=GREEN)
        B_target_label = MathTex("\\vec{B}'", font_size=24).next_to(B_target.get_end(), UR, buff=0.1)
        
        self.play(Transform(B, B_target), Transform(B_label, B_target_label))
        self.wait(0.5)

        # Show same dot product
        new_dot_product = MathTex("\\vec{A} \\cdot \\vec{B}' =", "3.5", font_size=32)
        new_dot_product.to_edge(DOWN)
        self.play(Transform(dot_product_value, new_dot_product))
        self.wait(1)

        # Clear and show key message
        self.play(
            FadeOut(B),
            FadeOut(B_label),
            FadeOut(grid),
            FadeOut(level_lines),
            FadeOut(dot_product_value),
            FadeOut(A_label)
        )
        
        message = Text("Vector A defines a linear functional", font_size=24)
        message.to_edge(DOWN)
        self.play(Write(message))
        self.wait(1.5)

        # Show final key point
        final_text = Text("All vectors on same contour yield same dot product", font_size=24)
        final_text.next_to(message, UP, buff=0.2)
        self.play(Write(final_text))
        self.wait(2)

        self.play(
            FadeOut(title),
            FadeOut(message),
            FadeOut(final_text)
        )
        self.wait(0.5)
