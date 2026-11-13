from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("Multi-Head Attention Layers", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Multi-head attention visualization
        head1 = Text("Head 1: Subject-Verb", font_size=24).shift(UP * 1.5)
        head2 = Text("Head 2: Adjective-Noun", font_size=24).shift(UP * 0.5)
        head3 = Text("Head 3: Object-Preposition", font_size=24).shift(DOWN * 0.5)
        head4 = Text("Head 4: Temporal Relations", font_size=24).shift(DOWN * 1.5)

        self.play(Write(head1), Write(head2), Write(head3), Write(head4))
        self.wait(1)

        # Merge back into one vector
        merged = Rectangle(width=2, height=1, color=BLUE, fill_opacity=0.3).shift(DOWN * 2)
        merged.shift(0.0 * RIGHT + -0.32 * UP)  # layout: separation vector
        self.play(FadeOut(head1, head2, head3, head4), Create(merged))
        self.wait(1)

        # RNN vs Transformer comparison
        rnn_text = Text("RNN: Sequential Processing", font_size=24).to_edge(UP).shift(DOWN * 2)
        trans_text = Text("Transformer: Self-Attention", font_size=24).to_edge(UP).shift(DOWN * 2)

        rnn_text.shift(0.0 * RIGHT + -0.32 * UP)  # layout: separation vector
        self.play(Write(rnn_text))
        self.wait(0.5)
        self.play(Transform(rnn_text, trans_text))
        self.wait(1)

        # Swap word order example
        sentence1 = Text("Cat sat", font_size=24).to_edge(LEFT).shift(DOWN * 3)
        sentence2 = Text("Sat cat", font_size=24).to_edge(RIGHT).shift(DOWN * 3)

        self.play(Write(sentence1), Write(sentence2))
        self.wait(0.5)

        # Color-coded wave patterns
        wave1 = always_redraw(lambda: DashedLine(start=LEFT * 2 + DOWN * 3, end=RIGHT * 2 + DOWN * 3, color=RED))
        wave2 = always_redraw(lambda: DashedLine(start=LEFT * 2 + DOWN * 3, end=RIGHT * 2 + DOWN * 3, color=BLUE))

        self.play(Create(wave1), Create(wave2))
        self.wait(1)

        # Dot product calculation
        q = Vector([1, 1], color=YELLOW)
        k = Vector([1, -1], color=GREEN)
        q_label = Text("Q", font_size=24).next_to(q.get_end(), UP)
        k_label = Text("K", font_size=24).next_to(k.get_end(), DOWN)

        self.play(Create(q), Create(k), Write(q_label), Write(k_label))
        self.wait(0.5)

        calc = MathTex("1 \\cdot 1 + 1 \\cdot (-1) = 0", font_size=30)
        calc.to_edge(DOWN)
        self.play(Write(calc))
        self.wait(1)

        # Transformer block diagram
        attn_layer = Rectangle(width=2, height=1, color=PURPLE, fill_opacity=0.3).shift(UP * 1)
        ff_layer = Rectangle(width=2, height=1, color=ORANGE, fill_opacity=0.3).next_to(attn_layer, DOWN)
        input_vec = Vector([0, 1], color=WHITE).shift(LEFT * 3 + UP * 1)
        output_vec = Vector([0, 1], color=WHITE).shift(RIGHT * 3 + DOWN * 1)

        self.play(Create(attn_layer), Create(ff_layer), Create(input_vec), Create(output_vec))
        self.wait(0.5)

        # Decoder-only vs Encoder-Decoder
        dec_only = Text("Decoder-only", font_size=24).to_edge(LEFT)
        enc_dec = Text("Encoder-Decoder", font_size=24).to_edge(RIGHT)

        self.play(Write(dec_only), Write(enc_dec))
        self.wait(1)

        # Encoder-only vs Decoder stack
        enc_only = Rectangle(width=2, height=1, color=RED, fill_opacity=0.3).shift(LEFT * 3 + DOWN * 1)
        dec_stack = Rectangle(width=2, height=1, color=BLUE, fill_opacity=0.3).shift(RIGHT * 3 + DOWN * 1)

        self.play(Create(enc_only), Create(dec_stack))
        self.wait(1)

        # Triangular mask
        matrix = Matrix([["1", "0", "0"], ["0", "1", "0"], ["0", "0", "1"]], v_buff=0.5, h_buff=0.5)
        matrix.to_edge(DOWN)
        self.play(Write(matrix))
        self.wait(1)

        # Layer normalization
        norm_text = Text("Layer Normalization", font_size=24).to_edge(UP).shift(DOWN * 3)
        self.play(Write(norm_text))
        self.wait(0.5)

        # Fade out everything
        self.play(FadeOut(title, rnn_text, sentence1, sentence2, wave1, wave2, q, k, q_label, k_label,
                          calc, attn_layer, ff_layer, input_vec, output_vec, dec_only, enc_dec,
                          enc_only, dec_stack, matrix, norm_text))
        self.wait(0.5)
