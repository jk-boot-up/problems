# 104. Maximum Depth of Binary Tree

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

## Problem

Return the **maximum depth** of a binary tree: the number of nodes on the longest path from the root down to a leaf.

**Example 1**
```
Input:  root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2**
```
Input:  root = [1,null,2]
Output: 2
```

**Constraints**
* `0 <= n <= 10^4`; `-100 <= Node.val <= 100`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-level-order-bfs](v1-level-order-bfs/README.md) | Level-order BFS | `O(n)` | `O(w)` | [▶ animation](v1-level-order-bfs/animation/index.html) |
| [v2-recursive-dfs](v2-recursive-dfs/README.md) | Recursive DFS | `O(n)` | `O(h)` | [▶ animation](v2-recursive-dfs/animation/index.html) |
