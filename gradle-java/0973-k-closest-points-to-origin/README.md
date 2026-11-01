# 973. K Closest Points to Origin

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/k-closest-points-to-origin/)

## Problem

Return the `k` points closest to the origin `(0, 0)` by Euclidean distance, in any order.

**Example**
```
points = [[1,3],[-2,2]], k = 1          → [[-2,2]]
points = [[3,3],[5,-1],[-2,4]], k = 2   → [[3,3],[-2,4]]
```

**Constraints**
* `1 <= k <= points.length <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-max-heap-of-size-k](v1-max-heap-of-size-k/README.md) | Max-heap of size k | `O(n log k)` | `O(k)` | [▶ animation](v1-max-heap-of-size-k/animation/index.html) |
