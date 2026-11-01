# 645. Set Mismatch

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/set-mismatch/)

## Problem

A set held `1..n`, but one number was duplicated, replacing another. Given the resulting array `nums`, return `[duplicate, missing]`.

**Example**
```
[1,2,2,4] → [2,3],   [1,1] → [1,2]
```

**Constraints**
* `2 <= n <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-counting-array](v1-counting-array/README.md) | Counting array | `O(n)` | `O(n)` | [▶ animation](v1-counting-array/animation/index.html) |
