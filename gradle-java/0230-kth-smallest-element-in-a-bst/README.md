# 230. Kth Smallest Element in a BST

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

## Problem

Given the root of a BST and an integer `k`, return the `k`-th smallest value (1-indexed).

**Example 1**
```
Input:  root = [3,1,4,null,2], k = 1
Output: 1
```

**Example 2**
```
Input:  root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

**Constraints**
* `1 <= k <= n <= 10^4`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-full-in-order-list](v1-full-in-order-list/README.md) | Full in-order list | `O(n)` | `O(n)` | [▶ animation](v1-full-in-order-list/animation/index.html) |
| [v2-iterative-in-order-stop-early](v2-iterative-in-order-stop-early/README.md) | Iterative in-order, stop early | `O(h + k)` | `O(h)` | [▶ animation](v2-iterative-in-order-stop-early/animation/index.html) |
