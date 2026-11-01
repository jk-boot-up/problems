# 113. Path Sum II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/path-sum-ii/)

## Problem

Return every **root-to-leaf** path whose node values add up to `targetSum`, each as a list of values.

**Example**
```
root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
→ [[5,4,11,2],[5,8,4,5]]
```

**Constraints**
* `0 <= n <= 5000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dfs-with-backtracking](v1-dfs-with-backtracking/README.md) | DFS with backtracking | `O(n · h)` | `O(h)` | [▶ animation](v1-dfs-with-backtracking/animation/index.html) |
