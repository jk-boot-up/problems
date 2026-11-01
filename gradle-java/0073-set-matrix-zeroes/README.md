# 73. Set Matrix Zeroes

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/set-matrix-zeroes/)

## Problem

Given an `m × n` integer matrix, if a cell is `0`, set its entire row and column to `0`. Do it **in place**.

**Example 1**
```
Input:  [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

**Example 2**
```
Input:  [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

**Constraints**
* `1 <= m, n <= 200`, `-2^31 <= matrix[i][j] <= 2^31 - 1`

**Follow-up:** a constant-space solution.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-row-and-column-sets](v1-row-and-column-sets/README.md) | Row and column sets | `O(m·n)` | `O(m + n)` | [▶ animation](v1-row-and-column-sets/animation/index.html) |
| [v2-markers-in-row-column-0](v2-markers-in-row-column-0/README.md) | Markers in row/column 0 | `O(m·n)` | `O(1)` | [▶ animation](v2-markers-in-row-column-0/animation/index.html) |
