# 695. Max Area of Island — v1: DFS flood fill

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/max-area-of-island/)

## Problem

In a binary grid, an island is a group of `1`s connected 4-directionally. Return the area of the largest island (0 if none).

**Example**
```
A grid with islands of sizes 1, 3, 4 and 6 → 6
```

**Constraints**
* `1 <= m, n <= 50`

## Approach: DFS flood fill

> Flood-fill each island once, counting its cells, and keep the largest count.

**Flood fill.** For each unvisited `1`, run DFS with an explicit stack, zeroing cells as they are counted.

* Time: **O(m·n)** — each cell is visited once.
* Space: **O(m·n)** — the stack in the worst case.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0695/v1/MaxAreaOfIsland.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0695/v1/MaxAreaOfIslandTest.java` | JUnit 6 tests |
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
