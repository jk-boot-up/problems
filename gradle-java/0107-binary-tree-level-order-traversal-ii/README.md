# 107. Binary Tree Level Order Traversal II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

## Problem

Return the level-order traversal from the **bottom** level up (each level left to right).

**Example**
```
[3,9,20,null,null,15,7] → [[15,7],[9,20],[3]]
```

**Constraints**
* `0 <= n <= 2000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bfs-prepend-levels](v1-bfs-prepend-levels/README.md) | BFS, prepend levels | `O(n)` | `O(w)` | [▶ animation](v1-bfs-prepend-levels/animation/index.html) |
