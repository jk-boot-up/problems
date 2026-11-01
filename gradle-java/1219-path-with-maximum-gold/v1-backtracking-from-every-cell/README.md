# 1219. Path with Maximum Gold — v1: Backtracking from every cell

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/path-with-maximum-gold/)

## Problem

Each grid cell holds some gold (0 means empty). You may start and stop at any cell with gold, move up/down/left/right, never visit a
cell twice and never enter an empty cell. Return the most gold you can collect.

**Example**
```
[[0,6,0],[5,8,7],[0,9,0]] → 24   (9 → 8 → 7)
[[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]] → 28
```

**Constraints**
* `1 <= m, n <= 15`, at most 25 cells contain gold

## Approach: Backtracking from every cell

> Start a backtracking walk from every gold cell, temporarily emptying cells on the current path.

**DFS with undo.** From a cell, take its gold, set it to 0 so the path cannot reuse it, try the four neighbours, then restore it. Run this
from every gold cell and keep the best total.

* Time: **O(k · 3ᵏ)** — `k <= 25` gold cells; after the first move each step has at most 3 new directions.
* Space: **O(k)** — recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1219/v1/PathWithMaximumGold.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1219/v1/PathWithMaximumGoldTest.java` | JUnit 6 tests |
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
