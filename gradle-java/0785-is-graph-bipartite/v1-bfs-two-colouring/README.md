# 785. Is Graph Bipartite? — v1: BFS two-colouring

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/is-graph-bipartite/)

## Problem

`graph[u]` lists the neighbours of node `u` in an undirected graph (possibly disconnected). Return `true` if the nodes can be split into two
sets so that every edge joins nodes from different sets.

**Example**
```
[[1,2,3],[0,2],[0,1,3],[0,2]] → false
[[1,3],[0,2],[1,3],[0,2]]     → true
```

**Constraints**
* `1 <= n <= 100`

## Approach: BFS two-colouring

> Two-colour the graph with BFS; an edge between two nodes of the same colour means it is not bipartite.

**Colouring.** For every uncoloured node, start a BFS, colouring it 1 and each neighbour the opposite colour. A neighbour that already has
the same colour proves an odd cycle.

* Time: **O(V + E)** — each node and edge once.
* Space: **O(V)** — colours and queue.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0785/v1/IsGraphBipartite.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0785/v1/IsGraphBipartiteTest.java` | JUnit 6 tests |
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
