# 218. The Skyline Problem

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/the-skyline-problem/)

## Problem

Each building is `[left, right, height]`, sorted by `left`. Return the **skyline**: the key points `[x, height]` where the outline's height
changes, sorted by `x`. The last point always has height 0. No two consecutive points may have the same height.

**Example**
```
[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
  → [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
[[0,2,3],[2,5,3]] → [[0,3],[5,0]]
```

**Constraints**
* `1 <= buildings.length <= 10^4`, `0 <= left < right <= 2^31 - 1`, `1 <= height <= 2^31 - 1`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-height-at-every-edge](v1-height-at-every-edge/README.md) | Height at every edge | `O(n²)` | `O(n)` | [▶ animation](v1-height-at-every-edge/animation/index.html) |
| [v2-sweep-line-with-a-max-heap](v2-sweep-line-with-a-max-heap/README.md) | Sweep line with a max-heap | `O(n log n)` | `O(n)` | [▶ animation](v2-sweep-line-with-a-max-heap/animation/index.html) |
