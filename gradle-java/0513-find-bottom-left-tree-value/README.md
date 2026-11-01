# 513. Find Bottom Left Tree Value

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-bottom-left-tree-value/)

## Problem

Return the leftmost value in the **last** row of a binary tree.

**Example**
```
[2,1,3]                          → 1
[1,2,3,4,null,5,6,null,null,7]   → 7
```

**Constraints**
* `1 <= n <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-right-to-left-bfs](v1-right-to-left-bfs/README.md) | Right-to-left BFS | `O(n)` | `O(w)` | [▶ animation](v1-right-to-left-bfs/animation/index.html) |
