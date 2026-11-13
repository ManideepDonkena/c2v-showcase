# Noise model

Points are on the 0-100 scale (M9, NVG, D-VGAIN, or raw P(right) x 100).

## Repeat noise (same input twice)

232 questions in 29 identical-input pairs (ours vs autofix (identical frames), repeat r1, repeat r2): 33 moved by more than 0.01, the largest by +46.2 points of P(right).
Repeat noise alone puts 95% of version differences within ±7.2 M9 points on one topic and ±1.9 on the mean of all topics.

## Comparisons

| | Question | n | Mean | 95% CI (topics, questions) | MDE | p (measurement) | p Holm | p (over topics) | > 0 | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| N1 | NOVEL-12: the base video teaches (M9 > 0, 3 frames vs no video) | 10 | +42.4 | [+6.9, +62.2] | 39.4 | 0.0001 | 0.0004 | 0.00781 | 9/10 | real, and holds over topics |
| N2 | NOVEL-12: the gain is specific (own video − another topic's video, M9) | 10 | +64.4 | [+44.2, +104.9] | 42.7 | 0.0001 | 0.0004 | 0.00195 | 10/10 | real, and holds over topics |
| N3 | NOVEL-12: the dense video teaches (NVG, dense vs no video) | 10 | +14.1 | [-10.9, +28.4] | 28.0 | 0.0499 | n/a | 0.0156 | 9/10 | beyond noise for these videos only (not over topics / not after correction) |
| N4 | NOVEL-12: 3 frames teach more than the dense video (M9 − NVG dense) | 10 | +28.4 | [+0.4, +52.7] | 37.7 | 0.0020 | n/a | 0.0137 | 8/10 | real, and holds over topics |
| L1 | Layout study: Claude-fixed − ours (M9, preregistered) | 10 | +5.1 | [-10.0, +22.9] | 24.2 | 0.2661 | 0.445 | 0.619 | 5/10 | within noise |
| L2 | Layout study: autofix − ours (M9) | 10 | -0.0 | [-1.5, +1.5] | 2.0 | 0.9481 | n/a | 1 | 1/10 | within noise |
| L3 | Layout study: Claude-fixed − ours (M7, dense video + motion bonus) | 10 | +1.5 | [-10.7, +11.4] | 15.5 | 0.6432 | n/a | 0.674 | 6/10 | within noise |
| P1 | MMMC pilot, 3B student: learner − base (M9) | 9 | -23.7 | [-186.2, +27.4] | 160.2 | 0.2226 | 0.445 | 0.727 | 5/9 | within noise |
| P2 | MMMC pilot, 3B student: own − other topic (raw P(right), R9) | 12 | +6.4 | [-0.0, +16.8] | 12.5 | 0.0094 | n/a | 0.0283 | 9/12 | beyond noise for these videos only (not over topics / not after correction) |
| P3 | MMMC pilot, gemma: own − other topic (raw P(right), R9; M9 undefined at the ceiling) | 12 | +13.0 | [+3.5, +25.0] | 15.6 | 0.0001 | n/a | 0.000488 | 12/12 | real, and holds over topics |
| P4 | MMMC pilot, gemma: learner − base (raw P(right), R9) | 12 | +0.1 | [-0.1, +0.4] | 0.3 | 0.4143 | n/a | 0.41 | 6/12 | within noise |
| N5 | NOVEL-12: 3 frames at 768 px − the same frames at 512 px (M9) | 10 | +18.8 | [-3.6, +48.5] | 37.2 | 0.0079 | n/a | 0.0332 | 6/10 | beyond noise for these videos only (not over topics / not after correction) |
| N6 | NOVEL-12: 3 frames at 512 px − the dense video at 512 px (M9 − NVG dense) | 10 | +9.6 | [-27.3, +32.8] | 42.6 | 0.2210 | n/a | 0.377 | 6/10 | within noise |
| H1 | Haiku 5.5 student: the base video teaches (M9 > 0, binary) | 10 | +89.2 | [+61.3, +100.0] | 30.8 | 0.0001 | n/a | 0.00391 | 9/10 | real, and holds over topics |
| H2 | Haiku 5.5 student: own video − another topic's video (M9) | 10 | +150.6 | [+105.8, +236.7] | 95.7 | 0.0001 | n/a | 0.00195 | 10/10 | real, and holds over topics |
| H3 | Haiku 5.5 student: Claude-fixed − ours (M9) | 10 | -1.5 | [-17.5, +15.7] | 22.3 | 0.7768 | n/a | 0.875 | 2/10 | within noise |
| S1 | Sonnet 5.5 student: the base video teaches (M9 > 0, binary) | 10 | +45.9 | [+5.5, +72.4] | 47.7 | 0.0008 | n/a | 0.0117 | 8/10 | real, and holds over topics |
| S2 | Sonnet 5.5 student: own video − another topic's video (M9) | 10 | +90.8 | [+51.1, +151.1] | 70.6 | 0.0001 | n/a | 0.00195 | 10/10 | real, and holds over topics |
| S3 | Sonnet 5.5 student: Claude-fixed − ours (M9) | 10 | -16.3 | [-58.5, +6.9] | 49.3 | 0.0796 | n/a | 0.539 | 4/10 | within noise |
| N7 | NOVEL-12, stage F0: learner repair − base (M9) | 10 | +6.1 | [-12.9, +28.1] | 29.5 | 0.3560 | n/a | 0.453 | 6/10 | within noise |
| N8 | NOVEL-12, stage F0: learner repair − generic repair (M9) | 10 | +6.1 | [-14.1, +27.2] | 29.9 | 0.3918 | n/a | 0.449 | 6/10 | within noise |
| R1 | NOVEL-12, stage F1: learner repair − base (M9) | 10 | +7.7 | [-4.2, +25.3] | 21.7 | 0.1317 | n/a | 0.125 | 4/10 | within noise |
| R1g | NOVEL-12, stage F1: learner repair − generic repair (M9) | 10 | +5.6 | [-9.4, +22.3] | 22.4 | 0.3253 | n/a | 0.328 | 4/10 | within noise |
| R2 | NOVEL-12, stage F2: learner repair − base (M9) | 10 | +12.2 | [-0.0, +32.8] | 23.7 | 0.0173 | n/a | 0.125 | 4/10 | beyond noise for these videos only (not over topics / not after correction) |
| R2g | NOVEL-12, stage F2: learner repair − generic repair (M9) | 10 | +3.4 | [-3.6, +12.4] | 11.4 | 0.1709 | n/a | 0.344 | 4/10 | within noise |
| R3 | NOVEL-12, stage F3: learner repair − base (M9) | 10 | +3.4 | [+0.0, +13.5] | 11.0 | 0.0077 | n/a | 1 | 1/10 | beyond noise for these videos only (not over topics / not after correction) |
| R3g | NOVEL-12, stage F3: learner repair − generic repair (M9) | 10 | +2.1 | [-4.1, +12.2] | 11.8 | 0.5635 | n/a | 0.875 | 2/10 | within noise |
| R4 | NOVEL-12, stage F4: learner repair − base (M9) | 10 | +2.5 | [-0.1, +7.1] | 5.6 | 0.1013 | n/a | 0.25 | 3/10 | within noise |
| R4g | NOVEL-12, stage F4: learner repair − generic repair (M9) | 10 | +2.0 | [-1.9, +7.3] | 6.5 | 0.2680 | n/a | 0.375 | 3/10 | within noise |
| R5 | NOVEL-12, stage F5: learner repair − base (M9) | 10 | +6.0 | [+0.0, +15.7] | 11.7 | 0.0235 | n/a | 0.125 | 4/10 | beyond noise for these videos |
| R5g | NOVEL-12, stage F5: learner repair − generic repair (M9) | 10 | +6.3 | [+0.3, +16.5] | 11.6 | 0.0154 | n/a | 0.0625 | 5/10 | beyond noise for these videos |

Preregistered layout rule (mean >= +5 and >= 70% of topics ahead): fires now = False; it fires on noise alone in 8.2% of randomisations.

Repeat noise, claude_haiku_5_5: 8 of 320 answers changed when the frames pass was asked again; 95% of M9 differences within ±22.2 on one topic and ±6.5 on the mean.

Repeat noise, claude_sonnet_5_5: 10 of 320 answers changed when the frames pass was asked again; 95% of M9 differences within ±25.0 on one topic and ±7.7 on the mean.

## Per topic (value, item-level p, SD from resampling the questions)

**N1** NOVEL-12: the base video teaches (M9 > 0, 3 frames vs no video)

- Tovan sums: +76.4 (p 0.0082, SD 12.4)
- Krell steps on a grid: +25.8 (p 0.148, SD 20.0)
- Vorn sequences: +42.7 (p 0.53, SD 58.3)
- Glint numbers: +79.2 (p 0.0879, SD 31.2)
- Mirthful triangles: +42.0 (p 0.0981, SD 22.6)
- Sorrel counts of lattice rectangles: -27.9 (p 0.322, SD 41.4)
- Quill distance: +26.9 (p 0.169, SD 18.5)
- Dapple numbers: +45.6 (p 0.26, SD 31.3)
- Orbit words: +61.9 (p 0.102, SD 23.3)
- Vells of 2×2 grids: +51.8 (p 0.108, SD 20.9)

**N2** NOVEL-12: the gain is specific (own video − another topic's video, M9)

- Tovan sums: +83.3 (p 0.0073, SD 17.3)
- Krell steps on a grid: +31.7 (p 0.183, SD 19.5)
- Vorn sequences: +90.7 (p 0.0757, SD 66.1)
- Glint numbers: +106.8 (p 0.0081, SD 28.5)
- Mirthful triangles: +73.6 (p 0.0165, SD 37.1)
- Sorrel counts of lattice rectangles: +43.1 (p 0.23, SD 64.0)
- Quill distance: +27.2 (p 0.0388, SD 16.9)
- Dapple numbers: +58.8 (p 0.155, SD 39.2)
- Orbit words: +67.8 (p 0.0392, SD 21.4)
- Vells of 2×2 grids: +61.5 (p 0.0457, SD 34.4)

**N3** NOVEL-12: the dense video teaches (NVG, dense vs no video)

- Tovan sums: +11.5 (p 0.754, SD 15.0)
- Krell steps on a grid: +18.1 (p 0.294, SD 17.1)
- Vorn sequences: +49.7 (p 0.124, SD 26.2)
- Glint numbers: +15.9 (p 0.63, SD 34.5)
- Mirthful triangles: +17.5 (p 0.676, SD 27.1)
- Sorrel counts of lattice rectangles: -16.0 (p 0.471, SD 29.9)
- Quill distance: +11.6 (p 0.525, SD 16.9)
- Dapple numbers: +7.9 (p 0.797, SD 28.0)
- Orbit words: +19.5 (p 0.224, SD 16.7)
- Vells of 2×2 grids: +4.8 (p 0.76, SD 26.2)

**N4** NOVEL-12: 3 frames teach more than the dense video (M9 − NVG dense)

- Tovan sums: +64.9 (p 0.0067, SD 14.2)
- Krell steps on a grid: +7.7 (p 0.786, SD 29.9)
- Vorn sequences: -7.0 (p 1, SD 54.5)
- Glint numbers: +63.3 (p 0.0683, SD 27.6)
- Mirthful triangles: +24.6 (p 0.536, SD 43.5)
- Sorrel counts of lattice rectangles: -11.9 (p 0.44, SD 17.1)
- Quill distance: +15.2 (p 0.55, SD 21.9)
- Dapple numbers: +37.7 (p 0.188, SD 27.3)
- Orbit words: +42.4 (p 0.067, SD 19.4)
- Vells of 2×2 grids: +47.0 (p 0.114, SD 26.7)

**L1** Layout study: Claude-fixed − ours (M9, preregistered)

- Tovan sums: -10.9 (p 0.208, SD 9.6)
- Krell steps on a grid: +24.2 (p 0.0686, SD 16.1)
- Vorn sequences: -3.1 (p 0.248, SD 1.5)
- Glint numbers: -8.0 (p 0.276, SD 10.0)
- Mirthful triangles: -25.9 (p 0.153, SD 15.8)
- Sorrel counts of lattice rectangles: +62.7 (p 0.0141, SD 18.8)
- Quill distance: +9.1 (p 0.323, SD 7.7)
- Dapple numbers: +2.8 (p 0.629, SD 14.1)
- Orbit words: +3.1 (p 0.783, SD 10.5)
- Vells of 2×2 grids: -2.7 (p 0.548, SD 4.7)

**L2** Layout study: autofix − ours (M9)

- Tovan sums: +0.0 (p 1, SD 0.0)
- Krell steps on a grid: +3.6 (p 0.987, SD 3.8)
- Vorn sequences: +0.0 (p 1, SD 0.0)
- Glint numbers: +0.0 (p 1, SD 0.0)
- Mirthful triangles: +0.0 (p 1, SD 0.0)
- Sorrel counts of lattice rectangles: +0.0 (p 1, SD 0.0)
- Quill distance: +0.0 (p 1, SD 0.0)
- Dapple numbers: -0.4 (p 0.75, SD 0.6)
- Orbit words: -2.4 (p 0.558, SD 3.6)
- Vells of 2×2 grids: -1.0 (p 0.526, SD 1.4)

**L3** Layout study: Claude-fixed − ours (M7, dense video + motion bonus)

- Tovan sums: +10.1 (p 0.328, SD 8.8)
- Krell steps on a grid: -6.6 (p 0.761, SD 20.7)
- Vorn sequences: +10.5 (p 0.0145, SD 4.2)
- Glint numbers: +5.3 (p 0.898, SD 8.4)
- Mirthful triangles: +4.2 (p 0.833, SD 7.7)
- Sorrel counts of lattice rectangles: -19.7 (p 0.0541, SD 20.1)
- Quill distance: -2.5 (p 0.255, SD 2.8)
- Dapple numbers: -7.2 (p 0.669, SD 15.8)
- Orbit words: +1.7 (p 0.923, SD 3.4)
- Vells of 2×2 grids: +18.8 (p 0.0848, SD 14.0)

**P1** MMMC pilot, 3B student: learner − base (M9)

- The inscribed square or rectangle proble: +24.6 (p 0.315, SD 44.6)
- Hamming error correction codes: -72.1 (p 0.0605, SD 14.2)
- Space-filling curves and the relationshi: -4.6 (p 0.941, SD 7.1)
- Uncertainty Principle in the Context of : +4.5 (p 0.314, SD 7.5)
- Holomorphic dynamics and iterated comple: n/a (p n/a, SD 6.0)
- Backpropagation calculus: n/a (p n/a, SD 0.9)
- Error correction codes and Hamming codes: +1.8 (p 0.318, SD 1.1)
- Large Language Models and Transformers i: n/a (p n/a, SD 17.4)
- Interconnections in number theory: π, pr: +77.8 (p 0.693, SD 4.4)
- Higher order derivatives: +7.5 (p 0.561, SD 3.7)
- Sum of normal distributions, Gaussian + : -252.7 (p 0.126, SD 284.3)
- The determinant: +0.0 (p 1, SD 0.0)

**P2** MMMC pilot, 3B student: own − other topic (raw P(right), R9)

- The inscribed square or rectangle proble: +7.0 (p 0.566, SD 11.6)
- Hamming error correction codes: +7.6 (p 0.0627, SD 5.3)
- Space-filling curves and the relationshi: -0.3 (p 1, SD 1.5)
- Uncertainty Principle in the Context of : +0.9 (p 0.938, SD 4.7)
- Holomorphic dynamics and iterated comple: +1.9 (p 0.567, SD 1.9)
- Backpropagation calculus: +2.3 (p 0.0609, SD 1.4)
- Error correction codes and Hamming codes: +1.9 (p 0.0629, SD 0.7)
- Large Language Models and Transformers i: +0.1 (p 0.817, SD 0.5)
- Interconnections in number theory: π, pr: +4.0 (p 0.123, SD 1.9)
- Higher order derivatives: -2.9 (p 0.368, SD 2.4)
- Sum of normal distributions, Gaussian + : +53.7 (p 0.126, SD 12.7)
- The determinant: +0.0 (p 1, SD 0.0)

**P3** MMMC pilot, gemma: own − other topic (raw P(right), R9; M9 undefined at the ceiling)

- The inscribed square or rectangle proble: +51.6 (p 0.0575, SD 10.3)
- Hamming error correction codes: +0.2 (p 1, SD 0.2)
- Space-filling curves and the relationshi: +0.3 (p 0.122, SD 0.3)
- Uncertainty Principle in the Context of : +12.9 (p 0.0591, SD 7.8)
- Holomorphic dynamics and iterated comple: +20.0 (p 0.127, SD 17.6)
- Backpropagation calculus: +10.0 (p 0.0659, SD 9.0)
- Error correction codes and Hamming codes: +10.1 (p 0.318, SD 8.3)
- Large Language Models and Transformers i: +47.4 (p 0.0591, SD 8.9)
- Interconnections in number theory: π, pr: +0.8 (p 0.872, SD 0.7)
- Higher order derivatives: +0.0 (p 1, SD 0.0)
- Sum of normal distributions, Gaussian + : +0.1 (p 1, SD 0.1)
- The determinant: +2.0 (p 0.371, SD 1.7)

**P4** MMMC pilot, gemma: learner − base (raw P(right), R9)

- The inscribed square or rectangle proble: +0.8 (p 0.687, SD 0.8)
- Hamming error correction codes: -0.0 (p 1, SD 0.0)
- Space-filling curves and the relationshi: +0.4 (p 0.748, SD 0.3)
- Uncertainty Principle in the Context of : +0.3 (p 0.5, SD 0.3)
- Holomorphic dynamics and iterated comple: +0.0 (p 1, SD 0.0)
- Backpropagation calculus: -0.0 (p 0.507, SD 0.0)
- Error correction codes and Hamming codes: -0.3 (p 0.88, SD 0.3)
- Large Language Models and Transformers i: +0.0 (p 1, SD 0.0)
- Interconnections in number theory: π, pr: -0.1 (p 0.696, SD 0.1)
- Higher order derivatives: -0.0 (p 1, SD 0.0)
- Sum of normal distributions, Gaussian + : +0.0 (p 0.504, SD 0.0)
- The determinant: -0.1 (p 0.258, SD 0.1)

**N5** NOVEL-12: 3 frames at 768 px − the same frames at 512 px (M9)

- Tovan sums: +20.1 (p 0.0324, SD 9.3)
- Krell steps on a grid: -8.3 (p 0.499, SD 7.7)
- Vorn sequences: -1.7 (p 1, SD 55.6)
- Glint numbers: +65.1 (p 0.0463, SD 28.7)
- Mirthful triangles: +25.2 (p 0.0167, SD 12.4)
- Sorrel counts of lattice rectangles: +51.4 (p 0.114, SD 64.6)
- Quill distance: -5.2 (p 0.911, SD 17.6)
- Dapple numbers: -5.2 (p 0.785, SD 15.3)
- Orbit words: +21.0 (p 0.334, SD 19.8)
- Vells of 2×2 grids: +25.8 (p 0.123, SD 18.6)

**N6** NOVEL-12: 3 frames at 512 px − the dense video at 512 px (M9 − NVG dense)

- Tovan sums: +44.8 (p 0.0157, SD 20.1)
- Krell steps on a grid: +16.0 (p 0.573, SD 28.7)
- Vorn sequences: -5.3 (p 0.505, SD 9.3)
- Glint numbers: -1.7 (p 0.875, SD 18.5)
- Mirthful triangles: -0.6 (p 1, SD 35.6)
- Sorrel counts of lattice rectangles: -63.4 (p 0.0448, SD 70.2)
- Quill distance: +20.5 (p 0.467, SD 27.1)
- Dapple numbers: +42.9 (p 0.103, SD 23.3)
- Orbit words: +21.4 (p 0.344, SD 20.1)
- Vells of 2×2 grids: +21.2 (p 0.31, SD 17.2)

**H1** Haiku 5.5 student: the base video teaches (M9 > 0, binary)

- Tovan sums: +100.0 (p 0.0157, SD 0.0)
- Krell steps on a grid: +100.0 (p 0.0608, SD 0.0)
- Vorn sequences: +100.0 (p 0.51, SD 0.0)
- Glint numbers: +91.7 (p 0.0151, SD 8.5)
- Mirthful triangles: +100.0 (p 0.0154, SD 0.0)
- Sorrel counts of lattice rectangles: +0.0 (p 1, SD 40.9)
- Quill distance: +100.0 (p 0.0325, SD 0.0)
- Dapple numbers: +100.0 (p 0.0076, SD 0.0)
- Orbit words: +100.0 (p 0.122, SD 0.0)
- Vells of 2×2 grids: +100.0 (p 0.0327, SD 0.0)

**H2** Haiku 5.5 student: own video − another topic's video (M9)

- Tovan sums: +133.3 (p 0.123, SD 39.9)
- Krell steps on a grid: +150.0 (p 0.0155, SD 89.7)
- Vorn sequences: +280.0 (p 0.0331, SD 169.4)
- Glint numbers: +83.3 (p 0.0142, SD 13.8)
- Mirthful triangles: +100.0 (p 0.0295, SD 11.7)
- Sorrel counts of lattice rectangles: +300.0 (p 0.0166, SD 89.7)
- Quill distance: +95.7 (p 0.0159, SD 9.8)
- Dapple numbers: +112.5 (p 0.0063, SD 9.1)
- Orbit words: +145.5 (p 0.0311, SD 102.2)
- Vells of 2×2 grids: +105.9 (p 0.008, SD 20.3)

**H3** Haiku 5.5 student: Claude-fixed − ours (M9)

- Tovan sums: +0.0 (p 1, SD 0.0)
- Krell steps on a grid: +0.0 (p 1, SD 0.0)
- Vorn sequences: +0.0 (p 1, SD 0.0)
- Glint numbers: +4.2 (p 1, SD 4.2)
- Mirthful triangles: +0.0 (p 1, SD 0.0)
- Sorrel counts of lattice rectangles: +25.0 (p 1, SD 50.3)
- Quill distance: +0.0 (p 1, SD 0.0)
- Dapple numbers: -16.7 (p 0.12, SD 6.4)
- Orbit words: -27.3 (p 0.241, SD 35.5)
- Vells of 2×2 grids: +0.0 (p 1, SD 0.0)

**S1** Sonnet 5.5 student: the base video teaches (M9 > 0, binary)

- Tovan sums: +12.5 (p 1, SD 52.0)
- Krell steps on a grid: -33.3 (p 1, SD 59.5)
- Vorn sequences: +90.9 (p 0.249, SD 15.5)
- Glint numbers: +54.5 (p 0.559, SD 76.2)
- Mirthful triangles: +89.5 (p 0.0293, SD 5.9)
- Sorrel counts of lattice rectangles: +0.0 (p 1, SD 28.6)
- Quill distance: +62.5 (p 0.0651, SD 19.0)
- Dapple numbers: +78.9 (p 0.0149, SD 13.9)
- Orbit words: +50.0 (p 0.374, SD 29.0)
- Vells of 2×2 grids: +53.8 (p 0.251, SD 23.7)

**S2** Sonnet 5.5 student: own video − another topic's video (M9)

- Tovan sums: +75.0 (p 0.251, SD 30.6)
- Krell steps on a grid: +200.0 (p 0.309, SD 163.6)
- Vorn sequences: +81.8 (p 0.124, SD 20.6)
- Glint numbers: +63.6 (p 0.537, SD 78.4)
- Mirthful triangles: +89.5 (p 0.0327, SD 16.3)
- Sorrel counts of lattice rectangles: +100.0 (p 0.127, SD 90.7)
- Quill distance: +62.5 (p 0.0587, SD 19.8)
- Dapple numbers: +57.9 (p 0.0925, SD 22.3)
- Orbit words: +85.7 (p 0.124, SD 55.6)
- Vells of 2×2 grids: +92.3 (p 0.0296, SD 53.0)

**S3** Sonnet 5.5 student: Claude-fixed − ours (M9)

- Tovan sums: +12.5 (p 1, SD 12.7)
- Krell steps on a grid: -166.7 (p 0.129, SD 70.7)
- Vorn sequences: -9.1 (p 1, SD 16.6)
- Glint numbers: +0.0 (p 1, SD 0.0)
- Mirthful triangles: +10.5 (p 0.504, SD 5.9)
- Sorrel counts of lattice rectangles: +14.3 (p 1, SD 10.8)
- Quill distance: +4.2 (p 1, SD 4.3)
- Dapple numbers: -5.3 (p 1, SD 8.7)
- Orbit words: +0.0 (p 1, SD 0.0)
- Vells of 2×2 grids: -23.1 (p 0.497, SD 20.3)

**N7** NOVEL-12, stage F0: learner repair − base (M9)

- Tovan sums: +10.9 (p 0.137, SD 10.0)
- Krell steps on a grid: +38.5 (p 0.101, SD 17.4)
- Vorn sequences: +19.1 (p 0.742, SD 41.5)
- Glint numbers: -7.7 (p 0.111, SD 8.5)
- Mirthful triangles: +10.1 (p 0.815, SD 37.7)
- Sorrel counts of lattice rectangles: +44.7 (p 0.106, SD 19.9)
- Quill distance: -14.0 (p 0.306, SD 10.2)
- Dapple numbers: -37.6 (p 0.218, SD 21.6)
- Orbit words: +8.7 (p 0.759, SD 19.1)
- Vells of 2×2 grids: -11.8 (p 0.186, SD 10.2)

**N8** NOVEL-12, stage F0: learner repair − generic repair (M9)

- Tovan sums: -0.0 (p 0.873, SD 0.0)
- Krell steps on a grid: +35.6 (p 0.0892, SD 17.2)
- Vorn sequences: -3.0 (p 1, SD 25.1)
- Glint numbers: +15.5 (p 0.881, SD 36.8)
- Mirthful triangles: +35.3 (p 0.415, SD 42.0)
- Sorrel counts of lattice rectangles: +26.0 (p 0.244, SD 17.5)
- Quill distance: -22.3 (p 0.394, SD 17.0)
- Dapple numbers: -39.3 (p 0.186, SD 22.4)
- Orbit words: +10.2 (p 0.757, SD 20.1)
- Vells of 2×2 grids: +2.7 (p 1, SD 8.7)

**R1** NOVEL-12, stage F1: learner repair − base (M9)

- Tovan sums: +10.9 (p 0.14, SD 9.6)
- Krell steps on a grid: +0.0 (p 1, SD 0.0)
- Vorn sequences: +19.1 (p 0.748, SD 38.3)
- Glint numbers: -7.7 (p 0.108, SD 9.6)
- Mirthful triangles: +10.1 (p 0.826, SD 36.8)
- Sorrel counts of lattice rectangles: +44.7 (p 0.111, SD 20.3)
- Quill distance: +0.0 (p 1, SD 0.0)
- Dapple numbers: +0.0 (p 1, SD 0.0)
- Orbit words: +0.0 (p 1, SD 0.0)
- Vells of 2×2 grids: +0.0 (p 1, SD 0.0)

**R1g** NOVEL-12, stage F1: learner repair − generic repair (M9)

- Tovan sums: -0.0 (p 0.877, SD 0.0)
- Krell steps on a grid: -2.8 (p 0.359, SD 2.1)
- Vorn sequences: -3.0 (p 1, SD 26.0)
- Glint numbers: +15.5 (p 0.881, SD 38.4)
- Mirthful triangles: +10.1 (p 0.823, SD 36.3)
- Sorrel counts of lattice rectangles: +44.7 (p 0.105, SD 20.7)
- Quill distance: -8.2 (p 0.719, SD 18.3)
- Dapple numbers: -1.7 (p 0.4, SD 1.5)
- Orbit words: +1.5 (p 0.718, SD 3.4)
- Vells of 2×2 grids: +0.0 (p 1, SD 0.0)

**R2** NOVEL-12, stage F2: learner repair − base (M9)

- Tovan sums: +11.1 (p 0.389, SD 10.1)
- Krell steps on a grid: +33.3 (p 0.19, SD 16.9)
- Vorn sequences: +10.6 (p 1, SD 39.1)
- Glint numbers: +0.0 (p 1, SD 0.0)
- Mirthful triangles: +0.0 (p 1, SD 0.0)
- Sorrel counts of lattice rectangles: +67.0 (p 0.0503, SD 23.3)
- Quill distance: +0.0 (p 1, SD 0.0)
- Dapple numbers: +0.0 (p 1, SD 0.0)
- Orbit words: +0.0 (p 1, SD 0.0)
- Vells of 2×2 grids: +0.0 (p 1, SD 0.0)

**R2g** NOVEL-12, stage F2: learner repair − generic repair (M9)

- Tovan sums: +0.4 (p 0.745, SD 0.4)
- Krell steps on a grid: +27.4 (p 0.071, SD 13.6)
- Vorn sequences: -1.4 (p 0.813, SD 15.3)
- Glint numbers: +1.8 (p 0.753, SD 8.0)
- Mirthful triangles: +0.0 (p 1, SD 0.0)
- Sorrel counts of lattice rectangles: +12.4 (p 0.232, SD 11.0)
- Quill distance: +0.0 (p 1, SD 0.0)
- Dapple numbers: +0.0 (p 1, SD 0.0)
- Orbit words: -6.7 (p 0.439, SD 5.0)
- Vells of 2×2 grids: +0.0 (p 1, SD 0.0)

**R3** NOVEL-12, stage F3: learner repair − base (M9)

- Tovan sums: +0.0 (p 1, SD 0.0)
- Krell steps on a grid: +0.0 (p 1, SD 0.0)
- Vorn sequences: +0.0 (p 1, SD 0.0)
- Glint numbers: +0.0 (p 1, SD 0.0)
- Mirthful triangles: +34.1 (p 0.0077, SD 20.3)
- Sorrel counts of lattice rectangles: +0.0 (p 1, SD 0.0)
- Quill distance: +0.0 (p 1, SD 0.0)
- Dapple numbers: +0.0 (p 1, SD 0.0)
- Orbit words: +0.0 (p 1, SD 0.0)
- Vells of 2×2 grids: +0.0 (p 1, SD 0.0)

**R3g** NOVEL-12, stage F3: learner repair − generic repair (M9)

- Tovan sums: -10.5 (p 0.504, SD 10.2)
- Krell steps on a grid: -2.8 (p 0.356, SD 2.1)
- Vorn sequences: +0.0 (p 1, SD 0.0)
- Glint numbers: +0.0 (p 1, SD 0.0)
- Mirthful triangles: +34.1 (p 0.0068, SD 19.9)
- Sorrel counts of lattice rectangles: +0.0 (p 1, SD 0.0)
- Quill distance: +0.0 (p 1, SD 0.0)
- Dapple numbers: +0.0 (p 1, SD 0.0)
- Orbit words: +0.0 (p 1, SD 0.0)
- Vells of 2×2 grids: +0.3 (p 0.809, SD 1.4)

**R4** NOVEL-12, stage F4: learner repair − base (M9)

- Tovan sums: +10.9 (p 0.15, SD 10.2)
- Krell steps on a grid: +0.4 (p 0.87, SD 1.0)
- Vorn sequences: +0.0 (p 1, SD 0.0)
- Glint numbers: +0.0 (p 1, SD 0.0)
- Mirthful triangles: +13.4 (p 0.305, SD 8.7)
- Sorrel counts of lattice rectangles: +0.0 (p 1, SD 0.0)
- Quill distance: +0.0 (p 1, SD 0.0)
- Dapple numbers: +0.0 (p 1, SD 0.0)
- Orbit words: +0.0 (p 1, SD 0.0)
- Vells of 2×2 grids: +0.0 (p 1, SD 0.0)

**R4g** NOVEL-12, stage F4: learner repair − generic repair (M9)

- Tovan sums: +0.2 (p 1, SD 0.2)
- Krell steps on a grid: +8.7 (p 0.427, SD 10.1)
- Vorn sequences: +0.0 (p 1, SD 0.0)
- Glint numbers: +0.0 (p 1, SD 0.0)
- Mirthful triangles: +13.4 (p 0.308, SD 8.5)
- Sorrel counts of lattice rectangles: +0.0 (p 1, SD 0.0)
- Quill distance: -2.3 (p 0.899, SD 10.7)
- Dapple numbers: +0.0 (p 1, SD 0.0)
- Orbit words: +0.0 (p 1, SD 0.0)
- Vells of 2×2 grids: +0.0 (p 1, SD 0.0)

**R5** NOVEL-12, stage F5: learner repair − base (M9)

- Tovan sums: +10.9 (p 0.21, SD 9.5)
- Krell steps on a grid: +16.9 (p 0.0849, SD 16.3)
- Vorn sequences: +0.0 (p 1, SD 0.0)
- Glint numbers: +0.0 (p 1, SD 0.0)
- Mirthful triangles: +0.0 (p 1, SD 0.0)
- Sorrel counts of lattice rectangles: +30.2 (p 0.142, SD 16.7)
- Quill distance: +2.1 (p 0.728, SD 3.9)
- Dapple numbers: +0.0 (p 1, SD 0.0)
- Orbit words: +0.0 (p 1, SD 0.0)
- Vells of 2×2 grids: +0.0 (p 1, SD 0.0)

**R5g** NOVEL-12, stage F5: learner repair − generic repair (M9)

- Tovan sums: +10.9 (p 0.206, SD 10.1)
- Krell steps on a grid: +17.6 (p 0.188, SD 16.2)
- Vorn sequences: +0.0 (p 1, SD 0.0)
- Glint numbers: +0.0 (p 1, SD 0.0)
- Mirthful triangles: +0.0 (p 1, SD 0.0)
- Sorrel counts of lattice rectangles: +30.2 (p 0.135, SD 17.6)
- Quill distance: +2.1 (p 0.724, SD 3.9)
- Dapple numbers: +2.0 (p 0.439, SD 2.7)
- Orbit words: +0.0 (p 1, SD 0.0)
- Vells of 2×2 grids: +0.0 (p 1, SD 0.0)
