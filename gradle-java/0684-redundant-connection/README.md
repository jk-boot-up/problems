# 684. Redundant Connection

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/redundant-connection/)

## Problem

A tree on nodes `1..n` had one extra edge added. Given the `n` edges, return an edge that can be removed so the graph becomes a tree; if
several work, return the one that appears last in the input.

**Example**
```
[[1,2],[1,3],[2,3]]                 → [2,3]
[[1,2],[2,3],[3,4],[1,4],[1,5]]     → [1,4]
```

**Constraints**
* `3 <= n <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-union-find](v1-union-find/README.md) | Union-find | `O(n·α(n))` | `O(n)` | [▶ animation](v1-union-find/animation/index.html) |
