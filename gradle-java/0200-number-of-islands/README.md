# 200. Number of Islands

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-islands/)

## Problem

Given an `m × n` grid of `'1'` (land) and `'0'` (water), count the **islands**. An island is a group of land cells connected
horizontally or vertically; the grid is surrounded by water.

**Example 1**
```
Input:
11110
11010
11000
00000
Output: 1
```

**Example 2**
```
Input:
11000
11000
00100
00011
Output: 3
```

**Constraints**
* `1 <= m, n <= 300`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bfs-flood-fill](v1-bfs-flood-fill/README.md) | BFS flood fill | `O(m·n)` | `O(min(m, n))` | [▶ animation](v1-bfs-flood-fill/animation/index.html) |
| [v2-dfs-flood-fill](v2-dfs-flood-fill/README.md) | DFS flood fill | `O(m·n)` | `O(m·n)` | [▶ animation](v2-dfs-flood-fill/animation/index.html) |
