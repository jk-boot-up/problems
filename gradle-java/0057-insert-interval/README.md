# 57. Insert Interval

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Intervals &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/insert-interval/)

## Problem

`intervals` is sorted by start and non-overlapping. Insert `newInterval` and merge where needed, so the result is still
sorted and non-overlapping. Return the result.

**Example 1**
```
Input:  intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

**Example 2**
```
Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

**Constraints**
* `0 <= intervals.length <= 10^4`; `0 <= start <= end <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-three-phase-linear-scan](v1-three-phase-linear-scan/README.md) | Three-phase linear scan | `O(n)` | `O(n)` | [▶ animation](v1-three-phase-linear-scan/animation/index.html) |
