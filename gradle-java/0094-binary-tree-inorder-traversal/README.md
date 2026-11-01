# 94. Binary Tree Inorder Traversal

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-tree-inorder-traversal/)

## Problem

Return the **inorder** traversal (left, node, right) of a binary tree's values.

**Example**
```
[1,null,2,3] → [1,3,2]
```

**Constraints**
* `0 <= n <= 100`

**Follow-up:** iteratively.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-recursive](v1-recursive/README.md) | Recursive | `O(n)` | `O(h)` | [▶ animation](v1-recursive/animation/index.html) |
| [v2-iterative-with-a-stack](v2-iterative-with-a-stack/README.md) | Iterative with a stack | `O(n)` | `O(h)` | [▶ animation](v2-iterative-with-a-stack/animation/index.html) |
