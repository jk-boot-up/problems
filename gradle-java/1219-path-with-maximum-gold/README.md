# 1219. Path with Maximum Gold

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/path-with-maximum-gold/)

## Problem

Each grid cell holds some gold (0 means empty). You may start and stop at any cell with gold, move up/down/left/right, never visit a
cell twice and never enter an empty cell. Return the most gold you can collect.

**Example**
```
[[0,6,0],[5,8,7],[0,9,0]] → 24   (9 → 8 → 7)
[[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]] → 28
```

**Constraints**
* `1 <= m, n <= 15`, at most 25 cells contain gold

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-backtracking-from-every-cell](v1-backtracking-from-every-cell/README.md) | Backtracking from every cell | `O(k · 3ᵏ)` | `O(k)` | [▶ animation](v1-backtracking-from-every-cell/animation/index.html) |
