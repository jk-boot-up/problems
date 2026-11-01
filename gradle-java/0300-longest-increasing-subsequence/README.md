# 300. Longest Increasing Subsequence

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/)

## Problem

Return the length of the longest **strictly increasing subsequence** of `nums` (elements in order, not necessarily contiguous).

**Example**
```
[10,9,2,5,3,7,101,18] → 4   ([2,3,7,101])
[0,1,0,3,2,3]         → 4
[7,7,7,7]             → 1
```

**Constraints**
* `1 <= nums.length <= 2500`

**Follow-up:** O(n log n).

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-quadratic-dp](v1-quadratic-dp/README.md) | Quadratic DP | `O(n²)` | `O(n)` | [▶ animation](v1-quadratic-dp/animation/index.html) |
| [v2-tails-array-binary-search](v2-tails-array-binary-search/README.md) | Tails array + binary search | `O(n log n)` | `O(n)` | [▶ animation](v2-tails-array-binary-search/animation/index.html) |
