# 559. Maximum Depth of N-ary Tree

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)

## Problem

Return the maximum depth (number of nodes on the longest root-to-leaf path) of an n-ary tree.

The tree uses `NaryMaxDepth.Node`, which has `val` and `children`.

**Example**
```
1 → (3 → 5, 6), 2, 4   → 3
```

**Constraints**
* `0 <= n <= 10^4`, height at most 1000

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-recursive-depth](v1-recursive-depth/README.md) | Recursive depth | `O(n)` | `O(h)` | [▶ animation](v1-recursive-depth/animation/index.html) |
