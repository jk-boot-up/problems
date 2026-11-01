# 515. Find Largest Value in Each Tree Row

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)

## Problem

Return the largest value in each row of a binary tree, from top to bottom.

**Example**
```
[1,3,2,5,3,null,9] → [1,3,9]
[1,2,3]            → [1,3]
```

**Constraints**
* `0 <= n <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bfs-with-a-level-maximum](v1-bfs-with-a-level-maximum/README.md) | BFS with a level maximum | `O(n)` | `O(w)` | [▶ animation](v1-bfs-with-a-level-maximum/animation/index.html) |
