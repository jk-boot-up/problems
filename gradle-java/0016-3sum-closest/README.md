# 16. 3Sum Closest

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/3sum-closest/)

## Problem

Find three numbers in `nums` whose sum is closest to `target` and return that sum. Exactly one answer exists.

**Example**
```
nums = [-1,2,1,-4], target = 1 → 2   (-1 + 2 + 1)
nums = [0,0,0], target = 1     → 0
```

**Constraints**
* `3 <= nums.length <= 500`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-two-pointers](v1-sort-two-pointers/README.md) | Sort + two pointers | `O(n²)` | `O(log n)` | [▶ animation](v1-sort-two-pointers/animation/index.html) |
