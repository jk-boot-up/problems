# 63. Unique Paths II — v1: One rolling row

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/unique-paths-ii/)

## Problem

A robot starts at the top-left of an `m × n` grid and moves only **right** or **down** to the bottom-right. Cells with `1` are
obstacles. Return the number of unique paths (it fits in 32 bits).

**Example**
```
[[0,0,0],
 [0,1,0],
 [0,0,0]] → 2
```

**Constraints**
* `1 <= m, n <= 100`

## Approach: One rolling row

> Paths into a cell = paths from above + paths from the left, and an obstacle cell has zero paths.

**Counting DP.** `dp[j]` is the number of ways into column `j` of the current row: `dp[j] = 0` on an obstacle, otherwise
`dp[j] += dp[j - 1]` (above is what is already in `dp[j]`, plus the left neighbour).

* Time: **O(m·n)** — each cell once.
* Space: **O(n)** — one row.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0063/v1/UniquePathsII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0063/v1/UniquePathsIITest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
