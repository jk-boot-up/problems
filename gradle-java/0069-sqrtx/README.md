# 69. Sqrt(x)

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sqrtx/)

## Problem

Given a non-negative integer `x`, return the square root of `x` rounded **down** to an integer, without using built-in power or square
root functions.

**Example**
```
4 → 2,   8 → 2 (2.828…)
```

**Constraints**
* `0 <= x <= 2^31 - 1`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-binary-search](v1-binary-search/README.md) | Binary search | `O(log x)` | `O(1)` | [▶ animation](v1-binary-search/animation/index.html) |
| [v2-newton-s-method](v2-newton-s-method/README.md) | Newton's method | `O(log x)` | `O(1)` | [▶ animation](v2-newton-s-method/animation/index.html) |
