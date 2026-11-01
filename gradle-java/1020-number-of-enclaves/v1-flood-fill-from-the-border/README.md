# 1020. Number of Enclaves — v1: Flood fill from the border

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph DFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-enclaves/)

## Problem

In a grid of `0` (sea) and `1` (land), a move goes to a 4-adjacent land cell or off the grid edge. Return the number of land cells from
which you **cannot** walk off the grid.

**Example**
```
0 0 0 0
1 0 1 0
0 1 1 0      → 3
0 0 0 0
```

**Constraints**
* `1 <= m, n <= 500`

## Approach: Flood fill from the border

> Sink every land cell reachable from the border; whatever land is left cannot walk off the grid.

**Reverse the question.** A land cell can escape iff it is connected to a border land cell. Flood fill (iteratively, with a stack) from
every border land cell, marking cells as visited. Count the land cells that were never reached.

* Time: **O(mn)**.
* Space: **O(mn)** — the visited marks and stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1020/v1/NumberOfEnclaves.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1020/v1/NumberOfEnclavesTest.java` | JUnit 6 tests |
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
