# 124. Binary Tree Maximum Path Sum

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

## Problem

A **path** is a sequence of nodes connected by edges, each node used at most once; it need not pass through the root. Return the
maximum sum of node values over all non-empty paths.

**Example 1**
```
Input:  [1,2,3]
Output: 6   (2 → 1 → 3)
```

**Example 2**
```
Input:  [-10,9,20,null,null,15,7]
Output: 42   (15 → 20 → 7)
```

**Constraints**
* `1 <= n <= 3 * 10^4`; `-1000 <= Node.val <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-post-order-dfs-with-gains](v1-post-order-dfs-with-gains/README.md) | Post-order DFS with gains | `O(n)` | `O(h)` | [▶ animation](v1-post-order-dfs-with-gains/animation/index.html) |
