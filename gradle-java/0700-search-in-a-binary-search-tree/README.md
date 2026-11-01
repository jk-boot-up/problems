# 700. Search in a Binary Search Tree

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/search-in-a-binary-search-tree/)

## Problem

Return the subtree rooted at the node whose value is `val` in a BST, or `null` if it does not exist.

**Example**
```
root = [4,2,7,1,3], val = 2 → [2,1,3],   val = 5 → null
```

**Constraints**
* `1 <= n <= 5000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-iterative-descent](v1-iterative-descent/README.md) | Iterative descent | `O(h)` | `O(1)` | [▶ animation](v1-iterative-descent/animation/index.html) |
