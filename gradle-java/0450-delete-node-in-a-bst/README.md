# 450. Delete Node in a BST

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/delete-node-in-a-bst/)

## Problem

Delete the node with value `key` from a BST (if present) and return the root of the still-valid BST.

**Example**
```
root = [5,3,6,2,4,null,7], key = 3 → [5,4,6,2,null,null,7]  (or [5,2,6,null,4,null,7])
```

**Constraints**
* `0 <= n <= 10^4`; values are unique.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-recursive-delete-with-successor](v1-recursive-delete-with-successor/README.md) | Recursive delete with successor | `O(h)` | `O(h)` | [▶ animation](v1-recursive-delete-with-successor/animation/index.html) |
