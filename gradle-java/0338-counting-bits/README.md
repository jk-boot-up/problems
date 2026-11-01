# 338. Counting Bits

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/counting-bits/)

## Problem

For every `i` in `0..n`, return the number of `1` bits in its binary representation.

**Example**
```
n = 5 → [0,1,1,2,1,2]
```

**Constraints**
* `0 <= n <= 10^5`

**Follow-up:** O(n) without a built-in bit count.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dp-on-i-1](v1-dp-on-i-1/README.md) | DP on i >> 1 | `O(n)` | `O(1)` | [▶ animation](v1-dp-on-i-1/animation/index.html) |
