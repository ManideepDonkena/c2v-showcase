from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Inscribed Square Problem: A Topological Journey", font_size=24)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Initial rectangle
        rect = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.3)
        rect.move_to(ORIGIN)
        self.play(Create(rect))
        self.wait(1)

        # Text: "While rectangles are guaranteed, squares are not so easily found."
        text1 = Text("While rectangles are guaranteed, squares are not so easily found.", font_size=24)
        text1.to_edge(DOWN)
        self.play(Write(text1))
        self.wait(2)

        # Shrink and rotate animation
        target_rect = Rectangle(width=2.5, height=2.5, color=RED, fill_opacity=0.3)
        target_rect.move_to(ORIGIN)
        
        self.play(
            rect.animate.scale(0.625).rotate(PI/6),
            run_time=1.5
        )
        self.wait(0.5)

        # Try different orientations
        for i in range(3):
            self.play(
                rect.animate.rotate(PI/4),
                run_time=0.8
            )
            self.wait(0.3)
        
        # Show failure cases
        self.play(
            rect.animate.rotate(PI/12).scale(1.2),
            run_time=1
        )
        self.wait(1)

        # Clear text and show problem statement
        self.play(FadeOut(text1))
        self.wait(0.5)
        
        # Text: "Inscribed Square Problem?"
        problem_text = Text("Inscribed Square Problem?", font_size=36, color=YELLOW)
        problem_text.to_edge(UP)
        problem_text.shift(0.0 * RIGHT + -0.48 * UP)  # layout: separation vector
        self.play(Write(problem_text))
        self.wait(1)

        # Show ellipse example (for context)
        ellipse = Ellipse(width=4, height=2.5, color=GREEN, fill_opacity=0.3)
        ellipse.move_to(ORIGIN)
        self.play(
            FadeOut(rect),
            Create(ellipse),
            run_time=1
        )
        self.wait(1)

        # Text: "For specific shapes like ellipses, squares exist..."
        text2 = Text("For specific shapes like ellipses, squares exist,", font_size=24)
        text2.to_edge(DOWN)
        self.play(Write(text2))
        self.wait(1.5)

        # Text: "...but proving their existence for any arbitrary simple closed curve remains a famous open problem in mathematics."
        text3 = Text("but proving their existence for *any* arbitrary simple closed curve", font_size=24)
        text3.next_to(text2, DOWN, buff=0.2)
        text3.shift(0.0 * RIGHT + 0.19 * UP)  # layout: separation vector
        self.play(Write(text3))
        self.wait(1.5)

        text4 = Text("remains a famous open problem in mathematics.", font_size=24)
        text4.next_to(text3, DOWN, buff=0.2)
        self.play(Write(text4))
        self.wait(2)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(problem_text),
            FadeOut(ellipse),
            FadeOut(text2),
            FadeOut(text3),
            FadeOut(text4),
            run_time=1
        )
        self.wait(0.5)
