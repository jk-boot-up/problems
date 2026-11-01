# 797. All Paths From Source to Target

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/all-paths-from-source-to-target/)

## Problem

Given a **DAG** of `n` nodes where `graph[i]` lists the nodes reachable from `i`, return every path from node `0` to node `n - 1`, in any order.

**Example**
```
[[1,2],[3],[3],[]]           → [[0,1,3],[0,2,3]]
[[4,3,1],[3,2,4],[3],[4],[]] → [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
```

**Constraints**
* `2 <= n <= 15`; no cycles.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dfs-with-backtracking](v1-dfs-with-backtracking/README.md) | DFS with backtracking | `O(2ⁿ · n)` | `O(n)` | [▶ animation](v1-dfs-with-backtracking/animation/index.html) |
