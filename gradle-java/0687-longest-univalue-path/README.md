# 687. Longest Univalue Path

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree DFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-univalue-path/)

## Problem

Return the length (number of **edges**) of the longest path in a binary tree where every node has the same value. The path need not pass
through the root.

**Example**
```
[5,4,5,1,1,null,5] → 2
[1,4,5,4,4,null,5] → 2
```

**Constraints**
* `0 <= n <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dfs-returning-arm-lengths](v1-dfs-returning-arm-lengths/README.md) | DFS returning arm lengths | `O(n)` | `O(h)` | [▶ animation](v1-dfs-returning-arm-lengths/animation/index.html) |
