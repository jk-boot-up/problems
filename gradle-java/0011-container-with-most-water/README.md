# 11. Container With Most Water

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

## Solutions

Each version is a separate Gradle subproject, ordered from the simplest idea to the most efficient one.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Brute force | `O(n²)` | `O(1)` | [▶ animation](v1/animation/index.html) |
| [v2](v2/README.md) | Two pointers | `O(n)` | `O(1)` | [▶ animation](v2/animation/index.html) |

## Build and test

Only a JDK is needed to start Gradle; JDK 25 is downloaded automatically if it is missing.

```bash
./gradlew test          # every version
./gradlew :v1:test      # one version
```

## Animation

Open `vN/animation/index.html` in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech engine
  (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared across versions.

Use the header to switch between Light, Medium and Dark themes and between solution versions.
