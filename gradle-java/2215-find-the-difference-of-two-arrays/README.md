# 2215. Find the Difference of Two Arrays

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-the-difference-of-two-arrays/)

## Problem

Return `[a, b]` where `a` holds the distinct values of `nums1` not in `nums2`, and `b` the distinct values of `nums2` not in `nums1`
(any order).

**Example**
```
nums1 = [1,2,3], nums2 = [2,4,6] → [[1,3],[4,6]]
```

**Constraints**
* `1 <= nums1.length, nums2.length <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-hash-sets](v1-two-hash-sets/README.md) | Two hash sets | `O(m + n)` | `O(m + n)` | [▶ animation](v1-two-hash-sets/animation/index.html) |
