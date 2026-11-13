from manim import *

class S2(Scene):
    def construct(self):
        # Title
        title = Text("The Solution: Parity Bits", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Grid positions (1 to 7)
        grid_positions = [1, 2, 3, 4, 5, 6, 7]
        grid_labels = [Integer(i) for i in grid_positions]
        grid_mobs = VGroup(*[grid_labels[i].scale(0.6).move_to(LEFT * 3 + UP * (3.5 - i * 0.5)) for i in range(len(grid_positions))])
        self.play(FadeIn(grid_mobs))
        self.wait(0.5)

        # Slots for bits
        slots = [Rectangle(width=0.8, height=0.8).move_to(LEFT * 3 + UP * (3.5 - i * 0.5)) for i in range(len(grid_positions))]
        slot_labels = [Text("P1" if i == 0 else "D1" if i == 1 else "P2" if i == 2 else "D2" if i == 3 else "P4" if i == 4 else "D3" if i == 5 else "X").scale(0.5).move_to(slots[i].get_center()) for i in range(len(slots))]
        self.play(*[Create(slot) for slot in slots], *[Write(label) for label in slot_labels])
        self.wait(1)

        # Highlight parity positions
        p1_slot = slots[0]
        p2_slot = slots[2]
        p4_slot = slots[4]
        self.play(
            p1_slot.animate.set_fill(GREEN, opacity=0.5),
            p2_slot.animate.set_fill(GREEN, opacity=0.5),
            p4_slot.animate.set_fill(GREEN, opacity=0.5)
        )
        self.wait(1)
        
        # Show parity bit coverage
        p1_cover = Text("Covers 1,3,5,7", font_size=24).next_to(p1_slot, DOWN, buff=0.2)
        p2_cover = Text("Covers 2,3,6,7", font_size=24).next_to(p2_slot, DOWN, buff=0.2)
        p4_cover = Text("Covers 4,5,6,7", font_size=24).next_to(p4_slot, DOWN, buff=0.2)

        self.play(Write(p1_cover))
        self.wait(0.5)
        self.play(Write(p2_cover))
        self.wait(0.5)
        self.play(Write(p4_cover))
        self.wait(1)

        # Fade out old text
        self.play(FadeOut(p1_cover, p2_cover, p4_cover))

        # Show comparison: simple parity vs Hamming
        simple = Text("Simple Parity", font_size=24).to_edge(LEFT).shift(DOWN * 2)
        hamming = Text("Hamming Code", font_size=24).to_edge(RIGHT).shift(DOWN * 2)

        self.play(Write(simple), Write(hamming))
        self.wait(0.5)

        # Show simple parity fail
        fail = Text("Detects odd errors only", font_size=20).next_to(simple, DOWN)
        self.play(Write(fail))
        self.wait(1)

        # Show Hamming code ability
        fix = Text("Finds and fixes single error", font_size=20).next_to(hamming, DOWN)
        self.play(Write(fix))
        self.wait(1.5)

        # Final summary
        summary = Text("3 parity bits for 4 data bits", font_size=24).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(1.5)

        self.play(FadeOut(title, grid_mobs, *slots, *slot_labels, simple, hamming, fail, fix, summary))
        self.wait(0.5)
