# 413. Arithmetic Slices

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/arithmetic-slices/)

## Problem

An array is **arithmetic** if it has at least three elements and equal differences between neighbours. Return the number of arithmetic
contiguous subarrays of `nums`.

**Example**
```
[1,2,3,4] → 3   ([1,2,3], [2,3,4], [1,2,3,4])
[1]       → 0
```

**Constraints**
* `1 <= nums.length <= 5000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-run-length-dp](v1-run-length-dp/README.md) | Run length DP | `O(n)` | `O(1)` | [▶ animation](v1-run-length-dp/animation/index.html) |
