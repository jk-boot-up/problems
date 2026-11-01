# 566. Reshape the Matrix

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reshape-the-matrix/)

## Problem

Reshape an `m × n` matrix into `r × c`, filling row by row in the original row-major order. If `r × c != m × n`, return the original matrix.

**Example**
```
mat = [[1,2],[3,4]], r = 1, c = 4 → [[1,2,3,4]]
mat = [[1,2],[3,4]], r = 2, c = 4 → [[1,2],[3,4]]
```

**Constraints**
* `1 <= m, n <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-row-major-index-mapping](v1-row-major-index-mapping/README.md) | Row-major index mapping | `O(m·n)` | `O(m·n)` | [▶ animation](v1-row-major-index-mapping/animation/index.html) |
