# 1631. Path With Minimum Effort — v1: Dijkstra on the max edge

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Shortest Path &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/path-with-minimum-effort/)

## Problem

In a grid of heights, a route goes from the top-left to the bottom-right, moving up/down/left/right. Its **effort** is the largest absolute
height difference between two consecutive cells. Return the minimum effort.

**Example**
```
[[1,2,2],[3,8,2],[5,3,5]] → 2
[[1,2,3],[3,8,4],[5,3,5]] → 1
```

**Constraints**
* `1 <= rows, cols <= 100`, `1 <= heights <= 10^6`

## Approach: Dijkstra on the max edge

> Dijkstra where a path's cost is its largest single step instead of the sum of steps.

**Minimax Dijkstra.** Extending a path can only keep or raise its maximum step, so the greedy order of Dijkstra still holds. Store
`effort[cell]`, pop the cell with the smallest effort, and relax each neighbour with `max(effort[cell], |height difference|)`.

* Time: **O(mn log(mn))**.
* Space: **O(mn)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1631/v1/PathWithMinimumEffort.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1631/v1/PathWithMinimumEffortTest.java` | JUnit 6 tests |
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
