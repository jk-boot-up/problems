# 74. Search a 2D Matrix

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/search-a-2d-matrix/)

## Problem

In an `m × n` matrix, each row is sorted ascending and the first value of each row is greater than the last value of the previous row.
Return `true` if `target` is in the matrix. Run in O(log(m·n)).

**Example**
```
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]:  target 3 → true,  target 13 → false
```

**Constraints**
* `1 <= m, n <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-binary-search-on-the-flattened-index](v1-binary-search-on-the-flattened-index/README.md) | Binary search on the flattened index | `O(log(m·n))` | `O(1)` | [▶ animation](v1-binary-search-on-the-flattened-index/animation/index.html) |
