# 11. Container With Most Water — v1: Brute force

[← Problem statement](../README.md)

> Measure every pair of lines.

## Approach

**All pairs.** For every `i < j`, the area is `min(h[i], h[j]) * (j - i)`; keep the maximum.

* Time: **O(n²)** — about n²/2 pairs.
* Space: **O(1)** — the best area.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0011/v1/ContainerWithMostWater.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0011/v1/ContainerWithMostWaterTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
