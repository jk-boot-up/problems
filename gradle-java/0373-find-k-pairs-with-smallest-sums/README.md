# 373. Find K Pairs with Smallest Sums

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

## Problem

Given two sorted arrays `nums1` and `nums2` and an integer `k`, return the `k` pairs `[u, v]` (u from nums1, v from nums2) with the
smallest sums.

**Example**
```
Input:  nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
```

**Constraints**
* `1 <= nums1.length, nums2.length <= 10^5`; `1 <= k <= 10^4`; `k <= nums1.length * nums2.length`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-min-heap-over-row-heads](v1-min-heap-over-row-heads/README.md) | Min-heap over row heads | `O(k log k)` | `O(k)` | [▶ animation](v1-min-heap-over-row-heads/animation/index.html) |
