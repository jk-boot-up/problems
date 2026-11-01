# 743. Network Delay Time

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/network-delay-time/)

## Problem

`times[i] = [u, v, w]` is a directed edge from node `u` to `v` taking `w` time. A signal starts at node `k`. Return the time for all `n`
nodes to receive it, or `-1` if some node never does.

**Example**
```
times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2 → 2
times = [[1,2,1]], n = 2, k = 2                  → -1
```

**Constraints**
* `1 <= k <= n <= 100`; `1 <= times.length <= 6000`; `0 <= w <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dijkstra-with-a-heap](v1-dijkstra-with-a-heap/README.md) | Dijkstra with a heap | `O(E log V)` | `O(V + E)` | [▶ animation](v1-dijkstra-with-a-heap/animation/index.html) |
