# 560. Subarray Sum Equals K

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/)

## Problem

Return the number of contiguous subarrays of `nums` whose sum equals `k`.

**Example**
```
nums = [1,1,1], k = 2 → 2,   nums = [1,2,3], k = 3 → 2
```

**Constraints**
* `1 <= nums.length <= 2 * 10^4`; `-1000 <= nums[i] <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-prefix-sums-hash-map](v1-prefix-sums-hash-map/README.md) | Prefix sums + hash map | `O(n)` | `O(n)` | [▶ animation](v1-prefix-sums-hash-map/animation/index.html) |
