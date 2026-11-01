# 1020. Number of Enclaves

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph DFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-enclaves/)

## Problem

In a grid of `0` (sea) and `1` (land), a move goes to a 4-adjacent land cell or off the grid edge. Return the number of land cells from
which you **cannot** walk off the grid.

**Example**
```
0 0 0 0
1 0 1 0
0 1 1 0      → 3
0 0 0 0
```

**Constraints**
* `1 <= m, n <= 500`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-flood-fill-from-the-border](v1-flood-fill-from-the-border/README.md) | Flood fill from the border | `O(mn)` | `O(mn)` | [▶ animation](v1-flood-fill-from-the-border/animation/index.html) |
