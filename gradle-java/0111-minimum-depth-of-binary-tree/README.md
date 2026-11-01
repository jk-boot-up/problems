# 111. Minimum Depth of Binary Tree

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

## Problem

Return the **minimum depth** of a binary tree: the number of nodes on the shortest path from the root down to a **leaf** (a node with no
children).

**Example**
```
[3,9,20,null,null,15,7]          → 2
[2,null,3,null,4,null,5,null,6]  → 5
```

**Constraints**
* `0 <= n <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bfs-to-the-first-leaf](v1-bfs-to-the-first-leaf/README.md) | BFS to the first leaf | `O(n)` | `O(w)` | [▶ animation](v1-bfs-to-the-first-leaf/animation/index.html) |
