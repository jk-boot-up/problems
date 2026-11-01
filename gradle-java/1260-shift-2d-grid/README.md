# 1260. Shift 2D Grid

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/shift-2d-grid/)

## Problem

One shift moves every element one place right in row-major order, with the last element wrapping to the top-left. Return the grid after `k`
shifts.

**Example**
```
grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1 → [[9,1,2],[3,4,5],[6,7,8]]
```

**Constraints**
* `1 <= m, n <= 50`; `0 <= k <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-flat-index-rotation](v1-flat-index-rotation/README.md) | Flat index rotation | `O(m·n)` | `O(m·n)` | [▶ animation](v1-flat-index-rotation/animation/index.html) |
