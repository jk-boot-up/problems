# 1091. Shortest Path in Binary Matrix — v1: 8-direction BFS

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

## Problem

In an `n × n` grid of `0` (open) and `1` (blocked), return the number of cells on the shortest path from the top-left to the
bottom-right moving in any of the 8 directions through open cells, or `-1`.

**Example**
```
[[0,1],[1,0]]                 → 2
[[0,0,0],[1,1,0],[1,1,0]]     → 4
[[1,0,0],[1,1,0],[1,1,0]]     → -1
```

**Constraints**
* `1 <= n <= 100`

## Approach: 8-direction BFS

> BFS over the 8-connected open cells from the top-left; the first time it reaches the bottom-right is the shortest path.

**BFS.** Every move costs the same, so breadth-first search finds the shortest path. Start from `(0,0)` with length 1 (if it is open), mark
cells when they are queued, and explore all 8 neighbours. The length when `(n-1, n-1)` is dequeued is the answer.

* Time: **O(n²)** — each cell once, 8 neighbours.
* Space: **O(n²)** — the queue and marks.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1091/v1/ShortestPathBinaryMatrix.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1091/v1/ShortestPathBinaryMatrixTest.java` | JUnit 6 tests |
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
