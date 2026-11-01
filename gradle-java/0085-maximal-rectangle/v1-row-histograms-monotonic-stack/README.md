# 85. Maximal Rectangle — v1: Row histograms + monotonic stack

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximal-rectangle/)

## Problem

Given a binary matrix of `'0'` and `'1'`, return the area of the largest rectangle containing only `'1'`s.

**Example**
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0   → 6
```

**Constraints**
* `1 <= rows, cols <= 200`

## Approach: Row histograms + monotonic stack

> Each row turns the matrix above it into a histogram; reuse the largest-rectangle-in-histogram stack per row.

**Histogram per row.** `heights[c]` counts consecutive `'1'`s ending at the current row in column `c` (reset to 0 on `'0'`). After each
row, the largest rectangle in that histogram is the best rectangle whose bottom edge is this row.

* Time: **O(m·n)** — each row costs O(n) for the stack.
* Space: **O(n)** — the heights and the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0085/v1/MaximalRectangle.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0085/v1/MaximalRectangleTest.java` | JUnit 6 tests |
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
