# 133. Clone Graph — v2: BFS with a clone map

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

## Approach: BFS with a clone map

> Map every original node to its copy the first time you see it; the map also stops cycles from looping forever.

**BFS + `MyHashMap<original, copy>`.** Copy the start node and enqueue it. For each dequeued node, look at its neighbours: create a copy
the first time a neighbour is seen (and enqueue it), then add the neighbour's copy to the current copy's neighbour list.

* Time: **O(V + E)** — each node and edge is processed once.
* Space: **O(V)** — the map and the queue.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0133/v2/CloneGraph.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0133/v2/CloneGraphTest.java` | JUnit 6 tests |
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

* [v1-recursive-dfs-with-a-clone-map](../v1-recursive-dfs-with-a-clone-map/README.md): Recursive DFS with a clone map (`O(V + E)` time, `O(V)` space)
