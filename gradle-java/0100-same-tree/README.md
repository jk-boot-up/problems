# 100. Same Tree

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/same-tree/)

## Problem

Given the roots `p` and `q` of two binary trees, return `true` if they are structurally identical with equal values in every node.

**Example 1**
```
Input:  p = [1,2,3], q = [1,2,3]
Output: true
```

**Example 2**
```
Input:  p = [1,2], q = [1,null,2]
Output: false
```

**Constraints**
* `0 <= n <= 100`; `-10^4 <= Node.val <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-recursive-comparison](v1-recursive-comparison/README.md) | Recursive comparison | `O(n)` | `O(h)` | [▶ animation](v1-recursive-comparison/animation/index.html) |
