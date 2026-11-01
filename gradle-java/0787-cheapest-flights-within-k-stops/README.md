# 787. Cheapest Flights Within K Stops

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

## Problem

`flights[i] = [from, to, price]`. Return the cheapest price from `src` to `dst` using at most `k` stops (k + 1 flights), or `-1`.

**Example**
```
n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1 → 700
n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0 → 500
```

**Constraints**
* `1 <= n <= 100`; `0 <= k < n`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bellman-ford-with-k-1-rounds](v1-bellman-ford-with-k-1-rounds/README.md) | Bellman–Ford with k + 1 rounds | `O(k · E)` | `O(n)` | [▶ animation](v1-bellman-ford-with-k-1-rounds/animation/index.html) |
