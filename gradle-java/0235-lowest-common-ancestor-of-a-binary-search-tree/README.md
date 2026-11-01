# 235. Lowest Common Ancestor of a Binary Search Tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

## Problem

Given a BST and two of its nodes `p` and `q`, return their lowest common ancestor (a node is a descendant of itself).

**Example**
```
root = [6,2,8,0,4,7,9,null,null,3,5]: p = 2, q = 8 → 6;  p = 2, q = 4 → 2
```

**Constraints**
* `2 <= n <= 10^5`; values are unique; `p` and `q` exist.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-walk-down-by-value](v1-walk-down-by-value/README.md) | Walk down by value | `O(h)` | `O(1)` | [▶ animation](v1-walk-down-by-value/animation/index.html) |
