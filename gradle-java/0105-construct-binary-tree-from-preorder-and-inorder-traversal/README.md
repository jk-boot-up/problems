# 105. Construct Binary Tree from Preorder and Inorder Traversal

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

## Problem

Given the `preorder` and `inorder` traversals of a binary tree with **unique** values, build and return the tree.

**Example 1**
```
Input:  preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

**Example 2**
```
Input:  preorder = [-1], inorder = [-1]
Output: [-1]
```

**Constraints**
* `1 <= n <= 3000`; values are unique.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-linear-search-for-the-root](v1-linear-search-for-the-root/README.md) | Linear search for the root | `O(n²)` | `O(h)` | [▶ animation](v1-linear-search-for-the-root/animation/index.html) |
| [v2-hash-map-of-inorder-positions](v2-hash-map-of-inorder-positions/README.md) | Hash map of inorder positions | `O(n)` | `O(n)` | [▶ animation](v2-hash-map-of-inorder-positions/animation/index.html) |
