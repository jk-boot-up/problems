# 109. Convert Sorted List to Binary Search Tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Divide & Conquer &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)

## Problem

Convert a sorted singly linked list into a height-balanced BST.

**Example**
```
-10 → -3 → 0 → 5 → 9  →  [0,-3,9,-10,null,5]  (one valid answer)
```

**Constraints**
* `0 <= n <= 2 * 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-in-order-simulation](v1-in-order-simulation/README.md) | In-order simulation | `O(n)` | `O(log n)` | [▶ animation](v1-in-order-simulation/animation/index.html) |
