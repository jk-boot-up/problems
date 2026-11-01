# 90. Subsets II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/subsets-ii/)

## Problem

`nums` may contain duplicates. Return all **distinct** subsets, in any order.

**Example**
```
[1,2,2] → [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

**Constraints**
* `1 <= nums.length <= 10`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sorted-backtracking-with-skips](v1-sorted-backtracking-with-skips/README.md) | Sorted backtracking with skips | `O(n · 2ⁿ)` | `O(n)` | [▶ animation](v1-sorted-backtracking-with-skips/animation/index.html) |
