# 509. Fibonacci Number

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/fibonacci-number/)

## Problem

`F(0) = 0`, `F(1) = 1`, `F(n) = F(n-1) + F(n-2)`. Return `F(n)`.

**Example**
```
n = 2 → 1,   n = 3 → 2,   n = 4 → 3
```

**Constraints**
* `0 <= n <= 30`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-naive-recursion](v1-naive-recursion/README.md) | Naive recursion | `O(2ⁿ)` | `O(n)` | [▶ animation](v1-naive-recursion/animation/index.html) |
| [v2-two-rolling-values](v2-two-rolling-values/README.md) | Two rolling values | `O(n)` | `O(1)` | [▶ animation](v2-two-rolling-values/animation/index.html) |
