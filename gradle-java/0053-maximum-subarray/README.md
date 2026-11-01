# 53. Maximum Subarray

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Kadane's Algorithm &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-subarray/)

## Problem

Given an integer array `nums`, find the contiguous subarray (at least one element) with the largest sum, and return that sum.

**Example 1**
```
Input:  nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6   ([4,-1,2,1])
```

**Example 2**
```
Input:  nums = [-1]
Output: -1
```

**Constraints**
* `1 <= nums.length <= 10^5`; `-10^4 <= nums[i] <= 10^4`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-brute-force-over-all-starts](v1-brute-force-over-all-starts/README.md) | Brute force over all starts | `O(n²)` | `O(1)` | [▶ animation](v1-brute-force-over-all-starts/animation/index.html) |
| [v2-kadane-s-algorithm](v2-kadane-s-algorithm/README.md) | Kadane's algorithm | `O(n)` | `O(1)` | [▶ animation](v2-kadane-s-algorithm/animation/index.html) |
