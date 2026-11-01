# 66. Plus One

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/plus-one/)

## Problem

A large integer is given as an array of `digits` (most significant first, no leading zeros). Add one and return the resulting digits.

**Example**
```
[1,2,3] → [1,2,4],   [4,3,2,1] → [4,3,2,2],   [9] → [1,0]
```

**Constraints**
* `1 <= digits.length <= 100`; `0 <= digits[i] <= 9`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-carry-from-the-right](v1-carry-from-the-right/README.md) | Carry from the right | `O(n)` | `O(1)` | [▶ animation](v1-carry-from-the-right/animation/index.html) |
