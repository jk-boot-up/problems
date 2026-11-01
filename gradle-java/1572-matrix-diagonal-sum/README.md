# 1572. Matrix Diagonal Sum

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/matrix-diagonal-sum/)

## Problem

Return the sum of a square matrix's primary diagonal and secondary diagonal, counting the shared centre element (odd `n`) only once.

**Example**
```
[[1,2,3],[4,5,6],[7,8,9]] → 25   (1 + 5 + 9 + 3 + 7)
[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]] → 8
```

**Constraints**
* `1 <= n <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-one-pass-over-rows](v1-one-pass-over-rows/README.md) | One pass over rows | `O(n)` | `O(1)` | [▶ animation](v1-one-pass-over-rows/animation/index.html) |
