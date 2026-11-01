# 42. Trapping Rain Water — v1: Prefix / suffix maximum arrays

[← Problem statement](../README.md)

> Precompute the tallest wall to the left and to the right of every bar.

## Approach

**Precomputed maxima.** `leftMax[i]` = tallest bar in `0..i`, `rightMax[i]` = tallest in `i..n-1`.
Water at `i` = `min(leftMax[i], rightMax[i]) - height[i]`.

* Time: **O(n)** — three linear passes.
* Space: **O(n)** — two arrays of maxima.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0042/v1/TrappingRainWater.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0042/v1/TrappingRainWaterTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v1:test`.
