# 64. Minimum Path Sum — v1: Full DP table

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-path-sum/)

## Problem

Given an `m × n` grid of non-negative numbers, find a path from the top-left to the bottom-right, moving only **right** or **down**,
that minimizes the sum of the numbers along it. Return that sum.

**Example**
```
[[1,3,1],
 [1,5,1],
 [4,2,1]]  → 7   (1 → 3 → 1 → 1 → 1)
```

**Constraints**
* `1 <= m, n <= 200`; `0 <= grid[i][j] <= 200`

## Approach: Full DP table

> dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]) in a full m × n table.

**2D table.** Same recurrence, storing every cell's best sum (also lets you rebuild the path).

* Time: **O(m·n)** — each cell once.
* Space: **O(m·n)** — the table.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0064/v1/MinimumPathSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0064/v1/MinimumPathSumTest.java` | JUnit 6 tests |
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

* [v2-one-rolling-row](../v2-one-rolling-row/README.md): One rolling row (`O(m·n)` time, `O(n)` space)
