# 189. Rotate Array

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/rotate-array/)

## Problem

Rotate the integer array `nums` to the right by `k` steps, in place. `k` is non-negative and may be larger than the array length.

**Example 1**
```
Input:  nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
```

**Example 2**
```
Input:  nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
```

**Constraints**
* `1 <= nums.length <= 10^5`
* `-2^31 <= nums[i] <= 2^31 - 1`
* `0 <= k <= 10^5`

**Follow-up:** can you do it in place with O(1) extra space?

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-extra-array](v1-extra-array/README.md) | Extra array | `O(n)` | `O(n)` | [▶ animation](v1-extra-array/animation/index.html) |
| [v2-triple-reversal](v2-triple-reversal/README.md) | Triple reversal | `O(n)` | `O(1)` | [▶ animation](v2-triple-reversal/animation/index.html) |
