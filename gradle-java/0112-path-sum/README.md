# 112. Path Sum

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/path-sum/)

## Problem

Return `true` if the tree has a **root-to-leaf** path whose values add up to `targetSum`. A leaf has no children.

**Example 1**
```
Input:  root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true   (5 → 4 → 11 → 2)
```

**Example 2**
```
Input:  root = [1,2,3], targetSum = 5
Output: false
```

**Constraints**
* `0 <= n <= 5000`; `-1000 <= Node.val, targetSum <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-recursive-dfs](v1-recursive-dfs/README.md) | Recursive DFS | `O(n)` | `O(h)` | [▶ animation](v1-recursive-dfs/animation/index.html) |
