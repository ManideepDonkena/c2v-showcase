from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Singularity and Collapse", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial parallelogram
        basis_i = Arrow(start=ORIGIN, end=[1, 0, 0], color=BLUE)
        basis_j = Arrow(start=ORIGIN, end=[0, 1, 0], color=GREEN)
        parallelogram = Polygon(ORIGIN, [1, 0, 0], [1, 1, 0], [0, 1, 0], fill_opacity=0.5, color=RED)
        self.play(Create(basis_i), Create(basis_j), FadeIn(parallelogram))
        self.wait(1)

        # Squash the parallelogram
        self.play(
            basis_i.animate.put_start_and_end_on(ORIGIN, [1, 0, 0]),
            basis_j.animate.put_start_and_end_on(ORIGIN, [1, 0, 0]),
            parallelogram.animate.become(Polygon(ORIGIN, [1, 0, 0], [2, 0, 0], [1, 0, 0]).set_fill(RED, opacity=0.5)),
            run_time=2
        )
        self.wait(1)

        # Show determinant = 0
        det_text = MathTex(r"\det(A) = 0", font_size=36)
        det_text.to_edge(DOWN)
        self.play(Write(det_text))
        self.wait(1.5)

        # Show basis vectors becoming collinear
        self.play(
            basis_i.animate.put_start_and_end_on(ORIGIN, [1, 0, 0]),
            basis_j.animate.put_start_and_end_on(ORIGIN, [1, 0, 0]),
            run_time=1.5
        )
        self.wait(1)

        # Show two identical vectors
        self.play(FadeOut(basis_i), FadeOut(basis_j), FadeOut(parallelogram))
        self.wait(0.5)
        
        basis_v1 = Arrow(start=ORIGIN, end=[1, 0, 0], color=BLUE)
        basis_v2 = Arrow(start=ORIGIN, end=[1, 0, 0], color=GREEN)
        self.play(Create(basis_v1), Create(basis_v2))
        self.wait(1)

        # Show no area enclosed
        no_area = Text("No Area Enclosed", font_size=24).next_to(basis_v1, DOWN)
        self.play(Write(no_area))
        self.wait(1.5)
        self.play(FadeOut(no_area))

        # Show lines representing solutions
        self.play(FadeOut(basis_v1), FadeOut(basis_v2))
        self.wait(0.5)

        line1 = Line([-3, 1, 0], [3, 1, 0], color=BLUE)
        line2 = Line([-3, 2, 0], [3, 2, 0], color=GREEN)
        self.play(Create(line1), Create(line2))
        self.wait(1)

        no_solution = Text("No Solution", font_size=24).next_to(line1, DOWN)
        self.play(Write(no_solution))
        self.wait(1.5)
        self.play(FadeOut(no_solution))

        # Show same line (infinite solutions)
        self.play(FadeOut(line1), FadeOut(line2))
        self.wait(0.5)

        line3 = Line([-3, 1, 0], [3, 1, 0], color=BLUE)
        self.play(Create(line3))
        self.wait(1)

        inf_solutions = Text("Infinite Solutions", font_size=24).next_to(line3, DOWN)
        self.play(Write(inf_solutions))
        self.wait(1.5)
        self.play(FadeOut(inf_solutions))

        # Final summary
        self.play(FadeOut(title), FadeOut(det_text), FadeOut(line3))
        self.wait(0.5)

        summary = Text("A zero determinant means the transformation collapses space.", font_size=24)
        summary.to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)
        self.play(FadeOut(summary))
