# 783. Minimum Distance Between BST Nodes

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)

## Problem

Return the minimum difference between the values of any two different nodes of a BST.

**Example**
```
[4,2,6,1,3] → 1,   [1,0,48,null,null,12,49] → 1
```

**Constraints**
* `2 <= n <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-in-order-with-previous-value](v1-in-order-with-previous-value/README.md) | In-order with previous value | `O(n)` | `O(h)` | [▶ animation](v1-in-order-with-previous-value/animation/index.html) |
