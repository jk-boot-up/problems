# 654. Maximum Binary Tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-binary-tree/)

## Problem

Build the **maximum binary tree** of distinct `nums`: the root is the maximum; its left subtree is built from the part before it and its right
subtree from the part after it, recursively.

**Example**
```
[3,2,1,6,0,5] → [6,3,5,null,2,0,null,null,1]
```

**Constraints**
* `1 <= nums.length <= 1000`; values are distinct.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-monotonic-stack](v1-monotonic-stack/README.md) | Monotonic stack | `O(n)` | `O(n)` | [▶ animation](v1-monotonic-stack/animation/index.html) |
