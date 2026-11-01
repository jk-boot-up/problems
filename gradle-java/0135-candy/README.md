# 135. Candy

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/candy/)

## Problem

`n` children stand in a line; `ratings[i]` is child `i`'s rating. Give out candies so that:
* every child gets at least one candy, and
* a child with a higher rating than a neighbour gets more candies than that neighbour.

Return the minimum total number of candies.

**Example 1**
```
Input:  ratings = [1,0,2]
Output: 5   (2, 1, 2)
```

**Example 2**
```
Input:  ratings = [1,2,2]
Output: 4   (1, 2, 1)
```

**Constraints**
* `1 <= n <= 2 * 10^4`
* `0 <= ratings[i] <= 2 * 10^4`

## Solutions

One solution, in subproject `v1`.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Optimal | `O(n)` | `O(n)` | [▶ animation](v1/animation/index.html) |

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
