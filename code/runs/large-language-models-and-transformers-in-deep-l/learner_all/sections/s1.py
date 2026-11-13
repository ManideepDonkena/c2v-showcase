from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Attention Mechanism", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Sentence
        sentence = Text("The cat sat on the mat", font_size=24).move_to(ORIGIN)
        self.play(Write(sentence))
        self.wait(1)

        # Highlight 'sat'
        sat_word = sentence[4]
        sat_word.set_color(YELLOW)
        self.play(sat_word.animate.set_color(WHITE))
        self.wait(0.5)

        # Glowing lines to 'cat' and 'mat'
        cat_word = sentence[1]
        mat_word = sentence[8]
        line1 = Line(cat_word.get_center(), sat_word.get_center(), color=GREEN, stroke_width=3)
        line2 = Line(mat_word.get_center(), sat_word.get_center(), color=GREEN, stroke_width=3)
        line3 = Line(sentence[0].get_center(), sat_word.get_center(), color=GRAY, stroke_width=1)
        line4 = Line(sentence[3].get_center(), sat_word.get_center(), color=GRAY, stroke_width=1)
        line5 = Line(sentence[6].get_center(), sat_word.get_center(), color=GRAY, stroke_width=1)

        line1.shift(0.0 * RIGHT + -0.28 * UP)  # layout: separation vector
        line2.shift(0.0 * RIGHT + -0.26 * UP)  # layout: separation vector
        self.play(Create(line1), Create(line2))
        self.play(FadeOut(line3), FadeOut(line4), FadeOut(line5))
        self.wait(1.5)

        # Weight matrix
        weight_matrix = Matrix([[0, 0.8, 0, 0, 0],
                                [0.8, 0, 0.7, 0, 0],
                                [0, 0.7, 0, 0.9, 0.6],
                                [0, 0, 0.9, 0, 0.5],
                                [0, 0, 0.6, 0.5, 0]],
                               element_to_mobject=DecimalNumber,
                               h_buff=1.2,
                               v_buff=1.2).move_to(3*RIGHT + 1.5*DOWN)
        weight_matrix.shift(0.0 * RIGHT + -1.6 * UP)  # layout: separation vector
        self.play(Write(weight_matrix))
        self.wait(1)

        # RNN vs Transformer
        rnn = Text("RNN", font_size=24).to_edge(LEFT, buff=1)
        transformer = Text("Transformer", font_size=24).to_edge(RIGHT, buff=1)
        self.play(Write(rnn), Write(transformer))
        self.wait(0.5)

        # Arrows
        arrow1 = Arrow(start=rnn.get_right(), end=transformer.get_left(), color=BLUE)
        self.play(GrowArrow(arrow1))
        self.wait(1)

        # Swapped sentences
        sentence1 = Text("Cat sat", font_size=24).move_to(3*LEFT + 2*UP)
        sentence2 = Text("Sat cat", font_size=24).move_to(3*LEFT + 0.5*UP)
        self.play(Write(sentence1), Write(sentence2))
        self.wait(1)

        # Wave patterns
        wave1 = always_redraw(lambda: VGroup(
            *[Line(start=(i, 1.5, 0), end=(i, 2.5, 0), color=RED) for i in range(-3, 4)]
        ).move_to(sentence1))
        wave2 = always_redraw(lambda: VGroup(
            *[Line(start=(i, -1.5, 0), end=(i, -2.5, 0), color=BLUE) for i in range(-3, 4)]
        ).move_to(sentence1))
        self.play(Create(wave1), Create(wave2))
        self.wait(1.5)
        # Dot product
        q = Vector([1, 1], color=RED)
        k = Vector([1, -1], color=BLUE)
        q_label = MathTex("Q", font_size=24).next_to(q.get_end(), UP)
        k_label = MathTex("K", font_size=24).next_to(k.get_end(), DOWN)
        self.play(Create(q), Create(k), Write(q_label), Write(k_label))
        self.wait(0.5)

        dot_result = MathTex("1 \\cdot 1 + 1 \\cdot (-1) = 0", font_size=30).to_edge(DOWN)
        self.play(Write(dot_result))
        self.wait(1.5)

        # Transformer block
        block = Rectangle(width=4, height=2, color=GREEN, fill_opacity=0.2).move_to(3*RIGHT + 1.5*DOWN)
        attn_label = Text("Multi-Head Attention", font_size=20).next_to(block, UP)
        ff_label = Text("Feed Forward Network", font_size=20).next_to(block, DOWN)
        self.play(Create(block), Write(attn_label), Write(ff_label))
        self.wait(1)

        # Decoder-only vs Encoder-Decoder
        decoder_only = Rectangle(width=3, height=2, color=ORANGE, fill_opacity=0.2).move_to(4*LEFT + 1.5*DOWN)
        encoder_decoder = Rectangle(width=3, height=2, color=PURPLE, fill_opacity=0.2).move_to(4*RIGHT + 1.5*DOWN)
        self.play(Create(decoder_only), Create(encoder_decoder))
        self.wait(0.5)

        # Labels
        d_label = Text("Decoder-only", font_size=20).next_to(decoder_only, UP)
        e_label = Text("Encoder-Decoder", font_size=20).next_to(encoder_decoder, UP)
        self.play(Write(d_label), Write(e_label))
        self.wait(1.5)

        # Cross attention
        cross_attn = Arrow(start=encoder_decoder.get_left(), end=decoder_only.get_right(), color=YELLOW)
        self.play(GrowArrow(cross_attn))
        self.wait(1)

        # Triangular mask
        matrix_mask = Matrix([[0, 0, 0, 0, 0],
                              [1, 0, 0, 0, 0],
                              [1, 1, 0, 0, 0],
                              [1, 1, 1, 0, 0],
                              [1, 1, 1, 1, 0]],
                             element_to_mobject=DecimalNumber,
                             h_buff=1.2,
                             v_buff=1.2).move_to(3*RIGHT + 1.5*DOWN)
        self.play(Transform(weight_matrix, matrix_mask))
        self.wait(1.5)

        # Normalization
        norm_label = Text("Layer Normalization", font_size=24).to_edge(DOWN)
        self.play(Write(norm_label))
        self.wait(1)

        # Fade out everything
        self.play(FadeOut(title), FadeOut(sentence), FadeOut(line1), FadeOut(line2),
                  FadeOut(weight_matrix), FadeOut(rnn), FadeOut(transformer), FadeOut(arrow1),
                  FadeOut(sentence1), FadeOut(sentence2), FadeOut(wave1), FadeOut(wave2),
                  FadeOut(q), FadeOut(k), FadeOut(q_label), FadeOut(k_label), FadeOut(dot_result),
                  FadeOut(block), FadeOut(attn_label), FadeOut(ff_label),
                  FadeOut(decoder_only), FadeOut(encoder_decoder), FadeOut(d_label), FadeOut(e_label),
                  FadeOut(cross_attn), FadeOut(norm_label))
        self.wait(0.5)
