# 1466. Reorder Routes to Make All Paths Lead to the City Zero

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)

## Problem

`n` cities form a tree of `n - 1` one-way roads `connections[i] = [a, b]` (from `a` to `b`). Return the minimum number of roads to reverse
so that every city can reach city 0.

**Example**
```
n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]] → 3
n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]       → 2
```

**Constraints**
* `2 <= n <= 5 * 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dfs-from-city-0-counting-outward-roads](v1-dfs-from-city-0-counting-outward-roads/README.md) | DFS from city 0 counting outward roads | `O(n)` | `O(n)` | [▶ animation](v1-dfs-from-city-0-counting-outward-roads/animation/index.html) |
