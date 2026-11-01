# 1448. Count Good Nodes in Binary Tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

## Problem

A node is **good** if no node on the path from the root to it has a greater value. Return the number of good nodes.

**Example**
```
[3,1,4,3,null,1,5] → 4,   [3,3,null,4,2] → 3,   [1] → 1
```

**Constraints**
* `1 <= n <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dfs-with-path-maximum](v1-dfs-with-path-maximum/README.md) | DFS with path maximum | `O(n)` | `O(h)` | [▶ animation](v1-dfs-with-path-maximum/animation/index.html) |
