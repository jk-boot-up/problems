# 994. Rotting Oranges — v1: Multi-source BFS

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/rotting-oranges/)

## Problem

In a grid, `0` is empty, `1` a fresh orange and `2` a rotten one. Every minute, fresh oranges next to (4-directionally) a rotten one
become rotten. Return the minutes until no fresh orange remains, or `-1` if that never happens.

**Example**
```
[[2,1,1],[1,1,0],[0,1,1]] → 4
[[2,1,1],[0,1,1],[1,0,1]] → -1
[[0,2]]                   → 0
```

**Constraints**
* `1 <= m, n <= 10`

## Approach: Multi-source BFS

> Multi-source BFS: all rotten oranges spread together, one minute per BFS level.

**BFS from every rotten orange at once.** Queue all rotten cells and count fresh ones. Each BFS level is one minute: rot the fresh
neighbours of the current level. At the end, any fresh orange left means `-1`.

* Time: **O(m·n)** — each cell is processed once.
* Space: **O(m·n)** — the queue.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0994/v1/RottingOranges.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0994/v1/RottingOrangesTest.java` | JUnit 6 tests |
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
