# 790. Domino and Tromino Tiling — v1: Linear recurrence

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/domino-and-tromino-tiling/)

## Problem

Count the ways to tile a `2 × n` board with `2 × 1` dominoes and L-shaped trominoes (both may be rotated). Return the count modulo
`10^9 + 7`.

**Example**
```
n = 3 → 5,   n = 1 → 1
```

**Constraints**
* `1 <= n <= 1000`

## Approach: Linear recurrence

> Counting tilings of a 2×n board satisfies f(n) = 2·f(n−1) + f(n−3).

**Recurrence.** Tracking full and half-filled boards leads to `f(n) = 2·f(n-1) + f(n-3)` with `f(0) = 1, f(1) = 1, f(2) = 2`. Compute it
iteratively modulo `10^9 + 7` using `long`.

* Time: **O(n)** — one loop.
* Space: **O(n)** — the table (three values would also do).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0790/v1/DominoTrominoTiling.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0790/v1/DominoTrominoTilingTest.java` | JUnit 6 tests |
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
