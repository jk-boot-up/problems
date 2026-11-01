# 912. Sort an Array

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sorting &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sort-an-array/)

## Problem

Sort `nums` in ascending order **without** built-in sort functions, in O(n log n) time and with as little extra space as possible.

**Example**
```
[5,2,3,1] → [1,2,3,5],   [5,1,1,2,0,0] → [0,0,1,1,2,5]
```

**Constraints**
* `1 <= nums.length <= 5 * 10^4`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-heap-sort-in-place](v1-heap-sort-in-place/README.md) | Heap sort (in place) | `O(n log n)` | `O(1)` | [▶ animation](v1-heap-sort-in-place/animation/index.html) |
| [v2-merge-sort](v2-merge-sort/README.md) | Merge sort | `O(n log n)` | `O(n)` | [▶ animation](v2-merge-sort/animation/index.html) |
