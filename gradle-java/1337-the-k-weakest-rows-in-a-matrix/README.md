# 1337. The K Weakest Rows in a Matrix

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/)

## Problem

Each row of a binary matrix has its soldiers (`1`) before its civilians (`0`). Row `i` is weaker than row `j` if it has fewer soldiers,
or the same number and `i < j`. Return the indices of the `k` weakest rows, weakest first.

**Example**
```
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], k = 3 → [2,0,3]
```

**Constraints**
* `2 <= m, n <= 100`, `1 <= k <= m`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-binary-search-counts-sort](v1-binary-search-counts-sort/README.md) | Binary search counts + sort | `O(m log n + m log m)` | `O(m)` | [▶ animation](v1-binary-search-counts-sort/animation/index.html) |
