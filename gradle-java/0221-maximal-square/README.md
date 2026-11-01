# 221. Maximal Square

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximal-square/)

## Problem

Given an `m × n` binary matrix of `'0'` and `'1'`, return the **area** of the largest square containing only `'1'`s.

**Example**
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0   → 4
```

**Constraints**
* `1 <= m, n <= 300`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dp-on-square-sides](v1-dp-on-square-sides/README.md) | DP on square sides | `O(m·n)` | `O(m·n)` | [▶ animation](v1-dp-on-square-sides/animation/index.html) |
