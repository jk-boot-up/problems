# 1091. Shortest Path in Binary Matrix

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

## Problem

In an `n × n` grid of `0` (open) and `1` (blocked), return the number of cells on the shortest path from the top-left to the
bottom-right moving in any of the 8 directions through open cells, or `-1`.

**Example**
```
[[0,1],[1,0]]                 → 2
[[0,0,0],[1,1,0],[1,1,0]]     → 4
[[1,0,0],[1,1,0],[1,1,0]]     → -1
```

**Constraints**
* `1 <= n <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-8-direction-bfs](v1-8-direction-bfs/README.md) | 8-direction BFS | `O(n²)` | `O(n²)` | [▶ animation](v1-8-direction-bfs/animation/index.html) |
