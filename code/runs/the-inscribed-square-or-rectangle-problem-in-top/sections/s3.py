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
        self.wait(0.5)

        # Animation of shrinking and rotating
        target_square = Square(side_length=2, color=RED, fill_opacity=0.3)
        target_square.move_to(ORIGIN)
        
        # Shrink and rotate animation
        anim1 = rect.animate.scale(0.5).rotate(PI/6)
        anim2 = rect.animate.scale(0.8).rotate(-PI/4)
        anim3 = rect.animate.scale(0.7).rotate(PI/3)
        anim4 = rect.animate.scale(0.9).rotate(-PI/6)
        
        self.play(anim1, run_time=1)
        self.wait(0.5)
        self.play(anim2, run_time=1)
        self.wait(0.5)
        self.play(anim3, run_time=1)
        self.wait(0.5)
        self.play(anim4, run_time=1)
        self.wait(0.5)

        # Show that it gets stuck
        stuck_rect = Rectangle(width=2, height=1, color=YELLOW, fill_opacity=0.3)
        stuck_rect.rotate(PI/8)
        stuck_rect.move_to(ORIGIN)
        
        self.play(Transform(rect, stuck_rect), run_time=0.5)
        self.wait(0.5)

        # Show multiple failed attempts
        for i in range(3):
            self.play(rect.animate.rotate(PI/4), run_time=0.5)
            self.wait(0.25)
        
        # Problem text
        problem_text = Text("Inscribed Square Problem?", font_size=36, color=YELLOW)
        problem_text.to_edge(UP)
        problem_text.shift(0.0 * RIGHT + -0.48 * UP)  # layout: separation vector
        self.play(Write(problem_text))
        self.wait(1)

        # Additional explanation text
        explanation = Text("While rectangles are guaranteed, squares are not so easily found.", font_size=24)
        explanation.next_to(problem_text, DOWN, buff=0.3)
        self.play(Write(explanation))
        self.wait(1.5)
        
        # Fade out
        self.play(FadeOut(rect), FadeOut(problem_text), FadeOut(explanation), run_time=0.5)
        self.wait(0.5)
