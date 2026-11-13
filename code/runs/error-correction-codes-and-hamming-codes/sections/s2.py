from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Solution: Parity Bits", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Positions array
        positions = [1, 2, 3, 4, 5, 6]
        pos_labels = [Text(str(p), font_size=24) for p in positions]
        for i, label in enumerate(pos_labels):
            label.next_to(ORIGIN, DOWN, buff=0.5).shift(RIGHT * (i - 2.5))
        self.play(*[Write(label) for label in pos_labels])
        self.wait(0.5)

        # Bit slots
        slots = [Rectangle(width=0.8, height=1.2, fill_opacity=0.2, color=BLUE) for _ in range(6)]
        for i, slot in enumerate(slots):
            slot.next_to(pos_labels[i], UP, buff=0.3)
        self.play(*[DrawBorderThenFill(slot) for slot in slots])
        self.wait(0.5)

        # Bit labels
        bit_labels = [Text("P1", font_size=24), Text("D1", font_size=24), Text("P2", font_size=24),
                      Text("D2", font_size=24), Text("P4", font_size=24), Text("D3", font_size=24)]
        for i, label in enumerate(bit_labels):
            label.next_to(slots[i], UP, buff=0.1)
        self.play(*[Write(label) for label in bit_labels])
        self.wait(0.5)

        # Show parity coverage
        p1_cover = [slots[0], slots[1], slots[3], slots[5]]
        p2_cover = [slots[2], slots[3], slots[5]]
        p4_cover = [slots[4], slots[5]]

        # Highlight P1 coverage
        p1_highlight = VGroup(*p1_cover).set_color(GREEN)
        self.play(ShowCreation(p1_highlight), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(p1_highlight))

        # Highlight P2 coverage
        p2_highlight = VGroup(*p2_cover).set_color(GREEN)
        self.play(ShowCreation(p2_highlight), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(p2_highlight))

        # Highlight P4 coverage
        p4_highlight = VGroup(*p4_cover).set_color(GREEN)
        self.play(ShowCreation(p4_highlight), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(p4_highlight))
        self.wait(0.5)

        # Final text
        final_text = Text("Parity bits detect and correct errors", font_size=24)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(1)

        self.play(FadeOut(title, *pos_labels, *slots, *bit_labels, final_text))
