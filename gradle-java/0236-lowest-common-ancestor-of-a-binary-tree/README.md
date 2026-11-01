# 236. Lowest Common Ancestor of a Binary Tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

## Problem

Given a binary tree and two of its nodes `p` and `q`, return their **lowest common ancestor**: the deepest node that has both `p`
and `q` as descendants (a node counts as a descendant of itself).

**Example 1**
```
Input:  root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
```

**Example 2**
```
Input:  same tree, p = 5, q = 4
Output: 5
```

**Constraints**
* `2 <= n <= 10^5`; values are unique; `p != q`; both exist in the tree.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-parent-map-and-ancestor-set](v1-parent-map-and-ancestor-set/README.md) | Parent map and ancestor set | `O(n)` | `O(n)` | [▶ animation](v1-parent-map-and-ancestor-set/animation/index.html) |
| [v2-recursive-search](v2-recursive-search/README.md) | Recursive search | `O(n)` | `O(h)` | [▶ animation](v2-recursive-search/animation/index.html) |
