# 1094. Car Pooling

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Prefix Sum &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/car-pooling/)

## Problem

A car with `capacity` empty seats drives east only. `trips[i] = [passengers, from, to]` picks up passengers at `from` and drops them at
`to`. Return whether every trip can be served.

**Example**
```
trips = [[2,1,5],[3,3,7]], capacity = 4 → false
trips = [[2,1,5],[3,3,7]], capacity = 5 → true
```

**Constraints**
* `1 <= trips.length <= 1000`, `0 <= from < to <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-difference-array-sweep](v1-difference-array-sweep/README.md) | Difference array sweep | `O(n + L)` | `O(L)` | [▶ animation](v1-difference-array-sweep/animation/index.html) |
