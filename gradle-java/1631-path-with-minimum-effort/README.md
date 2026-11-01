# 1631. Path With Minimum Effort

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Shortest Path &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/path-with-minimum-effort/)

## Problem

In a grid of heights, a route goes from the top-left to the bottom-right, moving up/down/left/right. Its **effort** is the largest absolute
height difference between two consecutive cells. Return the minimum effort.

**Example**
```
[[1,2,2],[3,8,2],[5,3,5]] → 2
[[1,2,3],[3,8,4],[5,3,5]] → 1
```

**Constraints**
* `1 <= rows, cols <= 100`, `1 <= heights <= 10^6`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dijkstra-on-the-max-edge](v1-dijkstra-on-the-max-edge/README.md) | Dijkstra on the max edge | `O(mn log(mn))` | `O(mn)` | [▶ animation](v1-dijkstra-on-the-max-edge/animation/index.html) |
