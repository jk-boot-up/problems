# 543. Diameter of Binary Tree

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/)

## Problem

Return the **diameter** of a binary tree: the number of edges on the longest path between any two nodes (it need not pass through the root).

**Example**
```
[1,2,3,4,5] → 3   (4 → 2 → 1 → 3 or 5 → 2 → 1 → 3)
```

**Constraints**
* `1 <= n <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-heights-with-a-running-best](v1-heights-with-a-running-best/README.md) | Heights with a running best | `O(n)` | `O(h)` | [▶ animation](v1-heights-with-a-running-best/animation/index.html) |
