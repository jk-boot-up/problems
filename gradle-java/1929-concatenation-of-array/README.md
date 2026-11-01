# 1929. Concatenation of Array

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/concatenation-of-array/)

## Problem

Return `ans` of length `2n` with `ans[i] = ans[i + n] = nums[i]`.

**Example**
```
[1,2,1]   → [1,2,1,1,2,1]
[1,3,2,1] → [1,3,2,1,1,3,2,1]
```

**Constraints**
* `1 <= n <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-write-both-copies](v1-write-both-copies/README.md) | Write both copies | `O(n)` | `O(n)` | [▶ animation](v1-write-both-copies/animation/index.html) |
