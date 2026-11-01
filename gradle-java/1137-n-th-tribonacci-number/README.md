# 1137. N-th Tribonacci Number

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/n-th-tribonacci-number/)

## Problem

`T0 = 0`, `T1 = 1`, `T2 = 1`, and `T(n+3) = T(n) + T(n+1) + T(n+2)`. Return `Tn`.

**Example**
```
n = 4 → 4,   n = 25 → 1389537
```

**Constraints**
* `0 <= n <= 37`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-three-rolling-values](v1-three-rolling-values/README.md) | Three rolling values | `O(n)` | `O(1)` | [▶ animation](v1-three-rolling-values/animation/index.html) |
