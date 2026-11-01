# 658. Find K Closest Elements

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-k-closest-elements/)

## Problem

Given a sorted array, return the `k` elements closest to `x`, in ascending order. `a` is closer than `b` if `|a - x| < |b - x|`, or equal
distance and `a < b`.

**Example**
```
arr = [1,2,3,4,5], k = 4, x = 3  → [1,2,3,4]
arr = [1,1,2,3,4,5], k = 4, x = -1 → [1,1,2,3]
```

**Constraints**
* `1 <= k <= arr.length <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-binary-search-on-the-window-start](v1-binary-search-on-the-window-start/README.md) | Binary search on the window start | `O(log(n − k) + k)` | `O(1)` | [▶ animation](v1-binary-search-on-the-window-start/animation/index.html) |
