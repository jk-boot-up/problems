# 435. Non-overlapping Intervals

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Intervals &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/non-overlapping-intervals/)

## Problem

Return the minimum number of intervals to remove so the rest do not overlap (touching at an endpoint is fine).

**Example**
```
[[1,2],[2,3],[3,4],[1,3]] → 1
[[1,2],[1,2],[1,2]]       → 2
[[1,2],[2,3]]             → 0
```

**Constraints**
* `1 <= intervals.length <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-greedy-by-end](v1-greedy-by-end/README.md) | Greedy by end | `O(n log n)` | `O(log n)` | [▶ animation](v1-greedy-by-end/animation/index.html) |
