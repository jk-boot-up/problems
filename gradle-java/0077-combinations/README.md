# 77. Combinations

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/combinations/)

## Problem

Return all combinations of `k` numbers chosen from `1..n`, in any order.

**Example**
```
Input:  n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
```

**Constraints**
* `1 <= n <= 20`; `1 <= k <= n`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-backtracking-with-pruning](v1-backtracking-with-pruning/README.md) | Backtracking with pruning | `O(C(n, k) · k)` | `O(k)` | [▶ animation](v1-backtracking-with-pruning/animation/index.html) |
