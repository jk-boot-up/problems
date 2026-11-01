# 378. Kth Smallest Element in a Sorted Matrix

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

## Problem

In an `n × n` matrix where every row and every column is sorted ascending, return the `k`-th smallest element (counting duplicates).

**Example**
```
matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8 → 13
matrix = [[-5]], k = 1 → -5
```

**Constraints**
* `1 <= n <= 300`, `-10^9 <= matrix[i][j] <= 10^9`, `1 <= k <= n²`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-min-heap-over-rows](v1-min-heap-over-rows/README.md) | Min-heap over rows | `O(k log n)` | `O(n)` | [▶ animation](v1-min-heap-over-rows/animation/index.html) |
| [v2-binary-search-on-value](v2-binary-search-on-value/README.md) | Binary search on value | `O(n log R)` | `O(1)` | [▶ animation](v2-binary-search-on-value/animation/index.html) |
