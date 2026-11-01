# 226. Invert Binary Tree

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/invert-binary-tree/)

## Problem

Invert a binary tree (mirror it left-to-right) and return its root.

**Example 1**
```
Input:  [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

**Example 2**
```
Input:  [2,1,3]
Output: [2,3,1]
```

**Constraints**
* `0 <= n <= 100`; `-100 <= Node.val <= 100`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-iterative-bfs](v1-iterative-bfs/README.md) | Iterative BFS | `O(n)` | `O(w)` | [▶ animation](v1-iterative-bfs/animation/index.html) |
| [v2-recursive-swap](v2-recursive-swap/README.md) | Recursive swap | `O(n)` | `O(h)` | [▶ animation](v2-recursive-swap/animation/index.html) |
