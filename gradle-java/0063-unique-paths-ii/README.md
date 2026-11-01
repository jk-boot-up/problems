# 63. Unique Paths II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/unique-paths-ii/)

## Problem

A robot starts at the top-left of an `m × n` grid and moves only **right** or **down** to the bottom-right. Cells with `1` are
obstacles. Return the number of unique paths (it fits in 32 bits).

**Example**
```
[[0,0,0],
 [0,1,0],
 [0,0,0]] → 2
```

**Constraints**
* `1 <= m, n <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-one-rolling-row](v1-one-rolling-row/README.md) | One rolling row | `O(m·n)` | `O(n)` | [▶ animation](v1-one-rolling-row/animation/index.html) |
