# 1351. Count Negative Numbers in a Sorted Matrix

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)

## Problem

A matrix is sorted in **non-increasing** order along every row and every column. Count its negative numbers.

**Example**
```
[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]] → 8
[[3,2],[1,0]] → 0
```

**Constraints**
* `1 <= m, n <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-staircase-walk](v1-staircase-walk/README.md) | Staircase walk | `O(m + n)` | `O(1)` | [▶ animation](v1-staircase-walk/animation/index.html) |
