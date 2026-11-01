# 2542. Maximum Subsequence Score

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-subsequence-score/)

## Problem

Choose `k` indices. The score is `(sum of chosen nums1) × (minimum of chosen nums2)`. Return the maximum score.

**Example**
```
nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3 → 12
nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1 → 30
```

**Constraints**
* `1 <= k <= n <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-by-nums2-min-heap-of-nums1](v1-sort-by-nums2-min-heap-of-nums1/README.md) | Sort by nums2 + min-heap of nums1 | `O(n log n)` | `O(n)` | [▶ animation](v1-sort-by-nums2-min-heap-of-nums1/animation/index.html) |
