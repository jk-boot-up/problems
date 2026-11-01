# 73. Set Matrix Zeroes — v2: Markers in row/column 0

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

## Approach: Markers in row/column 0

> Use the first row and first column as the zero markers, with two flags for the first row and column themselves.

**Reuse the first row and column.** First remember whether row 0 and column 0 contain a zero. Then, for every zero at `(i, j)`
with `i, j >= 1`, mark `matrix[i][0] = 0` and `matrix[0][j] = 0`. Zero every inner cell whose row or column is marked. Finally
zero row 0 and column 0 if their flags are set.

* Time: **O(m·n)** — a few passes over the matrix.
* Space: **O(1)** — two boolean flags.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0073/v2/SetMatrixZeroes.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0073/v2/SetMatrixZeroesTest.java` | JUnit 6 tests |
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

* [v1-row-and-column-sets](../v1-row-and-column-sets/README.md): Row and column sets (`O(m·n)` time, `O(m + n)` space)
