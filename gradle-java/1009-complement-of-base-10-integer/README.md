# 1009. Complement of Base 10 Integer

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/complement-of-base-10-integer/)

## Problem

The complement flips every bit of a number's binary representation (without leading zeros). Return the complement of `n`.

**Example**
```
5 (101) → 2 (010),   7 (111) → 0,   10 (1010) → 5 (0101),   0 → 1
```

**Constraints**
* `0 <= n < 10^9`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-all-ones-mask](v1-all-ones-mask/README.md) | All-ones mask | `O(log n)` | `O(1)` | [▶ animation](v1-all-ones-mask/animation/index.html) |
