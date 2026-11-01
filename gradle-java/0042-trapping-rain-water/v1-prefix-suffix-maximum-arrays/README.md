# 42. Trapping Rain Water — v1: Prefix / suffix maximum arrays

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/trapping-rain-water/)

## Problem

`height[i]` is the height of a bar of width 1. After it rains, how many units of water are trapped between the bars?

**Example 1**
```
Input:  height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

**Example 2**
```
Input:  height = [4,2,0,3,2,5]
Output: 9
```

**Constraints**
* `1 <= n <= 2 * 10^4`
* `0 <= height[i] <= 10^5`

## Approach: Prefix / suffix maximum arrays

> Precompute the tallest wall to the left and to the right of every bar.

**Precomputed maxima.** `leftMax[i]` = tallest bar in `0..i`, `rightMax[i]` = tallest in `i..n-1`.
Water at `i` = `min(leftMax[i], rightMax[i]) - height[i]`.

* Time: **O(n)** — three linear passes.
* Space: **O(n)** — two arrays of maxima.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0042/v1/TrappingRainWater.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0042/v1/TrappingRainWaterTest.java` | JUnit 6 tests |
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
