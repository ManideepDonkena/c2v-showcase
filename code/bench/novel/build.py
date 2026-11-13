"""Invented-concept topics (NOVEL-12): concepts no model can know, so a student's prior is at chance and a gain can
only come from the video. TOFU's fictitious-entity idea (and CounterVQA's counterfactual grounding) applied to teaching
videos.

Each concept has a card (definition, rules, one worked example) that the generator and the DEV quiz writer see, and 8
TEST questions written here, by a model family the pipeline never uses (Claude), from the card only. No pipeline step
sees TEST. Numeric answers are computed by the functions below, so the key cannot be wrong; option order is shuffled
with a fixed seed and balanced over A-D.

    python bench/novel/build.py   ->  bench/novel/cards.json, bench/novel/questions.json
"""

from __future__ import annotations

import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent


def tovan(a, b):
    return a + b + a * b


def krell(p):
    x, y = p
    return (y, x + 1)


def vorn(n):
    v = [1, 3]
    while len(v) < n:
        v.append(v[-1] + 2 * v[-2])
    return v[n - 1]


def glint(n):
    d = n % 10
    return d != 0 and n % d == 0


def mirthful(a, b, c):
    s = sorted((a, b, c))
    return 2 * s[2] <= 3 * s[0]


def sorrel(w, h):
    """w x h lattice rectangle: interior points minus boundary points."""
    return (w - 1) * (h - 1) - 2 * (w + h)


def quill(p, q):
    return abs(p[0] - q[0]) + 2 * abs(p[1] - q[1])


def dapple(n):
    return (n // 10) % 10 > n % 10


def brisk(xs):
    out = [xs[i] + xs[-1 - i] for i in range(len(xs) // 2)]
    return out + ([xs[len(xs) // 2]] if len(xs) % 2 else [])


def orbit(word):
    return "".join({"X": "XYY", "Y": "YX"}[c] for c in word)


def vell(a, b, c, d):
    return a * d - b - c


def lumen(h, k):
    return (h + 2 * k) % 7


CARDS = {
    "Tovan sums": (
        "The tovan sum of two whole numbers a and b is written a ⊕ b and equals a + b + a×b. "
        "Rules: (1) order does not matter: a ⊕ b = b ⊕ a. (2) 0 is neutral: 0 ⊕ b = b. "
        "(3) -1 swallows everything: (-1) ⊕ b = -1. (4) A chain is worked left to right. "
        f"Worked example: 2 ⊕ 3 = 2 + 3 + 6 = {tovan(2, 3)}."
    ),
    "Krell steps on a grid": (
        "A krell step moves a grid point (x, y) to (y, x + 1): swap the two numbers, then add 1 to the new second one. "
        "Rules: (1) a krell step always lands on a grid point. (2) Repeating krell steps from (0, 0) climbs a staircase "
        "(0,0) → (0,1) → (1,1) → (1,2) → (2,2). (3) Two krell steps move (x, y) to (x + 1, y + 1). "
        f"Worked example: one krell step from (3, 5) gives {krell((3, 5))}."
    ),
    "Vorn sequences": (
        "The vorn sequence starts 1, 3 and each next term is the previous term plus twice the term before it: "
        "v(n) = v(n-1) + 2×v(n-2). Rules: (1) every term is odd. (2) Each term is about twice the one before. "
        f"Worked example: v(3) = 3 + 2×1 = {vorn(3)}, v(4) = 5 + 2×3 = {vorn(4)}."
    ),
    "Glint numbers": (
        "A whole number is glint when its last digit is not 0 and the number is divisible by its last digit. "
        "Rules: (1) every number ending in 1 is glint. (2) A number ending in 0 is never glint. (3) A number ending in 5 "
        "is always glint. Worked example: 24 is glint because 24 ÷ 4 = 6; 26 is not glint because 26 ÷ 6 is not whole."
    ),
    "Mirthful triangles": (
        "A triangle is mirthful when twice its longest side is at most three times its shortest side "
        "(longest ≤ 1.5 × shortest). Rules: (1) every equilateral triangle is mirthful. (2) Scaling a triangle does not "
        "change whether it is mirthful. (3) The middle side does not matter. "
        "Worked example: sides 4, 5, 6 are mirthful (2×6 = 12 ≤ 3×4 = 12); sides 3, 4, 5 are not (10 > 9)."
    ),
    "Sorrel counts of lattice rectangles": (
        "For a rectangle drawn on grid points, its sorrel count is the number of grid points strictly inside it minus the "
        "number of grid points on its edges. A w × h rectangle has (w-1)×(h-1) points inside and 2×(w+h) on its edges. "
        "Rules: (1) small rectangles have negative sorrel counts. (2) Swapping width and height keeps the count. "
        f"Worked example: a 3 × 3 square has 4 inside and 12 on the edges, sorrel count {sorrel(3, 3)}."
    ),
    "Quill distance": (
        "The quill distance between two grid points counts each horizontal unit as 1 and each vertical unit as 2: "
        "|x1 - x2| + 2×|y1 - y2|. Rules: (1) it is the same in both directions. (2) Moving up is twice as costly as "
        "moving sideways. (3) The points at quill distance 2 from a point are 2 sideways or 1 up or down from it. "
        f"Worked example: from (0, 0) to (3, 2) the quill distance is 3 + 4 = {quill((0, 0), (3, 2))}."
    ),
    "Dapple numbers": (
        "A whole number is dapple when its tens digit is greater than its units digit (a one-digit number has tens "
        "digit 0, so it is never dapple). Rules: (1) every multiple of 10 from 10 to 90 is dapple. (2) Reversing the "
        "two digits of a dapple number with different digits gives a number that is not dapple. "
        "Worked example: 52 is dapple (5 > 2); 25 is not (2 < 5); 44 is not (4 = 4)."
    ),
    "Brisk folds of a list": (
        "A brisk fold folds a list of numbers in half and adds the numbers that land on each other: first + last, "
        "second + second-to-last, and so on; in a list of odd length the middle number stays alone at the end. "
        "Rules: (1) a fold keeps the total. (2) A fold roughly halves the length. "
        f"Worked example: brisk fold of [1, 2, 3, 4] is {brisk([1, 2, 3, 4])}; of [1, 2, 3] it is {brisk([1, 2, 3])}."
    ),
    "Orbit words": (
        "An orbit word grows by rewriting every letter at once: each X becomes XYY and each Y becomes YX. "
        "Start from X. Rules: (1) every orbit word starts with X. (2) Each rewrite makes the word longer. "
        f"Worked example: X → {orbit('X')} → {orbit(orbit('X'))}."
    ),
    "Vells of 2×2 grids": (
        "The vell of a 2 × 2 grid of numbers [[a, b], [c, d]] is a×d minus b minus c. "
        "Rules: (1) only the top-left and bottom-right numbers are multiplied. (2) Swapping b and c keeps the vell. "
        f"Worked example: the vell of [[2, 1], [3, 4]] is 2×4 - 1 - 3 = {vell(2, 1, 3, 4)}."
    ),
    "Lumen clocks": (
        "A lumen clock has 7 marks, 0 to 6, around a circle. One lumen tick moves the hand forward by 2 marks, wrapping "
        "past 6 back to 0. Rules: (1) after 7 ticks the hand is back where it started. (2) The hand visits every mark "
        f"before it returns. Worked example: from mark 3, two ticks go 3 → 5 → {lumen(3, 2)}."
    ),
}


def q(question, right, wrong):
    return {"question": question, "right": str(right), "wrong": [str(w) for w in wrong]}


def tests():
    t = {}
    t["Tovan sums"] = [
        q("What is 1 ⊕ 4 (tovan sum)?", tovan(1, 4), [5, 4, 10]),
        q("What is 3 ⊕ 3?", tovan(3, 3), [6, 9, 12]),
        q("Which number is neutral for the tovan sum (n ⊕ b = b for every b)?", 0, [1, -1, 2]),
        q("What is (-1) ⊕ 9?", -1, [8, -9, 9]),
        q("What is 2 ⊕ 2 ⊕ 2, worked left to right?", tovan(tovan(2, 2), 2), [6, 12, 18]),
        q("Is 5 ⊕ 7 equal to 7 ⊕ 5?", "Yes, always", ["No, never", "Only for odd numbers", "Only when one is 0"]),
        q("What is 0 ⊕ 6?", 6, [0, 7, 12]),
        q("A student says 2 ⊕ 3 = 5. What did they forget?", "To add the product 2×3",
          ["To subtract 1", "To swap the numbers", "To square the result"]),
    ]  # fmt: skip
    t["Krell steps on a grid"] = [
        q("Where does one krell step take (2, 7)?", krell((2, 7)), [(7, 2), (3, 7), (8, 2)]),
        q("Where do two krell steps take (3, 5)?", krell(krell((3, 5))), [(5, 4), (3, 7), (5, 3)]),
        q("Where does one krell step take (0, 0)?", krell((0, 0)), [(1, 0), (1, 1), (0, 0)]),
        q("Starting at (0, 0), where are you after four krell steps?", (2, 2), [(4, 0), (0, 4), (4, 4)]),
        q("What do two krell steps do to any point (x, y)?", "Add 1 to both x and y",
          ["Swap x and y", "Add 2 to y only", "Leave it unchanged"]),
        q("Which point comes right after (1, 1) on the staircase from (0, 0)?", krell((1, 1)), [(2, 1), (2, 2), (1, 0)]),
        q("Where does one krell step take (4, 4)?", krell((4, 4)), [(5, 4), (4, 4), (5, 5)]),
        q("After one krell step the first number of the new point is...", "the old second number",
          ["the old first number plus 1", "always 0", "the sum of both numbers"]),
    ]  # fmt: skip
    t["Vorn sequences"] = [
        q("What is the 5th vorn term v(5)?", vorn(5), [16, 19, 13]),
        q("What is v(6)?", vorn(6), [42, 32, 41]),
        q("What are the first two vorn terms?", "1 and 3", ["1 and 1", "1 and 2", "3 and 5"]),
        q("Which rule makes the next vorn term?", "previous + 2 × the one before it",
          ["2 × previous + 1", "previous + the one before it", "previous × 2"]),
        q("Is the vorn term v(10) odd or even?", "Odd", ["Even", "It depends on v(9)", "It is 0"]),
        q("About how does each vorn term compare with the one before it?", "About twice as large",
          ["About the same", "About three times as large", "About half as large"]),
        q("What is v(4)?", vorn(4), [9, 8, 7]),
        q("If v(7) = 85 and v(8) = 171, what is v(9)?", 171 + 2 * 85, [256, 342, 255]),
    ]  # fmt: skip
    t["Glint numbers"] = [
        q("Which number is glint?", 36, [38, 34, 27]),
        q("Which number is NOT glint?", 26, [24, 15, 31]),
        q("Is 40 glint?", "No, it ends in 0", ["Yes, 40 ÷ 4 = 10", "Yes, it is even", "Only in some cases"]),
        q("How many of 12, 13, 14, 15 are glint?", sum(glint(n) for n in (12, 13, 14, 15)), [1, 3, 4]),
        q("Which kind of number is always glint?", "Every number ending in 1",
          ["Every even number", "Every number ending in 0", "Every number ending in 7"]),
        q("Is 48 glint?", "Yes, 48 ÷ 8 = 6", ["No, 48 ÷ 8 is not whole", "No, it is even", "No, 8 is too large"]),
        q("Which number is glint?", 65, [67, 58, 46]),
        q("What decides whether a number is glint?", "Whether it divides evenly by its last digit",
          ["Whether its digits add to an even number", "Whether it is prime", "Whether its first digit divides it"]),
    ]  # fmt: skip
    t["Mirthful triangles"] = [
        q("Which triangle is mirthful?", "sides 5, 6, 7", ["sides 3, 4, 5", "sides 2, 3, 4", "sides 4, 4, 7"]),
        q("Is a triangle with sides 3, 4, 5 mirthful?", "No", ["Yes", "Only if it is right-angled", "It cannot be told"]),
        q("Is every equilateral triangle mirthful?", "Yes", ["No", "Only small ones", "Only large ones"]),
        q("A mirthful triangle is doubled in size. Is it still mirthful?", "Yes, always",
          ["No, never", "Only if its sides are even", "Only if it was equilateral"]),
        q("Which sides matter for being mirthful?", "Only the longest and the shortest",
          ["Only the middle one", "All three equally", "Only the longest"]),
        q("Sides 6, 8, 9: is the triangle mirthful?", "Yes" if mirthful(6, 8, 9) else "No",
          ["No" if mirthful(6, 8, 9) else "Yes", "Only if 8 is the base", "It cannot be told"]),
        q("Sides 4, 6, 7: is the triangle mirthful?", "Yes" if mirthful(4, 6, 7) else "No",
          ["No" if mirthful(4, 6, 7) else "Yes", "Only if 6 is the base", "It cannot be told"]),
        q("The shortest side is 10. What is the longest the longest side can be for a mirthful triangle?", 15,
          [20, 10, 30]),
    ]  # fmt: skip
    t["Sorrel counts of lattice rectangles"] = [
        q("What is the sorrel count of a 4 × 4 square?", sorrel(4, 4), [9, -16, 7]),
        q("What is the sorrel count of a 2 × 5 rectangle?", sorrel(2, 5), [4, -4, 10]),
        q("How many grid points are strictly inside a 5 × 3 rectangle?", 4 * 2, [15, 16, 6]),
        q("How many grid points lie on the edges of a 5 × 3 rectangle?", 2 * (5 + 3), [8, 15, 20]),
        q("A 3 × 7 and a 7 × 3 rectangle: how do their sorrel counts compare?", "They are equal",
          ["The 3 × 7 one is larger", "The 7 × 3 one is larger", "One is the negative of the other"]),
        q("What is the sorrel count of a 1 × 1 square?", sorrel(1, 1), [0, 1, -1]),
        q("For which rectangle is the sorrel count positive?", "8 × 8", ["2 × 2", "3 × 4", "1 × 9"]),
        q("The sorrel count is...", "points inside minus points on the edges",
          ["points on the edges minus points inside", "all grid points of the rectangle", "the area minus the perimeter"]),
    ]  # fmt: skip
    t["Quill distance"] = [
        q("What is the quill distance from (0, 0) to (2, 3)?", quill((0, 0), (2, 3)), [5, 7, 10]),
        q("What is the quill distance from (1, 1) to (4, 1)?", 3, [6, 4, 2]),
        q("What is the quill distance from (2, 0) to (2, 4)?", 8, [4, 6, 2]),
        q("Which point is at quill distance 2 from (0, 0)?", (0, 1), [(1, 1), (0, 2), (1, 2)]),
        q("Is the quill distance from A to B the same as from B to A?", "Yes, always",
          ["No, never", "Only on the x-axis", "Only when A is (0, 0)"]),
        q("Which move costs more in quill distance?", "One unit up", ["One unit right", "They cost the same",
          "It depends on the start"]),
        q("What is the quill distance from (-1, 2) to (1, -1)?", quill((-1, 2), (1, -1)), [5, 7, 9]),
        q("How many grid points are at quill distance exactly 2 from (0, 0)?", 4, [8, 2, 6]),
    ]  # fmt: skip
    t["Dapple numbers"] = [
        q("Which number is dapple?", 73, [37, 77, 7]),
        q("Is 30 dapple?", "Yes", ["No", "Only if divided by 10", "It cannot be told"]),
        q("Is 9 dapple?", "No", ["Yes", "Only as 09", "It cannot be told"]),
        q("How many numbers from 10 to 19 are dapple?", sum(dapple(n) for n in range(10, 20)), [0, 9, 10]),
        q("How many numbers from 20 to 29 are dapple?", sum(dapple(n) for n in range(20, 30)), [1, 3, 8]),
        q("64 is dapple. Is 46 dapple?", "No", ["Yes", "Only if it is even", "It cannot be told"]),
        q("Is 55 dapple?", "No", ["Yes", "Only because 5 is odd", "It cannot be told"]),
        q("A number is dapple when...", "its tens digit is greater than its units digit",
          ["its units digit is greater than its tens digit", "its digits add to an even number", "it is a multiple of 10"]),
    ]  # fmt: skip
    t["Brisk folds of a list"] = [
        q("What is the brisk fold of [2, 5, 1, 3, 4]?", brisk([2, 5, 1, 3, 4]), [[6, 8], [7, 4, 4], [6, 9, 1]]),
        q("What is the brisk fold of [1, 1, 1, 1]?", brisk([1, 1, 1, 1]), [[1, 1], [4], [2, 2, 2, 2]]),
        q("What is the brisk fold of [5, 0, 5, 0, 5, 0]?", brisk([5, 0, 5, 0, 5, 0]), [[10, 0, 10], [10, 5],
          [0, 10, 0]]),
        q("The list [3, 9, 4, 6] adds up to 22. What does its brisk fold add up to?", 22, [11, 44, 13]),
        q("How long is the brisk fold of a list of 9 numbers?", 5, [4, 9, 3]),
        q("Fold [1, 2, 3, 4, 5, 6, 7, 8] twice. What do you get?", brisk(brisk([1, 2, 3, 4, 5, 6, 7, 8])),
          [[9, 9, 9, 9], [36], [10, 26]]),
        q("In the brisk fold of [4, 7, 2], where does the 7 go?", "It stays alone at the end",
          ["It is added to 4", "It is added to 2", "It is dropped"]),
        q("In a brisk fold, the first number is added to...", "the last number",
          ["the second number", "the middle number", "itself"]),
    ]  # fmt: skip
    w2, w3 = orbit(orbit("X")), orbit(orbit(orbit("X")))
    t["Orbit words"] = [
        q("What does X become after one rewrite?", "XYY", ["XY", "YX", "XXY"]),
        q("What does Y become after one rewrite?", "YX", ["XY", "YY", "XYY"]),
        q("What is the orbit word after two rewrites from X?", w2, ["XYYXYY", "XYYYX", "XXYYXX"]),
        q("How long is the orbit word after three rewrites from X?", len(w3), [9, 13, 21]),
        q("How many X letters are in the word after two rewrites?", w2.count("X"), [2, 4, 1]),
        q("Which letter does every orbit word start with?", "X", ["Y", "It alternates", "It depends on the step"]),
        q("What does the word YY become after one rewrite?", "YXYX", ["XYYXYY", "YYXX", "XYXY"]),
        q("How are the letters rewritten?", "All letters at once, each by its own rule",
          ["One letter per step, left to right", "Only the last letter", "Only the X letters"]),
    ]  # fmt: skip
    t["Vells of 2×2 grids"] = [
        q("What is the vell of [[3, 1], [2, 5]]?", vell(3, 1, 2, 5), [13, 17, 15]),
        q("What is the vell of [[1, 1], [1, 1]]?", vell(1, 1, 1, 1), [0, 2, 1]),
        q("What is the vell of [[4, 0], [0, 4]]?", vell(4, 0, 0, 4), [8, 0, 4]),
        q("What is the vell of [[2, 3], [5, 1]]?", vell(2, 3, 5, 1), [-13, 17, 6]),
        q("Which two numbers are multiplied in a vell?", "top-left and bottom-right",
          ["top-right and bottom-left", "the two top numbers", "all four"]),
        q("Swap b and c in [[a, b], [c, d]]. What happens to the vell?", "It stays the same",
          ["It changes sign", "It doubles", "It becomes 0"]),
        q("What is the vell of [[0, 2], [3, 7]]?", vell(0, 2, 3, 7), [5, 21, -21]),
        q("What is the vell of [[5, 2], [2, 2]]?", vell(5, 2, 2, 2), [14, 10, 4]),
    ]  # fmt: skip
    t["Lumen clocks"] = [
        q("From mark 0, where is the hand after 1 tick?", lumen(0, 1), [1, 7, 0]),
        q("From mark 5, where is the hand after 1 tick?", lumen(5, 1), [6, 7, 1]),
        q("From mark 3, where is the hand after 3 ticks?", lumen(3, 3), [6, 0, 1]),
        q("From mark 4, how many ticks bring the hand back to 4?", 7, [2, 4, 14]),
        q("From mark 0, where is the hand after 4 ticks?", lumen(0, 4), [4, 8, 2]),
        q("Does the hand ever visit every mark?", "Yes, before it returns", ["No, only even marks",
          "No, only odd marks", "Only from mark 0"]),
        q("How many marks does a lumen clock have?", 7, [12, 6, 8]),
        q("One tick moves the hand by...", "2 marks forward", ["1 mark forward", "2 marks back", "7 marks"]),
    ]  # fmt: skip
    return t


def main():
    rng = random.Random(2026)
    letters = "ABCD"
    out = {}
    slots = []
    for topic, items in tests().items():
        rows = []
        for it in items:
            assert it["right"] not in it["wrong"] and len(set(it["wrong"])) == 3, (topic, it)
            if not slots:
                slots = list(letters) * 2
                rng.shuffle(slots)
            pos = letters.index(slots.pop())
            opts = it["wrong"][:]
            rng.shuffle(opts)
            opts.insert(pos, it["right"])
            rows.append({"question": it["question"], "options": dict(zip(letters, opts, strict=True)),
                         "answer": letters[pos]})  # fmt: skip
        out[topic] = rows
    (HERE / "questions.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    (HERE / "cards.json").write_text(json.dumps(CARDS, indent=1, ensure_ascii=False))
    from collections import Counter

    print(len(out), "topics,", sum(map(len, out.values())), "questions; answer letters",
          dict(Counter(r["answer"] for v in out.values() for r in v)))  # fmt: skip


if __name__ == "__main__":
    main()
