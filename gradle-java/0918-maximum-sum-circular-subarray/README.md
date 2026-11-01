# 918. Maximum Sum Circular Subarray

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Kadane's Algorithm &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-sum-circular-subarray/)

## Problem

`nums` is a **circular** array (the end connects to the start). Return the maximum possible sum of a non-empty subarray, where each
element may be used at most once.

**Example 1**
```
Input:  nums = [5,-3,5]
Output: 10   ([5,5], wrapping around)
```

**Example 2**
```
Input:  nums = [-3,-2,-3]
Output: -2
```

**Constraints**
* `1 <= n <= 3 * 10^4`; `-3 * 10^4 <= nums[i] <= 3 * 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-max-and-min-kadane](v1-max-and-min-kadane/README.md) | Max and min Kadane | `O(n)` | `O(1)` | [▶ animation](v1-max-and-min-kadane/animation/index.html) |
