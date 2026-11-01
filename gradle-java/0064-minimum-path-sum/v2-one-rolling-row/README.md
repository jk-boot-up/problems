# 64. Minimum Path Sum — v2: One rolling row

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

## Approach: One rolling row

> Each cell's cheapest path comes from the cheaper of its top and left neighbours.

**Row DP.** `dp[j]` holds the best sum to the current row's column `j`. Going left to right, `dp[j] = grid[i][j] + min(dp[j] (from above),
dp[j-1] (from the left))`, with edge cells having only one choice.

* Time: **O(m·n)** — each cell once.
* Space: **O(n)** — one row.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0064/v2/MinimumPathSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0064/v2/MinimumPathSumTest.java` | JUnit 6 tests |
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

* [v1-full-dp-table](../v1-full-dp-table/README.md): Full DP table (`O(m·n)` time, `O(m·n)` space)
