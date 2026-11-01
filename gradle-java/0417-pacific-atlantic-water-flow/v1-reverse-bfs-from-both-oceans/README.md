# 417. Pacific Atlantic Water Flow — v1: Reverse BFS from both oceans

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/)

## Problem

Rain flows from a cell to a 4-directional neighbour of **equal or lower** height. The Pacific touches the top and left edges, the
Atlantic the bottom and right edges. Return all cells from which water can reach **both** oceans.

**Example**
```
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
→ [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

**Constraints**
* `1 <= m, n <= 200`

## Approach: Reverse BFS from both oceans

> Flow backwards: climb uphill from each ocean's border; cells reached from both oceans are the answer.

**Reverse the flow.** From every Pacific border cell, BFS to neighbours that are **higher or equal** (water could flow down from them);
do the same for the Atlantic. Return the cells marked by both searches.

* Time: **O(m·n)** — two BFS passes.
* Space: **O(m·n)** — two visited grids.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0417/v1/PacificAtlanticWaterFlow.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0417/v1/PacificAtlanticWaterFlowTest.java` | JUnit 6 tests |
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
