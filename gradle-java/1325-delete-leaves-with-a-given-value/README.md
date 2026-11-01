# 1325. Delete Leaves With a Given Value

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree DFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/delete-leaves-with-a-given-value/)

## Problem

Delete every leaf whose value is `target`. If deleting leaves turns a parent into a target-valued leaf, delete it too, and so on.

**Example**
```
[1,2,3,2,null,2,4], target = 2 → [1,null,3,null,4]
[1,3,3,3,2],        target = 3 → [1,3,null,null,2]
[1,2,null,2,null,2], target = 2 → [1]
```

**Constraints**
* `1 <= n <= 3000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-post-order-pruning](v1-post-order-pruning/README.md) | Post-order pruning | `O(n)` | `O(h)` | [▶ animation](v1-post-order-pruning/animation/index.html) |
