# 743. Network Delay Time — v1: Dijkstra with a heap

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/network-delay-time/)

## Problem

`times[i] = [u, v, w]` is a directed edge from node `u` to `v` taking `w` time. A signal starts at node `k`. Return the time for all `n`
nodes to receive it, or `-1` if some node never does.

**Example**
```
times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2 → 2
times = [[1,2,1]], n = 2, k = 2                  → -1
```

**Constraints**
* `1 <= k <= n <= 100`; `1 <= times.length <= 6000`; `0 <= w <= 100`

## Approach: Dijkstra with a heap

> Dijkstra from the source; the answer is the largest shortest-path distance (or -1 if a node is unreachable).

**Dijkstra.** Build adjacency lists. Pop the closest unsettled node from a min-heap, settle it, and relax its edges. The latest settle time is
the answer if all `n` nodes were settled.

* Time: **O(E log V)** — each edge may push one heap entry.
* Space: **O(V + E)** — graph, distances and heap.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0743/v1/NetworkDelayTime.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0743/v1/NetworkDelayTimeTest.java` | JUnit 6 tests |
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
