from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("Pythagoras Theorem: Visual Proof", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Create right triangle
        a = 3
        b = 4
        c = np.sqrt(a**2 + b**2)
        
        # Triangle vertices
        A = np.array([-3, -2, 0])
        B = np.array([3, -2, 0])
        C = np.array([-3, 2, 0])
        
        # Triangle
        triangle = Polygon(A, B, C, color=WHITE)
        
        # Legs a and b (blue)
        leg_a = Line(A, C, color=BLUE)
        leg_b = Line(A, B, color=BLUE)
        
        # Hypotenuse c (red)
        hypotenuse = Line(B, C, color=RED)
        
        # Labels
        label_a = MathTex("a", font_size=30).next_to(leg_a, LEFT, buff=0.1)
        label_b = MathTex("b", font_size=30).next_to(leg_b, DOWN, buff=0.1)
        label_c = MathTex("c", font_size=30).next_to(hypotenuse, RIGHT, buff=0.1)
        
        # Right angle marker
        right_angle = Square(side_length=0.3, color=YELLOW, fill_opacity=1)
        right_angle.move_to(A)
        
        # Initial triangle setup
        self.play(Create(triangle), run_time=1)
        self.wait(0.5)
        
        # Show legs a and b
        self.play(Create(leg_a), Create(leg_b), run_time=1)
        self.wait(0.5)
        
        # Label legs
        self.play(Write(label_a), Write(label_b), run_time=1)
        self.wait(1)
        
        # Show hypotenuse
        self.play(Create(hypotenuse), run_time=1)
        self.wait(0.5)
        
        # Label hypotenuse
        self.play(Write(label_c), run_time=1)
        self.wait(1)
        
        # Show right angle marker
        self.play(FadeIn(right_angle), run_time=1)
        self.wait(1.5)
        
        # Narration text
        narration = Text("Every right-angled triangle has a special relationship between its three sides.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration), run_time=1)
        self.wait(2)
        
        # Clear narration
        self.play(FadeOut(narration))
        self.wait(0.5)
        
        # Explain legs and hypotenuse
        legs_text = Text("The two shorter sides touching the right angle are called legs.", font_size=24)
        legs_text.to_edge(DOWN)
        self.play(Write(legs_text), run_time=1)
        self.wait(2)
        
        # Clear legs text
        self.play(FadeOut(legs_text))
        self.wait(0.5)
        
        hypotenuse_text = Text("The longest side opposite the right angle is known as the hypotenuse.", font_size=24)
        hypotenuse_text.to_edge(DOWN)
        self.play(Write(hypotenuse_text), run_time=1)
        self.wait(2)
        
        # Clear hypotenuse text
        self.play(FadeOut(hypotenuse_text))
        self.wait(0.5)
        
        # Final wait
        self.wait(1)
