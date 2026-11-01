# 931. Minimum Falling Path Sum — v1: Row-by-row DP

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-falling-path-sum/)

## Problem

In an `n × n` matrix, a **falling path** starts anywhere in the first row and moves down one row at a time, to the cell directly below
or diagonally left/right. Return the minimum sum of a falling path.

**Example**
```
[[2,1,3],[6,5,4],[7,8,9]] → 13   (1 → 5 → 7  or  1 → 4 → 8)
[[-19,57],[-40,-5]]       → -59
```

**Constraints**
* `1 <= n <= 100`, `-100 <= matrix[i][j] <= 100`

## Approach: Row-by-row DP

> Row by row, each cell adds the cheapest of the up to three cells above it.

**DP.** `best[c]` is the cheapest path ending at column `c` of the current row. For the next row, each cell adds
`min(best[c-1], best[c], best[c+1])` (where they exist). The answer is the minimum of the last row.

* Time: **O(n²)**.
* Space: **O(n)** — two rows.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0931/v1/MinimumFallingPathSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0931/v1/MinimumFallingPathSumTest.java` | JUnit 6 tests |
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
