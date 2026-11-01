# 191. Number of 1 Bits

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-1-bits/)

## Problem

Return the number of set bits (`1`s) in the binary representation of a positive integer `n` (its Hamming weight).

**Example**
```
n = 11 (1011)            → 3
n = 128 (10000000)       → 1
n = 2147483645           → 30
```

**Constraints**
* `1 <= n <= 2^31 - 1`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-check-all-32-bits](v1-check-all-32-bits/README.md) | Check all 32 bits | `O(1)` | `O(1)` | [▶ animation](v1-check-all-32-bits/animation/index.html) |
| [v2-clear-lowest-set-bit](v2-clear-lowest-set-bit/README.md) | Clear lowest set bit | `O(k)` | `O(1)` | [▶ animation](v2-clear-lowest-set-bit/animation/index.html) |
