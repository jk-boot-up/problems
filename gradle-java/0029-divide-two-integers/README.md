# 29. Divide Two Integers

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/divide-two-integers/)

## Problem

Divide two integers **without** using multiplication, division or mod. The quotient truncates toward zero. If the result overflows 32 bits,
return `2^31 - 1`.

**Example**
```
10 / 3 = 3,   7 / -3 = -2,   -2147483648 / -1 = 2147483647
```

**Constraints**
* `-2^31 <= dividend, divisor <= 2^31 - 1`; `divisor != 0`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-exponential-subtraction](v1-exponential-subtraction/README.md) | Exponential subtraction | `O(log² n)` | `O(1)` | [▶ animation](v1-exponential-subtraction/animation/index.html) |
