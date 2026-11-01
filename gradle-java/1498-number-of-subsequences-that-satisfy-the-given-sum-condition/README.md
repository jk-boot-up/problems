# 1498. Number of Subsequences That Satisfy the Given Sum Condition

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)

## Problem

Count the non-empty subsequences of `nums` whose `min + max <= target`. Return the count modulo `10^9 + 7`.

**Example**
```
nums = [3,5,6,7],     target = 9  → 4    ([3], [3,5], [3,5,6], [3,6])
nums = [3,3,6,8],     target = 10 → 6
nums = [2,3,3,4,6,7], target = 12 → 61
```

**Constraints**
* `1 <= nums.length <= 10^5`, `1 <= nums[i], target <= 10^6`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-two-pointers-powers-of-two](v1-sort-two-pointers-powers-of-two/README.md) | Sort, two pointers, powers of two | `O(n log n)` | `O(n)` | [▶ animation](v1-sort-two-pointers-powers-of-two/animation/index.html) |
