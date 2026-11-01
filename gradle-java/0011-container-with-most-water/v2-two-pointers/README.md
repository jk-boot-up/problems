# 11. Container With Most Water — v2: Two pointers

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

## Approach: Two pointers

> Start with the widest container and always move the shorter wall inward: that is the only move that might help.

**Two pointers.** Start with `l = 0` and `r = n - 1` (maximum width). The area is limited by the shorter wall.
Moving the taller wall inward can only shrink the width without raising the limit, so always move the **shorter** one.

* Time: **O(n)** — each step moves one pointer inward.
* Space: **O(1)** — two pointers and the best area.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0011/v2/ContainerWithMostWater.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0011/v2/ContainerWithMostWaterTest.java` | JUnit 6 tests |
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

* [v1-brute-force](../v1-brute-force/README.md): Brute force (`O(n²)` time, `O(1)` space)
