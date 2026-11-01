# 637. Average of Levels in Binary Tree

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/average-of-levels-in-binary-tree/)

## Problem

Return the average value of the nodes on each level of a binary tree, from top to bottom. Answers within `10^-5` are accepted.

**Example**
```
Input:  [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
```

**Constraints**
* `1 <= n <= 10^4`; `-2^31 <= Node.val <= 2^31 - 1`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-level-order-bfs](v1-level-order-bfs/README.md) | Level-order BFS | `O(n)` | `O(w)` | [▶ animation](v1-level-order-bfs/animation/index.html) |
