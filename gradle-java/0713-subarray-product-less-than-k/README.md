# 713. Subarray Product Less Than K

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/subarray-product-less-than-k/)

## Problem

Given positive integers `nums`, return the number of contiguous subarrays whose product is **strictly less** than `k`.

**Example**
```
nums = [10,5,2,6], k = 100 → 8,   nums = [1,2,3], k = 0 → 0
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`; `1 <= nums[i] <= 1000`; `0 <= k <= 10^6`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sliding-window-on-the-product](v1-sliding-window-on-the-product/README.md) | Sliding window on the product | `O(n)` | `O(1)` | [▶ animation](v1-sliding-window-on-the-product/animation/index.html) |
