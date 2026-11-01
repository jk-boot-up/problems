# 7. Reverse Integer

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reverse-integer/)

## Problem

Reverse the digits of a signed 32-bit integer `x`. If the result overflows the 32-bit range, return 0. Assume no 64-bit integers are
available.

**Example**
```
123 → 321,   -123 → -321,   120 → 21,   1534236469 → 0
```

**Constraints**
* `-2^31 <= x <= 2^31 - 1`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-digit-popping-with-overflow-check](v1-digit-popping-with-overflow-check/README.md) | Digit popping with overflow check | `O(log x)` | `O(1)` | [▶ animation](v1-digit-popping-with-overflow-check/animation/index.html) |
