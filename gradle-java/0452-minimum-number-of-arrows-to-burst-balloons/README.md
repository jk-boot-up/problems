# 452. Minimum Number of Arrows to Burst Balloons

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Intervals &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

## Problem

Balloons are horizontal intervals `points[i] = [xstart, xend]` on a wall. A vertical arrow shot at `x` bursts every balloon with
`xstart <= x <= xend`. Return the **minimum** number of arrows needed to burst all balloons.

**Example 1**
```
Input:  points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2   (shoot at x = 6 and x = 11)
```

**Example 2**
```
Input:  points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
```

**Example 3**
```
Input:  points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
```

**Constraints**
* `1 <= points.length <= 10^5`; `-2^31 <= xstart < xend <= 2^31 - 1`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-greedy-by-end-point](v1-greedy-by-end-point/README.md) | Greedy by end point | `O(n log n)` | `O(log n)` | [▶ animation](v1-greedy-by-end-point/animation/index.html) |
