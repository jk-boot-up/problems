# 746. Min Cost Climbing Stairs

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/)

## Problem

`cost[i]` is the price of stepping off stair `i`; from there you climb 1 or 2 stairs. You may start at stair 0 or 1. Return the minimum cost
to reach the top (just past the last stair).

**Example**
```
[10,15,20] → 15,   [1,100,1,1,1,100,1,1,100,1] → 6
```

**Constraints**
* `2 <= cost.length <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-rolling-values](v1-two-rolling-values/README.md) | Two rolling values | `O(n)` | `O(1)` | [▶ animation](v1-two-rolling-values/animation/index.html) |
