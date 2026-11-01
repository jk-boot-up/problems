# 931. Minimum Falling Path Sum

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-falling-path-sum/)

## Problem

In an `n × n` matrix, a **falling path** starts anywhere in the first row and moves down one row at a time, to the cell directly below
or diagonally left/right. Return the minimum sum of a falling path.

**Example**
```
[[2,1,3],[6,5,4],[7,8,9]] → 13   (1 → 5 → 7  or  1 → 4 → 8)
[[-19,57],[-40,-5]]       → -59
```

**Constraints**
* `1 <= n <= 100`, `-100 <= matrix[i][j] <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-row-by-row-dp](v1-row-by-row-dp/README.md) | Row-by-row DP | `O(n²)` | `O(n)` | [▶ animation](v1-row-by-row-dp/animation/index.html) |
