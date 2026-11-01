# 98. Validate Binary Search Tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/validate-binary-search-tree/)

## Problem

Return `true` if a binary tree is a valid **BST**: every node's left subtree holds only smaller values, its right subtree only larger
values, and both subtrees are BSTs.

**Example 1**
```
Input:  [2,1,3]
Output: true
```

**Example 2**
```
Input:  [5,1,4,null,null,3,6]
Output: false   (3 is in the right subtree of 5 but smaller than 5)
```

**Constraints**
* `1 <= n <= 10^4`; `-2^31 <= Node.val <= 2^31 - 1`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-in-order-must-increase](v1-in-order-must-increase/README.md) | In-order must increase | `O(n)` | `O(h)` | [▶ animation](v1-in-order-must-increase/animation/index.html) |
| [v2-bounds-recursion](v2-bounds-recursion/README.md) | Bounds recursion | `O(n)` | `O(h)` | [▶ animation](v2-bounds-recursion/animation/index.html) |
