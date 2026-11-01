# 110. Balanced Binary Tree

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/balanced-binary-tree/)

## Problem

Return `true` if a binary tree is **height-balanced**: for every node, the heights of its two subtrees differ by at most 1.

**Example**
```
[3,9,20,null,null,15,7]     → true
[1,2,2,3,3,null,null,4,4]   → false
```

**Constraints**
* `0 <= n <= 5000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-height-with-early-exit](v1-height-with-early-exit/README.md) | Height with early exit | `O(n)` | `O(h)` | [▶ animation](v1-height-with-early-exit/animation/index.html) |
