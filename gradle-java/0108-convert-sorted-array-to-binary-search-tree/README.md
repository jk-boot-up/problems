# 108. Convert Sorted Array to Binary Search Tree

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Divide & Conquer &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

## Problem

Given a strictly increasing array `nums`, build a **height-balanced** BST (the depths of the two subtrees of every node differ by at
most one). Any valid answer is accepted.

**Example**
```
Input:  nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]   (one possible answer)
```

**Constraints**
* `1 <= nums.length <= 10^4`; strictly increasing.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-middle-element-as-root](v1-middle-element-as-root/README.md) | Middle element as root | `O(n)` | `O(log n)` | [▶ animation](v1-middle-element-as-root/animation/index.html) |
