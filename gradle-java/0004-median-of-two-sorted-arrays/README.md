# 4. Median of Two Sorted Arrays

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## Problem

Given two sorted arrays `nums1` (size `m`) and `nums2` (size `n`), return the **median** of all `m + n` values, in O(log(m + n)).

**Example 1**
```
Input:  nums1 = [1,3], nums2 = [2]
Output: 2.0
```

**Example 2**
```
Input:  nums1 = [1,2], nums2 = [3,4]
Output: 2.5
```

**Constraints**
* `0 <= m, n <= 1000`; `1 <= m + n <= 2000`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-merge-until-the-middle](v1-merge-until-the-middle/README.md) | Merge until the middle | `O(m + n)` | `O(1)` | [▶ animation](v1-merge-until-the-middle/animation/index.html) |
| [v2-binary-search-on-the-partition](v2-binary-search-on-the-partition/README.md) | Binary search on the partition | `O(log min(m, n))` | `O(1)` | [▶ animation](v2-binary-search-on-the-partition/animation/index.html) |
