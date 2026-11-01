# 85. Maximal Rectangle

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximal-rectangle/)

## Problem

Given a binary matrix of `'0'` and `'1'`, return the area of the largest rectangle containing only `'1'`s.

**Example**
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0   → 6
```

**Constraints**
* `1 <= rows, cols <= 200`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-row-histograms-monotonic-stack](v1-row-histograms-monotonic-stack/README.md) | Row histograms + monotonic stack | `O(m·n)` | `O(n)` | [▶ animation](v1-row-histograms-monotonic-stack/animation/index.html) |
