# 240. Search a 2D Matrix II — v1: Staircase from the top-right

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/search-a-2d-matrix-ii/)

## Problem

Each row of the `m × n` matrix is sorted left to right and each column top to bottom. Return `true` if `target` is in the matrix.

**Example**
```
[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target 5 → true,  target 20 → false
```

**Constraints**
* `1 <= m, n <= 300`

## Approach: Staircase from the top-right

> Start at the top-right corner: moving left decreases, moving down increases, so each step discards a row or a column.

**Staircase search.** At `(r, c)` starting from the top-right: if the value is larger than the target, the whole column below is larger
too, so `c--`; if smaller, the whole row to the left is smaller, so `r++`.

* Time: **O(m + n)** — each step removes a row or a column.
* Space: **O(1)** — two indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0240/v1/Search2DMatrixII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0240/v1/Search2DMatrixIITest.java` | JUnit 6 tests |
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
