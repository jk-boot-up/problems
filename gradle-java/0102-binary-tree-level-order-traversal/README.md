# 102. Binary Tree Level Order Traversal

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)

## Problem

Return the level-order traversal of a binary tree's values: left to right, level by level, as a list of lists.

**Example**
```
Input:  [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

**Constraints**
* `0 <= n <= 2000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-queue-level-by-level](v1-queue-level-by-level/README.md) | Queue, level by level | `O(n)` | `O(w)` | [▶ animation](v1-queue-level-by-level/animation/index.html) |
