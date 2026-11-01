# 34. Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## Problem

Given a sorted array `nums`, return the first and last index of `target` as `[first, last]`, or `[-1, -1]` if it is absent. Run in
O(log n).

**Example**
```
nums = [5,7,7,8,8,10]:  target 8 → [3,4],  target 6 → [-1,-1]
```

**Constraints**
* `0 <= nums.length <= 10^5`; sorted non-decreasing.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-lower-bounds](v1-two-lower-bounds/README.md) | Two lower bounds | `O(log n)` | `O(1)` | [▶ animation](v1-two-lower-bounds/animation/index.html) |
