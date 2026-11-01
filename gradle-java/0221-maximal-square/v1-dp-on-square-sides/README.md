# 221. Maximal Square — v1: DP on square sides

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximal-square/)

## Problem

Given an `m × n` binary matrix of `'0'` and `'1'`, return the **area** of the largest square containing only `'1'`s.

**Example**
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0   → 4
```

**Constraints**
* `1 <= m, n <= 300`

## Approach: DP on square sides

> side[i][j] = 1 + min(top, left, top-left): a square is limited by its smallest neighbouring square.

**Side lengths.** `side[i][j]` is the largest all-ones square whose bottom-right corner is `(i, j)`. For a `'1'` it is
`1 + min(side[i-1][j], side[i][j-1], side[i-1][j-1])`; for a `'0'` it is 0. Track the maximum side and return its square.

* Time: **O(m·n)** — each cell once.
* Space: **O(m·n)** — the side table (one row would also do).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0221/v1/MaximalSquare.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0221/v1/MaximalSquareTest.java` | JUnit 6 tests |
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
