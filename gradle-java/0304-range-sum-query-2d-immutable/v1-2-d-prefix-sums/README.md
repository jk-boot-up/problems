# 304. Range Sum Query 2D - Immutable — v1: 2-D prefix sums

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Prefix Sum &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/range-sum-query-2d-immutable/)

## Problem

Implement `NumMatrix`:

* `NumMatrix(int[][] matrix)`
* `int sumRegion(int row1, int col1, int row2, int col2)` — the sum of the rectangle with corners `(row1, col1)` and `(row2, col2)`,
  inclusive, in O(1).

**Example**
```
matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
sumRegion(2,1,4,3) → 8, sumRegion(1,1,2,2) → 11, sumRegion(1,2,2,4) → 12
```

**Constraints**
* `1 <= m, n <= 200`, up to `10^4` queries

## Approach: 2-D prefix sums

> 2-D prefix sums: a rectangle is one big prefix minus two strips plus the corner counted twice.

**Inclusion–exclusion.** `P[r][c]` is the sum of the top-left `r × c` block, built as
`P[r][c] = M[r-1][c-1] + P[r-1][c] + P[r][c-1] - P[r-1][c-1]`. A query is
`P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]`.

* Time: **O(1)** — per query, after O(mn) setup.
* Space: **O(mn)** — the prefix table.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0304/v1/NumMatrix.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0304/v1/NumMatrixTest.java` | JUnit 6 tests |
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
