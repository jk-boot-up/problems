# 530. Minimum Absolute Difference in BST

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

## Problem

Given the root of a **BST**, return the minimum absolute difference between the values of any two different nodes.

**Example 1**
```
Input:  [4,2,6,1,3]
Output: 1
```

**Example 2**
```
Input:  [1,0,48,null,null,12,49]
Output: 1
```

**Constraints**
* `2 <= n <= 10^4`; `0 <= Node.val <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-in-order-with-previous-value](v1-in-order-with-previous-value/README.md) | In-order with previous value | `O(n)` | `O(h)` | [▶ animation](v1-in-order-with-previous-value/animation/index.html) |
