# 994. Rotting Oranges

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/rotting-oranges/)

## Problem

In a grid, `0` is empty, `1` a fresh orange and `2` a rotten one. Every minute, fresh oranges next to (4-directionally) a rotten one
become rotten. Return the minutes until no fresh orange remains, or `-1` if that never happens.

**Example**
```
[[2,1,1],[1,1,0],[0,1,1]] → 4
[[2,1,1],[0,1,1],[1,0,1]] → -1
[[0,2]]                   → 0
```

**Constraints**
* `1 <= m, n <= 10`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-multi-source-bfs](v1-multi-source-bfs/README.md) | Multi-source BFS | `O(m·n)` | `O(m·n)` | [▶ animation](v1-multi-source-bfs/animation/index.html) |
