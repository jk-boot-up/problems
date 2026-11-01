# 399. Evaluate Division

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/evaluate-division/)

## Problem

You are given equations `Ai / Bi = values[i]` between variables (strings). For each query `Cj / Dj`, return its value, or `-1.0` if it
cannot be determined. Variables that never appear in an equation are unknown (even `x / x` gives `-1.0`). There are no contradictions
or divisions by zero.

**Example**
```
Input:  equations = [["a","b"],["b","c"]], values = [2.0,3.0]
        queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.0, 0.5, -1.0, 1.0, -1.0]
```

**Constraints**
* `1 <= equations.length, queries.length <= 20`; `0 < values[i] <= 20`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-weighted-union-find](v1-weighted-union-find/README.md) | Weighted union-find | `O((E + Q)·α(V))` | `O(V)` | [▶ animation](v1-weighted-union-find/animation/index.html) |
| [v2-weighted-graph-dfs](v2-weighted-graph-dfs/README.md) | Weighted graph + DFS | `O(Q·(V + E))` | `O(V + E)` | [▶ animation](v2-weighted-graph-dfs/animation/index.html) |
