# 42. Trapping Rain Water

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

## Solutions

Each version is a separate Gradle subproject, ordered from the simplest idea to the most efficient one.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Prefix / suffix maximum arrays | `O(n)` | `O(n)` | [▶ animation](v1/animation/index.html) |
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
