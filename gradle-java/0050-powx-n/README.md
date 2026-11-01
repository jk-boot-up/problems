# 50. Pow(x, n)

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/powx-n/)

## Problem

Implement `pow(x, n)`: `x` raised to the integer power `n` (which may be negative).

**Example**
```
pow(2.0, 10) = 1024.0,   pow(2.1, 3) = 9.261,   pow(2.0, -2) = 0.25
```

**Constraints**
* `-100.0 < x < 100.0`; `-2^31 <= n <= 2^31 - 1`; the result fits in a double.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-recursive-fast-power](v1-recursive-fast-power/README.md) | Recursive fast power | `O(log n)` | `O(log n)` | [▶ animation](v1-recursive-fast-power/animation/index.html) |
| [v2-iterative-binary-exponentiation](v2-iterative-binary-exponentiation/README.md) | Iterative binary exponentiation | `O(log n)` | `O(1)` | [▶ animation](v2-iterative-binary-exponentiation/animation/index.html) |
