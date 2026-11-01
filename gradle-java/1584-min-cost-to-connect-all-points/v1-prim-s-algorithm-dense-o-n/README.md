# 1584. Min Cost to Connect All Points — v1: Prim's algorithm (dense O(n²))

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/min-cost-to-connect-all-points/)

## Problem

Connect all `points` (2-D, integer coordinates) so every pair is linked by some path; connecting two points costs their Manhattan distance
`|x1 - x2| + |y1 - y2|`. Return the minimum total cost.

**Example**
```
[[0,0],[2,2],[3,10],[5,2],[7,0]] → 20
[[3,12],[-2,5],[-4,1]]           → 18
```

**Constraints**
* `1 <= n <= 1000`; all points distinct.

## Approach: Prim's algorithm (dense O(n²))

> Prim's algorithm on the complete graph: repeatedly attach the cheapest point not yet connected.

**Array-based Prim.** Keep `best[i]`, the cheapest edge from point `i` into the growing tree. Each round, pick the unconnected point with the
smallest `best`, add its cost, and lower `best[j]` for every other unconnected point through it. A dense graph makes this O(n²) version
faster than a heap.

* Time: **O(n²)** — n rounds, each scanning all points.
* Space: **O(n)** — the best and visited arrays.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1584/v1/MinCostConnectPoints.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1584/v1/MinCostConnectPointsTest.java` | JUnit 6 tests |
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
