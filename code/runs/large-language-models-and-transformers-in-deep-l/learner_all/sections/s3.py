from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("The Decoder Stack & Probability", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Decoder stack
        decoder_block = Rectangle(height=1, width=2, color=BLUE, fill_opacity=0.3).shift(LEFT * 2)
        decoder_text = Text("Decoder Block", font_size=24).move_to(decoder_block.get_center())
        decoder_text.shift(0.0 * RIGHT + 0.78 * UP)  # layout: separation vector
        self.play(Create(decoder_block), Write(decoder_text))
        self.wait(0.5)

        # Stack of blocks
        stack = VGroup(*[decoder_block.copy() for _ in range(3)]).arrange(DOWN, buff=0.2)
        stack.shift(LEFT * 2)
        decoder_text.shift(0.0 * RIGHT + 1.2 * UP)  # layout: separation vector
        self.play(Transform(decoder_block, stack))
        self.wait(0.5)

        # Dense layer
        dense_layer = Rectangle(height=1, width=2, color=GREEN, fill_opacity=0.3).shift(RIGHT * 2)
        dense_text = Text("Dense Layer", font_size=24).move_to(dense_layer.get_center())
        self.play(Create(dense_layer), Write(dense_text))
        self.wait(0.5)

        # Bar chart
        bars = VGroup(*[Rectangle(height=0.5, width=0.3, color=YELLOW) for _ in range(5)])
        bars.arrange(RIGHT, buff=0.1).shift(DOWN * 1)
        bar_labels = [Text("there", font_size=20), Text("cat", font_size=20), Text("sat", font_size=20),
                      Text("the", font_size=20), Text("is", font_size=20)]
        for i, label in enumerate(bar_labels):
            label.next_to(bars[i], DOWN, buff=0.1)
        self.play(Create(bars), Write(VGroup(*bar_labels)))
        self.wait(0.5)

        # Highlight tallest bar
        self.play(bars[0].animate.set_fill(RED, opacity=0.8))
        self.wait(0.5)

        # Text overlay
        text1 = Text("Processed info flows into probability distribution", font_size=24).to_edge(DOWN)
        self.play(Write(text1))
        self.wait(1)

        # RNN vs Transformer comparison
        rnn = Rectangle(height=1, width=3, color=RED, fill_opacity=0.3).shift(LEFT * 4)
        rnn_text = Text("RNN", font_size=24).move_to(rnn.get_center())
        trans = Rectangle(height=1, width=3, color=BLUE, fill_opacity=0.3).shift(RIGHT * 4)
        trans_text = Text("Transformer", font_size=24).move_to(trans.get_center())

        self.play(Create(rnn), Write(rnn_text))
        self.wait(0.5)
        self.play(Create(trans), Write(trans_text))
        self.wait(0.5)
        # Attention weights
        words1 = VGroup(Text("Cat"), Text("sat")).arrange(RIGHT, buff=0.5).shift(UP * 1)
        words2 = VGroup(Text("Sat"), Text("cat")).arrange(RIGHT, buff=0.5).shift(DOWN * 1)
        self.play(Write(words1), Write(words2))
        self.wait(0.5)

        # Attention weights
        attention_weights = VGroup(
            Line(words1[0].get_right(), words1[1].get_left(), color=BLUE),
            Line(words1[1].get_left(), words1[0].get_right(), color=BLUE)
        )
        self.play(Create(attention_weights))
        self.wait(0.5)

        # Color-coded wave pattern
        wave1 = always_redraw(lambda: DashedLine(
            start=words1[0].get_center() + UP * 0.2,
            end=words1[0].get_center() + DOWN * 0.2,
            color=RED
        ))
        wave2 = always_redraw(lambda: DashedLine(
            start=words2[0].get_center() + UP * 0.2,
            end=words2[0].get_center() + DOWN * 0.2,
            color=GREEN
        ))
        self.play(Write(wave1), Write(wave2))
        self.wait(1)

        # Dot product demo
        q = Arrow(start=ORIGIN, end=[1, 1, 0], color=YELLOW)
        k = Arrow(start=ORIGIN, end=[1, -1, 0], color=PURPLE)
        q_label = Text("Q", font_size=24).next_to(q.get_end(), UP)
        k_label = Text("K", font_size=24).next_to(k.get_end(), DOWN)

        self.play(Create(q), Create(k), Write(q_label), Write(k_label))
        self.wait(0.5)

        result = MathTex("1 \\cdot 1 + 1 \\cdot -1 = 0", font_size=30)
        result.to_edge(DOWN)
        self.play(Write(result))
        self.wait(1)

        # Single block diagram
        block = Rectangle(height=2, width=4, color=BLUE, fill_opacity=0.3).shift(UP * 1)
        attn = Text("Multi-Head\nAttention", font_size=20).move_to(block.get_center())
        self.play(Create(block), Write(attn))
        self.wait(0.5)

        ff = Rectangle(height=1, width=2, color=GREEN, fill_opacity=0.3).next_to(block, DOWN)
        ff_label = Text("Feed-Forward", font_size=20).move_to(ff.get_center())
        self.play(Create(ff), Write(ff_label))
        self.wait(0.5)

        # Add and normalize
        add_arrow = Arrow(start=block.get_bottom(), end=ff.get_top(), color=WHITE)
        norm = Text("Add & Norm", font_size=20).next_to(add_arrow, RIGHT)
        self.play(Create(add_arrow), Write(norm))
        self.wait(0.5)

        # Decoder-only vs Encoder-Decoder
        dec_only = Rectangle(height=1.5, width=3, color=BLUE, fill_opacity=0.3).shift(LEFT * 4)
        dec_text = Text("Decoder Only", font_size=20).move_to(dec_only.get_center())
        enc_dec = Rectangle(height=1.5, width=3, color=GREEN, fill_opacity=0.3).shift(RIGHT * 4)
        enc_text = Text("Encoder-Decoder", font_size=20).move_to(enc_dec.get_center())

        self.play(Create(dec_only), Write(dec_text))
        self.wait(0.5)
        self.play(Create(enc_dec), Write(enc_text))
        self.wait(0.5)

        # Cross attention
        cross_attn = Line(enc_dec.get_right(), dec_only.get_left(), color=RED)
        self.play(Create(cross_attn))
        self.wait(0.5)

        # Triangular mask
        matrix = VGroup(*[VGroup(*[Square(side_length=0.3) for _ in range(4)]) for _ in range(4)])
        matrix.arrange_in_grid(rows=4, cols=4, buff=0.1).shift(DOWN * 1)
        self.play(Create(matrix))
        self.wait(0.5)

        # Mask upper triangle
        mask = Rectangle(width=1.2, height=1.2, color=RED, fill_opacity=0.5).shift(matrix[0][1].get_center())
        self.play(FadeIn(mask))
        self.wait(0.5)

        # Normalization
        norm_before = Text("Without Norm", font_size=24).to_edge(UP)
        norm_after = Text("With Layer Norm", font_size=24).to_edge(UP)
        self.play(Write(norm_before))
        self.wait(1)
        self.play(Transform(norm_before, norm_after))
        self.wait(1)

        # Final text
        final_text = Text("Decoder stack generates probability distribution over vocabulary", font_size=24).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, decoder_block, dense_layer, bars, bar_labels,
                                 rnn, trans, words1, words2, attention_weights, wave1, wave2,
                                 q, k, q_label, k_label, result, block, attn, ff, ff_label,
                                 add_arrow, norm, dec_only, dec_text, enc_dec, enc_text,
                                 cross_attn, matrix, mask, norm_before, final_text)))
