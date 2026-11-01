# 209. Minimum Size Subarray Sum

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/)

## Problem

Given positive integers `nums` and a positive `target`, return the minimal length of a contiguous subarray whose sum is
**at least** `target`. Return `0` if no such subarray exists.

**Example 1**
```
Input:  target = 7, nums = [2,3,1,2,4,3]
Output: 2   ([4,3])
```

**Example 2**
```
Input:  target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

**Constraints**
* `1 <= target <= 10^9`
* `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^4`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-prefix-sums-binary-search](v1-prefix-sums-binary-search/README.md) | Prefix sums + binary search | `O(n log n)` | `O(n)` | [▶ animation](v1-prefix-sums-binary-search/animation/index.html) |
| [v2-sliding-window](v2-sliding-window/README.md) | Sliding window | `O(n)` | `O(1)` | [▶ animation](v2-sliding-window/animation/index.html) |
