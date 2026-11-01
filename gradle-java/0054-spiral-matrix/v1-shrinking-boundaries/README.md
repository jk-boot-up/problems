# 54. Spiral Matrix — v1: Shrinking boundaries

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/spiral-matrix/)

## Problem

Given an `m × n` matrix, return all of its elements in **spiral order** (clockwise, starting at the top-left).

**Example 1**
```
Input:  [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2**
```
Input:  [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

**Constraints**
* `1 <= m, n <= 10`, `-100 <= matrix[i][j] <= 100`

## Approach: Shrinking boundaries

> Peel the matrix layer by layer: walk the top row, right column, bottom row and left column, shrinking the bounds.

**Four boundaries.** Keep `top`, `bottom`, `left`, `right`. Walk the top row left→right (`top++`), the right column top→bottom
(`right--`), then, if rows remain, the bottom row right→left (`bottom--`), and if columns remain, the left column bottom→top
(`left++`). Repeat until the bounds cross.

* Time: **O(m·n)** — every cell is visited once.
* Space: **O(1)** — four bounds, apart from the output list.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0054/v1/SpiralMatrix.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0054/v1/SpiralMatrixTest.java` | JUnit 6 tests |
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
