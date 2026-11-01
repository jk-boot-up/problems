# 73. Set Matrix Zeroes — v1: Row and column sets

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/set-matrix-zeroes/)

## Problem

Given an `m × n` integer matrix, if a cell is `0`, set its entire row and column to `0`. Do it **in place**.

**Example 1**
```
Input:  [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

**Example 2**
```
Input:  [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

**Constraints**
* `1 <= m, n <= 200`, `-2^31 <= matrix[i][j] <= 2^31 - 1`

**Follow-up:** a constant-space solution.

## Approach: Row and column sets

> Record which rows and columns contain a zero, then zero them in a second pass.

**Two boolean arrays.** `zeroRow[i]` and `zeroCol[j]` are set for every zero. A second pass zeroes a cell if its row or column is flagged.

* Time: **O(m·n)** — two passes.
* Space: **O(m + n)** — the two flag arrays.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0073/v1/SetMatrixZeroes.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0073/v1/SetMatrixZeroesTest.java` | JUnit 6 tests |
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

* [v2-markers-in-row-column-0](../v2-markers-in-row-column-0/README.md): Markers in row/column 0 (`O(m·n)` time, `O(1)` space)
