# 223. Rectangle Area

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/rectangle-area/)

## Problem

Two axis-aligned rectangles are given by their bottom-left `(ax1, ay1)`, `(bx1, by1)` and top-right `(ax2, ay2)`, `(bx2, by2)` corners.
Return the total area they cover.

**Example**
```
ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2 → 45
ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=-2, by1=-2, bx2=2, by2=2 → 16
```

**Constraints**
* `-10^4 <= all coordinates <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-inclusion-exclusion](v1-inclusion-exclusion/README.md) | Inclusion–exclusion | `O(1)` | `O(1)` | [▶ animation](v1-inclusion-exclusion/animation/index.html) |
