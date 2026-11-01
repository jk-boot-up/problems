# 106. Construct Binary Tree from Inorder and Postorder Traversal

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

## Problem

Given the `inorder` and `postorder` traversals of a binary tree with **unique** values, build and return the tree.

**Example 1**
```
Input:  inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
```

**Example 2**
```
Input:  inorder = [-1], postorder = [-1]
Output: [-1]
```

**Constraints**
* `1 <= n <= 3000`; values are unique.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-hash-map-walk-postorder-backwards](v1-hash-map-walk-postorder-backwards/README.md) | Hash map, walk postorder backwards | `O(n)` | `O(n)` | [▶ animation](v1-hash-map-walk-postorder-backwards/animation/index.html) |
