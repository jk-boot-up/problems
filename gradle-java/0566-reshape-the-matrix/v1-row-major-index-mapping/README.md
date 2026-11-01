# 566. Reshape the Matrix — v1: Row-major index mapping

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reshape-the-matrix/)

## Problem

Reshape an `m × n` matrix into `r × c`, filling row by row in the original row-major order. If `r × c != m × n`, return the original matrix.

**Example**
```
mat = [[1,2],[3,4]], r = 1, c = 4 → [[1,2,3,4]]
mat = [[1,2],[3,4]], r = 2, c = 4 → [[1,2],[3,4]]
```

**Constraints**
* `1 <= m, n <= 100`

## Approach: Row-major index mapping

> Read cells in row-major order and write them in the same order into an r × c matrix.

**Flat index.** Cell number `k` lives at `(k / n, k % n)` in the input and at `(k / c, k % c)` in the output.

* Time: **O(m·n)** — each cell once.
* Space: **O(m·n)** — the new matrix.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0566/v1/ReshapeMatrix.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0566/v1/ReshapeMatrixTest.java` | JUnit 6 tests |
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
