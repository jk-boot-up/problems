# 617. Merge Two Binary Trees

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/merge-two-binary-trees/)

## Problem

Merge two binary trees: overlapping nodes sum their values; a node present in only one tree is used as is. Return the merged tree.

**Example**
```
root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7] → [3,4,5,5,4,null,7]
```

**Constraints**
* `0 <= nodes <= 2000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-recursive-overlay](v1-recursive-overlay/README.md) | Recursive overlay | `O(min(n, m))` | `O(h)` | [▶ animation](v1-recursive-overlay/animation/index.html) |
