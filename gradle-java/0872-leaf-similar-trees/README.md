# 872. Leaf-Similar Trees

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/leaf-similar-trees/)

## Problem

Two binary trees are **leaf-similar** if their leaf values, read left to right, form the same sequence. Return whether `root1` and `root2`
are leaf-similar.

**Example**
```
[3,5,1,6,2,9,8,null,null,7,4] and [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8] → true
[1,2,3] and [1,3,2] → false
```

**Constraints**
* `1 <= nodes <= 200`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-collect-leaf-sequences](v1-collect-leaf-sequences/README.md) | Collect leaf sequences | `O(n + m)` | `O(n + m)` | [▶ animation](v1-collect-leaf-sequences/animation/index.html) |
