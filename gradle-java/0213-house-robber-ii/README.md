# 213. House Robber II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/house-robber-ii/)

## Problem

Same as House Robber, but the houses are arranged in a **circle**: the first and last houses are neighbours. Return the maximum amount.

**Example**
```
[2,3,2] → 3,   [1,2,3,1] → 4,   [1,2,3] → 3
```

**Constraints**
* `1 <= nums.length <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-linear-passes](v1-two-linear-passes/README.md) | Two linear passes | `O(n)` | `O(1)` | [▶ animation](v1-two-linear-passes/animation/index.html) |
