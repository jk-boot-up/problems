# 1161. Maximum Level Sum of a Binary Tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)

## Problem

The root is level 1, its children level 2, and so on. Return the smallest level whose node values have the maximal sum.

**Example**
```
[1,7,0,7,-8,null,null] → 2,   [989,null,10250,98693,-89388,null,null,null,-32127] → 2
```

**Constraints**
* `1 <= n <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-level-order-bfs](v1-level-order-bfs/README.md) | Level-order BFS | `O(n)` | `O(w)` | [▶ animation](v1-level-order-bfs/animation/index.html) |
