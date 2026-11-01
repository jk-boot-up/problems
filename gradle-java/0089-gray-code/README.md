# 89. Gray Code

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/gray-code/)

## Problem

Return any `n`-bit Gray code sequence: `2^n` integers starting at 0, each appearing once, where consecutive values (and the last and first)
differ in exactly one bit.

**Example**
```
n = 2 → [0,1,3,2],   n = 1 → [0,1]
```

**Constraints**
* `1 <= n <= 16`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-formula-i-i-1](v1-formula-i-i-1/README.md) | Formula i ^ (i >> 1) | `O(2ⁿ)` | `O(1)` | [▶ animation](v1-formula-i-i-1/animation/index.html) |
