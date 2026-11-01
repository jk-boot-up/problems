# 1971. Find if Path Exists in Graph

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Union Find &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-if-path-exists-in-graph/)

## Problem

Given an undirected graph with `n` nodes and a list of edges, return whether there is a path from `source` to `destination`.

**Example**
```
n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2 → true
n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5 → false
```

**Constraints**
* `1 <= n <= 2 * 10^5`, up to `2 * 10^5` edges

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-union-find](v1-union-find/README.md) | Union–find | `O((n + E) · α(n))` | `O(n)` | [▶ animation](v1-union-find/animation/index.html) |
