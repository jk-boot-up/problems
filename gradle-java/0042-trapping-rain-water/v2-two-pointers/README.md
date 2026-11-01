# 42. Trapping Rain Water — v2: Two pointers

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

## Approach: Two pointers

> Water above a bar is limited by the lower of the tallest walls on each side; two pointers always move the lower side.

**Two pointers.** Water at `i` is `min(maxLeft, maxRight) - height[i]`. Keep `l` and `r` at the ends with running `leftMax` and
`rightMax`. If `leftMax < rightMax`, the left side is the bottleneck for `l`, so its water is exactly `leftMax - height[l]`.
Add it and move `l` right. Otherwise do the same on the right.

* Time: **O(n)** — each bar is visited once.
* Space: **O(1)** — two pointers and two maxima.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0042/v2/TrappingRainWater.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0042/v2/TrappingRainWaterTest.java` | JUnit 6 tests |
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
  engine (use the 🔊 *Narration* button to turn the voice on or off; a female voice, Amy when installed, is preferred). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v1-prefix-suffix-maximum-arrays](../v1-prefix-suffix-maximum-arrays/README.md): Prefix / suffix maximum arrays (`O(n)` time, `O(n)` space)
