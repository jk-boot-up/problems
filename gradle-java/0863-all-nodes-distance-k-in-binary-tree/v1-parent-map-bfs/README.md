# 863. All Nodes Distance K in Binary Tree — v1: Parent map + BFS

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

## Problem

Given the root of a binary tree, a `target` node in it and an integer `k`, return the values of all nodes exactly `k` edges away from
`target`, in any order.

**Example**
```
root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2 → [7,4,1]
root = [1], target = 1, k = 3 → []
```

**Constraints**
* `1 <= n <= 500`, unique values, `0 <= k <= 1000`

## Approach: Parent map + BFS

> Record each node's parent, then the tree is an undirected graph; BFS k steps from the target.

**Make it a graph.** One DFS stores each node's parent in a `MyHashMap` (keyed by node identity). Now every node has up to three
neighbours: left, right and parent. Run BFS from `target` for `k` levels, with a visited set so no node is used twice; the last level is
the answer.

* Time: **O(n)**.
* Space: **O(n)** — the parent map, visited set and queue.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0863/v1/DistanceK.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0863/v1/DistanceKTest.java` | JUnit 6 tests |
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
