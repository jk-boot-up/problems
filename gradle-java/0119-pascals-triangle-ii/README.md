# 119. Pascal's Triangle II

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/pascals-triangle-ii/)

## Problem

Return row `rowIndex` (0-based) of Pascal's triangle.

**Example**
```
3 → [1,3,3,1],   0 → [1],   1 → [1,1]
```

**Constraints**
* `0 <= rowIndex <= 33`

**Follow-up:** O(rowIndex) extra space.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-one-row-updated-right-to-left](v1-one-row-updated-right-to-left/README.md) | One row, updated right to left | `O(k²)` | `O(k)` | [▶ animation](v1-one-row-updated-right-to-left/animation/index.html) |
