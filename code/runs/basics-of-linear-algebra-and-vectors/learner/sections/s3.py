from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Scalar Multiplication", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Initial vector V
        V = Vector([2, 1], color=BLACK)
        V_label = MathTex("\\vec{v}", font_size=24).next_to(V.get_end(), UR, buff=0.1)
        self.play(Create(V), Write(V_label))
        self.wait(1)

        # Slider
        k_value = ValueTracker(1)
        k_label = MathTex("k =", font_size=24)
        k_text = always_redraw(lambda: DecimalNumber(k_value.get_value(), font_size=24))
        k_group = VGroup(k_label, k_text).arrange(RIGHT, buff=0.2)
        k_group.to_edge(DOWN)
        k_group.shift(UP * 0.24)
        self.play(Write(k_group))
        self.wait(0.5)
        
        # Animation of scalar multiplication
        self.play(
            k_value.animate.set_value(2),
            run_time=2,
            rate_func=linear
        )
        self.wait(1)

        # Show vector stretching
        V2 = always_redraw(lambda: Vector([2*k_value.get_value(), k_value.get_value()], color=BLACK))
        V2_label = MathTex("\\vec{v}", font_size=24).next_to(V2.get_end(), UR, buff=0.1)
        self.play(ReplacementTransform(V, V2), ReplacementTransform(V_label, V2_label))
        self.wait(1)

        # Flip direction
        self.play(
            k_value.animate.set_value(-1),
            run_time=2,
            rate_func=linear
        )
        self.wait(1)

        # Show direction flip
        V3 = always_redraw(lambda: Vector([-2*k_value.get_value(), -k_value.get_value()], color=BLACK))
        V3_label = MathTex("\\vec{v}", font_size=24).next_to(V3.get_end(), DL, buff=0.1)
        self.play(ReplacementTransform(V2, V3), ReplacementTransform(V2_label, V3_label))
        self.wait(1)

        # Final explanation text
        explanation = Text("If k > 0: same direction", font_size=24)
        explanation.to_edge(DOWN)
        explanation.shift(UP * 0.5)  # Move up to avoid overlap
        self.play(Write(explanation))
        self.wait(1)

        self.play(
            k_value.animate.set_value(1),
            run_time=1,
            rate_func=linear
        )
        self.wait(0.5)

        # Change text to negative
        self.play(Transform(explanation, Text("If k < 0: opposite direction", font_size=24)))
        self.wait(1.5)

        # Clean up
        self.play(FadeOut(title), FadeOut(k_group), FadeOut(explanation))
        self.wait(0.5)
