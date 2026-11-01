# 312. Burst Balloons

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/burst-balloons/)

## Problem

Bursting balloon `i` earns `nums[left] * nums[i] * nums[right]`, where `left` and `right` are its current neighbours (out of range counts
as 1). Burst all balloons to collect the maximum total.

**Example**
```
[3,1,5,8] → 167   (3·1·5 + 3·5·8 + 1·3·8 + 1·8·1)
[1,5]     → 10
```

**Constraints**
* `1 <= n <= 300`; `0 <= nums[i] <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-interval-dp-on-the-last-balloon](v1-interval-dp-on-the-last-balloon/README.md) | Interval DP on the last balloon | `O(n³)` | `O(n²)` | [▶ animation](v1-interval-dp-on-the-last-balloon/animation/index.html) |
