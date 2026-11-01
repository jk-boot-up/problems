# 268. Missing Number

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/missing-number/)

## Problem

`nums` contains `n` distinct numbers from the range `[0, n]`. Return the one number in the range that is missing.

**Example**
```
[3,0,1] → 2,   [0,1] → 2,   [9,6,4,2,3,5,7,0,1] → 8
```

**Constraints**
* `1 <= n <= 10^4`

**Follow-up:** O(1) extra space and O(n) time.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-gauss-sum](v1-gauss-sum/README.md) | Gauss sum | `O(n)` | `O(1)` | [▶ animation](v1-gauss-sum/animation/index.html) |
| [v2-xor-indices-and-values](v2-xor-indices-and-values/README.md) | XOR indices and values | `O(n)` | `O(1)` | [▶ animation](v2-xor-indices-and-values/animation/index.html) |
