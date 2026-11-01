# 62. Unique Paths — v2: One rolling row

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/unique-paths/)

## Problem

A robot on an `m × n` grid starts at the top-left and moves only right or down. How many unique paths reach the bottom-right corner?

**Example**
```
m = 3, n = 7 → 28,   m = 3, n = 2 → 3
```

**Constraints**
* `1 <= m, n <= 100`; the answer fits in 32 bits.

## Approach: One rolling row

> Paths into a cell = paths from above + paths from the left.

**Row DP.** Start with a row of 1s (one way along the top edge). For each next row, `dp[j] += dp[j - 1]`.

* Time: **O(m·n)** — each cell once.
* Space: **O(n)** — one row.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0062/v2/UniquePaths.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0062/v2/UniquePathsTest.java` | JUnit 6 tests |
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

* [v1-combinatorics](../v1-combinatorics/README.md): Combinatorics (`O(min(m, n))` time, `O(1)` space)
