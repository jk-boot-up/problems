# 40. Combination Sum II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/combination-sum-ii/)

## Problem

Find all unique combinations of `candidates` that sum to `target`. Each candidate may be used **once**; the input may contain duplicates,
but the output must not contain duplicate combinations.

**Example**
```
candidates = [10,1,2,7,6,1,5], target = 8 → [[1,1,6],[1,2,5],[1,7],[2,6]]
```

**Constraints**
* `1 <= candidates.length <= 100`; `1 <= target <= 30`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sorted-backtracking-with-skips](v1-sorted-backtracking-with-skips/README.md) | Sorted backtracking with skips | `O(2ⁿ · n)` | `O(n)` | [▶ animation](v1-sorted-backtracking-with-skips/animation/index.html) |
