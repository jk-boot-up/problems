# 463. Island Perimeter

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/island-perimeter/)

## Problem

A grid of `1` (land) and `0` (water) contains exactly one island with no lakes. Return the island's perimeter.

**Example**
```
0 1 0 0
1 1 1 0    → 16
0 1 0 0
1 1 0 0
```

**Constraints**
* `1 <= rows, cols <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-count-cells-and-shared-edges](v1-count-cells-and-shared-edges/README.md) | Count cells and shared edges | `O(mn)` | `O(1)` | [▶ animation](v1-count-cells-and-shared-edges/animation/index.html) |
