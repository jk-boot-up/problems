# 26. Remove Duplicates from Sorted Array

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## Problem

`nums` is sorted in non-decreasing order. Remove the duplicates **in place** so each distinct value appears once, keeping
their relative order. Return `k`, the number of distinct values; the first `k` slots of `nums` must hold them.

**Example 1**
```
Input:  nums = [1,1,2]
Output: 2, nums = [1,2,_]
```

**Example 2**
```
Input:  nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`
* `-100 <= nums[i] <= 100`, sorted non-decreasing

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-pointers](v1-two-pointers/README.md) | Two pointers | `O(n)` | `O(1)` | [▶ animation](v1-two-pointers/animation/index.html) |
