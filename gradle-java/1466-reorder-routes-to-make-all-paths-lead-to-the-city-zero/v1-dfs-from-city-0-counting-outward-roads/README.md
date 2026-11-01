# 1466. Reorder Routes to Make All Paths Lead to the City Zero — v1: DFS from city 0 counting outward roads

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)

## Problem

`n` cities form a tree of `n - 1` one-way roads `connections[i] = [a, b]` (from `a` to `b`). Return the minimum number of roads to reverse
so that every city can reach city 0.

**Example**
```
n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]] → 3
n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]       → 2
```

**Constraints**
* `2 <= n <= 5 * 10^4`

## Approach: DFS from city 0 counting outward roads

> Walk outward from city 0 ignoring direction; every road that points away from 0 must be flipped.

**Signed adjacency.** Store each road in both directions, tagged `1` if it is an original road (pointing away from the walk) and `0` if it is
the reverse. DFS from 0: whenever we cross an original road outward, it points away from 0 and must be flipped.

* Time: **O(n)** — each road is seen twice.
* Space: **O(n)** — the adjacency lists.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1466/v1/ReorderRoutes.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1466/v1/ReorderRoutesTest.java` | JUnit 6 tests |
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
