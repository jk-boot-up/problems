# 114. Flatten Binary Tree to Linked List

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

## Problem

Flatten a binary tree **in place** into a "linked list" that uses the `right` pointers, with every `left` set to `null`, in
**preorder** order.

**Example**
```
Input:  [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

**Constraints**
* `0 <= n <= 2000`

**Follow-up:** O(1) extra space.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-preorder-list-then-relink](v1-preorder-list-then-relink/README.md) | Preorder list, then relink | `O(n)` | `O(n)` | [▶ animation](v1-preorder-list-then-relink/animation/index.html) |
| [v2-in-place-splicing-o-1-space](v2-in-place-splicing-o-1-space/README.md) | In-place splicing (O(1) space) | `O(n)` | `O(1)` | [▶ animation](v2-in-place-splicing-o-1-space/animation/index.html) |
