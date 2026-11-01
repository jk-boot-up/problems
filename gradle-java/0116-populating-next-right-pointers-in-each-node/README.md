# 116. Populating Next Right Pointers in Each Node

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

## Problem

In a **perfect** binary tree (all leaves on the same level, every parent has two children), set each `next` pointer to the node on its right,
or `null` at the end of a level. Use O(1) extra space.

**Example**
```
[1,2,3,4,5,6,7] → levels linked: 1 → null; 2 → 3 → null; 4 → 5 → 6 → 7 → null
```

**Constraints**
* `0 <= n <= 2^12 - 1`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-use-the-level-above](v1-use-the-level-above/README.md) | Use the level above | `O(n)` | `O(1)` | [▶ animation](v1-use-the-level-above/animation/index.html) |
