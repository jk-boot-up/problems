# 120. Triangle

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/triangle/)

## Problem

Given a `triangle` of numbers, return the minimum path sum from top to bottom. From row `i`, index `j`, you may move to index `j` or
`j + 1` of the next row.

**Example**
```
   2
  3 4
 6 5 7
4 1 8 3
Output: 11   (2 + 3 + 5 + 1)
```

**Constraints**
* `1 <= triangle.length <= 200`

**Follow-up:** O(n) extra space, n = number of rows.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bottom-up-with-one-row](v1-bottom-up-with-one-row/README.md) | Bottom-up with one row | `O(n²)` | `O(n)` | [▶ animation](v1-bottom-up-with-one-row/animation/index.html) |
