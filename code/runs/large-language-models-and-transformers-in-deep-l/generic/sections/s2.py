from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Multi-Head Attention Layers", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Input vector
        input_vector = Rectangle(width=1.5, height=1, color=BLUE, fill_opacity=0.3)
        input_vector.shift(2 * LEFT + 0.5 * UP)
        input_text = Text("Input", font_size=24).next_to(input_vector, DOWN)
        
        self.play(Create(input_vector), Write(input_text))
        self.wait(1)

        # Split into heads
        head1 = Rectangle(width=1.5, height=1, color=RED, fill_opacity=0.3)
        head1.shift(1.5 * LEFT + 2 * DOWN)
        head1_label = Text("Head 1", font_size=24).next_to(head1, DOWN)
        
        head2 = Rectangle(width=1.5, height=1, color=GREEN, fill_opacity=0.3)
        head2.shift(0.5 * LEFT + 2 * DOWN)
        head2_label = Text("Head 2", font_size=24).next_to(head2, DOWN)
        
        head3 = Rectangle(width=1.5, height=1, color=YELLOW, fill_opacity=0.3)
        head3.shift(0.5 * RIGHT + 2 * DOWN)
        head3_label = Text("Head 3", font_size=24).next_to(head3, DOWN)
        
        head4 = Rectangle(width=1.5, height=1, color=PURPLE, fill_opacity=0.3)
        head4.shift(1.5 * RIGHT + 2 * DOWN)
        head4_label = Text("Head 4", font_size=24).next_to(head4, DOWN)

        # Arrows from input to heads
        arrow1 = Arrow(input_vector.get_bottom(), head1.get_top(), buff=0.1)
        arrow2 = Arrow(input_vector.get_bottom(), head2.get_top(), buff=0.1)
        arrow3 = Arrow(input_vector.get_bottom(), head3.get_top(), buff=0.1)
        arrow4 = Arrow(input_vector.get_bottom(), head4.get_top(), buff=0.1)

        arrow1.shift(0.54 * RIGHT + 0.0 * UP)  # layout: separation vector
        arrow2.shift(0.5 * RIGHT + 0.0 * UP)  # layout: separation vector
        arrow3.shift(0.49 * RIGHT + 0.0 * UP)  # layout: separation vector
        self.play(
            Create(arrow1), Create(arrow2), Create(arrow3), Create(arrow4),
            Create(head1), Create(head2), Create(head3), Create(head4),
            Write(head1_label), Write(head2_label), Write(head3_label), Write(head4_label)
        )
        self.wait(1.5)

        # Head 1 highlights subject-verb
        highlight1 = Rectangle(width=1.5, height=1, color=RED, fill_opacity=0.6)
        highlight1.shift(1.5 * LEFT + 2 * DOWN)
        sv_text = Text("Subject-Verb", font_size=20).next_to(highlight1, UP)
        
        self.play(
            FadeOut(head1), 
            FadeOut(head1_label),
            Create(highlight1),
            Write(sv_text)
        )
        self.wait(1.5)

        # Head 2 highlights adjective-noun
        highlight2 = Rectangle(width=1.5, height=1, color=GREEN, fill_opacity=0.6)
        highlight2.shift(0.5 * LEFT + 2 * DOWN)
        an_text = Text("Adjective-Noun", font_size=20).next_to(highlight2, UP)
        
        self.play(
            FadeOut(head2),
            FadeOut(head2_label),
            Create(highlight2),
            Write(an_text)
        )
        self.wait(1.5)

        # Merge back
        output_vector = Rectangle(width=1.5, height=1, color=BLUE, fill_opacity=0.3)
        output_vector.shift(2 * RIGHT + 0.5 * UP)
        output_text = Text("Output", font_size=24).next_to(output_vector, DOWN)

        arrow_merge1 = Arrow(highlight1.get_top(), output_vector.get_bottom(), buff=0.1)
        arrow_merge2 = Arrow(highlight2.get_top(), output_vector.get_bottom(), buff=0.1)
        arrow_merge3 = Arrow(head3.get_top(), output_vector.get_bottom(), buff=0.1)
        arrow_merge4 = Arrow(head4.get_top(), output_vector.get_bottom(), buff=0.1)

        self.play(
            FadeOut(highlight1), FadeOut(sv_text),
            FadeOut(highlight2), FadeOut(an_text),
            Create(arrow_merge1), Create(arrow_merge2), 
            Create(arrow_merge3), Create(arrow_merge4),
            Create(output_vector), Write(output_text)
        )
        self.wait(2)

        # Narration text
        narration = Text("To capture diverse linguistic patterns, transformers use multiple 'attention heads' in parallel.", font_size=24)
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2.5)

        # Second part of narration
        narration2 = Text("Each head learns to focus on different aspects of the data, such as grammar or syntax.", font_size=24)
        narration2.to_edge(DOWN)
        self.play(Transform(narration, narration2))
        self.wait(3)

        # Clean up
        self.play(
            FadeOut(title),
            FadeOut(input_vector), FadeOut(input_text),
            FadeOut(output_vector), FadeOut(output_text),
            FadeOut(narration)
        )
        self.wait(0.5)
