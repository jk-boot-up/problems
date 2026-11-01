# 538. Convert BST to Greater Tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/convert-bst-to-greater-tree/)

## Problem

Change every node's value in a BST to the sum of its original value and all values **greater** than it.

**Example**
```
[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
  → [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
[0,null,1] → [1,null,1]
```

**Constraints**
* `0 <= n <= 10^4`; values are unique

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-reverse-in-order-with-a-running-sum](v1-reverse-in-order-with-a-running-sum/README.md) | Reverse in-order with a running sum | `O(n)` | `O(h)` | [▶ animation](v1-reverse-in-order-with-a-running-sum/animation/index.html) |
