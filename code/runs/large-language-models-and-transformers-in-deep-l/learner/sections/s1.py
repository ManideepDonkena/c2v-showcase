from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Attention Mechanism", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Sentence
        sentence = "The cat sat on the mat"
        words = [Text(w, font_size=24) for w in sentence.split()]
        words_group = VGroup(*words).arrange(RIGHT, buff=0.5).move_to(ORIGIN)
        self.play(Write(words_group))
        self.wait(1)

        # Highlight 'sat'
        sat_word = words[3]
        sat_word_copy = sat_word.copy().set_color(YELLOW)
        self.play(Transform(sat_word, sat_word_copy))
        self.wait(0.5)

        # Draw attention lines
        lines = []
        for i, word in enumerate(words):
            if i == 3: continue  # skip 'sat'
            line = Line(sat_word.get_center(), word.get_center(), color=WHITE, stroke_width=2)
            if i in [1, 5]:  # cat and mat
                line.set_color(GREEN).set_opacity(1.0)
            else:
                line.set_opacity(0.3)
            lines.append(line)

        self.play(*[Create(l) for l in lines])
        self.wait(1.5)

        # Weight matrix overlay
        matrix = [[0 for _ in range(len(words))] for _ in range(len(words))]
        matrix[3][1] = 0.8
        matrix[3][5] = 0.7
        matrix[3][0] = 0.2
        matrix[3][2] = 0.1
        matrix[3][4] = 0.3

        matrix_tex = MathTex(
            "\\begin{bmatrix}",
            "0 & 0.8 & 0.2 & 0.1 & 0.3 & 0 \\\\",
            "0 & 0 & 0 & 0 & 0 & 0 \\\\",
            "0 & 0 & 0 & 0 & 0 & 0 \\\\",
            "0 & 0 & 0 & 0 & 0 & 0 \\\\",
            "0 & 0 & 0 & 0 & 0 & 0 \\\\",
            "0 & 0.7 & 0.3 & 0.1 & 0.2 & 0 \\\\",
            "\\end{bmatrix}",
            font_size=24
        ).move_to(UP * 1.5)

        self.play(Write(matrix_tex))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(words_group), FadeOut(sat_word), *[FadeOut(l) for l in lines], FadeOut(matrix_tex))

        # RNN vs Transformer comparison
        rnn_text = Text("RNN: Sequential processing", font_size=24).to_edge(UP)
        trans_text = Text("Transformer: Self-Attention", font_size=24).to_edge(UP)

        rnn_text.shift(0.0 * RIGHT + 0.48 * UP)  # layout: separation vector
        self.play(Write(rnn_text))
        self.wait(0.5)

        # RNN chain
        rnn_words = [Text(w, font_size=20) for w in "The cat sat on the mat".split()]
        rnn_group = VGroup(*rnn_words).arrange(RIGHT, buff=0.3).move_to(DOWN * 1)
        self.play(Write(rnn_group))
        self.wait(0.5)

        # Arrows
        arrows = []
        for i in range(len(rnn_words) - 1):
            arrow = Arrow(rnn_words[i].get_right(), rnn_words[i+1].get_left(), buff=0.1, color=BLUE)
            arrows.append(arrow)
        self.play(*[Create(a) for a in arrows])
        self.wait(1)

        # Replace with Transformer
        self.play(Transform(rnn_text, trans_text))
        self.wait(0.5)

        # Transformer connections
        self.play(FadeOut(rnn_group), *[FadeOut(a) for a in arrows])

        # New sentence
        sentence2 = "The cat sat on the mat"
        words2 = [Text(w, font_size=24) for w in sentence2.split()]
        words2_group = VGroup(*words2).arrange(RIGHT, buff=0.5).move_to(ORIGIN)
        self.play(Write(words2_group))
        self.wait(0.5)

        # Swap words
        words3 = [Text(w, font_size=24) for w in "Sat cat on the mat".split()]
        words3_group = VGroup(*words3).arrange(RIGHT, buff=0.5).move_to(DOWN * 1)
        self.play(Write(words3_group))
        self.wait(0.5)

        # Color-coded wave pattern
        wave1 = always_redraw(lambda: 
            VGroup(
                *[Line(words2[i].get_left(), words2[i].get_right(), color=RED, stroke_width=2).shift(DOWN * 0.3) for i in range(len(words2))]
            )
        )

        wave2 = always_redraw(lambda:
            VGroup(
                *[Line(words3[i].get_left(), words3[i].get_right(), color=BLUE, stroke_width=2).shift(DOWN * 0.3) for i in range(len(words3))]
            )
        )

        self.play(Write(wave1), Write(wave2))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(words2_group), FadeOut(words3_group), FadeOut(wave1), FadeOut(wave2))

        # Dot product example
        q = Vector([1, 1], color=GREEN)
        k = Vector([1, -1], color=RED)
        q_label = MathTex("Q", font_size=24).next_to(q.get_end(), UP)
        k_label = MathTex("K", font_size=24).next_to(k.get_end(), DOWN)

        self.play(Create(q), Create(k), Write(q_label), Write(k_label))
        self.wait(0.5)

        # Show calculation
        calc = MathTex("1 \\cdot 1 + 1 \\cdot (-1) = 0", font_size=30).to_edge(DOWN)
        self.play(Write(calc))
        self.wait(1.5)

        # Fade out
        self.play(FadeOut(q), FadeOut(k), FadeOut(q_label), FadeOut(k_label), FadeOut(calc))

        # Final text
        final_text = Text("Self-Attention: Quadratic complexity", font_size=24).to_edge(UP)
        self.play(Write(final_text))
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(final_text))
