# 410. Split Array Largest Sum

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/split-array-largest-sum/)

## Problem

Split `nums` into `k` non-empty contiguous subarrays so that the **largest** subarray sum is as small as possible. Return that sum.

**Example**
```
nums = [7,2,5,10,8], k = 2 → 18   ([7,2,5] and [10,8])
nums = [1,2,3,4,5],  k = 2 → 9
nums = [1,4,4],      k = 3 → 4
```

**Constraints**
* `1 <= nums.length <= 1000`, `0 <= nums[i] <= 10^6`, `1 <= k <= min(50, nums.length)`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dp-over-prefixes-and-pieces](v1-dp-over-prefixes-and-pieces/README.md) | DP over prefixes and pieces | `O(k · n²)` | `O(k · n)` | [▶ animation](v1-dp-over-prefixes-and-pieces/animation/index.html) |
| [v2-binary-search-on-the-cap](v2-binary-search-on-the-cap/README.md) | Binary search on the cap | `O(n log S)` | `O(1)` | [▶ animation](v2-binary-search-on-the-cap/animation/index.html) |
