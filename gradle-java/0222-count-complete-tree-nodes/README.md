# 222. Count Complete Tree Nodes

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/count-complete-tree-nodes/)

## Problem

Count the nodes of a **complete** binary tree: every level is full except possibly the last, which is filled from the left.

**Example 1**
```
Input:  [1,2,3,4,5,6]
Output: 6
```

**Example 2**
```
Input:  []
Output: 0
```

**Constraints**
* `0 <= n <= 5 * 10^4`; the tree is complete.

**Follow-up:** faster than O(n).

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-count-every-node](v1-count-every-node/README.md) | Count every node | `O(n)` | `O(log n)` | [▶ animation](v1-count-every-node/animation/index.html) |
| [v2-perfect-subtree-shortcut](v2-perfect-subtree-shortcut/README.md) | Perfect-subtree shortcut | `O(log² n)` | `O(log n)` | [▶ animation](v2-perfect-subtree-shortcut/animation/index.html) |
