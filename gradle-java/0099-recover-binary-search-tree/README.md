# 99. Recover Binary Search Tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/recover-binary-search-tree/)

## Problem

Exactly two nodes of a BST had their values swapped by mistake. Recover the tree **without changing its structure**.

**Example**
```
[1,3,null,null,2] → [3,1,null,null,2]
[3,1,4,null,null,2] → [2,1,4,null,null,3]
```

**Constraints**
* `2 <= n <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-in-order-scan-for-inversions](v1-in-order-scan-for-inversions/README.md) | In-order scan for inversions | `O(n)` | `O(h)` | [▶ animation](v1-in-order-scan-for-inversions/animation/index.html) |
