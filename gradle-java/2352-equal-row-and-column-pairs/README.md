# 2352. Equal Row and Column Pairs

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/equal-row-and-column-pairs/)

## Problem

Given an `n × n` grid, return the number of pairs `(r, c)` such that row `r` and column `c` contain the same values in the same order.

**Example**
```
[[3,2,1],[1,7,6],[2,7,7]]                 → 1
[[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]] → 3
```

**Constraints**
* `1 <= n <= 200`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-hash-rows-look-up-columns](v1-hash-rows-look-up-columns/README.md) | Hash rows, look up columns | `O(n²)` | `O(n²)` | [▶ animation](v1-hash-rows-look-up-columns/animation/index.html) |
