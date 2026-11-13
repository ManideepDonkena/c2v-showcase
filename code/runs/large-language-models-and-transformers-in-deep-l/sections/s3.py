from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Decoder Stack & Probability", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Stack of decoder blocks
        decoder_blocks = VGroup(*[Rectangle(width=2, height=1, color=BLUE, fill_opacity=0.5).add(Text(f"Block {i+1}", font_size=16)) for i in range(4)])
        decoder_blocks.arrange(DOWN, buff=0.2)
        decoder_blocks.center()
        self.play(Create(decoder_blocks))
        self.wait(1)

        # Merged vectors
        merged_vector = Rectangle(width=3, height=1, color=YELLOW, fill_opacity=0.5)
        merged_vector_label = Text("Merged Vectors", font_size=24)
        merged_vector_label.next_to(merged_vector, UP)
        merged_vector_label.shift(0.0 * RIGHT + 0.5 * UP)  # layout: separation vector
        self.play(FadeIn(merged_vector), Write(merged_vector_label))
        self.wait(0.5)

        # Arrows from merged vectors to decoder stack
        arrow1 = Arrow(merged_vector.get_top(), decoder_blocks[0].get_bottom(), buff=0.2)
        self.play(GrowArrow(arrow1))
        self.wait(1)

        # Arrows between decoder blocks
        arrows = VGroup()
        for i in range(3):
            arrow = Arrow(decoder_blocks[i].get_bottom(), decoder_blocks[i+1].get_top(), buff=0.2)
            arrows.add(arrow)
        self.play(*[GrowArrow(a) for a in arrows])
        self.wait(1)

        # Output from last decoder block
        output_rect = Rectangle(width=3, height=1, color=GREEN, fill_opacity=0.5)
        output_rect.next_to(decoder_blocks[-1], DOWN, buff=0.5)
        output_label = Text("Output", font_size=24)
        output_label.next_to(output_rect, UP)
        self.play(FadeIn(output_rect), Write(output_label))
        self.wait(0.5)

        # Arrow to dense layer
        arrow2 = Arrow(output_rect.get_top(), output_rect.get_top() + UP*1.5, buff=0.2)
        self.play(GrowArrow(arrow2))
        self.wait(0.5)

        # Dense layer
        dense_layer = Rectangle(width=3, height=1, color=ORANGE, fill_opacity=0.5)
        dense_layer.next_to(output_rect.get_top() + UP*1.5, DOWN, buff=0.2)
        dense_label = Text("Dense Layer", font_size=24)
        dense_label.next_to(dense_layer, UP)
        self.play(FadeIn(dense_layer), Write(dense_label))
        self.wait(1)

        # Arrow to bar chart
        arrow3 = Arrow(dense_layer.get_bottom(), dense_layer.get_bottom() + DOWN*1.5, buff=0.2)
        self.play(GrowArrow(arrow3))
        self.wait(0.5)

        # Bar chart
        bars = VGroup()
        bar_heights = [0.8, 1.2, 0.6, 2.0, 1.0, 0.4, 1.5]
        max_height = max(bar_heights)
        for i, h in enumerate(bar_heights):
            bar = Rectangle(width=0.4, height=h*2, color=PURPLE, fill_opacity=0.7)
            bar.next_to(dense_layer.get_bottom() + DOWN*1.5, LEFT, buff=0.3)
            bar.shift(RIGHT * (i - len(bar_heights)/2 + 0.5) * 0.6)
            bars.add(bar)

        self.play(FadeIn(bars))
        self.wait(1)

        # Labels for bars
        labels = VGroup()
        words = ["the", "and", "to", "there", "of", "a", "in"]
        for i, word in enumerate(words):
            label = Text(word, font_size=20)
            label.next_to(bars[i], DOWN, buff=0.2)
            labels.add(label)

        self.play(Write(labels))
        self.wait(1)

        # Highlight tallest bar
        highlight = SurroundingRectangle(bars[3], color=RED, buff=0.1)
        self.play(Create(highlight))
        self.wait(1)

        # Key text
        key_text = Text("Next predicted word: 'there'", font_size=24)
        key_text.to_edge(DOWN)
        self.play(Write(key_text))
        self.wait(2)

        # Fade out everything except title and key text
        self.play(
            FadeOut(decoder_blocks),
            FadeOut(merged_vector), FadeOut(merged_vector_label),
            FadeOut(output_rect), FadeOut(output_label),
            FadeOut(dense_layer), FadeOut(dense_label),
            FadeOut(bars), FadeOut(labels),
            FadeOut(arrow1), FadeOut(arrow2), FadeOut(arrow3),
            FadeOut(highlight)
        )
        self.wait(1)

        # Final key text
        final_text = Text("The model calculates likelihood of every word", font_size=24)
        final_text.to_edge(DOWN)
        self.play(Transform(key_text, final_text))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(key_text))
        self.wait(0.5)
