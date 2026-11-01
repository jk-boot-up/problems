# 279. Perfect Squares

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/perfect-squares/)

## Problem

Return the least number of perfect squares (`1, 4, 9, 16, …`) that sum to `n`.

**Example**
```
12 → 3 (4 + 4 + 4),   13 → 2 (4 + 9)
```

**Constraints**
* `1 <= n <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dp-over-amounts](v1-dp-over-amounts/README.md) | DP over amounts | `O(n·√n)` | `O(n)` | [▶ animation](v1-dp-over-amounts/animation/index.html) |
