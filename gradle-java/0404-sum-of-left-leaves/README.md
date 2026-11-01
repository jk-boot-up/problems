# 404. Sum of Left Leaves

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree DFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sum-of-left-leaves/)

## Problem

Return the sum of all **left leaves**: leaves that are the left child of their parent.

**Example**
```
[3,9,20,null,null,15,7] → 24   (9 + 15)
[1]                     → 0
```

**Constraints**
* `1 <= n <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dfs-with-an-is-left-flag](v1-dfs-with-an-is-left-flag/README.md) | DFS with an is-left flag | `O(n)` | `O(h)` | [▶ animation](v1-dfs-with-an-is-left-flag/animation/index.html) |
