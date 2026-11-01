# 173. Binary Search Tree Iterator

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/binary-search-tree-iterator/)

## Problem

Implement an iterator over a BST that returns values in **ascending** (in-order) order:
* `BSTIterator(TreeNode root)`
* `int next()`: the next smallest value (always valid when called)
* `boolean hasNext()`

**Example**
```
root = [7,3,15,null,null,9,20]
next() → 3, next() → 7, hasNext() → true, next() → 9, next() → 15, next() → 20, hasNext() → false
```

**Constraints**
* `1 <= n <= 10^5`

**Follow-up:** O(1) average time per call and O(h) memory.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-flatten-to-a-list-first](v1-flatten-to-a-list-first/README.md) | Flatten to a list first | `O(1)` | `O(n)` | [▶ animation](v1-flatten-to-a-list-first/animation/index.html) |
| [v2-controlled-stack](v2-controlled-stack/README.md) | Controlled stack | `O(1)` | `O(h)` | [▶ animation](v2-controlled-stack/animation/index.html) |
