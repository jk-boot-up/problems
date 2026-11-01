# 778. Swim in Rising Water — v1: Min-heap on path maximum

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/swim-in-rising-water/)

## Problem

`grid[i][j]` is the elevation of a cell in an `n × n` grid. At time `t` the water level is `t`, and you can swim between adjacent cells whose
elevations are both at most `t`. Return the least time to go from the top-left to the bottom-right.

**Example**
```
[[0,2],[1,3]] → 3
```

**Constraints**
* `1 <= n <= 50`; values are a permutation of `0 .. n²-1`.

## Approach: Min-heap on path maximum

> Dijkstra where a path's cost is its highest cell: always expand the lowest reachable cell next.

**Minimax Dijkstra.** A path's cost is the maximum elevation on it. Pop the cell with the smallest current maximum from a heap, push its
unvisited neighbours with cost `max(current, elevation)`. The first time the target is popped, its cost is the answer.

* Time: **O(n² log n)** — each cell is pushed once into a heap of size up to n².
* Space: **O(n²)** — visited grid and heap.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0778/v1/SwimInRisingWater.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0778/v1/SwimInRisingWaterTest.java` | JUnit 6 tests |
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
