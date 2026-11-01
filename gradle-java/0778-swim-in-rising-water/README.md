# 778. Swim in Rising Water

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/swim-in-rising-water/)

## Problem

`grid[i][j]` is the elevation of a cell in an `n × n` grid. At time `t` the water level is `t`, and you can swim between adjacent cells whose
elevations are both at most `t`. Return the least time to go from the top-left to the bottom-right.

**Example**
```
[[0,2],[1,3]] → 3
```

**Constraints**
* `1 <= n <= 50`; values are a permutation of `0 .. n²-1`.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-min-heap-on-path-maximum](v1-min-heap-on-path-maximum/README.md) | Min-heap on path maximum | `O(n² log n)` | `O(n²)` | [▶ animation](v1-min-heap-on-path-maximum/animation/index.html) |
