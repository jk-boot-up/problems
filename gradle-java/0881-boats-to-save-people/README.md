# 881. Boats to Save People

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/boats-to-save-people/)

## Problem

Each boat carries at most two people with total weight at most `limit` (every person weighs at most `limit`). Return the minimum number of
boats.

**Example**
```
people = [1,2], limit = 3 → 1,   [3,2,2,1], limit = 3 → 3,   [3,5,3,4], limit = 5 → 4
```

**Constraints**
* `1 <= people.length <= 5 * 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-two-pointers](v1-sort-two-pointers/README.md) | Sort + two pointers | `O(n log n)` | `O(log n)` | [▶ animation](v1-sort-two-pointers/animation/index.html) |
