# 979. Distribute Coins in Binary Tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree DFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/distribute-coins-in-binary-tree/)

## Problem

A binary tree has `n` nodes and `n` coins in total (`node.val` coins on each node). One move sends one coin across one edge. Return the
fewest moves so that every node has exactly one coin.

**Example**
```
[3,0,0] → 2
[0,3,0] → 3
```

**Constraints**
* `1 <= n <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-post-order-surplus](v1-post-order-surplus/README.md) | Post-order surplus | `O(n)` | `O(h)` | [▶ animation](v1-post-order-surplus/animation/index.html) |
