# 790. Domino and Tromino Tiling

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/domino-and-tromino-tiling/)

## Problem

Count the ways to tile a `2 × n` board with `2 × 1` dominoes and L-shaped trominoes (both may be rotated). Return the count modulo
`10^9 + 7`.

**Example**
```
n = 3 → 5,   n = 1 → 1
```

**Constraints**
* `1 <= n <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-linear-recurrence](v1-linear-recurrence/README.md) | Linear recurrence | `O(n)` | `O(n)` | [▶ animation](v1-linear-recurrence/animation/index.html) |
