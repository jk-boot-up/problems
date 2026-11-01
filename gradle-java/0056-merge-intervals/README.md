# 56. Merge Intervals

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Intervals &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/merge-intervals/)

## Problem

Given an array of `intervals` where `intervals[i] = [start, end]`, merge all overlapping intervals and return the
non-overlapping intervals that cover exactly the same ranges.

**Example 1**
```
Input:  [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

**Example 2**
```
Input:  [[1,4],[4,5]]
Output: [[1,5]]   (touching intervals overlap)
```

**Constraints**
* `1 <= intervals.length <= 10^4`; `0 <= start <= end <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-then-sweep](v1-sort-then-sweep/README.md) | Sort, then sweep | `O(n log n)` | `O(n)` | [▶ animation](v1-sort-then-sweep/animation/index.html) |
