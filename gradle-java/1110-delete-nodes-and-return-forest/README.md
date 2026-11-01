# 1110. Delete Nodes And Return Forest

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree DFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/delete-nodes-and-return-forest/)

## Problem

Delete every node whose value is in `to_delete`. The remaining nodes form a forest; return the roots of its trees, in any order.

**Example**
```
root = [1,2,3,4,5,6,7], to_delete = [3,5] → [[1,2,null,4],[6],[7]]
root = [1,2,4,null,3],  to_delete = [3]   → [[1,2,4]]
```

**Constraints**
* `1 <= n <= 1000`, distinct values

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-post-order-with-a-delete-set](v1-post-order-with-a-delete-set/README.md) | Post-order with a delete set | `O(n + d)` | `O(h + d)` | [▶ animation](v1-post-order-with-a-delete-set/animation/index.html) |
