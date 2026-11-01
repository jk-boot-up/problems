# 240. Search a 2D Matrix II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/search-a-2d-matrix-ii/)

## Problem

Each row of the `m × n` matrix is sorted left to right and each column top to bottom. Return `true` if `target` is in the matrix.

**Example**
```
[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target 5 → true,  target 20 → false
```

**Constraints**
* `1 <= m, n <= 300`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-staircase-from-the-top-right](v1-staircase-from-the-top-right/README.md) | Staircase from the top-right | `O(m + n)` | `O(1)` | [▶ animation](v1-staircase-from-the-top-right/animation/index.html) |
