# 103. Binary Tree Zigzag Level Order Traversal

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

## Problem

Return the zigzag level-order traversal: the first level left to right, the next right to left, and so on.

**Example**
```
Input:  [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
```

**Constraints**
* `0 <= n <= 2000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bfs-with-alternating-direction](v1-bfs-with-alternating-direction/README.md) | BFS with alternating direction | `O(n)` | `O(w)` | [▶ animation](v1-bfs-with-alternating-direction/animation/index.html) |
