# 200. Number of Islands — v2: DFS flood fill

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-islands/)

## Problem

Given an `m × n` grid of `'1'` (land) and `'0'` (water), count the **islands**. An island is a group of land cells connected
horizontally or vertically; the grid is surrounded by water.

**Example 1**
```
Input:
11110
11010
11000
00000
Output: 1
```

**Example 2**
```
Input:
11000
11000
00100
00011
Output: 3
```

**Constraints**
* `1 <= m, n <= 300`

## Approach: DFS flood fill

> Scan the grid; each unvisited land cell starts a new island, which a flood fill sinks completely.

**Flood fill.** For each `'1'`, count one island and run DFS to turn the whole connected region into `'0'`, so it is never counted
again. (Iterative DFS with an explicit stack avoids deep recursion on large islands.)

* Time: **O(m·n)** — each cell is visited a constant number of times.
* Space: **O(m·n)** — the stack in the worst case (one giant island).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0200/v2/NumberOfIslands.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0200/v2/NumberOfIslandsTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v1-bfs-flood-fill](../v1-bfs-flood-fill/README.md): BFS flood fill (`O(m·n)` time, `O(min(m, n))` space)
