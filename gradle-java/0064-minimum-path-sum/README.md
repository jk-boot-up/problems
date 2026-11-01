# 64. Minimum Path Sum

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-path-sum/)

## Problem

Given an `m × n` grid of non-negative numbers, find a path from the top-left to the bottom-right, moving only **right** or **down**,
that minimizes the sum of the numbers along it. Return that sum.

**Example**
```
[[1,3,1],
 [1,5,1],
 [4,2,1]]  → 7   (1 → 3 → 1 → 1 → 1)
```

**Constraints**
* `1 <= m, n <= 200`; `0 <= grid[i][j] <= 200`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-full-dp-table](v1-full-dp-table/README.md) | Full DP table | `O(m·n)` | `O(m·n)` | [▶ animation](v1-full-dp-table/animation/index.html) |
| [v2-one-rolling-row](v2-one-rolling-row/README.md) | One rolling row | `O(m·n)` | `O(n)` | [▶ animation](v2-one-rolling-row/animation/index.html) |
