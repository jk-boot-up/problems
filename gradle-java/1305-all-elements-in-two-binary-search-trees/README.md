# 1305. All Elements in Two Binary Search Trees

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/)

## Problem

Return all values from two BSTs in one ascending list.

**Example**
```
root1 = [2,1,4], root2 = [1,0,3]   → [0,1,1,2,3,4]
root1 = [1,null,8], root2 = [8,1]  → [1,1,8,8]
```

**Constraints**
* `0 <= nodes per tree <= 5000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-in-order-lists-then-merge](v1-in-order-lists-then-merge/README.md) | In-order lists, then merge | `O(m + n)` | `O(m + n)` | [▶ animation](v1-in-order-lists-then-merge/animation/index.html) |
