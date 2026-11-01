# 589. N-ary Tree Preorder Traversal

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)

## Problem

Return the preorder traversal (node, then its children left to right) of an n-ary tree.

The tree uses `NaryPreorder.Node`, which has `val` and `children`.

**Example**
```
1
├─ 3
│  ├─ 5
│  └─ 6
├─ 2
└─ 4                → [1,3,5,6,2,4]
```

**Constraints**
* `0 <= n <= 10^4`, height at most 1000

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-iterative-with-a-stack](v1-iterative-with-a-stack/README.md) | Iterative with a stack | `O(n)` | `O(n)` | [▶ animation](v1-iterative-with-a-stack/animation/index.html) |
