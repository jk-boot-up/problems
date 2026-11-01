# 39. Combination Sum

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/combination-sum/)

## Problem

Given **distinct** positive `candidates` and a `target`, return all unique combinations whose sum is `target`. Each candidate may be
used **any number of times**. Two combinations are different if some number is used a different number of times.

**Example**
```
Input:  candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
```

**Constraints**
* `1 <= candidates.length <= 30`; `2 <= candidates[i] <= 40`; `1 <= target <= 40`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sorted-backtracking](v1-sorted-backtracking/README.md) | Sorted backtracking | `O(N^(T/M))` | `O(T/M)` | [▶ animation](v1-sorted-backtracking/animation/index.html) |
