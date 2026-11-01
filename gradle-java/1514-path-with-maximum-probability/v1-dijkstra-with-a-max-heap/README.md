# 1514. Path with Maximum Probability — v1: Dijkstra with a max-heap

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Shortest Path &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/path-with-maximum-probability/)

## Problem

An undirected graph has `n` nodes; edge `edges[i]` succeeds with probability `succProb[i]`. Return the highest probability of a path from
`start` to `end` (the product of its edges), or 0 if there is none.

**Example**
```
n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2 → 0.25
n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2 → 0.3
```

**Constraints**
* `2 <= n <= 10^4`, up to `2 * 10^4` edges, `0 <= succProb[i] <= 1`

## Approach: Dijkstra with a max-heap

> Dijkstra works for products of probabilities in [0, 1]: a path can only get less likely as it grows.

**Dijkstra, maximising.** Multiplying by a probability never increases a value, just as adding a non-negative weight never decreases a
distance. So the node with the highest known probability is final when it is popped from a max-heap. Relax each neighbour with
`best[u] * p`; skip stale heap entries.

* Time: **O((V + E) log V)**.
* Space: **O(V + E)** — adjacency and heap.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1514/v1/MaxProbabilityPath.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1514/v1/MaxProbabilityPathTest.java` | JUnit 6 tests |
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
