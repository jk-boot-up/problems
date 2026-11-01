# 785. Is Graph Bipartite?

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

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bfs-two-colouring](v1-bfs-two-colouring/README.md) | BFS two-colouring | `O(V + E)` | `O(V)` | [▶ animation](v1-bfs-two-colouring/animation/index.html) |
