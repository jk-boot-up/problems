# 18. 4Sum

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/4sum/)

## Problem

Return all unique quadruplets `[a, b, c, d]` from `nums` (distinct indices) whose sum equals `target`, in any order.

**Example**
```
nums = [1,0,-1,0,-2,2], target = 0 → [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
nums = [2,2,2,2,2], target = 8      → [[2,2,2,2]]
```

**Constraints**
* `1 <= nums.length <= 200`; `-10^9 <= nums[i], target <= 10^9`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-two-loops-two-pointers](v1-sort-two-loops-two-pointers/README.md) | Sort + two loops + two pointers | `O(n³)` | `O(log n)` | [▶ animation](v1-sort-two-loops-two-pointers/animation/index.html) |
