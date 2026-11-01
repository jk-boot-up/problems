# 547. Number of Provinces

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-provinces/)

## Problem

`isConnected[i][j] = 1` means cities `i` and `j` are directly connected. A province is a group of directly or indirectly connected cities.
Return the number of provinces.

**Example**
```
[[1,1,0],[1,1,0],[0,0,1]] → 2,   [[1,0,0],[0,1,0],[0,0,1]] → 3
```

**Constraints**
* `1 <= n <= 200`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-union-find](v1-union-find/README.md) | Union-find | `O(n²·α(n))` | `O(n)` | [▶ animation](v1-union-find/animation/index.html) |
