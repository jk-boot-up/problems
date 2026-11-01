# 42. Trapping Rain Water — v2: Two pointers

[← Problem statement](../README.md)

> Water above a bar is limited by the lower of the tallest walls on each side; two pointers always move the lower side.

## Approach

**Two pointers.** Water at `i` is `min(maxLeft, maxRight) - height[i]`. Keep `l` and `r` at the ends with running `leftMax` and
`rightMax`. If `leftMax < rightMax`, the left side is the bottleneck for `l`, so its water is exactly `leftMax - height[l]`.
Add it and move `l` right. Otherwise do the same on the right.

* Time: **O(n)** — each bar is visited once.
* Space: **O(1)** — two pointers and two maxima.

## Files

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0042/v2/TrappingRainWater.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0042/v2/TrappingRainWaterTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

Run the tests with `../gradlew :v2:test`.
