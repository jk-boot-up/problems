# 84. Largest Rectangle in Histogram

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/)

## Problem

Bars of width 1 have heights `heights[i]`. Return the area of the largest rectangle that fits inside the histogram.

**Example**
```
[2,1,5,6,2,3] → 10   (heights 5 and 6, width 2)
[2,4]         → 4
```

**Constraints**
* `1 <= heights.length <= 10^5`; `0 <= heights[i] <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-monotonic-stack](v1-monotonic-stack/README.md) | Monotonic stack | `O(n)` | `O(n)` | [▶ animation](v1-monotonic-stack/animation/index.html) |
