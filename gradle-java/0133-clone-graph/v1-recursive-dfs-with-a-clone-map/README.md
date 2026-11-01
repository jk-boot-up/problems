# 133. Clone Graph — v1: Recursive DFS with a clone map

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/clone-graph/)

## Problem

Given a reference to a node in a connected undirected graph, return a **deep copy** of the graph. Each node has an integer `val`
(1..n, unique) and a list of `neighbors`.

**Example**
```
Input:  adjList = [[2,4],[1,3],[2,4],[1,3]]   (a square 1-2-3-4)
Output: an identical but separate graph
```

**Constraints**
* `0 <= n <= 100`; no repeated edges or self-loops; the graph is connected.

## Approach: Recursive DFS with a clone map

> clone(node) returns the existing copy if there is one, otherwise copies the node and clones its neighbours.

**DFS + memo map.** Register the copy in the map **before** recursing into neighbours; that is what stops cycles.

* Time: **O(V + E)** — each node is copied once and each edge followed once.
* Space: **O(V)** — the map plus the recursion stack.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0133/v1/CloneGraph.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0133/v1/CloneGraphTest.java` | JUnit 6 tests |
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

* [v2-bfs-with-a-clone-map](../v2-bfs-with-a-clone-map/README.md): BFS with a clone map (`O(V + E)` time, `O(V)` space)
