# 11. Container With Most Water — v1: Brute force

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/container-with-most-water/)

## Problem

`height[i]` is the height of a vertical line at position `i`. Choose two lines that, together with the x-axis, form a container
holding the most water. Return that maximum amount: `min(height[i], height[j]) × (j - i)`.

**Example 1**
```
Input:  height = [1,8,6,2,5,4,8,3,7]
Output: 49   (lines at 1 and 8: min(8,7) × 7)
```

**Example 2**
```
Input:  height = [1,1]
Output: 1
```

**Constraints**
* `2 <= n <= 10^5`
* `0 <= height[i] <= 10^4`

## Approach: Brute force

> Measure every pair of lines.

**All pairs.** For every `i < j`, the area is `min(h[i], h[j]) * (j - i)`; keep the maximum.

* Time: **O(n²)** — about n²/2 pairs.
* Space: **O(1)** — the best area.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0011/v1/ContainerWithMostWater.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0011/v1/ContainerWithMostWaterTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

## Build and test

This folder is a standalone Gradle 9.8.2 project. Only a JDK is needed to start Gradle; JDK 25 is downloaded
automatically if it is missing.

```bash
./gradlew test
```

## Animation

Open [`animation/index.html`](animation/index.html) in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech
  engine (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v2-two-pointers](../v2-two-pointers/README.md): Two pointers (`O(n)` time, `O(1)` space)
