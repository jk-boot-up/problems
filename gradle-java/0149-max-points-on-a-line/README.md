# 149. Max Points on a Line

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/max-points-on-a-line/)

## Problem

Given an array of distinct `points[i] = [x, y]`, return the maximum number of points that lie on the same straight line.

**Example**
```
[[1,1],[2,2],[3,3]] → 3
[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]] → 4
```

**Constraints**
* `1 <= points.length <= 300`; `-10^4 <= x, y <= 10^4`; all points are distinct.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-slope-counting-per-anchor](v1-slope-counting-per-anchor/README.md) | Slope counting per anchor | `O(n² log C)` | `O(n)` | [▶ animation](v1-slope-counting-per-anchor/animation/index.html) |
