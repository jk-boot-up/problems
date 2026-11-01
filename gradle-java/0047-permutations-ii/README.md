# 47. Permutations II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/permutations-ii/)

## Problem

`nums` may contain duplicates. Return all **unique** permutations, in any order.

**Example**
```
[1,1,2] → [[1,1,2],[1,2,1],[2,1,1]]
```

**Constraints**
* `1 <= nums.length <= 8`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sorted-backtracking-with-used-flags](v1-sorted-backtracking-with-used-flags/README.md) | Sorted backtracking with used flags | `O(n · n!)` | `O(n)` | [▶ animation](v1-sorted-backtracking-with-used-flags/animation/index.html) |
