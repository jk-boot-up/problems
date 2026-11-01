# 1584. Min Cost to Connect All Points

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/min-cost-to-connect-all-points/)

## Problem

Connect all `points` (2-D, integer coordinates) so every pair is linked by some path; connecting two points costs their Manhattan distance
`|x1 - x2| + |y1 - y2|`. Return the minimum total cost.

**Example**
```
[[0,0],[2,2],[3,10],[5,2],[7,0]] → 20
[[3,12],[-2,5],[-4,1]]           → 18
```

**Constraints**
* `1 <= n <= 1000`; all points distinct.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-prim-s-algorithm-dense-o-n](v1-prim-s-algorithm-dense-o-n/README.md) | Prim's algorithm (dense O(n²)) | `O(n²)` | `O(n)` | [▶ animation](v1-prim-s-algorithm-dense-o-n/animation/index.html) |
