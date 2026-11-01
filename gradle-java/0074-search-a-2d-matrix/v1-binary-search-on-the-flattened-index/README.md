# 74. Search a 2D Matrix — v1: Binary search on the flattened index

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/search-a-2d-matrix/)

## Problem

In an `m × n` matrix, each row is sorted ascending and the first value of each row is greater than the last value of the previous row.
Return `true` if `target` is in the matrix. Run in O(log(m·n)).

**Example**
```
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]:  target 3 → true,  target 13 → false
```

**Constraints**
* `1 <= m, n <= 100`

## Approach: Binary search on the flattened index

> Rows are sorted and each row starts after the previous one ends, so the matrix is one sorted list in disguise.

**One virtual array.** Index `k` in `[0, m·n)` maps to `matrix[k / n][k % n]`. Run an ordinary binary search on `k`.

* Time: **O(log(m·n))** — standard binary search over m·n cells.
* Space: **O(1)** — a few indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0074/v1/Search2DMatrix.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0074/v1/Search2DMatrixTest.java` | JUnit 6 tests |
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
