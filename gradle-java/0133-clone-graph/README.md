# 133. Clone Graph

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

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-recursive-dfs-with-a-clone-map](v1-recursive-dfs-with-a-clone-map/README.md) | Recursive DFS with a clone map | `O(V + E)` | `O(V)` | [▶ animation](v1-recursive-dfs-with-a-clone-map/animation/index.html) |
| [v2-bfs-with-a-clone-map](v2-bfs-with-a-clone-map/README.md) | BFS with a clone map | `O(V + E)` | `O(V)` | [▶ animation](v2-bfs-with-a-clone-map/animation/index.html) |
