from manim import *

class S1(Scene):
    def construct(self):
        # Title
        title = Text("The Attention Mechanism", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Sentence
        sentence = "The cat sat on the mat"
        words = [Text(word, font_size=24) for word in sentence.split()]
        words_group = VGroup(*words).arrange(RIGHT, buff=0.5).move_to(ORIGIN)
        self.play(Write(words_group))
        self.wait(0.5)

        # Highlight 'sat'
        sat_word = words[2]
        sat_word_copy = sat_word.copy()
        self.play(sat_word.animate.set_fill(YELLOW, opacity=0.8), run_time=0.3)
        self.wait(0.5)

        # Connections from 'sat' to other words
        connections = []
        for i, word in enumerate(words):
            if i == 2: continue  # skip 'sat'
            line = Line(sat_word.get_center(), word.get_center(), color=BLUE, stroke_width=2)
            connections.append(line)
            self.play(Write(line), run_time=0.3)

        # Fade out lines to non-related words
        self.play(
            FadeOut(connections[0]),  # 'The'
            FadeOut(connections[2]),  # 'on'
            FadeOut(connections[3]),  # 'the'
            run_time=0.5
        )
        self.wait(0.5)

        # Highlight strong connections to 'cat' and 'mat'
        cat_word = words[1]
        mat_word = words[5]
        line_cat = Line(sat_word.get_center(), cat_word.get_center(), color=GREEN, stroke_width=4)
        line_mat = Line(sat_word.get_center(), mat_word.get_center(), color=GREEN, stroke_width=4)
        self.play(Write(line_cat), Write(line_mat), run_time=0.5)
        self.wait(1)

        # Weight matrix
        matrix_data = [
            [0, 0.8, 0.2, 0, 0, 0],
            [0.7, 0, 0.3, 0, 0, 0],
            [0.1, 0.9, 0, 0.2, 0, 0.8],
            [0, 0, 0.1, 0, 0.9, 0.1],
            [0, 0, 0, 0.3, 0, 0.7],
            [0, 0, 0.2, 0, 0.8, 0]
        ]
        matrix = Matrix(matrix_data, v_buff=0.4, h_buff=0.6).scale(0.6)
        matrix.to_corner(DOWN + LEFT)
        matrix_title = Text("Attention Weights", font_size=24).next_to(matrix, UP)
        self.play(Write(matrix_title), Write(matrix), run_time=1)
        self.wait(1)

        # Show key point
        key_point = Text("Self-attention calculates focus between words", font_size=24).to_edge(DOWN)
        self.play(Write(key_point))
        self.wait(1.5)

        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(words_group),
            FadeOut(sat_word_copy),
            FadeOut(line_cat),
            FadeOut(line_mat),
            FadeOut(matrix),
            FadeOut(matrix_title),
            FadeOut(key_point),
            run_time=0.5
        )
