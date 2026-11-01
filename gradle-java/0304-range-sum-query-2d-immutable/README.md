# 304. Range Sum Query 2D - Immutable

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Prefix Sum &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/range-sum-query-2d-immutable/)

## Problem

Implement `NumMatrix`:

* `NumMatrix(int[][] matrix)`
* `int sumRegion(int row1, int col1, int row2, int col2)` — the sum of the rectangle with corners `(row1, col1)` and `(row2, col2)`,
  inclusive, in O(1).

**Example**
```
matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
sumRegion(2,1,4,3) → 8, sumRegion(1,1,2,2) → 11, sumRegion(1,2,2,4) → 12
```

**Constraints**
* `1 <= m, n <= 200`, up to `10^4` queries

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-2-d-prefix-sums](v1-2-d-prefix-sums/README.md) | 2-D prefix sums | `O(1)` | `O(mn)` | [▶ animation](v1-2-d-prefix-sums/animation/index.html) |
