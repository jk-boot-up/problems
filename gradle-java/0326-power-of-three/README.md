# 326. Power of Three

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/power-of-three/)

## Problem

Return `true` if `n` is a power of three (`n == 3^x` for some integer `x >= 0`).

**Example**
```
27 → true
0  → false
-1 → false
45 → false
```

**Constraints**
* `-2^31 <= n <= 2^31 - 1`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-repeated-division](v1-repeated-division/README.md) | Repeated division | `O(log n)` | `O(1)` | [▶ animation](v1-repeated-division/animation/index.html) |
| [v2-divisor-of-3-19](v2-divisor-of-3-19/README.md) | Divisor of 3^19 | `O(1)` | `O(1)` | [▶ animation](v2-divisor-of-3-19/animation/index.html) |
