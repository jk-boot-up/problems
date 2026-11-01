# 863. All Nodes Distance K in Binary Tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

## Problem

Given the root of a binary tree, a `target` node in it and an integer `k`, return the values of all nodes exactly `k` edges away from
`target`, in any order.

**Example**
```
root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2 → [7,4,1]
root = [1], target = 1, k = 3 → []
```

**Constraints**
* `1 <= n <= 500`, unique values, `0 <= k <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-parent-map-bfs](v1-parent-map-bfs/README.md) | Parent map + BFS | `O(n)` | `O(n)` | [▶ animation](v1-parent-map-bfs/animation/index.html) |
