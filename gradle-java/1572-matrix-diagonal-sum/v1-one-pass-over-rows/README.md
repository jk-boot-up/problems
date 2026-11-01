# 1572. Matrix Diagonal Sum — v1: One pass over rows

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/matrix-diagonal-sum/)

## Problem

Return the sum of a square matrix's primary diagonal and secondary diagonal, counting the shared centre element (odd `n`) only once.

**Example**
```
[[1,2,3],[4,5,6],[7,8,9]] → 25   (1 + 5 + 9 + 3 + 7)
[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]] → 8
```

**Constraints**
* `1 <= n <= 100`

## Approach: One pass over rows

> Add mat[i][i] and mat[i][n−1−i] for each row; the centre cell of an odd matrix is counted once.

**Both diagonals per row.** Row `i` contributes `mat[i][i]` and `mat[i][n-1-i]`; when those are the same cell (`i == n-1-i`), add it once.

* Time: **O(n)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1572/v1/MatrixDiagonalSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1572/v1/MatrixDiagonalSumTest.java` | JUnit 6 tests |
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
