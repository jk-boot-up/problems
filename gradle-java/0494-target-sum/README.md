# 494. Target Sum

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/target-sum/)

## Problem

Put `+` or `-` in front of every number of `nums` so the expression evaluates to `target`. Return the number of ways.

**Example**
```
nums = [1,1,1,1,1], target = 3 → 5
nums = [1], target = 1          → 1
```

**Constraints**
* `1 <= nums.length <= 20`; `0 <= nums[i] <= 1000`; `-1000 <= target <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-subset-count-dp](v1-subset-count-dp/README.md) | Subset-count DP | `O(n · S)` | `O(S)` | [▶ animation](v1-subset-count-dp/animation/index.html) |
