# 54. Spiral Matrix

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/spiral-matrix/)

## Problem

Given an `m × n` matrix, return all of its elements in **spiral order** (clockwise, starting at the top-left).

**Example 1**
```
Input:  [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2**
```
Input:  [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

**Constraints**
* `1 <= m, n <= 10`, `-100 <= matrix[i][j] <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-shrinking-boundaries](v1-shrinking-boundaries/README.md) | Shrinking boundaries | `O(m·n)` | `O(1)` | [▶ animation](v1-shrinking-boundaries/animation/index.html) |
