# 199. Binary Tree Right Side View

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/)

## Problem

Imagine standing on the right side of a binary tree. Return the values you can see, from top to bottom.

**Example 1**
```
Input:  [1,2,3,null,5,null,4]
Output: [1,3,4]
```

**Example 2**
```
Input:  [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
```

**Constraints**
* `0 <= n <= 100`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-right-first-dfs](v1-right-first-dfs/README.md) | Right-first DFS | `O(n)` | `O(h)` | [▶ animation](v1-right-first-dfs/animation/index.html) |
| [v2-level-order-bfs](v2-level-order-bfs/README.md) | Level-order BFS | `O(n)` | `O(w)` | [▶ animation](v2-level-order-bfs/animation/index.html) |
