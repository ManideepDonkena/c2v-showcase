# Metric ladder: mmmc-n12-seed0

12 topics, 48 distinct videos. Defined, distinct values, reliability and separation: base videos (one per topic); in brackets, over all videos.

| Rung | Change | Defined | Distinct values | Own − other topic (base) | Reliability | learner−base ties |
|---|---|---|---|---|---|---|
| M0 | TeachQuiz, as in the pilot | 12/12 [48/48] | 5 [8] | n/a | n/a | 7 |
| M1 | + answers matched by order | 0/12 [0/48] | 0 [0] | n/a | n/a | None |
| M2 | + forced choice | 12/12 [48/48] | 4 [6] | +0.100 [+0.000, +0.250] 3/9/0, p 0.25 | 0.57 [0.651] (option order 0 vs 1) | 9 |
| M3 | + normalised gain (NVG) | 6/12 [24/48] | 3 [4] | +0.167 [+0.000, +0.333] 2/4/0, p 0.5 | 0.822 [0.725] (option order 0 vs 1) | 4 |
| M4 | + dense silent video | 0/12 [0/48] | 0 [0] | n/a | n/a | None |
| M5 | + motion control (D-VGAIN) | 0/12 [0/48] | 0 [0] | n/a | n/a | None |
| M6 | + continuous scoring | 0/12 [0/48] | 0 [0] | n/a | n/a | None |
| M7 | + option rotation | 0/12 [0/48] | 0 [0] | n/a | n/a | None |
| M8 | + prior filter (unknown items only) | 0/12 [0/48] | 0 [0] | n/a | n/a | None |
| M9 | M7 on 3 frames per section (no dense video) | 9/12 [36/48] | 9 [31] | +0.379 [-0.008, +0.963] 6/1/2, p 0.1484 | n/a | 1 |
| R7 | raw: dense video P(right) minus no-video P(right) | 0/12 [0/48] | 0 [0] | n/a | n/a | None |
| R9 | raw: 3 frames/section P(right) minus no-video P(right) | 12/12 [48/48] | 12 [41] | +0.064 [+0.008, +0.156] 9/1/2, p 0.0322 | 0.315 [0.7] (option order 0 vs 1) | 1 |

## Paired condition differences per rung

mean [bootstrap 95% CI] wins/ties/losses, Wilcoxon p

| Rung | learner − base | learner − generic | learner − learner_all | generic − base |
|---|---|---|---|---|
| M0 | +0.017 [-0.017, +0.055] 3/7/2, p 0.5 | -0.022 [-0.105, +0.061] 1/9/2, p 0.75 | -0.044 [-0.111, +0.006] 1/8/3, p 0.25 | +0.039 [-0.050, +0.144] 2/7/3, p 0.75 |
| M1 | n/a | n/a | n/a | n/a |
| M2 | -0.033 [-0.183, +0.067] 2/9/1, p 1.0 | +0.017 [+0.000, +0.050] 1/11/0, p 1.0 | +0.033 [+0.000, +0.100] 1/11/0, p 1.0 | -0.050 [-0.200, +0.050] 1/10/1, p 1.0 |
| M3 | +0.250 [+0.000, +0.583] 2/4/0, p 0.5 | +0.083 [+0.000, +0.250] 1/5/0, p 1.0 | +0.167 [+0.000, +0.500] 1/5/0, p 1.0 | +0.167 [+0.000, +0.500] 1/5/0, p 1.0 |
| M4 | n/a | n/a | n/a | n/a |
| M5 | n/a | n/a | n/a | n/a |
| M6 | n/a | n/a | n/a | n/a |
| M7 | n/a | n/a | n/a | n/a |
| M8 | n/a | n/a | n/a | n/a |
| M9 | -0.237 [-0.895, +0.236] 5/1/3, p 0.9453 | -0.006 [-0.247, +0.186] 4/2/3, p 0.5781 | +0.059 [-0.040, +0.168] 4/2/3, p 0.5781 | -0.231 [-0.867, +0.198] 4/1/4, p 0.9453 |
| R7 | n/a | n/a | n/a | n/a |
| R9 | -0.029 [-0.134, +0.044] 6/1/5, p 0.8984 | +0.002 [-0.019, +0.021] 5/2/5, p 0.7695 | +0.012 [-0.004, +0.038] 5/2/5, p 0.8457 | -0.031 [-0.133, +0.036] 5/1/6, p 0.9658 |

## What the student knows without the video

```
{
 "s_blind_mean": 0.867,
 "s_blind_p_mean": 0.817,
 "topics_blind_all_right": 6,
 "unknown_items_per_topic": [
  2,
  0,
  1,
  2,
  0,
  0,
  1,
  0,
  1,
  0,
  1,
  1
 ],
 "s_visual_mean": null,
 "s_visual_mean_all": null,
 "s_static_mean": null,
 "s_static_mean_all": null,
 "s_frames_mean": 0.817,
 "s_frames_mean_all": 0.779,
 "s_visual_p_mean": null,
 "s_visual_p_mean_all": null,
 "s_frames_p_mean": 0.795,
 "s_frames_p_mean_all": 0.77,
 "s_static_p_mean": null,
 "s_static_p_mean_all": null,
 "tq_abstained_mean": null,
 "tq_abstained_mean_all": null
}
```
