from manim import *

class S3(Scene):
    def construct(self):
        # Title
        title = Text("Detecting the Error", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Original codeword
        codeword = "0101"
        cw_text = Text(f"Transmitted: {codeword}", font_size=24)
        cw_text.next_to(title, DOWN, buff=0.5)
        self.play(Write(cw_text))
        self.wait(0.5)

        # Show error
        error_pos = 2
        codeword_text = cw_text.get_part_by_text(codeword)
        row = codeword_text.get_rows()[0]
        error_center = row[error_pos].get_center()
        
        error_indication = always_redraw(lambda: 
            Rectangle(width=0.8, height=1.2, color=RED, fill_opacity=0.3)
            .move_to(error_center)
        )
        self.play(Create(error_indication))
        self.wait(0.5)

        # Show syndrome calculation
        self.play(FadeOut(error_indication))

        # Parity checks
        parity_checks = [
            MathTex("p_1 = d_1 \\oplus d_2 \\oplus d_3 = 0 \\oplus 1 \\oplus 0 = 1"),
            MathTex("p_2 = d_1 \\oplus d_2 \\oplus d_4 = 0 \\oplus 1 \\oplus 1 = 0"),
            MathTex("p_3 = d_2 \\oplus d_3 \\oplus d_4 = 1 \\oplus 0 \\oplus 1 = 0")
        ]
        
        for i, check in enumerate(parity_checks):
            check.to_edge(DOWN).shift(UP * (i - 1))
            self.play(Write(check))
            self.wait(0.5)
            
        # Syndrome result
        syndrome = MathTex("S = 100")
        syndrome.next_to(parity_checks[-1], UP, buff=0.5)
        self.play(Write(syndrome))
        self.wait(0.5)

        # Show binary to decimal conversion
        conv_text = Text("Binary 100 = Decimal 4", font_size=24)
        conv_text.next_to(syndrome, DOWN, buff=0.5)
        self.play(Write(conv_text))
        self.wait(0.5)

        # Show correct position (error at index 2)
        self.play(FadeOut(conv_text))
        self.wait(0.5)
        
        # Highlight error position
        highlight = always_redraw(lambda: 
            Rectangle(width=0.8, height=1.2, color=YELLOW, fill_opacity=0.3)
            .move_to(error_center)
        )
        self.play(Create(highlight))
        self.wait(0.5)

        # Final explanation
        explanation = Text("Syndrome points to error position", font_size=24)
        explanation.next_to(highlight, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(1.5)

        # Clean up
        self.play(
            FadeOut(title),
            FadeOut(cw_text),
            FadeOut(parity_checks[0]),
            FadeOut(parity_checks[1]),
            FadeOut(parity_checks[2]),
            FadeOut(syndrome),
            FadeOut(highlight),
            FadeOut(explanation)
        )
