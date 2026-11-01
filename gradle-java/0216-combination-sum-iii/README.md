# 216. Combination Sum III

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/combination-sum-iii/)

## Problem

Find all combinations of `k` **distinct** digits from `1` to `9` that add up to `n`. Return each combination once, in any order.

**Example**
```
k = 3, n = 7 → [[1,2,4]]
k = 3, n = 9 → [[1,2,6],[1,3,5],[2,3,4]]
k = 4, n = 1 → []
```

**Constraints**
* `2 <= k <= 9`, `1 <= n <= 60`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-backtracking-over-digits-1-9](v1-backtracking-over-digits-1-9/README.md) | Backtracking over digits 1–9 | `O(C(9, k) · k)` | `O(k)` | [▶ animation](v1-backtracking-over-digits-1-9/animation/index.html) |
