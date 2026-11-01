# 733. Flood Fill

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/flood-fill/)

## Problem

Starting from pixel `(sr, sc)`, repaint it and every 4-directionally connected pixel of the same original colour with `color`. Return the image.

**Example**
```
image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2 → [[2,2,2],[2,2,0],[2,0,1]]
```

**Constraints**
* `1 <= m, n <= 50`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-iterative-dfs](v1-iterative-dfs/README.md) | Iterative DFS | `O(m·n)` | `O(m·n)` | [▶ animation](v1-iterative-dfs/animation/index.html) |
