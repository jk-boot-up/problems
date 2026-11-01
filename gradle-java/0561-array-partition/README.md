# 561. Array Partition

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/array-partition/)

## Problem

Group `2n` integers into `n` pairs to maximize the sum of `min(a, b)` over all pairs. Return that sum.

**Example**
```
[1,4,3,2] → 4 ((1,2), (3,4)),   [6,2,6,5,1,2] → 9
```

**Constraints**
* `1 <= n <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-and-take-every-other](v1-sort-and-take-every-other/README.md) | Sort and take every other | `O(n log n)` | `O(log n)` | [▶ animation](v1-sort-and-take-every-other/animation/index.html) |
