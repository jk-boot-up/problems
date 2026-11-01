# 1372. Longest ZigZag Path in a Binary Tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/)

## Problem

A zigzag path alternates between left and right child moves. Its length is the number of edges. Return the longest zigzag path in the tree.

**Example**
```
[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1] → 3
[1,1,1,null,1,null,null,1,1,null,1]                  → 4
```

**Constraints**
* `1 <= n <= 5 * 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dfs-with-two-lengths](v1-dfs-with-two-lengths/README.md) | DFS with two lengths | `O(n)` | `O(h)` | [▶ animation](v1-dfs-with-two-lengths/animation/index.html) |
