# 1254. Number of Closed Islands

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph DFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-closed-islands/)

## Problem

In this grid **`0` is land** and `1` is water. An island is a 4-connected group of `0`s; it is **closed** if it is completely surrounded
by water (it does not touch the grid border). Return the number of closed islands.

**Example**
```
1 1 1 1 1 1 1 0
1 0 0 0 0 1 1 0
1 0 1 0 1 1 1 0      → 2
1 0 0 0 0 1 0 1
1 1 1 1 1 1 1 0
```

**Constraints**
* `1 <= rows, cols <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sink-border-islands-then-count](v1-sink-border-islands-then-count/README.md) | Sink border islands, then count | `O(mn)` | `O(mn)` | [▶ animation](v1-sink-border-islands-then-count/animation/index.html) |
