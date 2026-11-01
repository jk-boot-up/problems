# 62. Unique Paths

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/unique-paths/)

## Problem

A robot on an `m × n` grid starts at the top-left and moves only right or down. How many unique paths reach the bottom-right corner?

**Example**
```
m = 3, n = 7 → 28,   m = 3, n = 2 → 3
```

**Constraints**
* `1 <= m, n <= 100`; the answer fits in 32 bits.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-combinatorics](v1-combinatorics/README.md) | Combinatorics | `O(min(m, n))` | `O(1)` | [▶ animation](v1-combinatorics/animation/index.html) |
| [v2-one-rolling-row](v2-one-rolling-row/README.md) | One rolling row | `O(m·n)` | `O(n)` | [▶ animation](v2-one-rolling-row/animation/index.html) |
