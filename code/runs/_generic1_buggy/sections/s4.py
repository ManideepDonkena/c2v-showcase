from manim import *

class S4(Scene):
    def construct(self):
        # Fade out previous shapes
        self.play(FadeOut(VGroup(*self.mobjects)))
        
        # Create the formula text
        formula = MathTex("a^2 + b^2 = c^2", font_size=60)
        
        # Create pulse animations for variables
        a_pulse = formula[0][0].animate.scale(1.2).set_color(YELLOW)
        b_pulse = formula[0][1].animate.scale(1.2).set_color(GREEN)
        c_pulse = formula[0][2].animate.scale(1.2).set_color(RED)
        
        # Create title text
        title = Text("The Formula Revealed", font_size=36)
        title.to_edge(UP)
        
        # Show title
        self.play(Write(title))
        self.wait(0.5)
        
        # Show formula
        self.play(Write(formula))
        self.wait(1)
        
        # Pulse variables
        self.play(a_pulse, run_time=0.3)
        self.play(a_pulse.copy().scale(1/1.2).set_color(WHITE), run_time=0.3)
        self.play(b_pulse, run_time=0.3)
        self.play(b_pulse.copy().scale(1/1.2).set_color(WHITE), run_time=0.3)
        self.play(c_pulse, run_time=0.3)
        self.play(c_pulse.copy().scale(1/1.2).set_color(WHITE), run_time=0.3)
        
        # Show narration text
        narration1 = Text("This relationship is called", font_size=24).to_edge(DOWN)
        narration2 = Text("the Pythagoras Theorem.", font_size=24).next_to(narration1, DOWN)
        self.play(Write(narration1))
        self.wait(0.5)
        narration2.shift(0.0 * RIGHT + 0.23 * UP)  # layout: separation vector
        self.play(Write(narration2))
        self.wait(1)
        
        # Clear narration
        self.play(FadeOut(VGroup(narration1, narration2)))
        
        # Show next part of narration
        narration3 = Text("It states that the square", font_size=24).to_edge(DOWN)
        narration4 = Text("of the hypotenuse is equal", font_size=24).next_to(narration3, DOWN)
        narration3.shift(0.0 * RIGHT + 0.48 * UP)  # layout: separation vector
        self.play(Write(narration3))
        self.wait(0.5)
        narration4.shift(0.0 * RIGHT + 0.72 * UP)  # layout: separation vector
        self.play(Write(narration4))
        self.wait(1)
        
        # Clear narration
        self.play(FadeOut(VGroup(narration3, narration4)))
        
        # Show final narration
        narration5 = Text("So, simply put: a squared plus", font_size=24).to_edge(DOWN)
        narration6 = Text("b squared equals c squared.", font_size=24).next_to(narration5, DOWN)
        self.play(Write(narration5))
        self.wait(0.5)
        self.play(Write(narration6))
        self.wait(1)
        
        # Clear final narration
        self.play(FadeOut(VGroup(narration5, narration6)))
        
        # Keep formula on screen
        self.wait(2)
