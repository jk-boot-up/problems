# 523. Continuous Subarray Sum

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Prefix Sum &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/continuous-subarray-sum/)

## Problem

Return `true` if `nums` has a contiguous subarray of length **at least 2** whose sum is a multiple of `k` (0 counts as a multiple).

**Example**
```
nums = [23,2,4,6,7], k = 6  → true   ([2,4])
nums = [23,2,6,4,7], k = 6  → true   (whole array, 42)
nums = [23,2,6,4,7], k = 13 → false
```

**Constraints**
* `1 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^9`, `1 <= k <= 2^31 - 1`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-prefix-remainders-in-a-hash-map](v1-prefix-remainders-in-a-hash-map/README.md) | Prefix remainders in a hash map | `O(n)` | `O(min(n, k))` | [▶ animation](v1-prefix-remainders-in-a-hash-map/animation/index.html) |
