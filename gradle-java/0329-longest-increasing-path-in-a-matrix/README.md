# 329. Longest Increasing Path in a Matrix

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)

## Problem

Return the length of the longest strictly increasing path in an integer matrix, moving up, down, left or right.

**Example**
```
[[9,9,4],[6,6,8],[2,1,1]] → 4   (1 → 2 → 6 → 9)
```

**Constraints**
* `1 <= m, n <= 200`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-memoized-dfs](v1-memoized-dfs/README.md) | Memoized DFS | `O(m·n)` | `O(m·n)` | [▶ animation](v1-memoized-dfs/animation/index.html) |
