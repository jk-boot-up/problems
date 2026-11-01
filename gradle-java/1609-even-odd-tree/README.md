# 1609. Even Odd Tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/even-odd-tree/)

## Problem

A tree is **Even-Odd** if, with the root at level 0:

* on even levels, all values are **odd** and strictly increasing left to right;
* on odd levels, all values are **even** and strictly decreasing left to right.

Return whether the tree is Even-Odd.

**Example**
```
[1,10,4,3,null,7,9,12,8,6,null,null,2] → true
[5,4,2,3,3,7]                           → false
[5,9,1,3,5,7]                           → false
```

**Constraints**
* `1 <= n <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-level-order-checks](v1-level-order-checks/README.md) | Level-order checks | `O(n)` | `O(w)` | [▶ animation](v1-level-order-checks/animation/index.html) |
