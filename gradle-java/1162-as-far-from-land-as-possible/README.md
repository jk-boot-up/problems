# 1162. As Far from Land as Possible

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/as-far-from-land-as-possible/)

## Problem

In an `n × n` grid of `0` (water) and `1` (land), find a water cell whose Manhattan distance to the nearest land is as large as possible,
and return that distance. Return `-1` if there is no land or no water.

**Example**
```
[[1,0,1],[0,0,0],[1,0,1]] → 2
[[1,0,0],[0,0,0],[0,0,0]] → 4
```

**Constraints**
* `1 <= n <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-multi-source-bfs](v1-multi-source-bfs/README.md) | Multi-source BFS | `O(n²)` | `O(n²)` | [▶ animation](v1-multi-source-bfs/animation/index.html) |
