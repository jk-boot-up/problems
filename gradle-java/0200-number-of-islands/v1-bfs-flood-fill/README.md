# 200. Number of Islands — v1: BFS flood fill

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

## Approach: BFS flood fill

> Same scan, but explore each island breadth-first with a queue.

**Queue instead of stack.** Each new land cell is enqueued and marked; neighbours are explored level by level.

* Time: **O(m·n)** — each cell is processed once.
* Space: **O(min(m, n))** — the BFS frontier of a grid stays roughly as wide as its smaller side.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0200/v1/NumberOfIslands.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0200/v1/NumberOfIslandsTest.java` | JUnit 6 tests |
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

* [v2-dfs-flood-fill](../v2-dfs-flood-fill/README.md): DFS flood fill (`O(m·n)` time, `O(m·n)` space)
