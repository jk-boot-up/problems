# 662. Maximum Width of Binary Tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-width-of-binary-tree/)

## Problem

The width of a level is the number of positions between its leftmost and rightmost non-null nodes, counting the null positions in between
as they would appear in a complete tree. Return the maximum width over all levels (it fits in 32 bits).

**Example**
```
[1,3,2,5,3,null,9]               → 4
[1,3,2,5,null,null,9,6,null,7]   → 7
```

**Constraints**
* `1 <= n <= 3000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bfs-with-position-indices](v1-bfs-with-position-indices/README.md) | BFS with position indices | `O(n)` | `O(w)` | [▶ animation](v1-bfs-with-position-indices/animation/index.html) |
