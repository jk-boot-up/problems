# 669. Trim a Binary Search Tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/trim-a-binary-search-tree/)

## Problem

Remove every node whose value lies outside `[low, high]` from a BST, keeping the relative structure of the remaining nodes. Return the new root.

**Example**
```
root = [1,0,2], low = 1, high = 2           → [1,null,2]
root = [3,0,4,null,2,null,null,1], low = 1, high = 3 → [3,2,null,1]
```

**Constraints**
* `1 <= n <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-recursive-trimming](v1-recursive-trimming/README.md) | Recursive trimming | `O(n)` | `O(h)` | [▶ animation](v1-recursive-trimming/animation/index.html) |
