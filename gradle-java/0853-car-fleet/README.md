# 853. Car Fleet

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/car-fleet/)

## Problem

Cars on a one-lane road drive toward `target`. Car `i` starts at `position[i]` with speed `speed[i]`. A faster car that catches a slower
one slows down and they move together as a **fleet**. Return the number of fleets that reach the target.

**Example**
```
target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3] → 3
```

**Constraints**
* `1 <= n <= 10^5`; positions are distinct and `< target`.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-by-position-compare-arrival-times](v1-sort-by-position-compare-arrival-times/README.md) | Sort by position, compare arrival times | `O(n log n)` | `O(n)` | [▶ animation](v1-sort-by-position-compare-arrival-times/animation/index.html) |
