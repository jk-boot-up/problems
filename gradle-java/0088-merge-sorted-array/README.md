# 88. Merge Sorted Array

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/merge-sorted-array/)

## Problem

You get two integer arrays `nums1` and `nums2`, both sorted in non-decreasing order, plus two counts `m` and `n`.
Only the first `m` values of `nums1` are real; its last `n` slots hold `0` as placeholders. `nums2` holds exactly `n` values.

Merge `nums2` into `nums1` **in place** so that `nums1` becomes one sorted array of length `m + n`. The method returns nothing.

**Example 1**
```
Input:  nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: nums1 = [1,2,2,3,5,6]
```

**Example 2**
```
Input:  nums1 = [0], m = 0, nums2 = [1], n = 1
Output: nums1 = [1]
```

**Constraints**
* `nums1.length == m + n`, `nums2.length == n`
* `0 <= m, n <= 200`, `1 <= m + n <= 200`
* `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-copy-and-sort](v1-copy-and-sort/README.md) | Copy and sort | `O((m + n) log(m + n))` | `O(log(m + n))` | [▶ animation](v1-copy-and-sort/animation/index.html) |
| [v2-three-pointers-from-the-back](v2-three-pointers-from-the-back/README.md) | Three pointers from the back | `O(m + n)` | `O(1)` | [▶ animation](v2-three-pointers-from-the-back/animation/index.html) |
