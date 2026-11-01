# 1260. Shift 2D Grid — v1: Flat index rotation

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/shift-2d-grid/)

## Problem

One shift moves every element one place right in row-major order, with the last element wrapping to the top-left. Return the grid after `k`
shifts.

**Example**
```
grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1 → [[9,1,2],[3,4,5],[6,7,8]]
```

**Constraints**
* `1 <= m, n <= 50`; `0 <= k <= 100`

## Approach: Flat index rotation

> Treat the grid as one flat list of m·n cells and rotate it right by k.

**Index arithmetic.** Cell number `i` (row-major) moves to `(i + k) mod (m·n)`.

* Time: **O(m·n)** — each cell once.
* Space: **O(m·n)** — the output grid.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1260/v1/Shift2DGrid.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1260/v1/Shift2DGridTest.java` | JUnit 6 tests |
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
