# 152. Maximum Product Subarray

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-product-subarray/)

## Problem

Return the largest product of a contiguous non-empty subarray of `nums` (it fits in 32 bits).

**Example**
```
[2,3,-2,4] → 6,   [-2,0,-1] → 0,   [-2,3,-4] → 24
```

**Constraints**
* `1 <= nums.length <= 2 * 10^4`; `-10 <= nums[i] <= 10`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-max-and-min-running-products](v1-max-and-min-running-products/README.md) | Max and min running products | `O(n)` | `O(1)` | [▶ animation](v1-max-and-min-running-products/animation/index.html) |
