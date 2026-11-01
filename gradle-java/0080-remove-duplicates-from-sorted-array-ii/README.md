# 80. Remove Duplicates from Sorted Array II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

## Problem

`nums` is sorted in non-decreasing order. Remove extra duplicates **in place** so that every distinct value appears **at most twice**,
keeping the relative order. Return `k`, the length of the result; the first `k` slots of `nums` must hold it. Use O(1) extra memory.

**Example 1**
```
Input:  nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
```

**Example 2**
```
Input:  nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`
* `-10^4 <= nums[i] <= 10^4`, sorted non-decreasing

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-compare-two-back](v1-compare-two-back/README.md) | Compare two back | `O(n)` | `O(1)` | [▶ animation](v1-compare-two-back/animation/index.html) |
